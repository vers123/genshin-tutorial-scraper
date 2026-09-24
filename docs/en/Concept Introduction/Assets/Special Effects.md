---
title: Special Effects
path_id: mhj2cxr3751a
updated_at: 2025-10-17 14:51:43
category: Concept Introduction/Assets
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhj2cxr3751a
---

# I. Definition of Special Effects

*Special effects* are art assets that can be used to enhance visual effects during gameplay.

Special effects must be attached to an entity, with each effect having a designated mount entity.

When a special effect plays, it uses the entity's *Attachment Point* as its origin and follows that point's position at runtime.

Referencing a special effect requires a VFX Player component.[VFX Playing](/ys/ugc/tutorial//detail/mh4ppo02m1o8).

# II. Classification of Special Effects

Based on the playback duration of special effect assets, timed effects pools and looping effects pools are provided

## **1. Timed Effects**

Timed special effects have an effective duration.

Timed effects will only play once when triggered, and will not repeat.

## **2. Looping Effects**

Looping effects have no fixed duration and continue playing until stopped or removed.

# **III. Using Special Effects**

## 1. Component Mounting

Supports mounting effects via the VFX Playing Component during prefab/entity editing. These effects are created alongside the entity

For editing details, please refer to [VFX Playing](/ys/ugc/tutorial//detail/mh4ppo02m1o8) for use.

## 2. Usage in Node Graphs

Supports creating and deleting special effect assets via effect-related nodes in the node graph.

Different reference special effect asset nodes are provided for different special effect types.

**Play Timed Effects**

Effects from the timed effect pool can be referenced by selecting entities with the "VFX Playing Component" and configuring *Attachment Points*.

If the Attachment Point is incorrect, the special effect will not play

If no Attachment Point is specified, it defaults to the GI\_RootNode

![](../../images/7cc9c8312e0e3116.png)

**Mount Looping Special Effect**

Effects from the looping effects pool can be referenced by selecting entities with the "VFX Playing Component" and configuring Attachment Points.

If the Attachment Point is incorrect, the special effect will not play

If no Attachment Point is specified, it defaults to the GI\_RootNode

![](../../images/a15ea617e3143d95.png)

**Clear Looping Special Effect**

Looping effects created by the "Mount Looping Special Effect" node can be cleared using this node

![](../../images/258cbc4f730e16a4.png)

**Clear Special Effects Based on Special Effect Assets**

Clear the specified special effect assets from the selected runtime entity

![](../../images/5211a1d185bf1d0b.png)

Click the ![](../../images/7e84fd7aa27e0ec4.png) icon to view all special effect enumerations and select the specified special effect asset

![](../../images/135477f52ad8a598.png)
