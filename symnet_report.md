# 🔍 SymNet 解析サマリー

**総数**: 11 件
- ✅ **OK**: 1 件
- ❌ **FAIL**: 10 件

## ❌ FAILの詳細

### FAIL 1
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 94.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 2
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 3
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 94.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 4
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 5
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 94.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 6
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.127.1 / MAC: 00:00:c0:a8:7f:01 / Val: 3232268033 (0xc0a87f01))]),:<=:([Const(IP: 192.168.127.1 / MAC: 00:00:c0:a8:7f:01 / Val: 3232268033 (0xc0a87f01))]))
```

### FAIL 7
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.127.0 / MAC: 00:00:c0:a8:7f:00 / Val: 3232268032 (0xc0a87f00))]),:<=:([Const(IP: 192.168.127.255 / MAC: 00:00:c0:a8:7f:ff / Val: 3232268287 (0xc0a87fff))]))
```

### FAIL 8
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.180.1 / MAC: 00:00:c0:a8:b4:01 / Val: 3232281601 (0xc0a8b401))]),:<=:([Const(IP: 192.168.180.1 / MAC: 00:00:c0:a8:b4:01 / Val: 3232281601 (0xc0a8b401))]))
```

### FAIL 9
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.180.0 / MAC: 00:00:c0:a8:b4:00 / Val: 3232281600 (0xc0a8b400))]),:<=:([Const(IP: 192.168.183.255 / MAC: 00:00:c0:a8:b7:ff / Val: 3232282623 (0xc0a8b7ff))]))
```

### FAIL 10
```
Symbol COLOR cannot :==:([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])
```

---
<br/>
---

# SymNet 解析レポート (1 / 11) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_pc-in` -> `rtx1210-lan3_pc-out-1` -> `rtx1210-lan3_o-in` -> `rtx1210-lan3_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])),Some(~(==([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)]))))`
- `Forward(rtx1210-lan3_pc-out-1)`

---

- `NoOp`
- `Forward(rtx1210-lan3_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (2 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (3 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -48)
```
Value: [Const(00:00:00:00:81:00 (MAC))]
```

#### `[Unknown (Offset -32)]` (AbsOffset: -32)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -29)]` (AbsOffset: -29)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -28)]` (AbsOffset: -28)
```
Value: [Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (4 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (5 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:~:(:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -48)
```
Value: [Const(00:00:00:00:81:00 (MAC))]
```

#### `[Unknown (Offset -32)]` (AbsOffset: -32)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -29)]` (AbsOffset: -29)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset -28)]` (AbsOffset: -28)
```
Value: [Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (6 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (7 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))])),Some(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (8 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (9 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))])),Some(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (10 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```

---
<br/>
---

# SymNet 解析レポート (11 / 11) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Symbol COLOR cannot :==:([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-Paint-0-in` -> `rtx1210-Paint-0-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_pc-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#-3844),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#57268),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#30943),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#-2010),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(Val: 4294967296 (0x100000000))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7173),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#59516),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#77355),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#44742),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-1402),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#62009),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#56843),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#-1906),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-3798),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#58471),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#49212),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-8639),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(ap-vlanencap-0-out)`

---

- `NoOp`
- `Forward(ap-wlan_o-out)`

---

- `NoOp`
- `Forward(poesw-port1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(00:00:00:00:81:00 (MAC))],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-2-out)`

---

- `NoOp`
- `Forward(poesw-port8_o-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_i-out)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 0.0.0.1 / MAC: 00:00:00:00:00:01 / Val: 1)],GenericNumeric)`
- `Forward(rtx1210-Paint-0-out)`

---

- `NoOp`
- `ConstrainRaw(L2+116,:==:([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 0.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(00:00:00:00:81:00 (MAC))]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(EthSrc),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(EthDst),GenericNumeric)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,Symbol(s),GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:==:([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)]),Some(==([Const(IP: 0.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#-3844)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#59516)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7173)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#44742)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 0.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#57268)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#77355)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#30943)
Constraints:
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#-2010)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - Val: 4294967296 (0x100000000)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-1402)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#62009)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#56843)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#-1906)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 0.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-3798)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#49212)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 0.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-8639)
```