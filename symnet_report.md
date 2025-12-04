# 🔍 SymNet 解析サマリー

**総数**: 40 件
- ✅ **OK**: 8 件
- ❌ **FAIL**: 32 件

## ✅ OKの最終到達モジュールと宛先IP制約

### OK 1 → [詳細レポートへ](#report-1)
```
最終到達: rtx1210 / cpu

宛先IP制約:
  - IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 2 → [詳細レポートへ](#report-2)
```
最終到達: rtx1210 / lan3_o

宛先IP制約:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 3 → [詳細レポートへ](#report-3)
```
最終到達: rtx1210 / cpu

宛先IP制約:
  - IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 4 → [詳細レポートへ](#report-4)
```
最終到達: rtx1210 / cpu

宛先IP制約:
  - IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 5 → [詳細レポートへ](#report-5)
```
最終到達: rtx1210 / lan3_o

宛先IP制約:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 6 → [詳細レポートへ](#report-6)
```
最終到達: host1 / host_o

宛先IP制約:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 7 → [詳細レポートへ](#report-7)
```
最終到達: host1 / host_o

宛先IP制約:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

### OK 8 → [詳細レポートへ](#report-8)
```
最終到達: host2 / host_o

宛先IP制約:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

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
IPFilter acl_vlan10_in: denied by rule dst 192.168.180.0/22
```

### FAIL 6
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 7
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]))
```

### FAIL 8
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.180.1 / MAC: 00:00:40:a8:b4:01 / Val: 1084797953 (0x40a8b401))]),:<=:([Const(IP: 192.168.180.1 / MAC: 00:00:40:a8:b4:01 / Val: 1084797953 (0x40a8b401))]))
```

### FAIL 9
```
Memory object @ L3+128 cannot :&:(:>=:([Const(IP: 192.168.180.0 / MAC: 00:00:40:a8:b4:00 / Val: 1084797952 (0x40a8b400))]),:<=:([Const(IP: 192.168.183.255 / MAC: 00:00:40:a8:b7:ff / Val: 1084798975 (0x40a8b7ff))]))
```

### FAIL 10
```
Unexpected packet dropped @ rtx1210-Discard-3
```

### FAIL 11
```
Unexpected packet dropped @ rtx1210-Discard-3
```

### FAIL 12
```
Unexpected packet dropped @ rtx1210-Discard-4
```

### FAIL 13
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 14
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 15
```
Memory object @ L2+116 cannot :==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])
```

### FAIL 16
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```

### FAIL 17
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 18
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))]))
```

### FAIL 19
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 20
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))]))
```

### FAIL 21
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 22
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.18 / MAC: 00:00:5e:00:53:12 / Val: 1577079570 (0x5e005312))]))
```

### FAIL 23
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 24
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

### FAIL 25
```
Memory object @ L2+116 cannot :==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])
```

### FAIL 26
```
Memory object @ L2+116 cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```

### FAIL 27
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 28
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))]))
```

### FAIL 29
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 30
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))]))
```

### FAIL 31
```
Memory object @ L2+0 cannot :==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])
```

### FAIL 32
```
Memory object @ L2+0 cannot :~:(:==:([Const(IP: 222.0.83.18 / MAC: 00:00:5e:00:53:12 / Val: 1577079570 (0x5e005312))]))
```

---
<br/>
---

# <a id="report-1"></a>SymNet 解析レポート (1 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-0` -> `rtx1210-cpu-in` -> `rtx1210-cpu-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))])),Some(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-0)`

---

- `NoOp`
- `Forward(rtx1210-cpu-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-2"></a>SymNet 解析レポート (2 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_o-in` -> `rtx1210-lan3_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,[Const(IP: 10.0.0.1 / Val: -1979711487 (0x-75ffffff))],GenericNumeric)`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `Forward(rtx1210-lan3_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-3"></a>SymNet 解析レポート (3 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-0` -> `rtx1210-cpu-in` -> `rtx1210-cpu-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))])),Some(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-0)`

---

- `NoOp`
- `Forward(rtx1210-cpu-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-4"></a>SymNet 解析レポート (4 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-0` -> `rtx1210-cpu-in` -> `rtx1210-cpu-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))])),Some(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-0)`

