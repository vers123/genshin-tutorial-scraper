---
title: Node Graph Variables
path_id: mhtq21i5la38
updated_at: 2026-08-06 11:25:46
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhtq21i5la38
---

# I. What are Node Graph Variables?

## 1. Definition of Node Graph Variables

A Node Graph Variable has a Life Cycle that follows its Node Graph, and is only valid in *Server Node Graphs*

Its functionality as a variable is largely the same as Custom Variables[Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica), but its Life Cycle and scope differ in certain ways

## 2. Life Cycle and Scope

The Life Cycle of a Node Graph Variable follows the Node Graph. In the case of an Entity Node Graph, when the Node Graph is mounted on an Entity, the Entity holds these variables and can set, obtain, and monitor events through the corresponding operation nodes

A Node Graph Variable can only be accessed within the Node Graph where said Node Graph Variable resides in, including setting, obtaining, and monitoring events

# II. Similarities and Differences with Custom Variables

The following graph outlines the similarities and differences between Node Graph Variables and Custom Variables

|  |  |  |
| --- | --- | --- |
|  | **Node Graph Variables** | **Custom Variables** |
| Life Cycle | Follow Node Graph | Follow Entity |
| Scope | Accessible only within the Node Graph where the variable is defined | Globally accessible, requires specifying the Entity |
| Naming Rules | Names must be unique within the same Node Graph | Names must be unique within the same Component (Entity) |
| Can be overridden on an Entity | Yes, but must be manually exposed | Yes, following the general Component parameter overwriting rules |
| Supported Data Types | All Basic and List Data Types | All Basic and List Data Types |
| Related Actions | Set Value, Obtain Value, Monitor Changes | Set Value, Obtain Value, Monitor Changes |

# **III. Why Use Node Graph Variables?**

Compared to [*Custom Variables*], Node Graph Variables have the following features:

Lightweight to use, they can be defined and used entirely within the Miliastra Sandbox, enabling complete logic and data authoring inside the sandboxAllows duplicate names, so multiple Node Graph Variables with the same name can exist on an Entity, provided they are distributed across different Node GraphsPrevents variables tied to Node Graph Functions from being exposed externally, reducing the complexity of reading Node Graph logicCreators (Craftspeople) can focus on encapsulating Node Graph Functions without concern for which Entity the Node Graph will be mounted on, allowing for more modular design

When designing gameplay data structures, we recommend that Creators apply these two functions as follows:

**Custom Variables**: Store general-purpose data that belongs to an Entity and is globally accessible in the Entity's Custom Variables

For example, the hit count of a mechanism is best stored in a Custom Variable, as it may need to be accessed or modified by other Entities and Node Graphs

**Node Graph Variables**: Store local, temporary variables that belong to the Node Graph within the Entity's Node Graph Variables

For example: When a Node Graph Function of an Object needs to temporarily store a global Player List, it is better to place it in Node Graph Variables. External systems do not require this variable, and storing it in Custom Variable Components could make understanding more difficult

# IV. Editing Node Graph Variables

## 1. Node Graph Variables Tab Entry Point

In the Node Graph Editing Tab - Shortcut menu, you can open the Node Graph Variables tab

![](../../images/df29fb6cae833d25.png)

## 2. Create New Node Graph Variables

Similar to Tab actions and [Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica), you can add and edit the configured Node Graph Variables

![](../../images/af4c9f327199f468.png)

## 3. Using Node Graph Variables in the Node Graph

In a Node Graph, you can use the following Node Graph-related nodes, with usage largely consistent with Custom Variable Nodes

![](../../images/04e191d05218c944.png)![](../../images/c5c158aa45dc77a1.png)![](../../images/97165b9ada85f519.png)

Additionally, you can create operation nodes for Node Graph Variables by dragging them from the Node Graph Variables Tab into the Editing Area

![](../../images/d068c0f3691d0e75.png)

After releasing, a shortcut creation menu appears, allowing you to choose to set or obtain operations for the Node Graph Variable

![](../../images/40a9bd0d2027f6a2.png)

After selection, a new Set or Obtain node for the Node Graph Variable is created automatically

![](../../images/070d15413c3f2b13.png)

## 4. Exposing Node Graph Variables to Stages

**Function of Exposing Node Graph Variables to Stages**

Through the Node Graph Variable exposure feature, you can overwrite the values of *Node Graph Variables* when editing Stages

For example:

In an Explosive Barrel Node Graph, a Node Graph Variable is used to define the Explosive DMG of the barrel. In Stage placement, however, you may want to configure two barrels with different DMG values

This can be done by exposing the Node Graph Variable to the Stage layer, then assigning different overwriting values to the two Explosive Barrel Entities

**Exposing Node Graph Variables to Stages**

Click the Expose button beside a Node Graph Variable and save the Node Graph to expose it to the Stage

![](../../images/db3eefbbd7690a3d.png)

In the Stage's Node Graph, you can view the number of Node Graph Variables currently exposed.

![](../../images/0a0aaab9771ad7da.png)

Click Edit Variable Count to adjust the overwrite values of this Node Graph Variable on the Entity

![](../../images/fa2170d57a83c841.png)
