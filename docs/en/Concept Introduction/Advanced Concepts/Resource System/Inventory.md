---
title: Inventory
path_id: mhb12f03r2y8
updated_at: 2025-10-20 17:30:59
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhb12f03r2y8
---

# I. Definition of Inventory

The inventory is a container for the entire resource system, managing all virtual items, equipment, and currency owned by the inventory owner

In the inventory interface, items are displayed in slots. Players can split, destroy, or discard items in the inventory during gameplay

# II. Editing Inventory

Open the system menu and click the [Currency and Inventory] button to enter the editing interface

![](../../../images/560b43dfc68c3c51.png)

Enter the Inventory tab to edit the inventory template's details

![](../../../images/a66f7d14ff8df444.png)

*Inventory Template Name*: ame defined by the creator (Craftsperson) for the inventory template

**Base Attributes**

*Inventory Slots*: Initial number of inventory slots, each slot can hold one type of item and may stack multiple copies of an item based on its stack limit*Destruction Debris*: When the inventory owner is defeated, all items in the inventory will be batch processed according to this setting. When this configuration is not set to "Apply Item Loot Rules", this configuration will override the same field configured in the item template

*Loot*: When the owner is defeated, all items in the inventory are converted into loot entities and created in the scene

*Destroy*: When the owner is defeated, all items in the inventory are destroyed

*Save*: When the owner is defeated, all items in the inventory are saved in the inventory. This setting only takes effect when the owner is a character. For other types of entities, the logic is the same as "Destroy"

*Apply Item Drop Rules*: Follow the "Destruction Debris" configuration for individual items within the inventory

*Loot Drop Mechanics*: When an inventory is dropped, all items will be converted into a single entity that drops in the scene, rather than creating separate entities for each item

*Shared Reward*: All players share the same inventory loot entity. Once one player picks it up, other players can no longer pick it up

*Individualized Reward*: Each player will have their own independent loot entity corresponding to the inventory contents, and players' pickup actions do not interfere with each other

*Corresponding Loot Appearance*: Configure a *Loot Prefab*, which is a prefab with physical properties. When the inventory content is created in the scene, it will be displayed using the related loot model

# III. Inventory Runtime Instance

During actual gameplay, the inventory template definition is referenced and instantiated by the[Inventory](/ys/ugc/tutorial//detail/mh5y5001vqd4) entity

![](../../../images/01e19e1e4e71852a.png)

#
