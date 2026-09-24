---
title: Unit Tag
path_id: mh8pro09mf5k
updated_at: 2025-10-21 23:17:01
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh8pro09mf5k
---

# I. Unit Tag Functions

*Unit Tags* can provide special markers for units. When creators (Craftspeople) are writing stage logic, they can use unit tags to quickly locate all units with that tag. All unit types that have physical entities in the scene can be configured with unit tags, including: *Creations, Characters, and Objects*

The same entity can be assigned multiple unit tags

# II. Global Definition of Unit Tags

Before using unit tags, they need to be globally defined in the Tool

## 1. Manage Unit Label Tool

The Manage Unit Label Tool has the following two entry points:

### (1) Left System Menu

Click [Manage Unit Label] in the system menu to open the Manage Unit Label tool.

![](../../../images/da30d5ba83e32e4a.png)

### (2) Basic Information Panel

Quickly open via the "Open Unit Label Manager" button in the Basic Information Panel's Manage Unit Label section

![](../../../images/d423c38a22aba368.png)

## 2. Defining Unit Tags

In the Manage Unit Lable interface, click "Create New Unit Tag" to add a new Unit Tag

![](../../../images/d3bbbd497882930e.png)

*Unit Tag Name*: The naming of Unit Tags serves as a reminder and is not used as a logical indexing method.  
*Index*: The unique identifier of this Unit Tag, used for identifying when modifying Unit Tag data in the node graph

*Find References*: Click this button to display all entities that reference this Unit Tag

# III. Configuring Unit Tags

On the basic information page of prefabs or entities, you can find their Unit Tags. Click "Add Unit Tags" to choose from multiple globally defined Unit Tags, which will take effect as the initial data. A prefab or entity can carry multiple tags at the same time

![](../../../images/5e8256794bf56a67.png)

# IV. Modifying Unit Tags Through Node Graphs

## Server Nodes

Clear Unit Tags From Entity

![](../../../images/435a85c20e5a31f0.png)

Add Unit Tag to Entity

![](../../../images/5c9cf080e92aced2.png)

Remove Unit Tag From Entity

![](../../../images/29fba27983ec46e6.png)

Get Entity List by Unit Tag

![](../../../images/a6aa1302517b612a.png)

Get Entity Unit Tag List

![](../../../images/c7925becbcc3bfc0.png)

## Client Node

Get Entity List by Unit Tag

![](../../../images/c5245b2e16cdccb8.png)

Get Entity's Unit Tag List

![](../../../images/cce06f4cf38471cb.png)
