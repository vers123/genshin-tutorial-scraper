---
title: Skill Resources
path_id: mhk58cry2452
updated_at: 2026-03-30 14:45:12
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhk58cry2452
---

# I. Definition of Skill Resources

*Skill Resources* are resources that need to be consumed when specific skills are cast. For example, "Elemental Energy" in the Classic Mode is a type of skill resource. The Miliastra Sandbox supports creators (Craftspeople) in defining their own types of skill resources and specifying which skill resources their skills require

# II. Editing Skill Resources

## 1. Entry Point for Editing

Enter through the *Skill Resource Management* button in the system menu bar

![](../../../images/4f57a724b913053e.png)

Open the interface to edit globally available skill resource types

## 2. Parameters Introduction

![](../../../images/13fa60fecf90316f.png)

*Skill Resource Name*: Name of skill resource*Configuration ID*: The unique identifier for the skill resource, which is required when calling it from the Node Graph*Growth Type*: The growth type determines the actual growth rules when external logic attempts to increase the quantity of skill resources. Currently, three types are supported

*Unconditional Growth*: When not exceeding the maximum obtainable value, this skill resource amount will grow unconditionally

*Follow Skill (Retaining Value)*: When attempting to change the skill resource amount, it will only succeed if the player currently has a skill that requires this resource. Otherwise, it will not take effect. When no skills require a certain skill resource, the resource amount will be saved

*Follow Skill (Not Retaining Value)*: Same rules as above, but when no skills require a certain skill resource, the resource amount will be reset to zero

*Maximum Obtainable Value*: The maximum value of skill resources. The amount of skill resources that a character can obtain cannot exceed this value*Reference Information*: Indicates which skills reference this skill resource

# III. Modifying Skill Resources in Node Graphs

![](../../../images/ca4f8fbe9212a5c7.png)

![](../../../images/2a0e3e07485f1cf8.png)
