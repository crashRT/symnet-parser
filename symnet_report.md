# SymNet 解析レポート (1 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (2 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -48)
```
Value:       [Const(00:00:00:00:81:00 (MAC))]
```

#### `[Unknown (Offset -32)]` (AbsOffset: -32)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -29)]` (AbsOffset: -29)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -28)]` (AbsOffset: -28)
```
Value:       [Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (3 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (4 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -48)
```
Value:       [Const(00:00:00:00:81:00 (MAC))]
```

#### `[Unknown (Offset -32)]` (AbsOffset: -32)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -29)]` (AbsOffset: -29)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -28)]` (AbsOffset: -28)
```
Value:       [Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (5 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (6 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))])),Some(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (7 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: ~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))), &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (8 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))])),Some(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: ~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))), ~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))), &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (9 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: ~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))), ~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))), ~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))), &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (10 / 11)

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),Some(&(List(>=([Const(0.0.0.0 (IP))]), <=([Const(255.255.255.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: ~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))), ~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))), ~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))), ~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))), &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```

---
<br/>
---

# SymNet 解析レポート (11 / 11)

## 🚦 1. 最終ステータス (Status)
```
No route
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:** `host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out` -> `ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out` -> `poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out` -> `rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`


## 📜 3. 実行された命令 (Instruction Trace)
- **[host1 / host]** `CreateTag(START,+0)`
- **[host1 / host]** `CreateTag(L3,+0)`
- **[host1 / host]** `AllocateRaw(IPVer_IHL,4)`
- **[host1 / host]** `AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPProto,8)`
- **[host1 / host]** `AssignRaw(IPProto,Symb(#29174),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPSrc,32)`
- **[host1 / host]** `AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(IPDst,32)`
- **[host1 / host]** `AssignRaw(IPDst,Symb(#-7282),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)`
- **[host1 / host]** `AllocateRaw(TTL,8)`
- **[host1 / host]** `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(TotalLength,16)`
- **[host1 / host]** `AssignRaw(TotalLength,Symb(#16052),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DSCP_ECN,4)`
- **[host1 / host]** `AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(IPChecksum,16)`
- **[host1 / host]** `AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Identification,16)`
- **[host1 / host]** `AssignRaw(Identification,Symb(#73735),GenericNumeric)`
- **[host1 / host]** `CreateTag(L4,TotalLength0)`
- **[host1 / host]** `AllocateRaw(SrcPort,16)`
- **[host1 / host]** `AssignRaw(SrcPort,Symb(#19440),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(DstPort,16)`
- **[host1 / host]** `AssignRaw(DstPort,Symb(#-7197),GenericNumeric)`
- **[host1 / host]** `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)`
- **[host1 / host]** `AllocateRaw(SeqNo,32)`
- **[host1 / host]** `AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(AckNo,32)`
- **[host1 / host]** `AssignRaw(AckNo,Symb(#-5840),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(DataOffset,4)`
- **[host1 / host]** `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+100,3)`
- **[host1 / host]** `AssignRaw(L4+100,Symb(#42065),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+103,1)`
- **[host1 / host]** `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+104,1)`
- **[host1 / host]** `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+105,1)`
- **[host1 / host]** `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(L4+106,1)`
- **[host1 / host]** `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_NS,1)`
- **[host1 / host]** `AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_URG,1)`
- **[host1 / host]** `AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_ECE,1)`
- **[host1 / host]** `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(Flag_CWR,1)`
- **[host1 / host]** `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / host]** `CreateTag(END,L4+12000)`
- **[host1 / host]** `Forward(host1-host-out)`
- **[host1 / host]** `NoOp`
- **[host1 / host]** `CreateTag(L2,L3--112)`
- **[host1 / host]** `AllocateRaw(EthSrc,48)`
- **[host1 / host]** `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EthDst,48)`
- **[host1 / host]** `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- **[host1 / host]** `AllocateRaw(EtherType,16)`
- **[host1 / host]** `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- **[host1 / etherencap-0]** `Forward(host1-etherencap-0-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / etherencap-0]** `Forward(host1-nic_o-out)`
- **[host1 / etherencap-0]** `NoOp`
- **[host1 / nic_o]** `Forward(ap-wifi1_i-out)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[host1 / nic_o]** `Forward(ap-vlan10-out-0)`
- **[host1 / nic_o]** `NoOp`
- **[host1 / nic_o]** `AllocateSymbol(s)`
- **[host1 / nic_o]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[host1 / nic_o]** `AllocateSymbol(d)`
- **[host1 / nic_o]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[host1 / nic_o]** `DeallocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `DeallocateRaw(EthDst,48)`
- **[host1 / nic_o]** `CreateTag(L2,L2--32)`
- **[host1 / nic_o]** `AllocateRaw(EthSrc,48)`
- **[host1 / nic_o]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EthDst,48)`
- **[host1 / nic_o]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(EtherType,16)`
- **[host1 / nic_o]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+112,3)`
- **[host1 / nic_o]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+115,1)`
- **[host1 / nic_o]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[host1 / nic_o]** `AllocateRaw(L2+116,12)`
- **[host1 / nic_o]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(s)`
- **[host1 / nic_o]** `DeallocateNamedSymbol(d)`
- **[ap / wifi1_i]** `Forward(ap-vlanencap-0-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / wifi1_i]** `Forward(ap-wlan_o-out)`
- **[ap / wifi1_i]** `NoOp`
- **[ap / vlan10]** `Forward(poesw-port1_i-out)`
- **[ap / vlan10]** `NoOp`
- **[ap / vlan10]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[ap / vlan10-out]** `Forward(poesw-tag-out-0)`
- **[ap / vlan10-out]** `NoOp`
- **[ap / vlan10-out]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[ap / vlan10-out]** `AllocateSymbol(s)`
- **[ap / vlan10-out]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateSymbol(d)`
- **[ap / vlan10-out]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `DeallocateRaw(EtherType,16)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+112,3)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+115,1)`
- **[ap / vlan10-out]** `DeallocateRaw(L2+116,12)`
- **[ap / vlan10-out]** `CreateTag(L2,L2+32)`
- **[ap / vlan10-out]** `AllocateRaw(EthSrc,48)`
- **[ap / vlan10-out]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlan10-out]** `AllocateRaw(EthDst,48)`
- **[ap / vlan10-out]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(s)`
- **[ap / vlan10-out]** `DeallocateNamedSymbol(d)`
- **[ap / vlanencap-0]** `Forward(poesw-vlandecap-3-out)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[ap / vlanencap-0]** `Forward(poesw-vlan10-out-0)`
- **[ap / vlanencap-0]** `NoOp`
- **[ap / vlanencap-0]** `AllocateSymbol(s)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateSymbol(d)`
- **[ap / vlanencap-0]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `DeallocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `CreateTag(L2,L2--32)`
- **[ap / vlanencap-0]** `AllocateRaw(EthSrc,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EthDst,48)`
- **[ap / vlanencap-0]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(EtherType,16)`
- **[ap / vlanencap-0]** `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+112,3)`
- **[ap / vlanencap-0]** `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+115,1)`
- **[ap / vlanencap-0]** `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- **[ap / vlanencap-0]** `AllocateRaw(L2+116,12)`
- **[ap / vlanencap-0]** `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(s)`
- **[ap / vlanencap-0]** `DeallocateNamedSymbol(d)`
- **[ap / wlan_o]** `Forward(poesw-vlanencap-2-out)`
- **[ap / wlan_o]** `NoOp`
- **[ap / wlan_o]** `Forward(poesw-port8_o-out)`
- **[ap / wlan_o]** `NoOp`
- **[poesw / port1_i]** `Forward(rtx1210-lan1_i-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- **[poesw / port1_i]** `Forward(rtx1210-Paint-0-out)`
- **[poesw / port1_i]** `NoOp`
- **[poesw / port1_i]** `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- **[poesw / tag]** `Forward(rtx1210-lan1_tag-out-0)`
- **[poesw / tag]** `NoOp`
- **[poesw / tag]** `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- **[poesw / tag]** `AllocateSymbol(s)`
- **[poesw / tag]** `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- **[poesw / tag]** `AllocateSymbol(d)`
- **[poesw / tag]** `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- **[poesw / tag]** `DeallocateRaw(EthSrc,48)`
- **[poesw / tag]** `DeallocateRaw(EthDst,48)`
- **[poesw / tag]** `DeallocateRaw(EtherType,16)`
- **[poesw / tag]** `DeallocateRaw(L2+112,3)`
- **[poesw / tag]** `DeallocateRaw(L2+115,1)`
- **[poesw / tag]** `DeallocateRaw(L2+116,12)`
- **[poesw / tag]** `CreateTag(L2,L2+32)`
- **[poesw / tag]** `AllocateRaw(EthSrc,48)`
- **[poesw / tag]** `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- **[poesw / tag]** `AllocateRaw(EthDst,48)`
- **[poesw / tag]** `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- **[poesw / tag]** `DeallocateNamedSymbol(s)`
- **[poesw / tag]** `DeallocateNamedSymbol(d)`
- **[poesw / tag-out]** `Forward(rtx1210-vlandecap-6-out)`
- **[poesw / tag-out]** `NoOp`
- **[poesw / tag-out]** `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- **[poesw / vlandecap-3]** `Forward(rtx1210-vlan10-out-0)`
- **[poesw / vlandecap-3]** `NoOp`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))]))),Some(~(&(List(>=([Const(0.0.0.0 (IP))]), <=([Const(255.255.255.255 (IP))]))))))`
- **[poesw / vlandecap-3]** `Fail(No route)`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value:       [Const(00:00:5e:00:53:00 (MAC))]
Constraints: ==([Const(00:00:5e:00:53:00 (MAC))])
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value:       [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value:       [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value:       Symb(#-9116)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value:       Symb(#-5033)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value:       Symb(#16052)
```

#### `[Identification]` (AbsOffset: 32)
```
Value:       Symb(#73735)
```

#### `[TTL]` (AbsOffset: 64)
```
Value:       [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value:       Symb(#29174)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value:       Symb(#47508)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value:       Symb(#-1675)
Constraints: &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[IPDst]` (AbsOffset: 128)
```
Value:       Symb(#-7282)
Constraints: ~(&(List(>=([Const(0.0.0.0 (IP))]), <=([Const(255.255.255.255 (IP))])))), ~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))), ~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))), ~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))), ~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))), &(List(>=([Const(0.0.0.0 (IP))]), <=([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])))
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value:       Symb(#19440)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[DstPort]` (AbsOffset: 176)
```
Value:       Symb(#-7197)
Constraints: &(List(>=([Const(0 (Port))]), <=([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])))
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value:       Symb(#-9912)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value:       Symb(#-5840)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value:       [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value:       Symb(#42065)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value:       Symb(#41395)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value:       [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value:       Symb(#71805)
```