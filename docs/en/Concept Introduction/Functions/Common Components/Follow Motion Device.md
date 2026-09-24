---
title: Follow Motion Device
path_id: mhig59rlkaou
updated_at: 2026-01-06 21:53:11
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhig59rlkaou
---

# I. Functions of the Follow Motion Device Component

The Follow Motion Device component gives an entity the ability to follow the movement of another entity

Only one Follow Motion Device can be active on a Follow Motion Device component at a time

# II. Editing Follow Motion Device Components

![](../../../images/562b3cb5ca6d609c.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click "Add Common Components" below, select and click "Follow Motion Device" to add it

(3) Click "Advanced Editing" to expand the editing tab

# III. Parameter Configuration

The parameters of the Follow Motion Device are as follows:

## 1. Basic Settings

![](../../../images/900525f50914ef3c.png)

*Initially Effective*: Whether it takes effect immediately after the entity is created

*Track Target*: You can choose the follow target for the follow motion device. Initially, it can be left unset, and later dynamically specified through a node graph.

*Follow Type*: Three follow types are currently provided

Completely Follow: Follow both locations and orientationsFollow Location: Only follow the target's location while maintaining the original orientationFollow Rotation: Only follow the target's orientation while maintaining the original location

*Follow Attachment Point*: Specify which attachment point to follow on the target

## 2. Follow Mode

*Follow Mode* defines the detailed behavior of tracking performance when the Follow Motion Device component on an entity executes tracking logic. Currently, three behavioral performances are provided:

### (1) Adsorption Tracking

![](../../../images/b11b881152bb25b0.png)

This method will strictly adhere to the configured following location settings

### (2) Delayed Tracking

![](../../../images/6463da5b1edc727c.png)

A tracking method with transition time. When the target's location changes, the Follow Motion Device will gradually move to the designated follow location within the configured transition time

*Transition Time*: The duration required to reach the target follow location

### (3) Constant Speed Tracking

![](../../../images/42df6c5c62177a5d.png)

A tracking method that follows at a specified speed. When the target's location changes, the Follow Motion Device will track it at the designated speed.

*Initial Speed*: The initial speed of the follow motion device

*Acceleration*: The speed increase value per second

*Acceleration Duration*: Duration of the acceleration behavior

*Correct Orientation to Movement Direction*: When set to "Yes", it will automatically adjust the forward orientation of the entity to match the velocity orientation

*Destination Target Radius*: In tracking behavior, when the distance between the following entity and the followed entity is less than the arrival target radius, the tracking is considered complete. After tracking finishes, the behavior will be the same as "adsorption".

## 3. Initial Following Location

![](../../../images/62740488f91cb1fc.png)

*Coordinate System Type*: Determines whether the follow offset is based on the target's world coordinate system or relative coordinate system

*Offset*: Location offset based on the follow target

*Rotation*: Orientation offset based on the follow target

# 4. Using Node Graph to Control Follow Motion Device

Activate/Disable Follow Motion Device

![](../../../images/f0a1219a20c1dc55.png)

Switch Follow Motion Device Target by Entity

![](../../../images/727b5f060b742c90.png)

Switch Follow Motion Device Target by GUID

![](../../../images/e9f0a5d55d3b6a0e.png)

Get Follow Motion Device Target

![](../../../images/70a2b03bd2523318.png)

### V. Special Notes

When an entity with a Follow Motion Device follows an object, if the object is destroyed during the follow process, the entity will immediately stop following and remain in its current position.

When an entity with a Follow Motion Device follows a player, if the character falls during the follow process, the entity will continue to move towards the location where the character fell. When the character revives, it is equivalent to re-entering the scene, and at this point, the entity will be reset to its creation position and will start following from the creation position again.
