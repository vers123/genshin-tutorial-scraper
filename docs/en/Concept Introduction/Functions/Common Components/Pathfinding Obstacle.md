---
title: Pathfinding Obstacle
path_id: mhvfxi07lbt4
updated_at: 2026-01-06 21:56:34
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhvfxi07lbt4
---

# I. Functions of the Pathfinding Obstacle Component

The navigation system uses a navigation mesh to define walkable areas in the scene

Pathfinding obstacles are objects in the scene that block navigation mesh generation or obstruct Creation movement

The Area settings in the Pathfinding Obstacle component mark regions that Creations cannot traverse

# II. Editing Pathfinding Obstacle Components

## **1. Adding Components**

![](../../../images/fb662f4fce80f5de.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Common Component", then select and click "Pathfinding Obstacle" to add it

(3) Click "Edit Details" to expand the Editing Tab

## **2. Editing Pathfinding Obstacle Components**

![](../../../images/5225cdcdf04b07e9.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Pathfinding Obstacle* | Use the dropdown menu to select a Pathfinding Obstacle type.  Toggle the checkbox to control whether the obstacle is active. The active state syncs with the Pathfinding Obstacle Editing Tab.  ![](../../../images/52f644eb5c39a8a2.png)![](../../../images/03beccc336c0a20e.png) |
| *\*Pathfinding Obstacle List* | Lists all Pathfinding Obstacles configured on the Entity |

# **III. Editing Pathfinding Obstacles**

## 1. **Add Pathfinding Obstacles**

![](../../../images/f6f9bde2d6c26790.png)

Click ![](../../../images/4562565b3a280723.png) to add a Pathfinding Obstacle.

Newly added Pathfinding Obstacles are **initially effective** by default

ID: X, where X is the obstacle's **sequence ID**. This value can be used as a Node input to control whether the Pathfinding Obstacle is enabled.

## 2. Related Parameters

![](../../../images/6b0592214b949a57.png)

Pathfinding Obstacles can be configured to be initially enabled or disabled

Multiple areas can be added to a single Pathfinding Obstacle using the [Add Pathfinding Obstacle] button

![](../../../images/ea71c6c33582a6e3.png)![](../../../images/bc9720352faeb90c.png)

When the Pathfinding Obstacle shape is a Cuboid:

*Center*: The offset of the area's center relative to the object's position

*Rotation*: The rotation applied to this area

*Zoom Multiplier*: Controls the size scaling of this area

*Runtime Effective Size*: The actual size of the obstacle applied at runtime. This value is read-only and serves only as reference. It is calculated based on both the object itself and its area scaling. If the scaling of the object or the area exceeds the obstacle's limits, the preview may differ from the effective runtime range. The runtime value takes precedence

Cuboid minimum effective size: 0.5\*0.5\*0.5. Maximum effective size: 30\*30\*30.

![](../../../images/b0d9934bde6f4320.png)![](../../../images/959c8762f7063900.png)

When the Pathfinding Obstacle shape is a Cylinder:

*Center*: The offset of the area's center relative to the object's position

*Angle*: The rotation angle of this area

*Radius*: The radius size of this area

*Height*: The height of this area

*Runtime Effective Size*: The actual size of the obstacle applied at runtime. This value is read-only and serves only as reference. It is calculated based on both the object itself and its area scaling. If the scaling of the object or the area exceeds the obstacle's limits, the preview may differ from the effective runtime range. The runtime value takes precedence

Cylinder minimum effective size: 0.25\*0.5. Maximum effective size: 15\*30.

# **IV. Managing Pathfinding Obstacles Through Node Graph**

## 1. Enable/Disable Pathfinding Obstacle

![](../../../images/21a2bf25c9bea1f3.png)

## 2. Enable/Disable Pathfinding Obstacle Feature

![](../../../images/5ddcb629fac20010.png)
