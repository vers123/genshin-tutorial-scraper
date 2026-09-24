---
title: Flow Control Node
path_id: mhn3j59zbuju
updated_at: 2026-02-16 15:30:26
category: Node Introduction/Client Nodes/Creation Status Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhn3j59zbuju
---

# I. General

## **1. Multiple Branches**

![](../../../images/d779dcfa782df241.png)

**Node Functions**

Accepts one input parameter as the control expression (supports Integer or String). Branches into multiple paths based on its value

When the value on an Output Pin equals the control expression, execution continues along that Output Pin. If no pin matches, the [Default] pin is taken

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Expression | Generic | Only supports Integers or Strings |

## **2. Double Branch**

![](../../../images/3526b67618bc9899.png)

**Node Functions**

Branches into True or False based on the evaluated condition

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |

###