---

- `NoOp`
- `Forward(rtx1210-cpu-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-5"></a>SymNet 解析レポート (5 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-3` -> `rtx1210-lan3_o-in` -> `rtx1210-lan3_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,[Const(IP: 10.0.0.1 / Val: -1979711487 (0x-75ffffff))],GenericNumeric)`
- `Forward(rtx1210-routing-out-3)`

---

- `NoOp`
- `Forward(rtx1210-lan3_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-6"></a>SymNet 解析レポート (6 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in` -> `ap-vlan10-out-1` -> `ap-wifi1_o-in` -> `ap-wifi1_o-out`  
`host1-nic_i-in` -> `host1-nic_i-out` -> `host1-noop-0-in` -> `host1-noop-0-out` -> `host1-host_o-in` -> `host1-host_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(ap-vlan10-out-1)`

---

- `NoOp`
- `Forward(ap-wifi1_o-out)`

---

- `NoOp`
- `Forward(host1-nic_i-out)`

---

- `NoOp`
- `Forward(host1-noop-0-out)`

---

- `NoOp`
- `Forward(host1-host_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - == 00:00:5e:00:53:11 (MAC)
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-7"></a>SymNet 解析レポート (7 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in` -> `ap-vlan10-out-1` -> `ap-wifi1_o-in` -> `ap-wifi1_o-out`  
`host1-nic_i-in` -> `host1-nic_i-out` -> `host1-noop-0-in` -> `host1-noop-0-out` -> `host1-host_o-in` -> `host1-host_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(ap-vlan10-out-1)`

---

- `NoOp`
- `Forward(ap-wifi1_o-out)`

---

- `NoOp`
- `Forward(host1-nic_i-out)`

---

- `NoOp`
- `Forward(host1-noop-0-out)`

---

- `NoOp`
- `Forward(host1-host_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - == 00:00:5e:00:53:11 (MAC)
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-8"></a>SymNet 解析レポート (8 / 40) ✅ OK

## 🚦 1. 最終ステータス (Status)
```
OK
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in` -> `poesw-vlan20-out-1` -> `poesw-vlanencap-5-in` -> `poesw-vlanencap-5-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-1` -> `ap-vlandecap-1-in` -> `ap-vlandecap-1-out` -> `ap-vlan20-in` -> `ap-vlan20-out-1` -> `ap-wifi2_o-in` -> `ap-wifi2_o-out`  
`host2-nic_i-in` -> `host2-nic_i-out` -> `host2-noop-1-in` -> `host2-noop-1-out` -> `host2-host_o-in` -> `host2-host_o-out`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(poesw-vlan20-out-1)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-5-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(ap-tag-out-1)`

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
- `Forward(ap-vlandecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(ap-vlan20-out-1)`

---

- `NoOp`
- `Forward(ap-wifi2_o-out)`

---

- `NoOp`
- `Forward(host2-nic_i-out)`

---

- `NoOp`
- `Forward(host2-noop-1-out)`

---

- `NoOp`
- `Forward(host2-host_o-out)`

---

- `NoOp`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
Constraints:
  - == 00:00:5e:00:53:12 (MAC)
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-9"></a>SymNet 解析レポート (9 / 40) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-10"></a>SymNet 解析レポート (10 / 40) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-11"></a>SymNet 解析レポート (11 / 40) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-12"></a>SymNet 解析レポート (12 / 40) ❌ FAIL

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
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-13"></a>SymNet 解析レポート (13 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
IPFilter acl_vlan10_in: denied by rule dst 192.168.180.0/22
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `Fail(IPFilter acl_vlan10_in: denied by rule dst 192.168.180.0/22)`


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
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-14"></a>SymNet 解析レポート (14 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

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
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-15"></a>SymNet 解析レポート (15 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:00 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

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
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-16"></a>SymNet 解析レポート (16 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))])),Some(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-17"></a>SymNet 解析レポート (17 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ IPDst cannot :&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-18"></a>SymNet 解析レポート (18 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Unexpected packet dropped @ rtx1210-Discard-3
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-1` -> `rtx1210-Discard-3-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:~:(:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])),Some(~(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]))))`
- `Forward(rtx1210-vlan10_nexthop-out-1)`

---

- `NoOp`
- `Fail(Unexpected packet dropped @ rtx1210-Discard-3)`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-19"></a>SymNet 解析レポート (19 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Unexpected packet dropped @ rtx1210-Discard-3
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-1` -> `rtx1210-Discard-3-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:~:(:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])),Some(~(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]))))`
- `Forward(rtx1210-vlan10_nexthop-out-1)`

