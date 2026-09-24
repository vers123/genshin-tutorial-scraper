---
title: Other Nodes
path_id: mhe4x4i9fiy4
updated_at: 2026-02-16 15:31:23
category: Node Introduction/Client Nodes/Creation Status Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhe4x4i9fiy4
---

## **1. Execute Only by Sequence**

![](../../../images/882f7e2816ec1810.png)

**Node Functions**

Start Event of the Creation Status Node Graph

The Creation Status Node Graph starts with an [**Execute Only by Sequence]** node. Each output pin connects to an Execution Node, allowing different actions to run as needed. If the entry conditions for the previous action are not met, the graph will enter the *Failed Execution* first. If the conditions are still not met, it will try the action on the next pin

The Creation Status Node Graph runs continuously. If a higher-priority behavior meets its conditions, the Complex Creation immediately switches to execute that behavior

If the conditions are not met, the Complex Creation may not execute any actions

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation is executing the behavior in Node C, but Node A's execution condition is met, the Complex Creation will immediately switch to executing the behavior in Node A

![](../../../images/5e003f87decf492c.png)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

##
