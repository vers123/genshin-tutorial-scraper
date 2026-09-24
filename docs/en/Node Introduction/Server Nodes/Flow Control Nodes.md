---
title: Flow Control Nodes
path_id: mh0kvz9d42e2
updated_at: 2026-01-09 00:22:49
category: Node Introduction/Server Nodes
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0kvz9d42e2
---

# I. General

## **1. Multiple Branches**

![](../../images/9219750810972610.png)

**Node Functions**

Accepts one input parameter as the control expression (supports Integer or String). Branches into multiple paths based on its value

When the value on an Output Pin equals the control expression, execution continues along that Output Pin. If no pin matches, the [Default] pin is taken

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Expression | Generic | Only supports Integers or Strings |

## **2. Double Branch**

![](../../images/6e6d28ab1fd5609d.png)

**Node Functions**

Branches into True or False based on the evaluated condition

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |

###
