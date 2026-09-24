---
title: Structure
path_id: mh2zrw94b0v6
updated_at: 2026-01-06 23:08:27
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2zrw94b0v6
---

# I. What is a Structure

A *Structure* is an advanced data type that lets Creators (Craftspeople) group different kinds of data together into a single piece of Custom data

For example, in some gameplay scenarios, a Creator (Craftsperson) may design a [Weapon] with multiple Attributes. This Weapon includes three fields: [Name], [ATK], and [Enhanced or Not]

Creators want Players to store a weapon's data as Custom Variables after obtaining it, so it can be reused later. Meanwhile, Players may acquire multiple different weapons that share the same fields during gameplay

Therefore, Structure can be used to effectively solve this requirement

Creators (Craftspeople) first define a Structure called [Weapon Data] with three Attributes: [Name] (*String*), [ATK] (*Floating Point Numbers*), and [Enhanced or Not] (*Boolean*)

![](../../images/c5e842a48dbc4893.png)

Once defined, [Weapon Data] can then be used like any other data type — for example, as a *Custom Variable*, and modified within a Node Graph using Nodes such as *Modify* *Structure*

![](../../images/f861a6017a2e29fc.png)

Creators (Craftspeople) can also combine it with data structures such as *Dictionary* to maintain complete weapon data in Custom Variables

As shown in the graph below, a Dictionary can be defined to map to [Weapon Data] Structures, functioning as a weapon database (with Integers used as IDs)

![](../../images/0e14f7166d29728b.png)

## 1. Definition of Structure

Structure is a Custom data structure that can be used in Server Node Graphs

Each Structure has a unique name that identifies it

Each Structure can contain multiple data entries of any type, and each entry must have a unique field name. These entries are called *Members* of the Structure

Taking the [Weapon Data] Structure as an example, its layout is as follows:

|  |  |
| --- | --- |
| **Field Name** | **Type** |
| Name | String |
| ATK | Floating Point Numbers |
| Enhanced or Not | Boolean |

Within a Structure, you can use all currently available data types: Basic, List, Dictionary, and Structure:

|  |  |
| --- | --- |
| **Data Types** | **List Data Types** |
| Entity | Entity List |
| GUID | GUID List |
| Integer | Integer List |
| Boolean | Boolean List |
| Floating Point Numbers | Floating Point Numbers List |
| String | String List |
| Faction | Faction List |
| 3D Vector | 3D Vector List |
| Prefab ID | Prefab ID List |
| Configuration ID | Configuration ID List |
| Custom Structure | Custom Structure List |
| Dictionaries of All Types |  |

It should be noted that Structures can also contain other Structures and Structure Lists (i.e., **support nested Structures**)

## 2. Key Points of Structure-Related Functions

**Structure Types**

The type of a Structure is completely determined by its name. Even if two Structures have identical internal data layouts, they are considered different Structures if their names differ, and cannot be connected in a Node Graph

Therefore, structures with the same name are not allowed

**Pass by Reference for Structures**

Similar to Lists, Structures in Node Graphs are passed by reference. As a result, Structure modification Nodes directly affect Structure data stored in Custom Variables and Node Graph Variables. For details, see [Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica)

Similarly, this modification method will not trigger the "When Custom Variable Changes" event; the changed value needs to be obtained through the "Get Custom Variable" node.

# II. Creating a Structure

Find the [Advanced Data Management] option in the menu to open the Structure Editing Tab

![](../../images/54d58799c952e83a.png)

In the Structure Editing Tab, you can view Structures already created in the Stage, add new Structures, and edit the values of Structure Members

You can add new Structures, as shown in Graph A

You can add new Members within a Structure, as shown in Graph B

![](../../images/c20402d56a1bfae8.png)

After creation is complete, you can use the defined Structures in features such as *Server Node Graph*, *Custom Variables*, and *Node Graph Variables*

# III. Using Structures in Generics

In a Server Node Graph, Structures and Structure Lists are special types of *Generic Pins*. You must select a specific Structure or Structure List before the corresponding Node can be defined as that Structure or Structure List type

On Generic Pins that support Structures, you can find [Structure] and [Structure List] options in the Generic dropdown menu. Expanding this menu displays all Structure data types currently defined in the Stage

![](../../images/9f3d6b9fcc15ba19.png)

![](../../images/1f33396b1271cf2f.png)

# IV. Structure-Related Nodes

## 1. Operation Nodes

**Assemble Structure**

Assemble a Structure by passing in or directly assigning values to each of its parameters

![](../../images/b3f5403ff70931e1.png)

To use this Node, first select the defined Structure type via the Generic selection button

![](../../images/f2204bff6a2b779f.png)

After selecting the corresponding Structure, the Node displays all Member variables defined in that Structure

![](../../images/aa34542fb70d511f.png)

**Node Type**: Operation

**Node Functions**

Fill in the values for each parameter in the Structure to generate Structure dataThis Node can only be used once the corresponding Structure type has been defined

**Split Structure**

Pass in a Structure to obtain the values of each Member within it

![](../../images/0c78951911c51b55.png)

To use this Node, first select the defined Structure type via the Generic selection button

![](../../images/7ac231d53cc20d2a.png)

After selecting the corresponding Structure, the Node displays all Member variables defined in that Structure

![](../../images/46eb79451ebecab9.png)

**Node Type**: Operation

**Node Functions**

Returns the values of all Members contained in the input Structure dataThis Node can only be used once the corresponding Structure type has been defined

## 2. Execution Nodes

**Modify Structure**

Pass in a Structure and edit the values of selected Members within it

![](../../images/ab1ff198bc58afea.png)

To use this Node, first select the defined Structure type via the Generic selection button

![](../../images/bb79de2735577479.png)

After selecting the corresponding Structure, the Node changes to the following layout:

![](../../images/1101edae080fdabe.png)

Use the dropdown menu to choose which Members to edit. Only the checked Members will have their values modified

![](../../images/28a9bd00bae1c6e7.png)

As shown in the graph below, only the values of [Name] and [ATK] fields are modified

![](../../images/d0823cac3cb608f2.png)

**Node Type**: Execution

**Node Functions**

Edit the values of selected Members within the Structure dataYou can select which values to edit. Values of unselected Members remain unchanged
