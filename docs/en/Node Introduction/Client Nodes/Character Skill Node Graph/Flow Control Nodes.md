---
title: Flow Control Nodes
path_id: mh9ulu0btt60
updated_at: 2026-04-02 09:30:31
category: Node Introduction/Client Nodes/Character Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh9ulu0btt60
---

# I. General

## **1. Double Branch**

![](../../../images/0ab5eafa299bd6b2.png)

**Node Functions**

Branches into True or False based on the evaluated condition

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |

## **2.** **Multiple Branches**

![](../../../images/2c3fd678453a0b68.png)

**Node Functions**

Takes an input parameter as a control expression (supports integers or strings). Multiple branches can be defined based on the value of the control expression.

Execution follows the output pin whose value matches the control expression. If no matching pin is found, it will proceed through the [Default] pin.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Expression | Generic | Supports only integers or strings |
