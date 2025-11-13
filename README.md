# SymNet Parser

SymNet の検証結果（JSON 形式）を人間が読みやすい Markdown 形式のレポートに変換する Python スクリプトです。

## 概要

SymNet は、ネットワークの動作を記号実行によって検証するツールです。このパーサーは、SymNet が出力する複雑な JSON 形式の検証結果を解析し、以下の情報を見やすく整形します：

- **検証ステータス**: パケットが目的地に到達できたか、失敗したか
- **ポートトレース**: パケットがどのノード・ポートを経由したか（ノードごとに改行）
- **命令トレース**: 各ノードでどのような処理が実行されたか（NoOp 以外を表示）
- **最終メモリ状態**: パケットヘッダーの各フィールドの値と制約条件

## 特徴

### コンテキストに応じた値の表示

- **IP アドレス**: 32 ビット値を `192.168.1.1 (IP)` 形式で表示
- **MAC アドレス**: 48 ビット値を `aa:bb:cc:dd:ee:ff (MAC)` 形式で表示
- **ポート番号**: 16 ビット値を `80 (Port)` 形式で表示
- **その他**: 範囲外の値は `Val: 4294967296 (0x100000000)` 形式で表示

### 読みやすい制約表示

複雑な Scala 形式の制約を以下のように変換：

```
元: ~(&(List(>=([Const(192.168.180.0)]), <=([Const(192.168.183.255)]))))
↓
変換後: NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
```

### ポートトレースの改行

ノードが変わるごとに改行を挿入し、パケットの経路を視覚的に把握しやすくします：

```
`host1-veth1-0` -> `AP-eth1-ap-bridge`
`AP-eth2-ap-bridge` -> `PoE-switch_eth1_1-if_eth`
`PoE-switch_eth8_1-if_eth` -> `RTX1210-lan1.1-eth`
```

### ノード・モジュール情報の表示

各命令がどのノードのどのモジュールで実行されたかを明示：

```
[Node: RTX1210 | Module: ip_forward]
  - If(...) Then Forward('RTX1210-lan1.1-eth) Else NoOp
```

## 必要な環境

- Python 3.6 以上
- 標準ライブラリのみ使用（追加インストール不要）
  - `json`
  - `re`
  - `ipaddress`

## 使い方

### 基本的な使い方

```bash
python3 parse_symnet.py
```

デフォルトでは以下のファイルを使用します：

- **入力**: `symnet_output.json`
- **出力**: `symnet_report.md`

### ファイル名を指定する場合

スクリプトの最後の行を編集してファイル名を変更できます：

```python
if __name__ == "__main__":
    parser = SymNetParser("入力ファイル.json")
    markdown = parser.to_markdown()
    with open("出力ファイル.md", "w", encoding="utf-8") as f:
        f.write(markdown)
    print("✅ レポート生成が完了しました: 出力ファイル.md")
```

## 入力ファイル形式

SymNet の検証結果を JSON 配列として保存したファイル：

```json
[
  {
    "status": "Success(RTX1210-lan3.1-eth)",
    "port_trace": {
      "host1-veth1-0": "AP-eth1-ap-bridge",
      "AP-eth2-ap-bridge": "PoE-switch_eth1_1-if_eth",
      ...
    },
    "instruction_trace": [
      {
        "port": "AP-eth1-ap-bridge",
        "instructions": [...]
      },
      ...
    ],
    "memory": {
      "0": {"value": "...", "constraints": []},
      ...
    }
  },
  ...
]
```

## 出力ファイル形式

Markdown 形式のレポートが生成され、以下のセクションで構成されます：

### 1. Status（検証結果）

```markdown
## Report 1

### Status

Success(RTX1210-lan3.1-eth)
```

### 2. Port Trace（ポート経路）

```markdown
### Port Trace

`host1-veth1-0` -> `AP-eth1-ap-bridge`
`AP-eth2-ap-bridge` -> `PoE-switch_eth1_1-if_eth`
```

### 3. Instruction Trace（命令トレース）

```markdown
### Instruction Trace

#### Port: `AP-eth1-ap-bridge`

[Node: AP | Module: ap-bridge]

- If(...) Then Forward('AP-eth2-ap-bridge) Else NoOp
```

### 4. Final Memory State（メモリ状態）

```markdown
### Final Memory State

#### `[EthDst]` (AbsOffset: 0)

Value: Symb(#12345)
Constraints:

- == aa:bb:cc:dd:ee:ff (MAC)
```

## フィールド名の対応表

スクリプトは以下のオフセットをフィールド名に変換します：

| オフセット | フィールド名 | 説明                            |
| ---------- | ------------ | ------------------------------- |
| 0          | EthDst       | イーサネット宛先 MAC アドレス   |
| 48         | EthSrc       | イーサネット送信元 MAC アドレス |
| 96         | EthType      | イーサネットタイプ              |
| 112        | VLAN         | VLAN ID                         |
| 128        | VLAN2        | 2 重タグ VLAN ID                |
| 56         | IPVer        | IP バージョン                   |
| 60         | IPHL         | IP ヘッダー長                   |
| 64         | IPTOS        | IP サービスタイプ               |
| 68         | IPLen        | IP パケット長                   |
| 72         | IPProto      | IP プロトコル                   |
| 80         | IPChecksum   | IP チェックサム                 |
| 96         | IPSrc        | IP 送信元アドレス               |
| 128        | IPDst        | IP 宛先アドレス                 |
| 160        | SrcPort      | 送信元ポート番号                |
| 176        | DstPort      | 宛先ポート番号                  |

## カスタマイズ

### 新しいフィールドの追加

`KNOWN_OFFSETS` 辞書に追加することで、新しいオフセットをフィールド名にマッピングできます：

```python
self.KNOWN_OFFSETS = {
    192: "YourField",  # 新しいフィールドを追加
    ...
}
```

### 制約フォーマットのカスタマイズ

`_format_constraint()` メソッドを編集することで、制約の表示形式を変更できます：

```python
def _format_constraint(self, constraint: str) -> str:
    # ここに独自の変換ロジックを追加
    ...
```

## トラブルシューティング

### JSON ファイルが見つからない

```
FileNotFoundError: [Errno 2] No such file or directory: 'symnet_output.json'
```

→ `symnet_output.json` が同じディレクトリに存在することを確認してください。

### JSON 形式エラー

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

→ 入力ファイルが正しい JSON 形式であることを確認してください。

### 文字化け

→ スクリプトは UTF-8 エンコーディングを使用しています。入力ファイルも UTF-8 であることを確認してください。

## ライセンス

このスクリプトは自由に使用・改変できます。

## 更新履歴

- **2025-11-13**: 初版作成
  - ポート名に個別バッククォート追加
  - ノード・モジュール情報表示
  - ポートトレースの改行処理
  - 制約の読みやすい表示
  - コンテキストに応じた値の変換
