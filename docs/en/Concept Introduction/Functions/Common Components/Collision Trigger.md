---
title: Collision Trigger
path_id: mh96ff0mujww
updated_at: 2026-06-23 20:00:23
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh96ff0mujww
---

# I. Functions of Collision Trigger Component

The collision trigger component provides a detection range for collision detection during stage runtime and serves as a tool for contact determination.

The collision trigger component supports multiple collision triggers to be active simultaneously.

## 1. Collision Detection between Collision Triggers and **Collision Trigger Source**

During stage runtime, the “Collision Trigger” continuously monitors other entities carrying "Collision Trigger Source Components".

When the runtime entity's "Collision Trigger Source" enters or exits the range of another entity with a "Collision Trigger Component", a collision between the two component ranges will send a node graph event to the entity configured with the "Collision Trigger".

This type of collision does not create physical collision barriers.

When a "Collision Trigger Source" collides with different "Collision Triggers", the collision detection between them is calculated independently

Example: When a "Collision Trigger Source" collides with "Collision Trigger 1" and "Collision Trigger 2", node graph events will be sent separately without affecting each other

## 2. Collision Trigger Source Components

[Collision Trigger Source](/ys/ugc/tutorial//detail/mhn95di01j84)

# II. Editing Collision Trigger Components

## 1. Add Components

![](../../../images/b2056f13ecc567e7.png)

(1) In the Entity/Prefab Editing interface, open the Component Editing Tab

(2) Click "Add Common Components" below, then select and click "Collision Trigger" to add it

(3) Click "Edit Details" to expand the editing tab

## 2. Editing Collision Trigger Components

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Trigger* | Enumerates the Collision Triggers that are active by default when the Entity is running.  Use the drop-down arrow to change the trigger's default active state via the checkbox next to the trigger; the updated state syncs to the corresponding trigger's detail editing page  ![](../../../images/8a6c3cd6f93a3ba1.png)![](../../../images/f27465ec75c9bf1d.png) |
| *\*Trigger List* | Enumerates all Collision Triggers configured for the Entity |

## **3. Editing Collision Triggers**

![](../../../images/3ee0277070c9c63f.png)

In the stage editor window, the entity will display the range of the currently selected collision trigger.

### **(1) Collision Trigger Group**

![](../../../images/bdda189f629d87ca.png)

Enumerate all predefined collision triggers for this entityClick ![](../../../images/3f7b25b3d2275af1.png)to add a collision trigger“ID: X”, where X is the “Trigger ID”, serves as a node input that allows you to adjust the collision trigger parameters

### (2) Basic Information of Collision Trigger

![](../../../images/5ac9bdc89ffacf55.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | If enabled, this collision trigger takes effect immediately upon Entity creation |
| *Effective Target* | Checks collision trigger sources only for the configured Entity types.  Provides *Character, Object, and Creation* enumerations |

### (3) Collision Trigger Range

![](../../../images/4a0007b980a8e181.png)

Click "Add Trigger Areas" to add new trigger areas. The ranges under the same collision trigger will be merged and take effect as a combined range

![](../../../images/84c7ad7bcaf0b0b5.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Trigger Area Shape* | Supports cuboids, spheres, and capsules. The specific size parameters expand based on the selected Shape |
| *Center* | Offset relative to the center of the Entity/Prefab |
| *Rotation* | Supports adjusting orientation along different axes based on the center location |
| *Zoom Multiplier* | The Trigger Area shape supports scale settings on different axes |

# III. Managing Collision Triggers Through Node Graph

Collision triggers for runtime entities can be managed via the node graph during runtime.

**When entering the collision trigger**

The active entity's "Collision Trigger Source" range enters the "Collision Trigger" range of another active entity.

Node graph events will be sent to the entity configured with "Collision Trigger"

![](../../../images/5511d91b80d74864.png)

**When Exiting Collision Trigger**

The "Collision Trigger Source" range of a runtime entity exits the "Collision Trigger" range of another runtime entity.

Node graph events will be sent to the entity configured with "Collision Trigger"

![](../../../images/9ef59682c1ad1ad2.png)

**Enable/Disable Collision Trigger**

The "Collision Trigger" Component supports dynamically adjusting activation parameters through Node Graphs

![](../../../images/feb81de5d4e20c91.png)