---

- `NoOp`
- `Fail(Unexpected packet dropped @ rtx1210-Discard-3)`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-20"></a>SymNet 解析レポート (20 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Unexpected packet dropped @ rtx1210-Discard-4
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-1` -> `rtx1210-Discard-4-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
- `AllocateRaw(Flag_ECE,1)`
- `AssignRaw(Flag_ECE,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_CWR,1)`
- `AssignRaw(Flag_CWR,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `CreateTag(END,L4+12000)`
- `Forward(host1-host-out)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,[Const(IP: 222.0.83.17 / MAC: 00:00:5e:00:53:11 / Val: 1577079569 (0x5e005311))],GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,[Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))],GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(host1-etherencap-0-out)`

---

- `NoOp`
- `Forward(host1-nic_o-out)`

---

- `NoOp`
- `Forward(ap-wifi1_i-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(ap-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(poesw-tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlandecap-3-out)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(poesw-vlan10-out-0)`

---

- `NoOp`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `CreateTag(L2,L2--32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `AllocateRaw(L2+96,16)`
- `AssignRaw(L2+96,[Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)],GenericNumeric)`
- `AllocateRaw(L2+112,3)`
- `AssignRaw(L2+112,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+115,1)`
- `AssignRaw(L2+115,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L2+116,12)`
- `AssignRaw(L2+116,[Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)],GenericNumeric)`
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
- `ConstrainRaw(L2+116,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(rtx1210-lan1_tag-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IP: 128.0.129.0 / MAC: 00:00:00:00:81:00 / Val: 33024)]),None)`
- `AllocateSymbol(s)`
- `AssignNamedSymbol(s,Address(L2+48),GenericNumeric)`
- `AllocateSymbol(d)`
- `AssignNamedSymbol(d,Address(L2+0),GenericNumeric)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DeallocateRaw(L2+112,3)`
- `DeallocateRaw(L2+115,1)`
- `DeallocateRaw(L2+116,12)`
- `CreateTag(L2,L2+32)`
- `AllocateRaw(L2+48,48)`
- `AssignRaw(L2+48,Symbol(s),GenericNumeric)`
- `AllocateRaw(L2+0,48)`
- `AssignRaw(L2+0,Symbol(d),GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlandecap-6-out)`

---

- `NoOp`
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+0,:==:([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))]),Some(==([Const(IP: 222.0.83.0 / MAC: 00:00:5e:00:53:00 / Val: 1577079552 (0x5e005300))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(L2+96,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(L2+48),GenericNumeric)`
- `CreateTag(L3,L2+112)`
- `DeallocateRaw(L2+48,48)`
- `DeallocateRaw(L2+0,48)`
- `DeallocateRaw(L2+96,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:~:(:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])),Some(~(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]))))`
- `Forward(rtx1210-vlan20_nexthop-out-1)`

---

- `NoOp`
- `Fail(Unexpected packet dropped @ rtx1210-Discard-4)`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`


