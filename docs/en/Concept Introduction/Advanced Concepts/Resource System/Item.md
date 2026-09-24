---
title: Item
path_id: mh1wwh99g1re
updated_at: 2025-10-20 15:54:33
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh1wwh99g1re
---

# I. Definition of Items

*Items* are virtual objects that players can obtain, use, or equip during gameplay. In Miliastra Wonderland, items are categorized into multiple types and are managed uniformly through the *inventory*

# II. Item Classification

Items are categorized into Equipment, Materials, Consumables, and Very Special Items

# III. Editing Items

In the item tab shown below, you can edit items

![](../../../images/adb324b9330e5586.png)

Click the "New Item" button and click Confirm in the Pop-Up to create a new item template

![](../../../images/1ea5ab5039322fa4.png)

![](../../../images/8ace53029bac7dbe.png)

![](../../../images/f65ee5c97f65d149.png)

*Item Name*: The name of the item displayed in the interface during gameplay

*Item Icon*: The icon displayed in the interface during gameplay

*Configuration ID*: The unique identifier of the item template, which can be used in Node Graphs

## 1. Basic Settings

![](../../../images/870082584f254525.png)

Basic settings primarily define an item's displayed information and how it appears in the inventory

*Rarity*: Rarity determines the background color of the item icon, currently available in gray, green, blue, purple, and orange

*Stack Limit*: The maximum number of items that can be stored in a single inventory slot within the inventory

*Associated Item Node Graph*: When an item enters the character's inventory, the related Node Graph will be attached to the character unit

*Inventory Ownership Tab*: Determines which tab the item will be sorted into when it enters the inventory

*Description*: The item's description that will be displayed in the interface during gameplay

*Has Currency Value*: Select "True" to relate a *currency value* to a single item, which serves as a value anchor for transactions in the *shop module*

*Display Currency Value:* Enable this to display the currency value of the item in the inventory

*Currency Value*: When the item has a currency value, clicking [Add Currency Value] allows you to configure the specific amount

## 2. Drop Settings

![](../../../images/a26b954b4cf22e24.png)

Items can drop into the scene from the inventory in multiple ways, including when the owner is defeated or through Node Graph triggers. The drop settings section defines the specific logic executed when a drop event occurs

*Destruction Debris*: The process executed when the item owner is defeated

*Loot*: When the owner is defeated, items are converted into loot entities and created in the scene

*Destroy*: When the owner is defeated, the items are destroyed

*Save*: When the owner is defeated, items are saved in the inventory. This setting is only meaningful when the owner is a character. For other types of entities, the logic is the same as Destroy

*Loot Drop Mechanics*: Divided into Shared Reward and Individualized Reward

*Shared Reward*: All players share the same loot. Once one player picks it up, other players cannot pick it up

*Individualized Reward*: Each player will receive their own independent copy of the dropped item, and players' pickup actions do not affect each other

*Corresponding Loot Appearance*: Configure a *loot prefab*, which is a physical entity component. When the virtual item is created in the scene, it will be displayed using the corresponding loot model

## 3. Interaction Settings

![](../../../images/0902d3601df71df4.png)

Interaction settings define what players can do with an item in their inventory

*Destructible*: Whether players can destroy this item in their inventory through interface actions

*Tradable*: Whether the item can be sold in the shop

*Usable*: Whether players can use an item through interface actions

*Allow Bulk Use*: Whether multiple items can be used in a single operation

*Auto Use Upon Pickup*: When set to "Yes", the item will be automatically used upon acquisition

*Cooldown (s)*: After using the item, it will enter cooldown and cannot be used again during this period

*Group Cooldown (s)*: When this item enters cooldown, all items related with the Linked Cooldown Group will enter cooldown simultaneously, with a duration equal to this value

*Linked Cooldown Group*: Configure a list of items that defines all items within the cooldown group
