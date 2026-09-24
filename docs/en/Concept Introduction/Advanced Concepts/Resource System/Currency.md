---
title: Currency
path_id: mhjzofrtnejy
updated_at: 2025-10-20 17:27:03
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhjzofrtnejy
---

# I. Definition of Currency

Currency is a general item used in gameplay. It is used to determine the value of virtual items and evaluate whether trades can be completed. Currency can be held by units and will increase or decrease through trading or Node Graph logic

# II. Editing Currency

Enter the editing interface through the [Currency and Inventory] button

![](../../../images/3c08120d02223b50.png)

Enter the Currency tab to edit the currency details

![](../../../images/87f3a27e1a8e9b52.png)

*Currency Name*: Name defined by the creator (Craftsperson) for the currency

*Configuration ID*: Unique identifier for currency data

**Base Attributes**

*Icon*: The display style of currency during gameplay. You can click the icon to select one from prefabricated icons*Destruction Debris*: The logic executed when the currency owner is defeated

*Loot*: Converted into loots and created in the scene

*Destroy*: Currency is destroyed

*Save*: Only applies to characters. Currency will be retained after character revival. For units other than characters, this is equivalent to Destroy

*Loot Drop Mechanics*: When currency drops, it will be converted into an entity that drops in the scene

*Shared Reward*: All players share the same currency loot entity. Once one player picks it up, other players can no longer pick it up

*Individualized Reward*: Each player will have their own independent currency loot entity generated locally, and players' pickup actions do not affect each other

*Corresponding Loot Appearance*: Configure a *loot prefab*, which is a prefab with physical properties. When a virtual item is created in the scene, it will be displayed using the related loot model*Display Priority**:* The higher the number, the higher the item will be displayed in the inventory
