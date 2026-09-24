---
title: Loot
path_id: mh22ge9durci
updated_at: 2026-02-06 17:14:34
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh22ge9durci
---

# I. Definition of Loots

When all virtual *items* (including items, equipment, currency, and inventory) are dropped in the scene, they will be converted into a prefab entity, which is the *Loot*

When editing the templates of the aforementioned virtual items, you need to relate them with a Loot prefab. If no relation is established, the drop logic will be blocked

Loots are special prefabs that, compared to standard dynamic unit prefabs, additionally carry a *Loot Content Component* each, and furthermore, some components available to dynamic unit prefabs are not available for loots

# II. Functions of Loot Content Components

All loot-type prefabs will permanently carry a Loot Content component that cannot be removed

The Loot Content component defines the drop behavior and pickup rules of loots

The Loot Content component supports configuring multiple pickup ranges simultaneously, and their effective ranges will stack

# III. Editing Loot Content Components

## 1. Location of the Loot Content Component

![](../../../images/63dd04db2090638c.png)

Enter the prefab library editor to view the corresponding Loot tab

Click "Advanced Editing" to expand the editing tab

## 2. Loot Settings

![](../../../images/bd14950a38d95cff.png)

When loots are created in the scene due to drop logic, this defines their drop behavior and pickup rules

*Pickup Rules*: How players collect loots during gameplay

*Interactive Pickup*: When the character is within pickup range of the loot, an interaction button will appear. Clicking the button will pick up the item directly

*Auto Pickup*: When the character is within pickup range of the loot, pickup will be automatically triggered

*Open Pickup Interface*: When the character is within pickup range of the loot, an interaction button will appear. Clicking the interaction button will open the loot pickup interface, where players need to select the corresponding loot to pick up. This is recommended when there are multiple items in the loot list

*Auto-Attract Pickup*: Requires additional configuration of "Auto-Attract Range". When the character enters the snap range, the dropped loot will move toward the character and automatically trigger pickup when they enter the pickup range

*Auto-Attract Pickup Range (m)*: The distance at which "Auto-Attract Pickup" triggers loots movement

*Local Filter*: There are two types of filters: Boolean filters and integer filters. For more details, see [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i)

*Filter Node Graph*: You can reference the filter nodes of the aforementioned selection types in the node graph to determine whether the conditions are met

*Loot Content*: Supports configuring a dictionary of virtual items contained in a loot within the component. When the loot is directly placed in the scene and spawned through prefab entities, it will contain all virtual items configured in the component. However, when the loot is created as loot drop/trophies, it will only contain the dropped virtual items, and the default data in the component will be overwritten

## 3. Pickup Range

![](../../../images/9381dc99fc5f4828.png)

*Pickup Range*: Defines the range within which players can collect loots. The structure is defined with common shapes, supporting three basic ones: cuboid, sphere, and capsule

# IV. Loot Pickup Instance

![](../../../images/d5bc2f4b56cb44d4.png)

# V. Node Graph Operations for Loot Components

## 1. Loot Component-Related Execution Nodes

Increase Loot Component Item Quantity

![](../../../images/302b136fbbe7ac41.png)

Increase Loot Component Currency Quantity

![](../../../images/8faaef610069f123.png)

## 2. Loot Component-Related Query Nodes

Get Loot Item Component Quantity

![](../../../images/54e3bee8b763f54a.png)

Get All Equipment from Loot Component

![](../../../images/9c008c680fcdeca4.png)

Get loot item component currency quantity

![](../../../images/7843672bcd35129d.png)
