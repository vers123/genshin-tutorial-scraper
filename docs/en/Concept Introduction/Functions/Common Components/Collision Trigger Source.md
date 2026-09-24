---
title: Collision Trigger Source
path_id: mhilp6rpz09y
updated_at: 2025-10-20 16:52:09
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhilp6rpz09y
---

# I. Functions of Collision Trigger Source Component

The Collision Trigger Source component provides collision detection trigger sources during stage runtime and serves as a tool for determining logical range contact.

The collision trigger source component can only have one collision trigger source enabled at a time.

## 1. Collision Detection between Collision Trigger Source and **Collision Triggers**

During stage runtime, the “Collision Trigger” continuously monitors other entities carrying "Collision Trigger Source Components".

When the runtime entity's "Collision Trigger Source" enters or exits the range of another entity with a "Collision Trigger Component", a collision between the two component ranges will send a node graph event to the entity configured with the "Collision Trigger"

This type of collision does not create physical collision barriers.

## 2. Collision Trigger Components

[Collision Trigger](/ys/ugc/tutorial//detail/mh8w69rzuc3i)

# II. Editing Collision Trigger Source Components

## 1. Add Components

![](../../../images/aa1f633974fb1954.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click "Add Common Components" below, select and click "Collision Trigger Source Components" to add it

(3) Click "Advanced Editing" to expand the editing tab

## 2. Editing Collision Trigger Source Components

![](../../../images/e67acea8c0c48a04.png)

Use "Advanced Editing" to adjust the shape and size parameters of the collision trigger source

![](../../../images/8e0dd512d26d998f.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | Whether to enable when the object is created |
| *Trigger Area Shape* | Supports cuboid, sphere, and capsule shapes. Different size configuration parameters will be displayed based on the selected shape |
| *Center* | Offset relative to the entity/prefab center |
| *Rotation* | Supports orientation adjustment along different axes based on the center position |
| *Zoom Multiplier* | The trigger area's shape supports defining scaling along different axes |

# III. Managing Collision Triggers Through Node Graph

You can manage the collision trigger for runtime entities via the node graph during its runtime

**When Entering Collision Trigger**

The active entity's "Collision Trigger Source" range enters the "Collision Trigger" range of another active entity.

Node graph events will be sent to the entity configured with "Collision Trigger"

![](../../../images/5f8d56b5600358a0.png)

**When Exiting Collision Trigger**

The "Collision Trigger Source" range of a runtime entity exits the "Collision Trigger" range of another runtime entity.

Node graph events will be sent to the entity configured with "Collision Trigger"

![](../../../images/fc8a3f10794bffaf.png)

**Activate/Disable Collision Trigger Source**

The "Collision Trigger Source" component supports dynamic adjustment of the enabled parameters through node graphs

![](../../../images/e607ba65fe24698f.png)

# IV. Examples

For entities that do not contain *collision trigger sources*, they cannot generate entry/collision range events through contact with *collision triggers*

Creations and character entities contain collision trigger sources by default, no additional editing required.

As shown in the graph,

Add a collision trigger source component to the "wooden box" and configure its size to match the box dimensionsAdd a collision trigger to the "Spiky Platform" and place it on the paving

In the graph below, an empty object is used to demonstrate the range for clarity. This does not represent the actual appearance in the editor and is only meant as a visual guide

The collision trigger source of the wooden box<->the collision trigger of the spiky platform. When they make contact, the spike platform will receive an *collision trigger entry event*If there are logical requirements, you can edit in the node graph. For example, if you want the wooden box to take damage when it hits the spiky platform, you can edit it through this example

![](../../../images/b2984c25a333d79d.png)
