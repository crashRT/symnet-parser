import json
import re
import ipaddress
from typing import Dict, Any

# --- 1. 定数変換ヘルパー関数 ---

# SymNetでは、Z3のInt型の範囲制限（-2^31 ~ 2^31-1）に対応するため、
# IPアドレスを格納する際に2^31を引いている
IP_OFFSET = 2147483648  # 2^31

def int_to_mac(val: int) -> str | None:
    if not (0 <= val <= 281474976710655):
        return None
    hex_str = f'{val:012x}'
    return ':'.join(hex_str[i:i+2] for i in (0, 2, 4, 6, 8, 10))

def int_to_ip(val: int) -> str | None:
    # SymNetから来た値は2^31引かれているので、元に戻す
    unsigned_val = val + IP_OFFSET
    
    if not (0 <= unsigned_val <= 4294967295):
        return None
    return str(ipaddress.IPv4Address(unsigned_val))

def format_constant(val_str: str, context_field_name: str | None = None) -> str:
    try:
        val = int(val_str)
    except ValueError:
        return val_str

    if val == 2048: return "IPv4 (0x0800)"
    if val == 2054: return "ARP (0x0806)"
    if val == 34525: return "VLAN (0x8100)"

    if context_field_name:
        if context_field_name.startswith("IP"):
            if (ip_val := int_to_ip(val)):
                return f"{ip_val} (IP)"
            else:
                # IPフィールドだが範囲外の値
                return f"Val: {val} (0x{val:x})"
        elif context_field_name.startswith("Eth"):
            if (mac_val := int_to_mac(val)):
                return f"{mac_val} (MAC)"
            else:
                # MACフィールドだが範囲外の値
                return f"Val: {val} (0x{val:x})"
        elif context_field_name.endswith("Port"):
            if 0 <= val <= 65535:
                if val == 80: return "80 (Port: HTTP)"
                if val == 443: return "443 (Port: HTTPS)"
                if val == 22: return "22 (Port: SSH)"
                if val == 53: return "53 (Port: DNS)"
                return f"{val} (Port)"
            else:
                # ポートフィールドだが範囲外の値
                return f"Val: {val} (0x{val:x})"

    possible_formats = []
    ip_val = int_to_ip(val)
    mac_val = int_to_mac(val)

    if ip_val:
        possible_formats.append(f"IP: {ip_val}")
    if mac_val:
        possible_formats.append(f"MAC: {mac_val}")

    raw_str = ""
    if val == 80: raw_str = "80 (Port: HTTP)"
    elif val == 443: raw_str = "443 (Port: HTTPS)"
    elif val == 22: raw_str = "22 (Port: SSH)"
    elif val == 53: raw_str = "53 (Port: DNS)"
    elif 0 <= val <= 65535:
        raw_str = f"Val: {val}"
    else:
        raw_str = f"Val: {val} (0x{val:x})"

    if not ip_val and not mac_val:
        return raw_str
    
    possible_formats.append(raw_str)
    return " / ".join(possible_formats)


# --- 2. メインのパーサクラス (to_markdown を修正) ---

