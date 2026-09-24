---
title: Equipment
path_id: mhsyagijjq5o
updated_at: 2025-10-21 02:11:53
category: Concept Introduction/Advanced Concepts/Resource System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhsyagijjq5o
---

# I. Definition of Equipment

Equipment is a sub-type of items that is managed through the inventory like regular items. The difference is that equipment can be equipped in Equip Slots to provide attribute bonuses or additional logic functions for the wearer

# II. Editing Equipment

## 1. Create New Equipment

Similar to the item editing tab, click "New Item" as shown in the graph below

![](../../../images/33c3c28283d1c5ec.png)

In the pop-up, scroll down to [Select Type] and choose Equipment to create a new equipment template

![](../../../images/27028e812a1f1e69.png)

## 2. Basic Settings

The basic settings of equipment are similar to regular items, but stacking configuration is not supported. Refer to [Item](/ys/ugc/tutorial//detail/mhbgx0rspbqu)

![](../../../images/17d2b531a908963c.png)

## 3. Interaction Settings

Interaction settings support additional settings for equipment types.

![](../../../images/40e02d303bbc2f0c.png)

*Equipment Type*: Equipment type can be defined in the Equipment Type tab. When attempting to equip an item, the *Equipment Slot* must support that equipment type in order to equip

*Show Type in Details*: Whether to display the equipment type information on the interface during gameplay

*Show Tags in Details*: Whether to display the equipment's tag information on the interface during gameplay

*Select Tag*: Here you can select the *tags* that this equipment should have from all pre-configured equipment tags

*Select Initial Affixes*: Here you can select the *initial affixes* that the equipment should carry from all pre-configured equipment affixes

## 4. Equipment Type

Equipment type is an attribute of equipment that is referenced by two working functions:

*Equipment Template*: Defines the type of the equipment itself

*Equipment Slot Template*: Defines which types of equipment can be equipped in each Equipment Slot

When there is a non-empty intersection between the type list configured in the equipment template and the type list of Equipment Slots, i.e., when any type matches successfully, the equipment can be successfully equipped

Enter the editing interface via *Manage Equipment Data* as shown in the image

![](../../../images/aae5e7e7946c6d0e.png)

Enter the Equipment Type tab to edit and add equipment types

![](../../../images/74a38756534bfb15.png)

*Type Name*: Name defined by the user for the type

*Configuration ID*: Unique identifier for equipment type data

*Reference List*: View all equipment templates using this type

## 5. Equipment Tags

Tags are visible annotations for equipment that can be used by creators (Craftspeople) to convey the characteristics of the equipment to players

In the Tags tab of Manage Equipment Data, you can define equipment tags so they can be referenced by equipment templates:

![](../../../images/78565b864ae720ca.png)

*Tag Name*: Name defined by the creators (Craftspeople) for the tag

*Configuration ID*: The unique identifier of the equipment tag data

*Reference List*: View all equipment templates using this tag

## 6. Equipment Affixes

Equipment affixes are the only source of equipment attribute bonuses and mechanical bonuses. Each piece of equipment can have multiple affixes. Based on the affix configuration, when the equipment enters the inventory or is equipped, the bonuses provided by the affixes will be applied to the owner or wearer entity

In the Affixes tab of Manage Equipment Data, you can define equipment affixes that can be referenced by equipment templates:

![](../../../images/e7f98b8ee39e5c0d.png)

*Affix Name*: Name defined by the user for the affix

*Configuration ID*: The unique identifier for equipment affix data

*Reference List*: View all equipment templates using this affix

**Affix Attributes**

![](../../../images/8652177050cb3a88.png)

*Effective Timing*: The timestamp when the affix's bonus effects will come into effect

*Effective When Obtained*: Takes effect on the inventory owner as soon as the equipment enters their inventory

*Effective When Equipped*: Only takes effect on the wearer when equipped in an Equipment Slot

Affixes are divided into different types, each providing different bonuses

*Base Attributes Bonus*: Provides basic combat attribute bonuses

*Select Attributes*: Choose a specific combat attribute to apply a bonus to. The bonus attribute type provided by each affix is unique

*Bonus Type*: There are two types — *Random Value* and *Fixed Value*. Random value bonuses will randomly select a value within the creator-configured range as the final bonus, whereas fixed value bonus will use the specific value configured by the creator (Craftsperson) as the final bonus

*Random Value Range*: When the bonus type is set to random value, the creator (Craftsperson) can configure the upper and lower limits of the random range

*Fixed Bonus Value*: When the bonus type is set to fixed value, the creator (Craftsperson) can configure the specific bonus amount

*Description Type*: When viewing equipment during gameplay, the specific description of the affix will be displayed on the interface. Creators (Craftspeople) can use preset description text or edit the affix description by themselves

*Fixed Description*: Use preset description text, which can only be used on affixes with base attribute bonus types

*Display Random Value Range in Description*: When enabled, the configured random value range will be shown at the end of the fixed description

*Custom Description*: Creator-defined description. After selecting this, you can input text in the text box below

*Insert Variable*: Insert placeholders in the affix description text to display the bonus range and actual bonus values

*Apply Node Graph*: Provides creator-defined node graph logic

*Related Node Graph*: When the entry type is "Assign Node Graph", you can select the Node Graph to be assigned

*Apply Unit Status*: Affixes can be bound to a unit status

*Corresponding Unit Status*: When the affix type is Apply Unit Status, you can select the unit status to be related

# III. Equipment Entities

When equipment is not picked up, it exists as a template in the loot component. When the equipment template is first obtained and enters the inventory, it will be initialized. At this time, the affix values will be randomized, and a *When**Equipment Is Initialized* event will be triggered. The event output parameter will return the unique index of the equipment entity, through which the equipment's attribute affixes can be dynamically modified. If Creators (Craftspeople) have custom equipment initialization rules, they can also write their own logic in this event to override the preset random rules

# IV. Equipment Slots

Equipment Slots are containers for equipment. Equipment affixes trigger depending on equipment behavior

## 1. Equipment Slot Template

Used to define the style, quantity, and equipment tags for each Equipment Slot. Enter the editing interface through the [Currency and Inventory] button

![](../../../images/d7d40f118ccb31be.png)

Enter the Equipment Slots tab to edit templates

![](../../../images/fb0f53c7ea73dde5.png)

*Template Name*: Name defined by the creators (Craftspeople) for the equipment slot template

*Configuration ID*: Unique identifier for Equip Slot template data

*Equipment Slot Style*: By clicking the "+" icon, you can dynamically stack Equipment Slots. After adding, you can configure detailed settings for each Equipment Slot

![](../../../images/c5a636f640ec27f2.png)

*Slot Settings*: Settings for individual Equip Slots

*Current Slot Name*: Creators (Craftspeople) can name the slot, which will be displayed at the bottom of the slot interface

*Equippable Types*: Select the types of equipment that can be equipped in this slot

*Icon*: The background graph displayed in the slot when no equipment is equipped

After configuration, an Equipment Slot will appear as shown in the graph below:

![](../../../images/1e2e7dc30c5c266b.png)

## 2. Equipment Slot Component

Equipment Slot Components can only be added to characters

![](../../../images/f192d30fa0ff1433.png)

Select Add Common Component > Add Equipmet Slot Component to add

![](../../../images/23b4034c6254767d.png)

The component interface is shown below

![](../../../images/4acae128a3c6eee9.png)

*Equipment Slot Template*: References pre-defined Equip Slot templates

# V. Modifying Equipment Attributes in Node Graphs

## 1. Equipment Related Execution Nodes

Modify Equipment Affix Value

![](../../../images/4b04cb91389e1a6f.png)

Remove Equipment Affix

![](../../../images/2bc753c333a52501.png)

Add Affix to Equipment

![](../../../images/59f2559e8cfd86b3.png)

Add Affix to Equipment at Specified ID

![](../../../images/7a473dc30a637a18.png)

## 2. Equipment Related Event Nodes

When Equipment Is Initialized

![](../../../images/203066b2324a8c84.png)

When Equipment Affix Value Changes

![](../../../images/388d7f82c7d569fc.png)

When Equipment Is Unequipped

![](../../../images/926fa7a22e7ab101.png)

When Equipment Is Equipped

![](../../../images/b0effcce5d11f938.png)

## 3. Equipment-Related Search Nodes

Query Equipment Tag List

![](../../../images/70600dc504373243.png)

Get Equipment Affix Config ID

![](../../../images/c82cb5fc3b93dff0.png)

Get Equipment Affix List

![](../../../images/3eda48ed3fd58dc3.png)

Get Equipment Affix Value

![](../../../images/fb1beaa9a32b6f1f.png)
