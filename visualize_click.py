#!/usr/bin/env python3
"""
SymNet Click Configuration Visualizer

Clickの設定ファイルを解析して、モジュール間の接続をGraphvizで可視化します。
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
import subprocess

class ClickModule:
    """Clickモジュールを表すクラス"""
    def __init__(self, name: str, module_type: str, config: str = ""):
        self.name = name
        self.module_type = module_type
        self.config = config
        self.connections: List[Tuple[int, str, int]] = []  # (出力ポート, 接続先モジュール, 入力ポート)
    
    def __repr__(self):
        return f"{self.name} :: {self.module_type}({self.config})"

class ClickParser:
    """Click設定ファイルのパーサー"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.modules: Dict[str, ClickModule] = {}
        self.connections: List[Tuple[str, int, str, int]] = []  # (from_module, from_port, to_module, to_port)
        self._inline_counter = 0
        
    def _create_inline_module(self, module_type: str, config: str = "") -> str:
        """インライン要素用の一時モジュールを作成"""
        self._inline_counter += 1
        inline_name = f"_inline_{module_type}_{self._inline_counter}"
        self.modules[inline_name] = ClickModule(inline_name, module_type, config)
        return inline_name
    
    def parse(self):
        """設定ファイルを解析"""
        with open(self.filepath, 'r') as f:
            content = f.read()
        
        # コメントを除去
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        
        # 行ごとに処理
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # セミコロンで分割（複数のコンポーネントが1行にある場合）
            components = [c.strip() for c in line.split(';') if c.strip()]
            
            for component in components:
                if '::' in component and '->' not in component:
                    # モジュール定義: "name :: Type(config)"
                    self._parse_module_definition(component)
                elif '->' in component:
                    # パス定義: "source -> target"
                    self._parse_path(component)
    
    def _parse_module_definition(self, definition: str):
        """モジュール定義を解析: name :: Type(config)"""
        match = re.match(r'(\w+)\s*::\s*(\w+)(?:\s*\((.*?)\)\s*)?$', definition)
        if match:
            name, mod_type, config = match.groups()
            config = config if config else ""
            self.modules[name] = ClickModule(name, mod_type, config)
    
    def _parse_path(self, path: str):
        """パス定義を解析: source[port] -> target -> ...
        
        パス要素の種類:
        - 名前付きモジュール: "module_name"
        - 名前付きモジュール+ポート: "module_name[0]"
        - インライン定義: ":: ClassName(config)"
        - インライン定義+呼び出し: "ClassName(config)"
        """
        # 矢印で分割
        parts = [p.strip() for p in re.split(r'\s*->\s*', path)]
        
        # すべての要素を解析してモジュールリストを作成
        modules_in_path = []
        for part in parts:
            if not part:
                continue
            
            current_module, current_port = self._parse_path_element(part)
            if current_module:
                modules_in_path.append((current_module, current_port))
        
        # 連続する要素間の接続を記録
        for i in range(len(modules_in_path) - 1):
            src_module, src_port = modules_in_path[i]
            tgt_module, _ = modules_in_path[i + 1]
            self.connections.append((src_module, src_port, tgt_module, 0))
    
    def _parse_path_element(self, element: str) -> Tuple[str, int]:
        """パス要素を解析してモジュール名とポート番号を返す
        
        Returns:
            (module_name, port_number) または (None, 0)
        """
        # パターン0: "name :: ClassName(config)" （パス中での名前付き定義）
        match = re.match(r'^(\w+)\s*::\s*([A-Z]\w*)\s*\((.*?)\)$', element)
        if match:
            module_name = match.group(1)
            class_name = match.group(2)
            config = match.group(3)
            # モジュールを登録
            if module_name not in self.modules:
                self.modules[module_name] = ClickModule(module_name, class_name, config)
            return (module_name, 0)
        
        # パターン1: "module_name[port]"
        match = re.match(r'^(\w+)\s*\[(\d+)\]$', element)
        if match:
            module_name = match.group(1)
            port = int(match.group(2))
            # モジュールが存在するかチェック（なくても名前を返す）
            return (module_name, port)
        
        # パターン2: "module_name"（既存または将来定義されるモジュール）
        match = re.match(r'^(\w+)$', element)
        if match:
            module_name = match.group(1)
            # モジュール名がマッチすればそのまま返す（後で定義される可能性がある）
            return (module_name, 0)
        
        # パターン3: ":: ClassName(config)" または "ClassName(config)"（インライン定義）
        match = re.match(r'^(?:::)?\s*([A-Z]\w*)\s*\((.*?)\)$', element)
        if match:
            class_name = match.group(1)
            config = match.group(2)
            inline_name = self._create_inline_module(class_name, config)
            return (inline_name, 0)
        
        # パターン4: 引数なしのインライン定義 "ClassName()" または "ClassName"
        match = re.match(r'^(?:::)?\s*([A-Z]\w*)(?:\(\))?$', element)
        if match:
            class_name = match.group(1)
            inline_name = self._create_inline_module(class_name, "")
            return (inline_name, 0)
        
        return (None, 0)