### ヘッダーフィールド (Header Fields)

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-21"></a>SymNet 解析レポート (21 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-22"></a>SymNet 解析レポート (22 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-23"></a>SymNet 解析レポート (23 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: [Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-24"></a>SymNet 解析レポート (24 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: [Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]
Constraints:
  - ~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-25"></a>SymNet 解析レポート (25 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-26"></a>SymNet 解析レポート (26 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:11 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:11 (MAC))])),Some(~(==([Const(00:00:5e:00:53:11 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-27"></a>SymNet 解析レポート (27 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-28"></a>SymNet 解析レポート (28 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:11 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:11 (MAC))])),Some(~(==([Const(00:00:5e:00:53:11 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-29"></a>SymNet 解析レポート (29 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-30"></a>SymNet 解析レポート (30 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:12 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:12 (MAC))])),Some(~(==([Const(00:00:5e:00:53:12 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-31"></a>SymNet 解析レポート (31 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-32"></a>SymNet 解析レポート (32 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-33"></a>SymNet 解析レポート (33 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in` -> `poesw-vlan20-out-1` -> `poesw-vlanencap-5-in` -> `poesw-vlanencap-5-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(poesw-vlan20-out-1)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-5-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: [Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-34"></a>SymNet 解析レポート (34 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ VLAN_VID cannot :~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in` -> `poesw-vlan20-out-1` -> `poesw-vlanencap-5-in` -> `poesw-vlanencap-5-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(poesw-vlan20-out-1)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-5-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])),Some(~(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -144`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -144)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -96)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
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
Value: [Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]
Constraints:
  - ~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))
```

#### `[Unknown (Offset -16)]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[IPVer_IHL]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[DSCP_ECN]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-35"></a>SymNet 解析レポート (35 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-36"></a>SymNet 解析レポート (36 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:11 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))]))),Some(~(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:11 (MAC))])),Some(~(==([Const(00:00:5e:00:53:11 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - NOT IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-37"></a>SymNet 解析レポート (37 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-38"></a>SymNet 解析レポート (38 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:11 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-1` -> `rtx1210-vlan10_nexthop-in` -> `rtx1210-vlan10_nexthop-out-0` -> `rtx1210-etherencap-2-in` -> `rtx1210-etherencap-2-out` -> `rtx1210-vlan10_out-in` -> `rtx1210-vlan10_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-1` -> `poesw-vlanencap-3-in` -> `poesw-vlanencap-3-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-0` -> `ap-vlandecap-0-in` -> `ap-vlandecap-0-out` -> `ap-vlan10-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))])),Some(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-1)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))]),Some(==([Const(IP: 192.168.127.2 / MAC: 00:00:40:a8:7f:02 / Val: 1084784386 (0x40a87f02))])))`
- `Forward(rtx1210-vlan10_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:11 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-2-out)`

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
- `Forward(rtx1210-vlan10_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

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
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:11 (MAC))]),Some(==([Const(00:00:5e:00:53:11 (MAC))])))`
- `Forward(poesw-vlan10-out-1)`

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
- `Forward(poesw-vlanencap-3-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]),Some(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])))`
- `Forward(ap-tag-out-0)`

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
- `Forward(ap-vlandecap-0-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:11 (MAC))])),Some(~(==([Const(00:00:5e:00:53:11 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:11 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-39"></a>SymNet 解析レポート (39 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :==:([Const(00:00:5e:00:53:00 (MAC))])
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in` -> `poesw-vlan20-out-1` -> `poesw-vlanencap-5-in` -> `poesw-vlanencap-5-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-1` -> `ap-vlandecap-1-in` -> `ap-vlandecap-1-out` -> `ap-vlan20-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(poesw-vlan20-out-1)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-5-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(ap-tag-out-1)`

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
- `Forward(ap-vlandecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```

---
<br/>
---

# <a id="report-40"></a>SymNet 解析レポート (40 / 40) ❌ FAIL

## 🚦 1. 最終ステータス (Status)
```
Memory object @ EthDst cannot :~:(:==:([Const(00:00:5e:00:53:12 (MAC))]))
```


## 🗺️ 2. パケットの経路 (Port Trace)
**Path:**
`host1-host-in` -> `host1-host-out` -> `host1-etherencap-0-in` -> `host1-etherencap-0-out` -> `host1-nic_o-in` -> `host1-nic_o-out`  
`ap-wifi1_i-in` -> `ap-wifi1_i-out` -> `ap-vlan10-in` -> `ap-vlan10-out-0` -> `ap-vlanencap-0-in` -> `ap-vlanencap-0-out` -> `ap-wlan_o-in` -> `ap-wlan_o-out`  
`poesw-port1_i-in` -> `poesw-port1_i-out` -> `poesw-tag-in` -> `poesw-tag-out-0` -> `poesw-vlandecap-3-in` -> `poesw-vlandecap-3-out` -> `poesw-vlan10-in` -> `poesw-vlan10-out-0` -> `poesw-vlanencap-2-in` -> `poesw-vlanencap-2-out` -> `poesw-port8_o-in` -> `poesw-port8_o-out`  
`rtx1210-lan1_i-in` -> `rtx1210-lan1_i-out` -> `rtx1210-lan1_tag-in` -> `rtx1210-lan1_tag-out-0` -> `rtx1210-vlandecap-6-in` -> `rtx1210-vlandecap-6-out` -> `rtx1210-acl_vlan10_in-in`  
`acl_vlan10_in-out-0`  
`rtx1210-vlan10-in` -> `rtx1210-vlan10-out-0` -> `rtx1210-etherDecap-1-in` -> `rtx1210-etherDecap-1-out` -> `rtx1210-routing-in` -> `rtx1210-routing-out-2` -> `rtx1210-vlan20_nexthop-in` -> `rtx1210-vlan20_nexthop-out-0` -> `rtx1210-etherencap-3-in` -> `rtx1210-etherencap-3-out` -> `rtx1210-vlan20_out-in` -> `rtx1210-vlan20_out-out` -> `rtx1210-lan1_o-in` -> `rtx1210-lan1_o-out`  
`poesw-port8_i-in` -> `poesw-port8_i-out` -> `poesw-tag-in` -> `poesw-tag-out-1` -> `poesw-vlandecap-4-in` -> `poesw-vlandecap-4-out` -> `poesw-vlan20-in` -> `poesw-vlan20-out-1` -> `poesw-vlanencap-5-in` -> `poesw-vlanencap-5-out` -> `poesw-port1_o-in` -> `poesw-port1_o-out`  
`ap-wlan_i-in` -> `ap-wlan_i-out` -> `ap-tag-in` -> `ap-tag-out-1` -> `ap-vlandecap-1-in` -> `ap-vlandecap-1-out` -> `ap-vlan20-in`  


## 📜 3. 実行された命令 (Instruction Trace)
- `CreateTag(START,+0)`
- `CreateTag(L3,+0)`
- `AllocateRaw(IPVer_IHL,4)`
- `AssignRaw(IPVer_IHL,Symb(#29180),GenericNumeric)`
- `AllocateRaw(IPProto,8)`
- `AssignRaw(IPProto,Symb(#-6055),GenericNumeric)`
- `AllocateRaw(IPSrc,32)`
- `AssignRaw(IPSrc,Symb(#33152),GenericNumeric)`
- `ConstrainRaw(IPSrc,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(IPDst,32)`
- `AssignRaw(IPDst,Symb(#83295),GenericNumeric)`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(0.0.0.0 (IP))]),:<=:([Const(255.255.255.255 (IP))])),None)`
- `AllocateRaw(TTL,8)`
- `AssignRaw(TTL,[Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)],GenericNumeric)`
- `AllocateRaw(TotalLength,16)`
- `AssignRaw(TotalLength,Symb(#-5892),GenericNumeric)`
- `AllocateRaw(DSCP_ECN,4)`
- `AssignRaw(DSCP_ECN,Symb(#39466),GenericNumeric)`
- `AllocateRaw(IPChecksum,16)`
- `AssignRaw(IPChecksum,Symb(#64703),GenericNumeric)`
- `AllocateRaw(Identification,16)`
- `AssignRaw(Identification,Symb(#-8124),GenericNumeric)`
- `CreateTag(L4,TotalLength0)`
- `AllocateRaw(SrcPort,16)`
- `AssignRaw(SrcPort,Symb(#53614),GenericNumeric)`
- `ConstrainRaw(SrcPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(DstPort,16)`
- `AssignRaw(DstPort,Symb(#-4953),GenericNumeric)`
- `ConstrainRaw(DstPort,:&:(:>=:([Const(0 (Port))]),:<=:([Const(Val: 65536 (0x10000))])),None)`
- `AllocateRaw(SeqNo,32)`
- `AssignRaw(SeqNo,Symb(#-3204),GenericNumeric)`
- `AllocateRaw(AckNo,32)`
- `AssignRaw(AckNo,Symb(#36231),GenericNumeric)`
- `AllocateRaw(DataOffset,4)`
- `AssignRaw(DataOffset,[Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)],GenericNumeric)`
- `AllocateRaw(L4+100,3)`
- `AssignRaw(L4+100,Symb(#19334),GenericNumeric)`
- `AllocateRaw(L4+103,1)`
- `AssignRaw(L4+103,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+104,1)`
- `AssignRaw(L4+104,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+105,1)`
- `AssignRaw(L4+105,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(L4+106,1)`
- `AssignRaw(L4+106,[Const(IP: 128.0.0.0 / MAC: 00:00:00:00:00:00 / Val: 0)],GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#90881),GenericNumeric)`
- `AllocateRaw(Flag_NS,1)`
- `AssignRaw(Flag_NS,Symb(#-5298),GenericNumeric)`
- `AllocateRaw(Flag_URG,1)`
- `AssignRaw(Flag_URG,Symb(#-5783),GenericNumeric)`
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
- `ConstrainRaw(IPSrc,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `Forward(acl_vlan10_in-out-0)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:00 (MAC))]),Some(==([Const(00:00:5e:00:53:00 (MAC))])))`
- `Forward(rtx1210-vlan10-out-0)`

---

- `NoOp`
- `ConstrainRaw(EtherType,:==:([Const(IPv4 (0x0800))]),None)`
- `AllocateSymbol(EtherSrc)`
- `AssignNamedSymbol(EtherSrc,Address(EthSrc),GenericNumeric)`
- `CreateTag(L3,VLAN_PCP)`
- `DeallocateRaw(EthSrc,48)`
- `DeallocateRaw(EthDst,48)`
- `DeallocateRaw(EtherType,16)`
- `DestroyTag(L2)`
- `Forward(rtx1210-etherDecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.1 (IP))]),:<=:([Const(192.168.127.1 (IP))]))),Some(~(&(List(>=([Const(192.168.127.1 (IP))]), <=([Const(192.168.127.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.127.0 (IP))]),:<=:([Const(192.168.127.255 (IP))]))),Some(~(&(List(>=([Const(192.168.127.0 (IP))]), <=([Const(192.168.127.255 (IP))]))))))`
- `ConstrainRaw(IPDst,:~:(:&:(:>=:([Const(192.168.180.1 (IP))]),:<=:([Const(192.168.180.1 (IP))]))),Some(~(&(List(>=([Const(192.168.180.1 (IP))]), <=([Const(192.168.180.1 (IP))]))))))`
- `ConstrainRaw(IPDst,:&:(:>=:([Const(192.168.180.0 (IP))]),:<=:([Const(192.168.183.255 (IP))])),Some(&(List(>=([Const(192.168.180.0 (IP))]), <=([Const(192.168.183.255 (IP))])))))`
- `AllocateSymbol(nexthop)`
- `AssignNamedSymbol(nexthop,Address(IPDst),GenericNumeric)`
- `Forward(rtx1210-routing-out-2)`

---

- `NoOp`
- `ConstrainNamedSymbol(nexthop,:==:([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))]),Some(==([Const(IP: 192.168.180.2 / MAC: 00:00:40:a8:b4:02 / Val: 1084797954 (0x40a8b402))])))`
- `Forward(rtx1210-vlan20_nexthop-out-0)`

---

- `NoOp`
- `CreateTag(L2,L3--112)`
- `AllocateRaw(EthSrc,48)`
- `AssignRaw(EthSrc,[Const(00:00:5e:00:53:00 (MAC))],GenericNumeric)`
- `AllocateRaw(EthDst,48)`
- `AssignRaw(EthDst,[Const(00:00:5e:00:53:12 (MAC))],GenericNumeric)`
- `AllocateRaw(EtherType,16)`
- `AssignRaw(EtherType,[Const(IPv4 (0x0800))],GenericNumeric)`
- `Forward(rtx1210-etherencap-3-out)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(rtx1210-vlan20_out-out)`

---

- `NoOp`
- `Forward(rtx1210-lan1_o-out)`

---

- `NoOp`
- `Forward(poesw-port8_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(poesw-tag-out-1)`

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
- `Forward(poesw-vlandecap-4-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:==:([Const(00:00:5e:00:53:12 (MAC))]),Some(==([Const(00:00:5e:00:53:12 (MAC))])))`
- `Forward(poesw-vlan20-out-1)`

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
- `AssignRaw(VLAN_VID,[Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)],GenericNumeric)`
- `DeallocateNamedSymbol(s)`
- `DeallocateNamedSymbol(d)`
- `Forward(poesw-vlanencap-5-out)`

---

- `NoOp`
- `Forward(poesw-port1_o-out)`

---

- `NoOp`
- `Forward(ap-wlan_i-out)`

---

- `NoOp`
- `ConstrainRaw(VLAN_VID,:~:(:==:([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)])),Some(~(==([Const(IP: 128.0.0.10 / MAC: 00:00:00:00:00:0a / Val: 10)]))))`
- `ConstrainRaw(VLAN_VID,:==:([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)]),Some(==([Const(IP: 128.0.0.20 / MAC: 00:00:00:00:00:14 / Val: 20)])))`
- `Forward(ap-tag-out-1)`

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
- `Forward(ap-vlandecap-1-out)`

---

- `NoOp`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:00 (MAC))])),Some(~(==([Const(00:00:5e:00:53:00 (MAC))]))))`
- `ConstrainRaw(EthDst,:~:(:==:([Const(00:00:5e:00:53:12 (MAC))])),Some(~(==([Const(00:00:5e:00:53:12 (MAC))]))))`


