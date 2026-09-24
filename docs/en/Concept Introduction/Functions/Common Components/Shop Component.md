---
title: Shop Component
path_id: mh0u129el2nm
updated_at: 2025-10-21 23:43:11
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0u129el2nm
---

# 1. Shop Component Functions

[Shop](/ys/ugc/tutorial//detail/mhi9s7isvp50) template configurations are referenced by shop components and instantiated at runtime

The shop component supports configuring multiple shops simultaneously

# II. Editing the Shop Component

## 1. Add Components

![](../../../images/728c7cdf974801f4.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Common Components" below, then click "Shop" to add it.

(3) Click "Advanced Editing" to expand the editing tab

## 2. Basic Concepts

![](../../../images/d543b204f39e2bc1.png)

*Shop ID*: A shop component can define multiple shops simultaneously, with independent configuration data between shops

*Shop Name*: The name of the shop

*Shop Template*: Reference a globally defined shop template

*\*Preview Shop Style*: Press to preview how the shop style actually appears during runtime with the current configuration

![](../../../images/a8af55f79c8e0442.png)

*Add Shop*: You can add a new shop

**III. Runtime Instance of the Shop**

![](../../../images/029e7cce9041d7ee.png)

# IV. Node Graph Operations

## 1. Shop-Related Execution Nodes

Remove Item From Inventory Shop Sales List

![](../../../images/120cecc2cc8d61cf.png)

Remove Item From Purchase List

![](../../../images/6d21c37c732edb54.png)

Remove Item From Custom Shop Sales List

![](../../../images/bf3b844b30df3fd4.png)

Open Shop

![](../../../images/b9312c7f6116f66b.png)

Close Shop

![](../../../images/203c2a55e5259a92.png)

Add New Item to Inventory Shop Sales List

![](../../../images/9f4b2d98ba44596d.png)

Add Items to the Purchase List

![](../../../images/6017251abf361525.png)

Add New Item to Custom Shop Sales List

![](../../../images/117b71b8484d0bd4.png)

Modify Inventory Shop Item Sales Info

![](../../../images/1380c32c12730411.png)

Modify Item Purchase Info in the Purchase List

![](../../../images/c6c22a019cd64cbe.png)

Modify Custom Shop Item Sales Info

![](../../../images/d69a2e0eab944bbb.png)

## 2. Shop Related Event Nodes

When selling inventory items in the Shop

![](../../../images/44f307f8fc13bf90.png)

When Custom Shop Item Is Sold

![](../../../images/9480c9aabfe92283.png)

When selling items to the shop

![](../../../images/a2132901afd9d22b.png)

## 3. Shop Related Query Nodes

Query Inventory Shop Item Sales Info

![](../../../images/bbd11cf934e578b4.png)

Query Inventory Shop Item Sales List

![](../../../images/3f6ca614e8a5a9cb.png)

Query Shop Purchase Item List

![](../../../images/ca9760a93a7603d1.png)

Query Shop Item Purchase Info

![](../../../images/133f49ddc95dfa32.png)

Query Custom Shop Item Sales List

![](../../../images/82e5d1ed87926322.png)

Query Custom Shop Item Sales Info

![](../../../images/fedd8bb288d8b822.png)
