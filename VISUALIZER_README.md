# Click Configuration Visualizer

SymNetのClick設定ファイルを解析して、モジュール間の接続を視覚的に表示するツールです。

## 機能

- Click設定ファイル（.click）を解析
- モジュール間の接続関係をグラフとして可視化
- モジュールタイプに応じた色分け
- PNG/SVG/PDF形式での出力

## 必要な環境

### Python
- Python 3.6 以上
- 標準ライブラリのみ使用（追加インストール不要）

### Graphviz（画像生成用）
```bash
# Ubuntu/Debian
sudo apt install graphviz

# macOS
brew install graphviz
```

**注意**: Graphvizがインストールされていない場合でも、DOT形式のファイルは生成されます。

## 使い方

### 基本的な使い方

```bash
python3 visualize_click.py <click設定ファイル> [出力ファイル]
```

### 例

```bash
# PNG画像を生成（デフォルト）
python3 visualize_click.py rtx1210.click

# 出力ファイル名を指定
python3 visualize_click.py rtx1210.click router_diagram.png

# SVG形式で出力
python3 visualize_click.py rtx1210.click router_diagram.svg

# PDF形式で出力
python3 visualize_click.py rtx1210.click router_diagram.pdf

# DOT形式のみ生成（Graphviz不要）
python3 visualize_click.py rtx1210.click router_diagram.dot
```

## 出力例

### モジュールの色分け

各モジュールタイプは以下のように色分けされます：

| モジュールタイプ | 色 | 説明 |
|-----------------|-----|------|
| FromDevice | 水色 | 入力デバイス |
| ToDevice | ピンク | 出力デバイス |
| IPClassifier | オレンジ | パケット分類器 |
| LinearIPLookup | 緑 | ルーティングテーブル |
| EtherEncap/Decap | 青/紫 | イーサネットカプセル化 |
| VLANEncap/Decap | ピンク紫/青紫 | VLANカプセル化 |
| Discard/Null | グレー | 破棄 |
| Paint | 黄色 | パケットマーキング |

### グラフの読み方

- **ボックス**: 各Clickモジュール
- **矢印**: モジュール間の接続
- **[番号]**: 出力ポート番号（複数出力がある場合）

### サンプル出力

rtx1210.clickの場合：

```
lan1_i (FromDevice) 
  ↓
lan1_tag (IPClassifier)
  ├─[0]→ VLANDecap → vlan10
  ├─[1]→ VLANDecap → vlan20
  └─[2]→ VLANDecap → Discard

vlan10 (IPClassifier)
  ├─[0]→ EtherDecap → routing
  └─[1]→ vlan10_out

routing (LinearIPLookup)
  ├─[0]→ cpu
  ├─[1]→ vlan10_nexthop
  ├─[2]→ vlan20_nexthop
  └─[3]→ lan3_o
```

## Click設定ファイルの形式

このツールは以下の形式のClick設定を解析します：

```click
// モジュール定義
module_name :: ModuleType(config_params);

// 接続
source -> target
source[port_number] -> target
source -> intermediate -> target
```

### 例

```click
lan3_i :: FromDevice();
lan3_o :: ToDevice();

routing :: LinearIPLookup(192.168.127.1/32 0 onlink, 192.168.127.0/24 1 onlink);

lan3_i -> EtherDecap() -> routing
routing[0] -> cpu
routing[1] -> vlan10_out
routing[3] -> lan3_o
```

## 対応している機能

### ✅ サポート済み

- モジュール定義の解析
- 単純な接続（A -> B）
- ポート番号付き接続（A[0] -> B）
- チェーン接続（A -> B -> C）
- コメントの除去（//）

### ⚠️ 制限事項

- 複雑なClick記法（条件分岐など）は未対応
- インライン要素は別モジュールとして扱われます
- 入力ポート番号は常に0として扱われます

## トラブルシューティング

### Graphvizがインストールされていない

```
⚠️  Graphvizがインストールされていません。
   DOTファイルのみ生成されました: rtx1210.dot
```

→ Graphvizをインストールするか、DOTファイルをオンラインビューアで表示できます：
- https://dreampuf.github.io/GraphvizOnline/
- https://edotor.net/

### モジュールが表示されない

→ Click設定ファイルの形式を確認してください。`name :: Type(config)` の形式である必要があります。

### 接続が表示されない

→ 接続は `->` 演算子で表現されている必要があります。モジュール名が正しく定義されているか確認してください。

## カスタマイズ

### モジュールの色を変更

`visualize_click.py`の`MODULE_COLORS`辞書を編集：

```python
MODULE_COLORS = {
    'FromDevice': '#E8F4F8',  # お好みの色コードに変更
    'YourModule': '#ABCDEF',  # 新しいモジュールタイプを追加
}
```

### レイアウト方向を変更

DOTファイルの`rankdir`を編集：

```python
'rankdir=LR;'  # 左から右（デフォルト）
'rankdir=TB;'  # 上から下
'rankdir=RL;'  # 右から左
'rankdir=BT;'  # 下から上
```

## ライセンス

このツールは自由に使用・改変できます。

## 更新履歴

- **2025-11-14**: 初版作成
  - Click設定ファイルの解析
  - Graphvizによる可視化
  - モジュールタイプ別の色分け
  - PNG/SVG/PDF/DOT形式の出力
