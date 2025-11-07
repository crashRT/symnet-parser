import json
import re
import ipaddress
from typing import Dict, Any

# --- 1. 定数変換ヘルパー関数 (変更なし) ---

def int_to_mac(val: int) -> str | None:
    if not (0 <= val <= 281474976710655):
        return None
    hex_str = f'{val:012x}'
    return ':'.join(hex_str[i:i+2] for i in (0, 2, 4, 6, 8, 10))

def int_to_ip(val: int) -> str | None:
    if not (0 <= val <= 4294967295):
        return None
    return str(ipaddress.IPv4Address(val))

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
        'L2': { 0: 'EthDst', 48: 'EthSrc', 96: 'EtherType' },
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
        parts = port_name.rsplit('-', 1)
        if len(parts) == 2:
            node_module = parts[0]
            return node_module.split('-', 1) if '-' in node_module else (node_module, '')
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
        
        # 命令とポートを対応付ける
        current_node = None
        current_module = None
        port_idx = 0
        
        # 最初のポートから開始
        if 0 in port_map:
            current_node, current_module = self._parse_port_name(port_map[0])
        
        for item in self.data['instruction_trace']:
            idx_str, instruction = list(item.items())[0]
            
            # Forward命令でポートが変わる
            if instruction.startswith('Forward('):
                port_idx += 1
                if port_idx in port_map:
                    current_node, current_module = self._parse_port_name(port_map[port_idx])
            
            # NoOp命令を簡略化
            if instruction.startswith('org.change.v2.analysis.processingmodels.instructions.NoOp'):
                instruction = 'NoOp'
            
            # ノード・モジュール情報を付加
            location = ""
            if current_node:
                if current_module:
                    location = f"**[{current_node} / {current_module}]** "
                else:
                    location = f"**[{current_node}]** "
            
            md_lines.append(f"- {location}`{self._translate_string(instruction)}`")
        
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

# --- 3. 実行 (変更なし) ---
if __name__ == "__main__":
    input_json_file = 'symnet_output.json'
    output_markdown_file = 'symnet_report.md'
    
    all_markdown_reports = [] 

    try:
        with open(input_json_file, 'r') as f:
            data_list = json.load(f) 
            
        if not isinstance(data_list, list):
            if isinstance(data_list, dict):
                data_list = [data_list]
            else:
                print(f"エラー: 入力JSONはオブジェクトまたはオブジェクトのリストである必要があります。")
                exit() 

        if not data_list:
            print("警告: 入力JSONリストが空です。")
            exit()

        for i, data_item in enumerate(data_list):
            if not isinstance(data_item, dict):
                print(f"警告: リストの {i} 番目のアイテムがJSONオブジェクトではありません。スキップします。")
                continue
                
            parser = SymNetParser(data_item)
            markdown_output = parser.to_markdown()
            
            report_title = f"# SymNet 解析レポート ({i + 1} / {len(data_list)})"
            
            markdown_output = markdown_output.replace(
                "# SymNet 解析レポート", 
                report_title
            )
            
            all_markdown_reports.append(markdown_output)

        if not all_markdown_reports:
            print("エラー: 有効なレポートが生成されませんでした。")
            exit()

        with open(output_markdown_file, 'w', encoding='utf-8') as f:
            f.write("\n\n---\n<br/>\n---\n\n".join(all_markdown_reports))
            
        print(f"✅ {len(all_markdown_reports)} 件のレポート生成が完了しました: {output_markdown_file}")
        
    except FileNotFoundError:
        print(f"エラー: '{input_json_file}' が見つかりません。")
        print(f"JSONデータを '{input_json_file}' という名前で保存してください。")
    except json.JSONDecodeError:
        print("エラー: JSONのパースに失敗しました。ファイルが破損している可能性があります。")