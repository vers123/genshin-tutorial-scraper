---
title: Skill Attribute Groups
path_id: mhyfcn91kiqi
updated_at: 2026-04-03 15:26:26
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhyfcn91kiqi
---

# I. What Are Skill Attribute Groups?

*Skill Attribute Groups* can be associated with skills. By modifying the values in an attribute group, certain skill behaviors can be changed dynamically

# II. Editing Skill Attribute Groups

Click [Skill Resource Management] in the System Menu to open the Skill Resource Management interface

![](../../../images/1d35e4f147cb7669.png)

In this interface, select the [Skill Attribute Group] tab to edit globally available attribute group settings

![](../../../images/d4ede6a7a28c5131.png)

*Attribute Group Name*: The name of the attribute group configuration

*Configuration ID*: The unique identifier for the Skill Attribute Group. Used when referencing it from external systems

*Attribute Type*: Skill Attribute Groups support different attribute types. The current version supports only two

*Animation Speed Multiplier*: Adds an additional modifier to base animation playback speed, making the animation play faster or slower. This also affects the trigger timing of the corresponding Skill Node Graph

*Cooldown Time Multiplier*: Adds an additional modifier to a skill's base cooldown time, making the skill cool down faster or slower

# III. Calculation Formula for Attribute Types

The stacking rules for additional Skill Attributes follow the formula below:

**Final Animation Speed = Initial Skill Attribute Group Value + Σ(Unit Status Modifier × Stacks) + Σ(Skill Track Modifier)**

*Initial Skill Attribute Group Value*: Initial value configured in the skill settings

*Unit Status Modifier*: Modifier added through Unit Status

*Stacks*: Total number of Unit Status stacks

*Skill Track Modifier*: Modifier applied through the Skill Track

**Final Skill Cooldown = Base Skill Cooldown × (Initial Skill Attribute Group Value + Σ(Unit Status Modifier × Stacks))**

*Base Skill Cooldown*: Initial value configured in the skill settings

*Initial Skill Attribute Group Value*: Initial value configured in the skill settings

*Unit Status Modifier*: Modifier added through Unit Status

*Stacks*: Total number of Unit Status stacks

# IV. How to Modify Skill Attribute Groups

## 1. Skill Configuration Referencing

In the Skill Editor, locate the "Skill Attribute Group" field under Numerical Configuration and click [Edit] to open the Attribute Group Editor

Use the dropdown menu to select a preconfigured Skill Attribute Group and associate it with the skill. The initial value of the attribute group will use the globally defined default value

![](../../../images/edb1cdcc6903981b.png)

## 2. Unit Status Modification

By using the [Adjust Animation Speed] and [Adjust Cooldown] Unit Status options, Craftspeople can dynamically modify the values of a specific Skill Attribute Group during runtime

![](../../../images/fed7fab640c4766a.png)

## 3. Skill Track Modification

By adding an "Adjust Animation Speed" event to the [Status Track] in the Skill Animation Editor, you can modify the animation speed of specific animation phases during skill execution. This method supports only fixed parameters and is typically used to improve animation presentation

![](../../../images/137be0826f47cc76.png)

# V. Node Graph

![](../../../images/a410bb06aa31ebe1.png)
