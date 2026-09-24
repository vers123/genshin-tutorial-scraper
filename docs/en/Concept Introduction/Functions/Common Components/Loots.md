---
title: Loots
path_id: mh9sn304he9c
updated_at: 2026-09-08 12:21:43
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh9sn304he9c
---

# 1. Functions of Loot Components

The Loot Component allows creators (Craftspeople) to configure a fixed Loot collection template data, which creates Loot based on this data template when the component holder is defeated

In design, it is recommended for implementing Loot-related concepts

The Loot component only supports configuring one set of Loot template data

# II. Editing the Loot Components

## 1. Add Components

![](../../../images/c77a763101a8edd8.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Common Components" below, then click "Loot" to add it.

(3) Click "Advanced Editing" to expand the editing tab

## 2. Basic Concepts

![](../../../images/578c69d88d688f6a.png)

### (1) Basic Settings

Configuration for Drop Behavior and Drop Methods

*Destruction Debris*: Defines how the drop configuration is handled when the component's owner is defeated

*Individual Drops*: Each virtual item in the Loot Content is converted into a corresponding Loot item and dropped separately

*Combined Drops*: Virtual items in the Loot Content are converted into a single Loot item and dropped

*Loot Drop Mechanics*: Divided into Shared Reward and Individualized Reward

*Shared Reward*: All players share the same loot. Once a player picks it up, other players cannot pick it up again

*Individualized Reward*: Each player's client will generate their own independent copy of the item, and players' looting actions do not affect each other

*Corresponding Loot Appearance*: Configure a *Loot* prefab, which is a physical entity prefab. When a virtual item is created in the scene, it will be displayed using the model of the associated drop prefab. This setting only takes effect when combined drops are selected; if individual drops are chosen, each drop will use the associated drop prefab configured in its own item or currency template

### (2) Loot Content

Configure virtual Loot data. Click "Add Items" to configure a list of virtual items

*Item List*: You can select all defined items, currency templates and quantities

![](../../../images/bf510f915fff2b4e.png)

# III. Loot Collection Examples

![](../../../images/49ad9b5c7ddd1dd3.png)

# IV. Node Graph Operations for Loot Components

### Loot Component Execution Nodes

Trigger Loot Drop

![](../../../images/dd0d7fa2f43aea06.png)

Set Loot Drop Content

![](../../../images/3d28fa5f6d68665a.png)