class SymNetParser:
    
    KNOWN_OFFSETS = {
        'L2': { 
            0: 'EthDst', 
            48: 'EthSrc', 
            96: 'EtherType',
            112: 'VLAN_PCP',      # Priority Code Point (3 bits)
            115: 'VLAN_DEI',      # Drop Eligible Indicator (1 bit)
            116: 'VLAN_VID'       # VLAN Identifier (12 bits)
        },
        'L3': { 0: 'IPVer_IHL', 4: 'DSCP_ECN', 16: 'TotalLength', 32: 'Identification', 64: 'TTL', 72: 'IPProto', 80: 'IPChecksum', 96: 'IPSrc', 128: 'IPDst' },
        'L4': { 0: 'SrcPort', 16: 'DstPort', 32: 'SeqNo', 64: 'AckNo', 96: 'DataOffset', 107: 'Flag_NS', 108: 'Flag_CWR', 109: 'Flag_ECE', 110: 'Flag_URG', 111: 'Flag_ACK', 112: 'Flag_PSH', 113: 'Flag_RST', 114: 'Flag_SYN', 115: 'Flag_FIN' }
    }
    
    # ( __init__ は変更なし)
    def __init__(self, json_data: Dict[str, Any]):
        self.data = json_data
        self.tags = {}
        self.abs_field_map = {}
        self.string_field_map = {}

        for tag_obj in self.data.get('memory', {}).get('tags', []):
            name, offset = list(tag_obj.items())[0]
            self.tags[name] = offset

        for tag_name, base_offset in self.tags.items():
            if tag_name in self.KNOWN_OFFSETS:
                for rel_offset, field_name in self.KNOWN_OFFSETS[tag_name].items():
                    self.string_field_map[f"{tag_name}+{rel_offset}"] = field_name
                    self.abs_field_map[base_offset + rel_offset] = field_name
    
    def _parse_port_name(self, port_name: str) -> tuple[str, str]:
        """ポート名からノード名とモジュール名を抽出する"""
        # ポート名の形式: <ノード>-<モジュール>-<方向>
        # 例: host1-host-in, ap-wifi1_i-in, rtx1210-lan1_i-in
        parts = port_name.split('-', 1)  # 最初の '-' で分割
        if len(parts) == 2:
            node = parts[0]
            # 残りの部分から方向 ("-in", "-out") を除去
            module_part = parts[1]
            if module_part.endswith('-in'):
                module = module_part[:-3]
            elif module_part.endswith('-out'):
                module = module_part[:-4]
            else:
                module = module_part
            return (node, module)
        return (port_name, '')
    
    def _format_constraint(self, constraint: str) -> str:
        """制約を読みやすく整形する"""
        # ~(&(List(...))) のような否定制約を検出
        if constraint.startswith('~(&(List('):
            # 否定制約を抽出
            inner = constraint[9:-3]  # "~(&(List(" と ")))" を削除
            parts = inner.split('), ')
            if len(parts) == 2:
                # [Const(...)] の部分を抽出
                min_part = parts[0].split('[Const(')[1].split(')]')[0]
                max_part = parts[1].split('[Const(')[1].split(')]')[0]
                return f"NOT IN [{min_part} - {max_part}]"
        
        # &(List(...)) のような範囲制約を検出
        elif constraint.startswith('&(List('):
            inner = constraint[7:-2]  # "&(List(" と "))" を削除
            parts = inner.split('), ')
            if len(parts) == 2:
                # [Const(...)] の部分を抽出
                min_part = parts[0].split('[Const(')[1].split(')]')[0]
                max_part = parts[1].split('[Const(')[1].split(')]')[0]
                return f"IN [{min_part} - {max_part}]"
        
        # ==(...) のような等価制約
        elif constraint.startswith('==([Const('):
            value = constraint.split('[Const(')[1].split(')]')[0]
            return f"== {value}"
        
        return constraint

    # ( _translate_string は変更なし)
    def _translate_string(self, s: str, context_field_name: str | None = None) -> str:
        if not isinstance(s, str):
            return str(s)

        inferred_context = context_field_name
        if inferred_context is None:
            for key, name in self.string_field_map.items():
                if key in s:
                    inferred_context = name
                    break 

        s = re.sub(
            r'\[Const\((\d+)\)\]',
            lambda m: f"[Const({format_constant(m.group(1), inferred_context)})]",
            s
        )
        
        sorted_keys = sorted(self.string_field_map.keys(), key=len, reverse=True)
        for key in sorted_keys:
            s = s.replace(key, self.string_field_map[key])
        
        return s

    def to_markdown(self) -> str:
        """解析結果を人間可読なMarkdown文字列として生成する"""
        md_lines = []
        md_lines.append("# SymNet 解析レポート\n") # この見出しは後で置換されます

        # --- 1. Status ---
        md_lines.append("## 🚦 1. 最終ステータス (Status)")
        md_lines.append("```")
        md_lines.append(self._translate_string(self.data['status']))
        md_lines.append("```")
        md_lines.append("\n")

        # --- 2. Port Trace ---
        md_lines.append("## 🗺️ 2. パケットの経路 (Port Trace)")
        
        # ポート情報を一度だけ読み取る
        port_map = {}
        path_ports = []
        for item in self.data['port_trace']:
            idx_str, port_name = list(item.items())[0]
            port_map[int(idx_str)] = port_name
            path_ports.append(port_name)
        
        # ノードが変わったら改行を入れる
        path_lines = []
        current_line = []
        prev_node = None
        
        for port in path_ports:
            node, _ = self._parse_port_name(port)
            
            if prev_node is not None and node != prev_node:
                # ノードが変わったので、現在の行を保存して新しい行を開始
                path_lines.append(" -> ".join(f"`{p}`" for p in current_line))
                current_line = [port]
            else:
                current_line.append(port)
            
            prev_node = node
        
        # 最後の行を追加
        if current_line:
            path_lines.append(" -> ".join(f"`{p}`" for p in current_line))
        
        md_lines.append("**Path:**")
        for line in path_lines:
            md_lines.append(f"{line}  ")
        md_lines.append("\n")

        # --- 3. Instruction Trace ---
        md_lines.append("## 📜 3. 実行された命令 (Instruction Trace)")
        
        for i, item in enumerate(self.data['instruction_trace']):
            idx_str, instruction = list(item.items())[0]
            
            # NoOp命令を簡略化
            if instruction.startswith('org.change.v2.analysis.processingmodels.instructions.NoOp'):
                instruction = 'NoOp'
            
            is_forward = instruction.startswith('Forward(')
            
            md_lines.append(f"- `{self._translate_string(instruction)}`")
            
            # Forward命令のあとに区切り線を追加（最後のForwardを除く）
            if is_forward and i < len(self.data['instruction_trace']) - 1:
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
        
        md_lines.append("\n")

        # --- 4. Memory State ---
        md_lines.append("## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)")
        
        md_lines.append("### タグ (Tags)")
        tags_str = ", ".join([f"`{name}: {offset}`" for name, offset in self.tags.items()])
        md_lines.append(tags_str)
        md_lines.append("\n")
        
        md_lines.append("### ヘッダーフィールド (Header Fields)")
        
        fields = []
        for item in self.data['memory']['header_fields']:
            offset_str, data = item.popitem()
            fields.append((int(offset_str), data))
        fields.sort(key=lambda x: x[0])
        
        for offset, data in fields:
            field_name = self.abs_field_map.get(offset, f"Unknown (Offset {offset})")
            
            expr = self._translate_string(data['expression'], field_name)
            constraints = [self._translate_string(c, field_name) for c in data['constraints']]
            
            md_lines.append(f"\n#### `[{field_name}]` (AbsOffset: {offset})")
            md_lines.append("```")
            md_lines.append(f"Value: {expr}")
            if constraints:
                md_lines.append("Constraints:")
                for c in constraints:
                    formatted = self._format_constraint(c)
                    md_lines.append(f"  - {formatted}")
            md_lines.append("```")

        return "\n".join(md_lines)

