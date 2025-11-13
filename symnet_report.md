# 🔍 SymNet 解析サマリー

**総数**: 19 件
- ✅ **OK**: 3 件
- ❌ **FAIL**: 16 件

## ❌ FAILの詳細

### FAIL 1
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 2
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 3
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 4
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 5
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 6
```
Symbol COLOR cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 7
```
Symbol COLOR cannot :==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])
```

### FAIL 8
```
Symbol COLOR cannot :==:([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])
```

### FAIL 9
```
Unexpected packet dropped @ rtx1210-Discard-4
```

### FAIL 10
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 11
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.127.1 / MAC: 00:00:40:a8:7f:01 / Val: 1084784385 (0x40a87f01))]),:<=:([Const(IP: 192.168.127.1 / MAC: 00:00:40:a8:7f:01 / Val: 1084784385 (0x40a87f01))]))
```

### FAIL 12
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.127.0 / MAC: 00:00:40:a8:7f:00 / Val: 1084784384 (0x40a87f00))]),:<=:([Const(IP: 192.168.127.255 / MAC: 00:00:40:a8:7f:ff / Val: 1084784639 (0x40a87fff))]))
```

### FAIL 13
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.180.1 / MAC: 00:00:40:a8:b4:01 / Val: 1084797953 (0x40a8b401))]),:<=:([Const(IP: 192.168.180.1 / MAC: 00:00:40:a8:b4:01 / Val: 1084797953 (0x40a8b401))]))
```

### FAIL 14
```
Memory object @ L3+128 cannot :~:(:&:(:>=:([Const(IP: 192.168.180.0 / MAC: 00:00:40:a8:b4:00 / Val: 1084797952 (0x40a8b400))]),:<=:([Const(IP: 192.168.183.255 / MAC: 00:00:40:a8:b7:ff / Val: 1084798975 (0x40a8b7ff))])))
```

### FAIL 15
```
Symbol COLOR cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```

### FAIL 16
```
Unexpected packet dropped @ rtx1210-Discard-5
```

---
<br/>
---

# SymNet 解析レポート (1 / 19) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-0` -> `rtx1210-cpu-in` -> `rtx1210-cpu-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))])),Some(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))))`
- `Forward(rtx1210-routing-out-0)`

---

- `NoOp`
- `Forward(rtx1210-cpu-out)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (2 / 19) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-0` -> `rtx1210-cpu-in` -> `rtx1210-cpu-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))])),Some(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))))`
- `Forward(rtx1210-routing-out-0)`

---

- `NoOp`
- `Forward(rtx1210-cpu-out)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (3 / 19) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_pc-in` -> `rtx1210-lan3_pc-out-1` -> `rtx1210-lan3_o-in` -> `rtx1210-lan3_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])),Some(~(==([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)]))))`
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (4 / 19) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (5 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
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
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


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

#### `[VLAN_PCP]` (AbsOffset: -32)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[VLAN_DEI]` (AbsOffset: -29)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[VLAN_VID]` (AbsOffset: -28)
```
Value: [Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (6 / 19) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (7 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


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

#### `[VLAN_PCP]` (AbsOffset: -32)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[VLAN_DEI]` (AbsOffset: -29)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[VLAN_VID]` (AbsOffset: -28)
```
Value: [Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (8 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (9 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Symbol COLOR cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-routing1_pc-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (10 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Symbol COLOR cannot :==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`


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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (11 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Symbol COLOR cannot :==:([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_pc-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:==:([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)]),Some(==([Const(IP: 128.0.0.3 / MAC: 00:00:00:00:00:03 / Val: 3)])))`


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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (12 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Unexpected packet dropped @ rtx1210-Discard-4
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-routing1_pc-in` -> `rtx1210-routing1_pc-out-0` -> `rtx1210-Discard-4-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-routing1_pc-out-0)`

---

- `NoOp`
- `Fail(Unexpected packet dropped @ rtx1210-Discard-4)`


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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (13 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (14 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (15 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (16 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (17 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (18 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Symbol COLOR cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```

---
<br/>
---

# SymNet 解析レポート (19 / 19) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Unexpected packet dropped @ rtx1210-Discard-5
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-Paint-1-in` -> `rtx1210-Paint-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-1` -> `rtx1210-vlan20-in` -> `rtx1210-vlan20-out-0` -> `rtx1210-Paint-2-in` -> `rtx1210-Paint-2-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-routing2_pc-in` -> `rtx1210-routing2_pc-out-0` -> `rtx1210-Discard-5-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#34784),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#12178),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#52355),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#72841),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-7749),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#53207),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#-7088),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#35064),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#-4608),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4200),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-8637),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#76235),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#-2314),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-2177),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-1063),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-2811),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AllocateRaw(VLAN_PCP,3)`
- `AssignRaw(VLAN_PCP,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_DEI,1)`
- `AssignRaw(VLAN_DEI,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(VLAN_VID,12)`
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
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
- `DeallocateRaw(VLAN_PCP,3)`
- `DeallocateRaw(VLAN_DEI,1)`
- `DeallocateRaw(VLAN_VID,12)`
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
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
- `Forward(rtx1210-Paint-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`
- `Forward(rtx1210-routing2_pc-out-1)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan20-out-0)`

---

- `NoOp`
- `AssignNamedSymbol(COLOR,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `Forward(rtx1210-Paint-2-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(COLOR,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(rtx1210-routing2_pc-out-0)`

---

- `NoOp`
- `Fail(Unexpected packet dropped @ rtx1210-Discard-5)`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
Constraints:
  - == 00:00:5e:00:53:00 (MAC)
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

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#34784)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#53207)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-7749)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#35064)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#12178)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#-7088)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#52355)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#72841)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#-4608)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4200)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-8637)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#76235)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#-2314)
```

#### `[Unknown (Offset 263)]` (AbsOffset: 263)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 264)]` (AbsOffset: 264)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 265)]` (AbsOffset: 265)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Unknown (Offset 266)]` (AbsOffset: 266)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_NS]` (AbsOffset: 267)
```
Value: Symb(#-1063)
```

#### `[Flag_CWR]` (AbsOffset: 268)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_ECE]` (AbsOffset: 269)
```
Value: [Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)]
```

#### `[Flag_URG]` (AbsOffset: 270)
```
Value: Symb(#-2811)
```