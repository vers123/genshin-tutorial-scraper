---
title: Flow Control Node
path_id: mhdu50rdh4c6
updated_at: 2026-08-07 15:29:12
category: Node Introduction/Client Nodes/Character Control Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdu50rdh4c6
---

# **I. General**

## **1. Double Branch**

![](../../../images/b69d9b9217202afb.png)

**Node Functions**

Branches into True or False based on the evaluated condition

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |

## **2. Multiple Branches**

![](../../../images/2ec15c1d583109a6.png)

**Node Functions**

Accepts one input parameter as the control expression (supports Integer or String). Branches into multiple paths based on its value

When the value on an Output Pin equals the control expression, execution continues along that Output Pin. If no pin matches, the [Default] pin is taken

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Expression | Generic | Only supports Integers or Strings |