# --- 3. 実行 ---
if __name__ == "__main__":
    input_json_files = [
        ('sefl.ok.json', '✅ OK'),
        ('sefl.fail.json', '❌ FAIL')
    ]
    
    all_markdown_reports = [] 
    ok_count = 0
    fail_count = 0
    fail_statuses = []

    for input_json_file, status_label in input_json_files:
        try:
            with open(input_json_file, 'r') as f:
                data_list = json.load(f) 
                
            if not isinstance(data_list, list):
                if isinstance(data_list, dict):
                    data_list = [data_list]
                else:
                    print(f"エラー: {input_json_file} の形式が不正です。")
                    continue

            if not data_list:
                print(f"警告: {input_json_file} が空です。")
                continue

            for data_item in data_list:
                if not isinstance(data_item, dict):
                    print(f"警告: {input_json_file} 内の一部のアイテムがJSONオブジェクトではありません。スキップします。")
                    continue
                    
                parser = SymNetParser(data_item)
                markdown_output = parser.to_markdown()
                all_markdown_reports.append((markdown_output, status_label))
                
                # OK/FAILのカウント
                if status_label == '✅ OK':
                    ok_count += 1
                else:
                    fail_count += 1
                    # FAILの場合はステータスを記録
                    status = data_item.get('status', 'Unknown')
                    fail_statuses.append(status)
            
            print(f"✅ {input_json_file} を読み込みました ({len(data_list)} 件)")
                
        except FileNotFoundError:
            print(f"警告: '{input_json_file}' が見つかりません。スキップします。")
        except json.JSONDecodeError:
            print(f"エラー: {input_json_file} のJSONパースに失敗しました。")

    if not all_markdown_reports:
        print("エラー: 有効なレポートが生成されませんでした。")
        exit()

    # サマリーセクションを作成
    summary_lines = []
    summary_lines.append("# 🔍 SymNet 解析サマリー\n")
    summary_lines.append(f"**総数**: {ok_count + fail_count} 件")
    summary_lines.append(f"- ✅ **OK**: {ok_count} 件")
    summary_lines.append(f"- ❌ **FAIL**: {fail_count} 件\n")
    
    if fail_count > 0:
        summary_lines.append("## ❌ FAILの詳細\n")
        for i, status in enumerate(fail_statuses, 1):
            # ステータスを整形（最初のparserのインスタンスを使用）
            formatted_status = all_markdown_reports[0][0]  # ダミー
            # 新しいダミーパーサーを作成してステータスを整形
            dummy_parser = SymNetParser({'memory': {'tags': []}, 'status': status, 'port_trace': [], 'instruction_trace': []})
            formatted_status = dummy_parser._translate_string(status)
            
            summary_lines.append(f"### FAIL {i}")
            summary_lines.append("```")
            summary_lines.append(formatted_status)
            summary_lines.append("```\n")
    
    summary = "\n".join(summary_lines)

    # レポート番号を付与
    total = len(all_markdown_reports)
    formatted_reports = []
    for i in range(total):
        markdown_output, status_label = all_markdown_reports[i]
        report_title = f"# SymNet 解析レポート ({i + 1} / {total}) {status_label}"
        markdown_output = markdown_output.replace(
            "# SymNet 解析レポート", 
            report_title
        )
        formatted_reports.append(markdown_output)

    # 結果を書き出し（サマリーを先頭に追加）
    output_markdown_file = 'symnet_report.md'
    with open(output_markdown_file, 'w', encoding='utf-8') as f:
        f.write(summary)
        f.write("\n---\n<br/>\n---\n\n")
        f.write("\n\n---\n<br/>\n---\n\n".join(formatted_reports))
        
    print(f"✅ 合計 {total} 件のレポート生成が完了しました: {output_markdown_file}")