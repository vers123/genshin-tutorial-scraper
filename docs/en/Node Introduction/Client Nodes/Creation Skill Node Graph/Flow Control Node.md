---
title: Flow Control Node
path_id: mhvwl90ktgkg
updated_at: 2026-04-02 09:31:44
category: Node Introduction/Client Nodes/Creation Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhvwl90ktgkg
---

# I. General

## **1. Double Branch**

![](../../../images/5c173d8f3ee3de81.png)

**Node Functions**

Branches into True or False based on the evaluated condition

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |

## **2.** **Multiple Branches**

![](../../../images/4695b88208dd6df2.png)

**Node Functions**

Takes an input parameter as a control expression (supports integers or strings). Multiple branches can be defined based on the value of the control expression.

Execution follows the output pin whose value matches the control expression. If no matching pin is found, it will proceed through the [Default] pin.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Expression | Generic | Supports only integers or strings |
