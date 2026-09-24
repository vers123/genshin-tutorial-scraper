---
title: Other Nodes
path_id: mh5bv0rnxwxi
updated_at: 2026-02-16 15:45:27
category: Node Introduction/Client Nodes/Creation Status Decision Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh5bv0rnxwxi
---

## **1. Execute Only by Sequence**

![](../../../images/ac7e9d175ecda099.png)

**Node Functions**

Start Event for the Creation Status Decision Node Graph

The Creation Status Decision Node Graph starts with an [**Execute Only by Sequence)]** node. Each output pin connects to a **[Switch to self execution status]** node, so you can execute different behaviors as needed. If the entry conditions for the previous state are not met, it will enter the *Failed Execution* first. If the conditions are still not met, it will try the state on the next pin

The Creation Status Decision Node Graph runs continuously. When a state earlier in the sequence meets its conditions, the Complex Creation immediately switches execution state and executes the Status Node Graphs in that preceding order

If no conditions are met, the Complex Creation may not execute any Status Node Graph

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation Status Node Graph in Node C is currently running, but Node A's execution conditions are met, the Complex Creation will immediately switch to the Creation Status Node Graph in Node A

![](../../../images/dee89c3b2cfe045f.png)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

##
