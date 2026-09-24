---
title: Cursor Collision Box
path_id: mhqv06r7uefa
updated_at: 2026-07-09 16:43:20
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqv06r7uefa
---

# I. Functions of the Cursor Collision Box Component

The Cursor Collision Box can be mounted on an Entity for cursor ray collision detection

# II. Editing the Cursor Collision Box Component

## **1. Add Components**

![](../../../images/bf4276bc2ccd7f7e.png)

(1) In the Entity/Prefab Editing interface, open the Component Editing Tab

(2) Click "Add Common Component" below, then select and click "Cursor Collision Box" to add it

(3) Click "Advanced Editing" to expand the editing tab

## **2. Editing the Cursor Collision Box Component**

![](../../../images/6065eae976df11bb.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Active Cursor Collision* | The dropdown menu lists the available Cursor Collision Boxes.  Check or uncheck each item to change whether it is active; after editing, the active status automatically syncs to the Pathfinding Obstacle Editing Tab  ![](../../../images/b82c8ba3b1a536a8.png)![](../../../images/1b17575919d0a4be.png) |
| *\*Cursor Collision Box List* | Lists all Cursor Colliders configured for the Entity |

# **III. Edit**ing Cursor Collision Box

## 1. **Add** Cursor Collision

![](../../../images/96d49012bdc4ddac.png)

Click ![](../../../images/71eb10cfeafae8f2.png) to add Cursor Collision

The newly added **Cursor Collision** is initially enabled by default

ID: X, where X represents the **index** of the Cursor Collision. As a Node input, it can be used to adjust whether that Cursor Collision is active

## 2. Related Parameters

![](../../../images/c6386a64bfa18ef4.png)

Cursor Collision supports configuring whether it is initially active

Use the [Add Cursor Collision] button to add multiple areas to a single Cursor Collision

![](../../../images/0bd0fd6925e0a280.png)

The shape of the trigger area supports Cuboid, Sphere, or Capsule

# **IV. Manage** Cursor Collision Boxes through the Node Graph

## 1. Enable/Disable Cursor Collision Box

![](../../../images/bd3ed73da498d8c8.png)
