---
title: Preset Status
path_id: mha3qx0datfk
updated_at: 2025-10-17 15:00:46
category: Concept Introduction/Assets
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mha3qx0datfk
---

# I. Definition of Preset Status

A Preset Status defines a dynamic object's runtime behavior.

Different performance animations are packaged as distinct Preset Statuses.

# II. Characteristics of Preset Statuses

Preset Statuses are runtime animations for dynamic objects; statuses in the same category are distinguished by their Status Values.

Each dynamic object has its own set of Preset Statuses.

A dynamic object's preset status comes from its Preset Status pool; different objects use different pools.

Supports editing and managing dynamic objects with multiple Preset Statuses.

Preset Statuses can be switched via node graphs at runtime.

# III. Editing Preset Statuses

## 1. Setting Initial Preset Status When Editing Dynamic Objects

![](../../images/1afa27ae5b5dcd65.png)

## 2. Managing Preset Statuses with Node Graphs

**Get Preset Status**

Get the Preset Status Value of the specified entity during stage runtime

![](../../images/4de26ae3384ae3f6.png)

**Set Preset Status** 

Configure the Preset Status and Status Values that take effect for entities at stage runtime

If the specified Status Value doesn't exist, the Preset Status won't change

![](../../images/0de0dfbff823e2e3.png)

**When Preset Status Changes**

When a runtime entity's Preset Status and specific Status Values change, events will be sent to the node graph

![](../../images/5f179e0bb75a1ddd.png)
