---
title: Shop
path_id: mht3udinyfqs
updated_at: 2025-10-21 02:20:30
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mht3udinyfqs
---

# I. Definition of Shop

The shop is a module that provides virtual item trading functionality, mounted onto entities as a component

Creators (Craftspeople) can customize the types of virtual items available for trade in a shop (supporting items, equipment, and currency), and configure corresponding selling and buying prices. During gameplay, players can perform buying and selling actions through the shop interface

# II. Types of Shops

There are two basic types of shops:

*Custom Items Shop*: This type of shop can operate independently from the shop owner's inventory, allowing free configuration of a shop template. Buyers will trade with the template data. This does not affect the actual inventory data of the shop owner

*Self Inventory Shop*: When a purchase occurs, the customer and the shop owner will perform an actual exchange of virtual items from their inventories. The shop cannot sell virtual items that the owner does not possess

# III. Editing Shops

The shop template is a complete shop information configuration. Open the system menu and click [Shop Template Management] at the location shown in the graph below to access the shop template editing interface.

![](../../../images/5d922ee7aa6a5470.png)

## 1. Basic Settings

Open the shop configuration interface and click "New Shop Template" to add and edit a template.

![](../../../images/ffbba1eb4328a5d8.png)

*Shop Name*: Shop name as defined by the creators (Craftspeople) during editing, meaningless during runtime.

*Configuration ID*: The unique identifier of the shop template, referenced by Shop components

## 2. Display Settings

This section defines the display information of the shop interface

![](../../../images/4dc6e223d85aa69c.png)

*Open Inventory When Shop Opens*: When enabled, the inventory interface will open simultaneously when players open the shop interface.  
*Shop Item Tab Type*: Determines how tabs are categorized in this shop

*No Tab*: No separate tab configuration, all virtual items are displayed under a single tab

*Default Tab*: Items will be automatically categorized according to their preset types

*Custom Tab*: Tab categorization configured by the creators (Craftspeople)

![](../../../images/ba077907fff893f1.png)

*\*New Tab*: Click to add a new custom tab. When using custom tabs, you can redefine item tabs later when configuring the shop sales list

## 3. Sale Settings

![](../../../images/30a1ef52590f058a.png)

*Shop Item Source*: Refers to the shop types described above, divided into personal inventory and custom list

*Self Inventory*: Virtual items for sale come from the shop owner's inventory. Only the selling price of each type of item can be redefined, and items that are not in the inventory cannot be sold

*\*Sale Range*: Divided into all items and select items, which determines whether all creator-defined items will be added by default when initializing the Sale Settings List

*Custom List*: Freely define the types and quantities of items for sale. This exists as a data template and does not affect the inventory data of the shop owner

*Price Settings*: Define the price list for this shop template

When the item source is from your own inventory, the table structure is shown in the graph below:

![](../../../images/bd0b9d237695c56f.png)

*Items*: List of all items that can be sold

*Affiliated Tab*: Defines which tab the item will be categorized under in the shop interface. When using custom tabs, creators (Craftspeople) can configure which tab each item belongs to

*Sort Priority*: Defines the sorting order of items in the shop interface. Items with higher priority will appear first

*Purchasable*: Only items marked as "True" will appear in the trading interface. This can be modified dynamically during gameplay to achieve the effect of unlocking new items

*Sell Price*: The amount of currency the buyer needs to purchase one of these items during a trade

When custom items are used, the list structure is shown in the graph below:

![](../../../images/c16f34878781f6a6.png)

Most fields are consistent with the inventory item sales list. This section will cover the parts that differ

*Item ID*: When using node graphs to dynamically modify the sales list, the ID is used to identify specific entries for modification. Since multiple identical items may appear in the template shop, different IDs can be used to locate the specific entry that needs to be modified

*Limited Stock*: If set to "No", items can be purchased infinitely. If set to "Yes", you can define the total quantity of this item available for sale in this shop

## 4. Purchase Settings

Purchase settings define the types of items and their prices that players can sell to the shop during trade

![](../../../images/bd4e4537e5978dcd.png)

*\*Purchase Range*: Defines the types of items that can be sold to the shop

*Not Purchasable*: Unable to sell items, the purchase list is empty

*All Items*: The purchase list includes all item types globally defined by the creator (Craftsperson)

*Select Items*: Creators (Craftspeople) can customize which items are available for purchase in the purchase list

*Purchase Price Settings*: Click the edit button to enter price list editing

![](../../../images/218d60552bf2ce24.png)

*Items*: List of all purchasable items  
*Sort Priority*: Defines the sorting order of items in the shop interface. Items with higher priority will appear first

*Can be purchased*: Set to "Yes" for items that can be sold to the shop, can be modified dynamically during gameplay

*Purchase Price*: The amount of currency the shop will pay when purchasing one of these items during a trade

# IV. Runtime Instance of the Shop

During gameplay, the shop template is referenced and instantiated by the [Shop Component](/ys/ugc/tutorial//detail/mho6gviqhsqs)

![](../../../images/5b39c300e1da992d.png)
