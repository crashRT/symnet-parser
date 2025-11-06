# SymNet 解析レポート

---
## 🚦 1. 最終ステータス (Status)
---
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


---
## 🗺️ 2. パケットの経路 (Port Trace)
---
**Path:** `host1 -> host1 -> host1 -> host1 -> host1 -> host1 -> ap -> ap -> ap`


---
## 📜 3. 実行された命令 (Instruction Trace)
---
```
- CreateTag(START,+0)
- CreateTag(L3,+0)
- AllocateRaw(IPVer_IHL,4)
- AssignRaw(IPVer_IHL,Symb(#-9116),GenericNumeric)
- AllocateRaw(IPProto,8)
- AssignRaw(IPProto,Symb(#29174),GenericNumeric)
- AllocateRaw(IPSrc,32)
- AssignRaw(IPSrc,Symb(#-1675),GenericNumeric)
- ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)
- AllocateRaw(IPDst,32)
- AssignRaw(IPDst,Symb(#-7282),GenericNumeric)
- ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(MAC: 00:01:00:00:00:00 / Val: 4294967296 (0x100000000))])),None)
- AllocateRaw(TTL,8)
- AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)
- AllocateRaw(TotalLength,16)
- AssignRaw(TotalLength,Symb(#16052),GenericNumeric)
- AllocateRaw(DSCP_ECN,4)
- AssignRaw(DSCP_ECN,Symb(#-5033),GenericNumeric)
- AllocateRaw(IPChecksum,16)
- AssignRaw(IPChecksum,Symb(#47508),GenericNumeric)
- AllocateRaw(Identification,16)
- AssignRaw(Identification,Symb(#73735),GenericNumeric)
- CreateTag(L4,TotalLength0)
- AllocateRaw(SrcPort,16)
- AssignRaw(SrcPort,Symb(#19440),GenericNumeric)
- ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)
- AllocateRaw(DstPort,16)
- AssignRaw(DstPort,Symb(#-7197),GenericNumeric)
- ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(IP: 0.1.0.0 / MAC: 00:00:00:01:00:00 / Val: 65536 (0x10000))])),None)
- AllocateRaw(SeqNo,32)
- AssignRaw(SeqNo,Symb(#-9912),GenericNumeric)
- AllocateRaw(AckNo,32)
- AssignRaw(AckNo,Symb(#-5840),GenericNumeric)
- AllocateRaw(DataOffset,4)
- AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)
- AllocateRaw(L4+100,3)
- AssignRaw(L4+100,Symb(#42065),GenericNumeric)
- AllocateRaw(L4+103,1)
- AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- AllocateRaw(L4+104,1)
- AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- AllocateRaw(L4+105,1)
- AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- AllocateRaw(L4+106,1)
- AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- AllocateRaw(Flag_NS,1)
- AssignRaw(Flag_NS,Symb(#63115),GenericNumeric)
- AllocateRaw(Flag_NS,1)
- AssignRaw(Flag_NS,Symb(#41395),GenericNumeric)
- AllocateRaw(Flag_URG,1)
- AssignRaw(Flag_URG,Symb(#71805),GenericNumeric)
- AllocateRaw(Flag_ECE,1)
- AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- AllocateRaw(Flag_CWR,1)
- AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)
- CreateTag(END,L4+12000)
- Forward(host1-host-out)
- org.change.v2.analysis.processingmodels.instructions.NoOp$@4f9a3314
- CreateTag(L2,L3--112)
- AllocateRaw(EthSrc,48)
- AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)
- AllocateRaw(EthDst,48)
- AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)
- AllocateRaw(EtherType,16)
- AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)
- Forward(host1-etherencap-0-out)
- org.change.v2.analysis.processingmodels.instructions.NoOp$@4f9a3314
- Forward(host1-nic_o-out)
- org.change.v2.analysis.processingmodels.instructions.NoOp$@4f9a3314
- Forward(ap-wifi1_i-out)
- org.change.v2.analysis.processingmodels.instructions.NoOp$@4f9a3314
- ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))
```


---
## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
---
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