# SymNet Parser

SymNet の検証結果（JSON 形式）を人間が読みやすい Markdown 形式のレポートに変換する Python スクリプトです。

## 概要

SymNet は、ネットワークの動作を記号実行によって検証するツールです。このパーサーは、SymNet が出力する複雑な JSON 形式の検証結果を解析し、以下の情報を見やすく整形します：

- **サマリー**: OK/FAIL の件数と失敗ステータスの一覧
- **検証ステータス**: パケットが目的地に到達できたか、失敗したか
- **ポートトレース**: パケットがどのノード・ポートを経由したか（ノードごとに改行）
- **命令トレース**: 各ノードでどのような処理が実行されたか（Forward 命令で区切り）
- **最終メモリ状態**: パケットヘッダーの各フィールドの値と制約条件

## 特徴

### コンテキストに応じた値の表示

- **IP アドレス**: 32 ビット値を `192.168.1.1 (IP)` 形式で表示
  - **IP オフセット変換**: SymNet では Z3 の 32 ビット符号付き整数型の制限（-2^31 ~ 2^31-1）に対応するため、IP アドレス値から 2^31 を引いて格納しています。パーサーは自動的に 2^31 を足し戻して正しい IP アドレスを表示します。
  - 例: `-2147483648` → `0.0.0.0`, `-1062731776` → `192.168.0.1`, `2147483647` → `255.255.255.255`
- **MAC アドレス**: 48 ビット値を `aa:bb:cc:dd:ee:ff (MAC)` 形式で表示
- **ポート番号**: 16 ビット値を `80 (Port: HTTP)` 形式で表示
- **EtherType**: `2048` → `IPv4 (0x0800)`, `2054` → `ARP (0x0806)`, `34525` → `VLAN (0x8100)`
- **その他**: 範囲外の値は `Val: 4294967296 (0x100000000)` 形式で表示

### 読みやすい制約表示

複雑な Scala 形式の制約を以下のように変換：

```
元: &(List(>=([Const(192.168.180.0)]), <=([Const(192.168.183.255)])))
↓
変換後: IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]

元: ~(&(List(>=([Const(192.168.180.0)]), <=([Const(192.168.183.255)]))))
↓
変換後: NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]

元: ==([Const(192.168.1.1)])
↓
変換後: == 192.168.1.1 (IP)
```

### ポートトレースの改行

ノードが変わるごとに改行を挿入し、パケットの経路を視覚的に把握しやすくします：

```
`host1-host-out` -> `host1-veth1-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-ap_bridge-in`  
`ap-ap_bridge-out` -> `ap-eth1-out`  
```

### ノード・モジュール情報の表示（削除）

~~各命令がどのノードのどのモジュールで実行されたかを明示：~~

~~```~~  
~~[Node: RTX1210 | Module: ip_forward]~~  
~~  - If(...) Then Forward('RTX1210-lan1.1-eth) Else NoOp~~  
~~```~~

**注**: 現在のバージョンでは、命令トレースは Forward 命令ごとに区切られ、NoOp 命令は簡略化されます。

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

- **入力**: `sefl.ok.json` と `sefl.fail.json`（両方のファイルから読み込み）
- **出力**: `symnet_report.md`

出力には以下が含まれます：
- サマリーセクション（OK/FAIL の件数と失敗ステータス）
- 各実行パスの詳細レポート（OK と FAIL にラベル付け）

### ファイル名を指定する場合

スクリプトの最後の方にある `input_json_files` リストを編集してファイル名を変更できます：

```python
if __name__ == "__main__":
    input_json_files = [
        ('sefl.ok.json', '✅ OK'),
        ('sefl.fail.json', '❌ FAIL')
    ]
    # ...
```

## 入力ファイル形式

SymNet の検証結果を JSON 配列として保存したファイル（`sefl.ok.json` と `sefl.fail.json`）：

```json
[
  {
    "status": "Success(rtx1210-lan3_o-out)",
    "port_trace": [
      {"0": "host1-host-in"},
      {"1": "host1-host-out"},
      ...
    ],
    "instruction_trace": [
      {"0": "Forward(host1-veth1-out)"},
      {"1": "org.change.v2.analysis.processingmodels.instructions.NoOp@..."},
      ...
    ],
    "memory": {
      "tags": [
        {"L2": 0},
        {"L3": 112},
        {"L4": 272}
      ],
      "header_fields": [
        {"0": {
          "expression": "Symb(#12345)",
          "constraints": ["==([Const(11819540237312)])"]
        }},
        ...
      ]
    }
  }
]
```

## 出力ファイル形式

Markdown 形式のレポートが生成され、以下のセクションで構成されます：

### 0. Summary（サマリー）

```markdown
# 🔍 SymNet 解析サマリー

**総数**: 131 件
- ✅ **OK**: 3 件
- ❌ **FAIL**: 128 件

## ❌ FAILの詳細

### FAIL 1
```
Fail(cannot :&:(:>=:([Const(-2147483648)]), :<=:([Const(2147483647)])))
```
```

### 1. Status（検証結果）

