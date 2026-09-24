---
title: Special Number Controls
path_id: mhg70rrcygcu
updated_at: 2026-08-06 16:41:08
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhg70rrcygcu
---

# I. Special Number Features

*Special Numbers* can be configured in the UI Layout to support displaying various types of skill-related data

During stage runtime, Special Number controls can be triggered through Node Graphs

# **II. Editing Special Numbers**

![](../../../images/eb33b918e78b9488.png)

## **1. Add Special Numbers**

In the *UI Control Group Editor window*, add UI Control Template - Special Number

![](../../../images/46d687bd4059c957.png)

## 2. Special Number Settings

![](../../../images/1411874ebe211553.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Data Source* | May select from Skill, Item, and Unit Status. Below are the available options under Skill |
| *Monitor Skill Slot* | Supports selecting any slot and monitoring skills based on the selected slot  ![](../../../images/3c35e53f905faca1.png) |
| *Data Content* | Can display Skill Remaining CD Time, Skill Usage(s), Skill Resources, and Skill Availability  ![](../../../images/50418eb7a2bce9bd.png) |
| *Time Unit* | Available options are Seconds, Minutes, and Hours |
| *Font Size* | Sets the font size of the number shown |

## 3. Notes

Under Unit Status settings, identical status effects from different sources can be configured to not stack. Consequently, at runtime, instances of the same status effect from different sources will be allocated to separate slots.

When the Data Source for a Special Number is set to Unit Status, if multiple instances of the same status effect exist simultaneously on a player (in separate slots), the UI will display the following values: [Unit Status Stack Count] will display the current cumulative stacks. [Remaining Unit Status Duration] will display the maximum remaining duration among all instances.

![](../../../images/ee170e5907db98ab.png)

# III. Additional Notes

Classic Mode now also supports configuring Special Number controls

When the Data Source is set to Unit Status, you can choose a Monitor Mode:

Monitor Entity Variable: Displays data from the specified unit status of the specified entityMonitor Parent: Needs to be used together with the Status Display Area control to display the unit statuses assigned by the Status Display Area (This allows unit statuses from different sources to be displayed separately in different slots)

![](../../../images/02185cd67ed138b0.png)
