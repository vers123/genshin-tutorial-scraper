---
title: Generic Pins
path_id: mh2oo29vhloy
updated_at: 2025-10-21 05:36:39
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2oo29vhloy
---

# I. What are Generic Pins?

While using the node graph, you may have encountered nodes with generic selection buttons (the small gear icon before the parameter pin)

![](../../images/be045e3f9ab08f09.png)

We call pins with such buttons *Generic Pins*, and nodes with generic pins are called *Generic Nodes*

Generic Pins represent **pins that can connect to multiple different data types**. The parameter types supported by each generic parameter pin can be viewed by clicking the generic selection button

Take the [Addition] node above as an example, both input parameters of this node support two types of input: [*Integers*] and [*Floating Point Numbers*]

![](../../images/816c17396f867312.png)

It should be noted that as explained in [Basic Concepts](/ys/ugc/tutorial//detail/mhk23ora1wom), although Generic Dodes and Generic Pins exist in the Node Graph, the Node Graph remains *strongly typed*.

Therefore, when uploading Node Graph data, all Generic Pins and Nodes must go through a process of ***Generic Type Determination***

Generic Type Determination refers to **assigning a concrete data type to each Generic Pin on a node**. Once all pins have a defined type, the node completes its Generic Type Determination and becomes valid for use

If a node remains in a generic state when entering playtest, it will be considered invalid and will not run properly at runtime.

Generic Type Determination may cause previously valid connections to break. (For example, if an integer type is changed to a string type, existing connections to integer pins will be disconnected)

Still taking the [Addition] node in the above graph as an example

When an Addition node is first added to the Node Graph, it defaults to a generic state, which means it is not yet a valid node for runtime execution

![](../../images/816c17396f867312.png)

After either connecting or manually defining the generic type, once the Node is set to a specific type (for example, integer addition as shown in the graph), it becomes a valid and usable node

![](../../images/4d8d141526dd7b8d.png)

# II. Generic Pin Type Determination

There are two ways to determine generic types: manual selection and connection-based determination

## **1. Manual Generic Type Determination**

Click the generic type selection button (the small gear before the parameter pin) to specify the generic type for that pin

![](../../images/90f010a5051fe6d5.png)

## **2. Connection-based Generic Type Determination**

A more common approach is to determine generic types through direct connections.

Connect the Generic Pin to another Parameter Pin. As long as the connected pin type is supported by the Node's generic types, the connection is valid

After the connection is complete, the Generic Pin will be determined as the pin type it is connected to

![](../../images/c35b87a081754171.png)

Generic Pins can also connect to other Generic Pins. In this case, both pins will be assigned the same default type

For example, when two Addition nodes are connected, both will be determined as integer type

![](../../images/c0097c31008387e1.png)

# III. Key Points for Using Generic Pins

## **1. Type Linkage of Multiple Generic Pins**

While using Generic Pins, you may notice some Nodes have multiple Generic Pins (Addition shown above is a typical example)

In fact, for each Generic Node's Generic Pins, their available parameter types are related to one another

When one pin's type is determined, it narrows the range of available types for the other pins.

Take the [Data Type Conversion] Node as an example. It has two Generic Pins: input and output

When the input pin is set to a 3D Vector type (as shown in the graph below)

![](../../images/5121e9dd3b0f0f75.png)

The Output Pin's Generic Pin will be restricted to only the String type, since there is only one possible Parameter Type combination where the input is a 3D Vector and the output is a String

![](../../images/c1d9964291ff30c8.png)

For most Nodes, once one Generic Pin's type is set, the others will be automatically determined. In practice, defining just one pin is usually enough

For instance, in an Addition node, if Input 1 is set to Integer, then Input 2 and the Result pin will also become Integer

![](../../images/30f6631e595cd711.png)

## **2. Checking Generic Pins on Event Nodes**

In most cases, for operation, search, and execution nodes, input and output pins usually have values or connections, so it's rare for them to remain undetermined at upload

However, event nodes sometimes don't use all their Output Parameters. Take the [When Custom Variable Changes] node as an example

![](../../images/7267347e7a1e4e69.png)

By default, this node is in a generic state. You need to define types for its [Pre-Change Value] and [Post-Change Value] Parameter Pins before it can function properly.

However, in some cases, these pins may remain unconnected. If uploaded in this generic state, the Node may fail to trigger correctly