## 🧠 4. 最終的なパケットのメモリ状態 (Final Memory State)
### タグ (Tags)
`L4: 160`, `START: 0`, `L3: 0`, `END: 12160`, `L2: -112`


### ヘッダーフィールド (Header Fields)

#### `[EthDst]` (AbsOffset: -112)
```
Value: [Const(00:00:5e:00:53:12 (MAC))]
Constraints:
  - ~(==([Const(00:00:5e:00:53:00 (MAC))]))
```

#### `[EthSrc]` (AbsOffset: -64)
```
Value: [Const(00:00:5e:00:53:00 (MAC))]
```

#### `[EtherType]` (AbsOffset: -16)
```
Value: [Const(IPv4 (0x0800))]
```

#### `[VLAN_PCP]` (AbsOffset: 0)
```
Value: Symb(#29180)
```

#### `[VLAN_VID]` (AbsOffset: 4)
```
Value: Symb(#39466)
```

#### `[TotalLength]` (AbsOffset: 16)
```
Value: Symb(#-5892)
```

#### `[Identification]` (AbsOffset: 32)
```
Value: Symb(#-8124)
```

#### `[TTL]` (AbsOffset: 64)
```
Value: [Const(IP: 128.0.0.255 / MAC: 00:00:00:00:00:ff / Val: 255)]
```

