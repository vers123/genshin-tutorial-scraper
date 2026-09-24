---
title: Edit ID
path_id: mhdlzsip9q98
updated_at: 2026-09-16 14:13:12
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdlzsip9q98
---

# I. Function Overview

The Edit ID feature allows Craftspeople to dynamically modify and reassign IDs during editing. It applies to all content containing ID references, including Entity GUIDs, Prefab IDs, and Configuration IDs

# II. Accessing the Function

![](../images/c5db0d3d000582a4.png)

Details Bar - ID field - To the right of Copy

# III. Editing an ID

Click Edit ID

![](../images/d0c7d6289e56422d.png)

Enter a new ID, then click Confirm Changes to apply the change

![](../images/1cb9933cfc6c4fea.png)

# IV. Effects

## 1. References

After an ID is changed, all references to the object from other content will be lost

## 2. Function Limitations

Some features do not allow IDs to be modified. IDs may only be viewable or may not be displayed

## 3. Validation

If the new ID fails any of the following checks, the change will not take effect:

The entered ID duplicates an existing IDThe input is emptyThe input exceeds the maximum lengthThe ID does not belong to the current project type

# V. Data Rules

## 1. ID Structure

IDs are displayed as decimal numbers in the Editor but are converted to 32-bit binary values for processing. The bit allocation is shown in the table below:

|  |  |
| --- | --- |
| Bit | Meaning/Rule |
| Bit 31 | 0 |
| Bit 30 | 1 |
| Bit 29 | 0 |
| Bits 22–28 | Type ID (see table below) |
| Bits 16–21 | Shared Creation Mode section ID |
| Bits 0–15 | Incremental ID |

## 2. ID Type Table

|  |  |  |
| --- | --- | --- |
| Config ID | Type | Editable Decimal ID Range |
| 0 | Invalid | 1073741824–1077936127 |
| 1 | Unit Status | 1077936128–1082130431 |
| 2 | Client Node Graphs | 1082130432–1086324735 |
| 4 | Classes | 1090519040–1094713343 |
| 5 | Class Growth Curves | 1094713344–1098907647 |
| 6 | Custom Skills | 1098907648–1103101951 |
| 7 | Energy | 1103101952–1107296255 |
| 8 | Normal Items, Equipment Items | 1107296256–1111490559 |
| 10 | Resources and Currency | 1115684864–1119879167 |
| 11 | Item Inventory | 1119879168–1124073471 |
| 12 | Equipment Types | 1124073472–1128267775 |
| 13 | Equipment Tags | 1128267776–1132462079 |
| 14 | Equipment Affixes | 1132462080–1136656383 |
| 15 | Shop Templates | 1136656384–1140850687 |
| 19 | Equipment Templates | 1153433600–1157627903 |
| 20 | Shields | 1157627904–1161822207 |
| 21 | Scan Templates | 1161822208–1166016511 |
| 24 | Paid DLC | 1174405120–1178599423 |
| 25 | Free DLC | 1178599424–1182793727 |
| 26 | Ambient Light Sources | 1182793728–1186988031 |
| 27 | Environment | 1186988032–1191182335 |
| 28 | Creation Skills | 1191182336–1195376639 |
| 30 | VFX Tools | 1199570944–1203765247 |
| 31 | Skill Attribute Group | 1203765248–1207959551 |
| 32 | Skill Variables | 1207959552–1212153855 |
| 33 | Reward DLC | 1212153856–1216348159 |
| 34 | Stage Objectives | 1216348160–1220542463 |
| 35 | Custom Mini-Maps | 1220542464–1224736767 |
| 36 | Custom Mini-Map Image Resources | 1224736768–1228931071 |
| 37 | Character Control Skills | 1228931072–1233125375 |

|  |  |  |
| --- | --- | --- |
| Entity ID | Type | Editable Decimal ID Range |
| 0 | Invalid | 1073741824–1077936127 |
| 1 | Objects (including Prefabs) | 1077936128–1082130431 |
| 2 | Creations | 1082130432–1086324735 |
| 5 | Stages | 1094713344–1098907647 |
