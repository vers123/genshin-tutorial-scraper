---
title: UI Control Group
path_id: mh280b9i9gxm
updated_at: 2026-05-08 12:22:39
category: Concept Introduction/Advanced Concepts/UI Control Groups Management
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh280b9i9gxm
---

# I. Definition of UI Control Groups

*UI Control Groups* are custom data for UI controls created by creators (Craftspeople).

A UI Control Group is data saved after combining and editing parameters for single or multiple prefab *UI Controls*.

UI Control Groups include two types: individual UI Controls and combined UI Controls.

[UI Controls](/ys/ugc/tutorial//detail/mhnapxrumtzy) refer to the various assets used to design and implement the [Interface Layout](/ys/ugc/tutorial//detail/mhozt0r74ng6)

# II. Editing UI Control Groups

UI Control Group templates can be directly referenced in *Interface Layout* configurations or managed through Node Graphs.

UI Control Groups can be managed uniformly through the UI Control Group Composite, or the states of individual UI Controls within can be managed separately.

## 1. Naming and ID

In the *UI Control Library Management Tool*, each UI Control Group has its own ID, which serves as an input parameter for the Node Graph

UI Control template combinations, and combined UI controls each have their own identifying ID

![](../../../images/bd5db5c754676490.png)

![](../../../images/7f26cf333a31839e.png)![](../../../images/63fb1c76eaec9154.png)![](../../../images/d25525e3baac80df.png)![](../../../images/fc35fb7e5ac68cd2.png)

## **2. UI Control Group Statuses**

(1) UI Control Group *Statuses*: **Active, Inactive**

Active Exists in the Interface Layout, with its display state managed through the node graphInactive Does not exist in the Interface Layout, and its display state cannot be manipulated

(2) *Display* *states* of the activated UI Control Groups: **Enabled, Disabled, Hidden**

Enabled: The UI Control Group visibility is turned on.

From the Hidden state to the Enabled state: The UI Control Group visibility is turned on.

From the Disabled state to the Enabled state: The UI Control Group is reinitialized and its visibility is enabled

Disabled: The UI Control Group visibility is turned off, and dynamically modified information is not saved

After reopening a Disabled UI Control Group, both its display and data are reinitialized

Hidden: The UI Control Group visibility is turned off while preserving dynamically modified information

After reopening a Hidden UI Control Group, both its display and data remain consistent with the state before hiding

# III. UI Control Group Management

## 1. Reference by Interface Layout

UI Control Group templates referenced in the Interface Layout are activated by default along with the Interface Layout. Their statuses cannot be modified. Only their display state can be adjusted.

## 2. Manage with Node Graphs

**Activate UI Control Group in Control Group Library**

During runtime, UI Control Groups can be created in the Player's current Interface Layout.

![](../../../images/8b3a1f23b7a0af40.png)

**Remove UI Control Group From Control Group Library**

At runtime, you can remove the UI Control Group created by the "**Activate UI Control Group in Control Group Library**" node from the Player's current Interface Layout

![](../../../images/db7c5cd58dfcd098.png)

**Modify UI Control Status Within the Interface Layout**

For an activated UI Control Group, you can adjust its display state.

![](../../../images/d52dfb4fcfe2cb1c.png)

**When UI Control Group Is Triggered**

This Event is only received by the Node Graph of the *Player* who triggered the Button.

![](../../../images/c140e72c4eb4dddb.png)