#### `[IPProto]` (AbsOffset: 72)
```
Value: Symb(#-6055)
```

#### `[IPChecksum]` (AbsOffset: 80)
```
Value: Symb(#64703)
```

#### `[IPSrc]` (AbsOffset: 96)
```
Value: Symb(#33152)
Constraints:
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[IPDst]` (AbsOffset: 128)
```
Value: Symb(#83295)
Constraints:
  - IN [192.168.180.0 (IP) - 192.168.183.255 (IP)]
  - NOT IN [192.168.180.1 (IP) - 192.168.180.1 (IP)]
  - NOT IN [192.168.127.0 (IP) - 192.168.127.255 (IP)]
  - NOT IN [192.168.127.1 (IP) - 192.168.127.1 (IP)]
  - IN [0.0.0.0 (IP) - 255.255.255.255 (IP)]
```

#### `[SrcPort]` (AbsOffset: 160)
```
Value: Symb(#53614)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[DstPort]` (AbsOffset: 176)
```
Value: Symb(#-4953)
Constraints:
  - IN [0 (Port) - Val: 65536 (0x10000)]
```

#### `[SeqNo]` (AbsOffset: 192)
```
Value: Symb(#-3204)
```

#### `[AckNo]` (AbsOffset: 224)
```
Value: Symb(#36231)
```

#### `[DataOffset]` (AbsOffset: 256)
```
Value: [Const(IP: 128.0.0.160 / MAC: 00:00:00:00:00:a0 / Val: 160)]
```

#### `[Unknown (Offset 260)]` (AbsOffset: 260)
```
Value: Symb(#19334)
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
Value: Symb(#-5298)
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
Value: Symb(#-5783)
```