class ClickVisualizer:
    """Graphvizを使用してClick設定を可視化"""
    
    # モジュールタイプごとの色設定
    MODULE_COLORS = {
        'FromDevice': '#E8F4F8',      # 入力デバイス - 水色
        'ToDevice': '#F8E8E8',        # 出力デバイス - ピンク
        'IPClassifier': '#FFF4E6',    # 分類器 - オレンジ
        'LinearIPLookup': '#E6F4E6',  # ルーティング - 緑
        'EtherEncap': '#F0E6FF',      # カプセル化 - 紫
        'EtherDecap': '#E6EEFF',      # デカプセル化 - 青
        'VLANEncap': '#FFE6F0',       # VLANカプセル化 - ピンク紫
        'VLANDecap': '#E6F0FF',       # VLANデカプセル化 - 青紫
        'Discard': '#F5F5F5',         # 破棄 - グレー
        'Null': '#F5F5F5',            # Null - グレー
        'Paint': '#FFFACD',           # ペイント - 黄色
    }
    
    def __init__(self, parser: ClickParser):
        self.parser = parser
        
    def _escape_label(self, text: str) -> str:
        """Graphviz用にラベルをエスケープ"""
        return text.replace('"', '\\"').replace('\n', '\\n')
    
    def _get_module_color(self, module_type: str) -> str:
        """モジュールタイプに応じた色を取得"""
        return self.MODULE_COLORS.get(module_type, '#FFFFFF')
    
    def _create_module_label(self, module: ClickModule) -> str:
        """モジュールのラベルを生成"""
        # インライン要素の場合は名前を省略
        if module.name.startswith('_inline_'):
            label = f"[{module.module_type}]"
        else:
            label = f"{module.name}"
            if module.module_type:
                label += f"\\n[{module.module_type}]"
        
        if module.config:
            # 設定が長い場合は省略
            config = module.config
            if len(config) > 40:
                config = config[:37] + "..."
            label += f"\\n({config})"
        return label
    
    def generate_dot(self) -> str:
        """Graphviz DOT形式のグラフを生成"""
        lines = [
            'digraph Click {',
            '  rankdir=LR;',  # 左から右へのレイアウト
            '  node [shape=box, style="rounded,filled", fontname="Arial"];',
            '  edge [fontname="Arial", fontsize=10];',
            ''
        ]
        
        # モジュールノードを追加
        for name, module in sorted(self.parser.modules.items()):
            color = self._get_module_color(module.module_type)
            label = self._create_module_label(module)
            
            # インライン要素は点線枠で表示
            if name.startswith('_inline_'):
                lines.append(f'  "{name}" [label="{label}", fillcolor="{color}", style="dashed,filled"];')
            else:
                lines.append(f'  "{name}" [label="{label}", fillcolor="{color}"];')
        
        lines.append('')
        
        # 接続エッジを追加
        for src_module, src_port, tgt_module, tgt_port in self.parser.connections:
            # ポート番号をラベルとして表示
            if src_port > 0:
                label = f"[{src_port}]"
                lines.append(f'  "{src_module}" -> "{tgt_module}" [label="{label}"];')
            else:
                lines.append(f'  "{src_module}" -> "{tgt_module}";')
        
        lines.append('}')
        return '\n'.join(lines)
    
    def save_dot(self, output_path: str):
        """DOTファイルを保存"""
        dot_content = self.generate_dot()
        with open(output_path, 'w') as f:
            f.write(dot_content)
        print(f"✅ DOTファイルを生成しました: {output_path}")
    
    def render(self, output_path: str, format: str = 'png', display: bool = False):
        """Graphvizでレンダリング"""
        dot_content = self.generate_dot()
        dot_file = output_path.rsplit('.', 1)[0] + '.dot'
        
        # DOTファイルを保存
        with open(dot_file, 'w') as f:
            f.write(dot_content)
        
        # Graphvizでレンダリング
        try:
            result = subprocess.run(
                ['dot', f'-T{format}', dot_file, '-o', output_path],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ 画像を生成しました: {output_path}")
            
            # 画像を表示
            if display and format in ['png', 'svg']:
                self._display_image(output_path, format)
            
            return True
        except FileNotFoundError:
            print("⚠️  Graphvizがインストールされていません。")
            print("   Ubuntuの場合: sudo apt install graphviz")
            print("   macOSの場合: brew install graphviz")
            print(f"   DOTファイルのみ生成されました: {dot_file}")
            return False
        except subprocess.CalledProcessError as e:
            print(f"❌ レンダリングエラー: {e.stderr}")
            return False
    
    def _display_image(self, image_path: str, format: str):
        """画像を表示"""
        import os
        
        # 環境変数でディスプレイが利用可能かチェック
        has_display = os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY')
        
        if format == 'png':
            # 方法1: imagemagick/ImageMagick の display コマンド
            try:
                subprocess.run(['display', image_path], check=False, timeout=1)
                return
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            # 方法2: feh (軽量画像ビューア)
            try:
                subprocess.run(['feh', image_path], check=False, timeout=1)
                return
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            # 方法3: eog (GNOME)
            try:
                subprocess.run(['eog', image_path], check=False, timeout=1)
                return
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            # 方法4: xdg-open (デフォルトアプリケーション)
            if has_display:
                try:
                    subprocess.Popen(['xdg-open', image_path], 
                                   stdout=subprocess.DEVNULL, 
                                   stderr=subprocess.DEVNULL)
                    print(f"💡 画像をデフォルトビューアで開きました")
                    return
                except FileNotFoundError:
                    pass
        
        elif format == 'svg':
            # SVGはブラウザで開く
            if has_display:
                try:
                    subprocess.Popen(['xdg-open', image_path],
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
                    print(f"💡 SVGをデフォルトブラウザで開きました")
                    return
                except FileNotFoundError:
                    pass
        
        # どの方法も使えない場合
        print(f"💡 画像を手動で開いてください: {image_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='SymNet Click設定ファイルを可視化',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
例:
  %(prog)s rtx1210.click                     # PNG画像を生成
  %(prog)s rtx1210.click -o router.svg       # SVG形式で出力
  %(prog)s rtx1210.click --display           # 生成後に画像を表示
  %(prog)s rtx1210.click -d -o diagram.png   # 生成して表示
        '''
    )
    
    parser.add_argument('input', help='Click設定ファイル (.click)')
    parser.add_argument('-o', '--output', help='出力ファイル名 (デフォルト: 入力ファイル名.png)')
    parser.add_argument('-d', '--display', action='store_true', 
                       help='生成後に画像を表示')
    parser.add_argument('-f', '--format', choices=['png', 'svg', 'pdf', 'dot'],
                       help='出力フォーマット (デフォルト: 拡張子から自動判定)')
    
    args = parser.parse_args()
    
    input_file = args.input
    
    # 出力ファイル名を決定
    if args.output:
        output_file = args.output
    else:
        # 拡張子を変更
        input_path = Path(input_file)
        output_file = str(input_path.with_suffix('.png'))
    
    # 出力フォーマットを判定
    if args.format:
        output_format = args.format
    else:
        output_format = Path(output_file).suffix[1:] or 'png'
        if output_format not in ['png', 'svg', 'pdf', 'dot']:
            output_format = 'png'
    
    print(f"📄 Click設定を解析中: {input_file}")
    
    # パース
    click_parser = ClickParser(input_file)
    click_parser.parse()
    
    print(f"   モジュール数: {len(click_parser.modules)}")
    print(f"   接続数: {len(click_parser.connections)}")
    
    # 可視化
    visualizer = ClickVisualizer(click_parser)
    
    if output_format == 'dot':
        visualizer.save_dot(output_file)
    else:
        visualizer.render(output_file, output_format, display=args.display)

if __name__ == '__main__':
    main()