```markdown
# SymNet 解析レポート (1 / 131) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
Success(rtx1210-lan3_o-out)
```
```

### 2. Port Trace（ポート経路）

```markdown
## 🗺️ 2. パケットの経路 (Port Trace)

**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-veth1-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-ap_bridge-in`  
```

### 3. Instruction Trace（命令トレース）

```markdown
## 📜 3. 実行された命令 (Instruction Trace)

- `Forward(host1-veth1-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-in)`
```

### 4. Final Memory State（メモリ状態）

```markdown
## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)

### タグ (Tags)
`L2: 0`, `L3: 112`, `L4: 272`

### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: 0)
```
Value: Symb(#12345)
Constraints:
  - == aa:bb:cc:dd:ee:ff (MAC)
```
```

## フィールド名の対応表

スクリプトは以下のオフセットをフィールド名に変換します：

### L2（レイヤー2 - イーサネット）

| オフセット | フィールド名 | 説明                           |
| ---------- | ------------ | ------------------------------ |
| 0          | EthDst       | イーサネット宛先 MAC アドレス  |
| 48         | EthSrc       | イーサネット送信元 MAC アドレス |
| 96         | EtherType    | イーサネットタイプ             |
| 112        | VLAN_PCP     | VLAN 優先度（3 ビット）         |
| 115        | VLAN_DEI     | VLAN Drop Eligible（1 ビット）  |
| 116        | VLAN_VID     | VLAN ID（12 ビット）            |

### L3（レイヤー3 - IP）

| オフセット | フィールド名   | 説明                |
| ---------- | -------------- | ------------------- |
| 0          | IPVer_IHL      | IP バージョン+ヘッダー長 |
| 4          | DSCP_ECN       | サービスタイプ      |
| 16         | TotalLength    | パケット長          |
| 32         | Identification | 識別子              |
| 64         | TTL            | 生存時間            |
| 72         | IPProto        | プロトコル          |
| 80         | IPChecksum     | チェックサム        |
| 96         | IPSrc          | 送信元 IP アドレス   |
| 128        | IPDst          | 宛先 IP アドレス     |

### L4（レイヤー4 - TCP/UDP）

| オフセット | フィールド名 | 説明                      |
| ---------- | ------------ | ------------------------- |
| 0          | SrcPort      | 送信元ポート番号          |
| 16         | DstPort      | 宛先ポート番号            |
| 32         | SeqNo        | シーケンス番号（TCP）      |
| 64         | AckNo        | 確認応答番号（TCP）        |
| 96         | DataOffset   | データオフセット（TCP）    |
| 107-115    | Flag_*       | TCP フラグ（NS～FIN）      |

## カスタマイズ

### 新しいフィールドの追加

`KNOWN_OFFSETS` 辞書に追加することで、新しいオフセットをフィールド名にマッピングできます：

```python
self.KNOWN_OFFSETS = {
    'L2': { 
        0: 'EthDst', 
        48: 'EthSrc', 
        # ...
        144: 'YourNewField',  # 新しいフィールドを追加
    },
    # ...
}
```

### IP オフセット値の調整

Z3 の整数型制限に対応するため、IP アドレスのオフセット値を変更できます：

```python
# SymNetでのIP変換に対応（デフォルト: 2^31）
IP_OFFSET = 2147483648  # この値を変更
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
警告: 'sefl.ok.json' が見つかりません。スキップします。
```

→ `sefl.ok.json` または `sefl.fail.json` が同じディレクトリに存在することを確認してください。両方のファイルがなくてもエラーにはなりませんが、少なくとも1つは必要です。

### JSON 形式エラー

```
エラー: sefl.ok.json のJSONパースに失敗しました。
```

→ 入力ファイルが正しい JSON 配列形式であることを確認してください。

### IP アドレスの表示がおかしい

→ `IP_OFFSET` の値が SymNet 側の実装と一致しているか確認してください。SymNet では `RepresentationConversion.scala` の `IP_OFFSET` と同じ値（デフォルト: 2147483648）を使用する必要があります。

### 文字化け

→ スクリプトは UTF-8 エンコーディングを使用しています。入力ファイルも UTF-8 であることを確認してください。

## ライセンス

このスクリプトは自由に使用・改変できます。

## 更新履歴

- **2025-11-13 (v2)**: IP オフセット変換対応
  - Z3 の 32 ビット符号付き整数対応のため、IP アドレス値に 2^31 を足し戻す機能を追加
  - サマリーセクションの追加（OK/FAIL 件数と失敗ステータス一覧）
  - 複数の JSON ファイル（sefl.ok.json, sefl.fail.json）からの読み込み
  - OK/FAIL ラベルをレポートタイトルに表示
  - VLAN フィールドの追加（VLAN_PCP, VLAN_DEI, VLAN_VID）
  
- **2025-11-13 (v1)**: 初版作成
  - ポート名に個別バッククォート追加
  - ポートトレースの改行処理（ノード単位）
  - 制約の読みやすい表示（IN/NOT IN 形式）
  - コンテキストに応じた値の変換（IP/MAC/Port）
  - Forward 命令での区切り線挿入
