---
title: On-Hit Detection
path_id: mh0ddb91cxwa
updated_at: 2026-03-27 15:37:16
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0ddb91cxwa
---

# I. Functions of On-Hit Detection Components

On-Hit Detection Components can send hit events to the server node graph when the hit area defined within the component encounters other entities or scene terrain (including water surfaces). In most cases, this can be used to handle the function of a projectile's hitbox

It can also immediately trigger an ability unit (attack only) locally when the hit area contacts other entities

On-Hit Detection Components support multiple on-Hit detection areas taking effect simultaneously, and their effective ranges will stack.

A typical use case is using this component as a projectile's On-Hit Detection Box. It determines when a projectile hits a target and processes post-hit events in the Node Graph (such as dealing damage or playing special effects)

# II. Editing On-Hit Detection Components

## 1. Add Components

![](../../../images/5e225b4cc6294175.png)

(1) In the Entity/Prefab Editing interface, open the Component Editing Tab

(2) Click "Add Common Components" below, then click "On-Hit Detection" to add it

(3) Click "Advanced Editing" to expand the editing tab

## 2. Editing Hit Rules

![](../../../images/e7d3ce4396a4a254.png)

The parameters and their functions are as follows:

|  |  |
| --- | --- |
| **Parameter** | **Function** |
| *Trigger Type* | Single Trigger: On-Hit Detection triggers only once during the component's entire life cycle. This means a hit event is sent to the Node Graph at most once during its entire life cycle  Non-Repeating Trigger: For each hit entity, On-Hit Detection triggers at most once.  Repeating Trigger: Can trigger multiple times, subject to trigger interval restrictions. After each trigger, must wait for the trigger interval time before triggering again |
| *Trigger Interval* | Only configurable when trigger type is set to Repeating Trigger |
| *Detection Delay Time* | When an entity is created, it will delay On-Hit Detection for the time configured in [On-Hit Detection Delay Time].  Common use is to prevent projectile-type objects from hitting their own launcher when fired |
| *Enable Continuous Collision Detection* | When enabled, activates Continuous Collision Detection (CCD) for hit detection  Continuous Collision Detection: When an entity is moving at high speed, conventional collision mechanisms may result in "tunneling" (where the entity passes through the collision target without triggering a collision) due to large position differences between frames. Enabling CCD makes entity collisions more precise during high-speed movement  CCD has a significant performance cost, so it is only recommended for use in appropriate scenarios (high-speed movement requiring precise hits) |
| *Continuous Collision Detection Type* | Above Speed Threshold: CCD is only enabled when the projectile's velocity exceeds the threshold, helping optimize performance.  Continuously Effective: Continuously effective, more performance cost |
| *Speed Threshold* | Only effective when CCD type is set to "Above Speed Threshold". CCD will be enabled when the projectile's velocity exceeds this value, which helps optimize performance |
| *Detection Radius* | Continuous Collision Detection is implemented by generating a cylinder with a certain radius in consecutive frames to assist with collision detection. The detection radius determines the radius of this cylinder. It is recommended to keep it consistent with the actual radius of the projectile. When the value is 0, ray casting is used for detection instead |
| *Filter Node Graph* | *Refer to Local Filter Node Graph*: Used to determine whether the current hit is valid. For the specific distinctions and usage of the two filters, see [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i). If both the filter and the local filter are used together, the hit is considered valid only if both conditions are satisfied.  The local filter will execute once every time a hit occurs.  An explanation of the correspondence between the basic nodes in the local filter Node Graph Get Self Entity Output parameter is projectile entity. Get Target Entity Output parameter is the entity that was hit. Get Current Character Output parameter is local character. Local filter example: ![](../../../images/0f0079dbe4e80eb5.png) |
| *Enable Filters Below* | When enabled, the filtering parameters below will be activated. When disabled, no filtering will be applied and all entities that can pass through the filter will be hit |
| *Faction Filter* | None: Does not hit entities of any faction.  Hostile Faction: Only hits entities hostile to the projectile.  Allied Faction: Only hits entities friendly to the projectile, excluding self.  Allied Faction Self Entity Included: Only hits entities friendly to the projectile, including self.  Own Faction: Only hits the faction the projectile belongs to.  All Factions: Hits all factions, including self.  All Factions Self Entity Excluded: Hits all factions, excluding self |
| *Entity Type Filter* | Multiple selectable options, including Objects, Characters and Creations |
| *Hit Layer Filter* | Multiple options can be selected. When multiple options are selected, multiple hits may occur (for example, when hitting an object with a hurtbox, two hit events may occur due to hitting both the object's collider and the hurtbox.)  Hurtbox: Only hits entities with hurtboxes.  Scene: Hits scene colliders, in this case the *On Hit Detection Triggered* node's *On-Hit* *Hurtbox* value is False  Object Self-Collision: On-Hit Detection triggered by collision with the object itself. Note that in this case, the hit hurtbox value in the node graph's On-Hit Detection Triggered is False, and no hit entity will be returned |
| *Execute Ability Unit When Hit* | References a group of ability units, see [Ability Units](/ys/ugc/tutorial//detail/mh0ucw9e76f6)  When on-hit detection is triggered, this group of ability units will be activated |

## 3. Editing Hit Areas

![](../../../images/deb14abcfcf9bac3.png)

Click [Add Trigger Area] to add a new hit area configuration

![](../../../images/4e778baac9ab9b8b.png)

![](../../../images/e089f7be7e78b996.png)

![](../../../images/25e0525a37c60272.png)

The On-Hit Detection Area is similar to the [Collision Trigger](/ys/ugc/tutorial//detail/mh8w69rzuc3i). Multiple detection areas can be configured, and when any detection area collides with an entity or scene, it will trigger a on-hit detection event

|  |  |
| --- | --- |
| **Parameter** | **Function** |
| *Trigger Area Shape* | Currently supports cuboid, sphere, and capsule detection areas |
| *Center* | Offset relative to the entity/prefab center |
| *Rotation* | Only configurable when a cuboid area is selected, the Euler angle rotation of the cuboid detection area |
| *Zoom Multiplier* | Only configurable when a cuboid area is selected, for scaling the length, width and height of the cuboid |
| *Radius* | Radius of the sphere/capsule |
| *Angle* | Can only be configured when a capsule area is selected, represents the angle of the capsule |
| *Height* | Can only be configured when a capsule area is selected, represents the height of the capsule |

# III. Using On-Hit Detection Functions in Node Graphs

**When On-Hit Detection Is Triggered**

![](../../../images/187626e229ce59fa.png)

**Node Type**: Event

**Node Functions**

When the on-hit detection component collides with an entity or scene, it pushes a [When On-Hit Detection Is Triggered] event to the component owner's node graphBased on the [Trigger Type] configuration in the on-hit detection component, this event may be triggered once or multiple times

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Common event parameter, the entity that triggered the event |
| Output Parameter | Event Source GUID | GUID | Common event parameter, GUID of the event trigger |
| Output Parameter | On-Hit Hurtbox | Boolean | Returns whether the entity's hurtbox was hit.  Returns [Yes] when hitting an entity's hurtbox, returns [No] when hitting scenes or colliding with itself |
| Output Parameter | On-Hit Entity | Entity | When hitting an entity's hurtbox, returns the hit entity. Returns null when hitting scenes or colliding with itself |
| Output Parameter | On-Hit Location | 3D Vector | Returns the on-hit location, regardless of whether an entity is hit |
