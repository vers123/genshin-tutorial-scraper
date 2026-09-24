---
title: Composite Node
path_id: mhkrg0rfoyhi
updated_at: 2026-08-06 11:21:37
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhkrg0rfoyhi
---

# I. What is a Composite Node?

## 1. Reusing a Function in the Node Graph

During the creation of Node Graphs, you may encounter many scenarios where logic can be reused:

As shown in the graph below, this Node Graph implements a continuous scoring device with the following rules:

When attacked, increase the Custom Variable [Hit Score] on the Entity by 3Then, at 1, 3, and 5 seconds, add 1 to the Custom Variable [Hit Score]

![](../../images/0d41b6149b11bd2e.png)

As the graph shows, the logic for increasing the Custom Variable score is repeated multiple times. This kind of repetition can cause issues during iteration

For example:

If adding points no longer meets your needs, you can change it to deducting points by replacing all addition operations with subtraction operations in bulk within the Node GraphIf you need to change the Custom Variable name used for scoring, you must edit the values in four nodes in the graph above. In more complex Node Graphs, it's easy to overlook some of these changes

## 2. Definition of Composite Nodes

Composite Nodes are designed to address the issues described above.

A Composite Node is a Node Type that allows Creators (Craftspeople) to define custom Node structures. Creators can encapsulate functions implemented in part of a Node Graph within a Composite Node and choose which parameters and Logic Pins to expose externally

In an external Node Graph, a Composite Node can be used like any other Node, following the standard Node Graph connection rules. However, Composite Nodes can only be used in Server Node Graphs and are not available in Client Node Graphs

After optimizing the Node Graph with Composite Nodes, the result is as follows. The Node Graph's functions are clearer and better support complex iterations

![](../../images/34005ad1d124ff18.png)

# II. Structure of Composite Nodes

## 1. External Node Graphs

A Composite Node can be used externally as a regular Node without needing to consider its internal implementation.

All of its Pins follow the standard Node connection rules.

## 2. Inside Composite Nodes

A Composite Node contains an internal *Sub Node Graph* that implements specific functions (for example, adding to a Custom Variable as shown below).

![](../../images/624fa634a18fb2c6.png)

Inside the Composite Node Graph, you can specify which Pins to expose externally (such as the Pins highlighted in the graph below).

In the graph below, the connections on these Pins are called *Virtual Pins*. These act as the Input Pins or Output Pins for the external connections of the Composite Node.

![](../../images/0d39541ed2b57fcb.png)

Exposed Pins can be used as regular Pins in an external Node Graph, as shown in the graph below. The ID numbers on the Virtual Pins match the Pin ID numbers in the Node Graph Editor.

Among these, [Target Entity], [Variable Name], and [Trigger Event] are exposed from the [Set Custom Variable] Node above.

![](../../images/1eb1b320ca2ed022.png)

# III. Editing Composite Nodes

## 1. Creating Composite Nodes

**Create Through Node Graphs**

In a Node Graph, select all Nodes that you want to encapsulate into a Composite Node

![](../../images/545a181bbe479660.png)

Right-click any of the selected Nodes and choose [Generate Composite Node] from the context menu

![](../../images/0d7699e7894de917.png)

This creates a new Composite Node

![](../../images/7d6839f2dcf09026.png)

**Create via Node Manager**

From the window menu in the upper-left corner, open the Node Manager Interface

![](../../images/d9f5c92b89a7418a.png)

In the Composite Node section on the left, you can add new Composite Node Tabs

![](../../images/d0b17a4c835c8721.png)

In the Composite Nodes Management Tab, right-click and select [Create Composite Node] to create a new Composite Node

![](../../images/77861179c60d4c6e.png)

## 2. Editing Composite Nodes

Double-click a Composite Node in the Node Graph or in the Node Manager to enter the Composite Node Editing Interface

This interface is divided into two parts

On the left is the [Composite Node Graph Editor] Interface, which functions the same way as other Node Graphs

On the right is the [Composite Node Preview] Interface, where you can view how the currently edited Composite Node is exposed, and adjust details such as Node names and Pin names

![](../../images/06eaadc78d8f6371.png)

**Composite Node Graph**

The Composite Node Graph works much like any other Node Graph, with the key difference being the presence of Virtual Pins

These Virtual Pins indicate which Pins connect to the outside of the Composite Node. Their configuration can be modified in the Composite Node Preview Tab

![](../../images/bd20fcf9c5edb5b8.png)

Right-click a Pin to expose it as an external Pin of the Composite Node

![](../../images/f78d110c10b315b8.png)

**Editing Composite Node Styles**

In the Composite Node Style Editing Tab, you can configure how the Composite Node is exposed externally

**Renaming Composite Nodes**

Double-click the Composite Node name to rename it

![](../../images/998f0deb214c2f00.png)

**Pin Details Editor**

![](../../images/4a366e92072aba05.png)

Supports the following edits:

Editing Pin names

Editing Parameter Box Hints for External Use

**Pin Actions**

Right-click a Pin to perform various actions, such as moving it up or down, or hiding it from display on the Composite Node

![](../../images/8487536049f599d6.png)

**Pin Merging**

When two Pins of the same type exist on a Composite Node, they can be merged

![](../../images/1b86633129d39f4c.png)![](../../images/827c7058770891ab.png)![](../../images/b7e7b491d3fed922.png)

After merging, the Pin functions as if it were connected to both Pins at the same time

As shown in the graph below, Virtual Pins 1 and 4 are connected to the first Input Parameter Pins of [Set Custom Variable] and [Get Custom Variable], respectively

![](../../images/d92a7291faaad08e.png)

After merging, the Composite Node's style appears as shown in the graph below

![](../../images/866d4be34692976e.png)

As shown, the [Target Entity] Pin of the Composite Node is now connected simultaneously to the first Input Parameter Pins of both [Set Custom Variable] and [Get Custom Variable]

![](../../images/81e076ca1022026f.png)

## 3. Using Composite Nodes in External Node Graphs

In an external Node Graph, the created Composite Nodes can be found under the [Composite Node] category

![](../../images/886558f7b032ff91.png)

Composite Nodes in a Node Graph follow the same rules as any other Node and can be used as any Node Type. As shown in the graph below, both graphs provide identical functionality

![](../../images/496bf329582a2598.png)

![](../../images/6a051e60db30281f.png)
