---
title: Inventory Component
path_id: mhir93rudpv2
updated_at: 2026-02-06 17:03:19
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhir93rudpv2
---

# I. Inventory Component Functions

The Inventory component directly references the [Inventory](/ys/ugc/tutorial//detail/mhogfq9bf86q) template and generates corresponding inventory instances at runtime

The Inventory component supports selecting only one inventory template at a time

The Inventory component can be mounted on characters, creations, and dynamic objects

# II. Editing Inventory Components

## 1. Add Components

![](../../../images/a061fba5b50e89dd.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Components" below, then click "Inventory" to add it

(3) Click "Advanced Editing" to expand the editing tab

## 2. Basic Concepts

By adding this component, you can configure the character's inventory component and define default items in the inventory

![](../../../images/e603bc3f4cc268a2.png)

*Inventory Template*: Reference an inventory template

*Starting Items**:* The default item configuration in the inventory. When gameplay starts, the character carries these contents by default

# III. Inventory Runtime Instance

![](../../../images/b9948aa8a610dcd9.png)

# IV. Inventory Data for Node Graph Operations

## 1. Inventory Component-Related Execution Nodes

Set Inventory Drop Items/Currency Amount

![](../../../images/856f8cbbfce870bc.png)

Set Inventory Item Drop Contents

![](../../../images/feb5e67ad701db9c.png)

Increase Inventory Item Quantity

![](../../../images/e9487bb70ad5f787.png)

Increase Inventory Currency Quantity

![](../../../images/1e1525e813636018.png)

Increase Maximum Inventory Capacity

![](../../../images/e6db5669bc96d19c.png)

## 2. Inventory Component-Related Event Nodes

When Item Is Lost From Inventory

![](../../../images/7aff1e19595ad37d.png)

When the Quantity of Inventory Item Changes

![](../../../images/d31f00a596beec96.png)

When Item Is Added to Inventory

![](../../../images/e679bd825445dd68.png)

When the Quantity of Inventory Currency Changes

![](../../../images/885072f1352120f2.png)

When items in the inventory are used

![](../../../images/c25c443c55f36de0.png)

## 3. Inventory Component-Related Query Nodes

Get Inventory Item Quantity

![](../../../images/d79048b877720d79.png)

Get Inventory Capacity

![](../../../images/e9fd8f6c2bec888c.png)

Get All Inventory Basic Items

![](../../../images/74d17d3bdb85d615.png)

Get All Inventory Equipment

![](../../../images/d10079c4a0cbf318.png)

Get All Inventory Currency

![](../../../images/22a2226a01413a81.png)

Get Inventory Currency Quantity

![](../../../images/c9e8212aa1bea3be.png)
