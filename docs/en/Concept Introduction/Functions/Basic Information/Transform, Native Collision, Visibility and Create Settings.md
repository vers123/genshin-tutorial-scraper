---
title: Transform, Native Collision, Visibility and Create Settings
path_id: mhzllq9fbdyq
updated_at: 2026-09-16 15:10:39
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhzllq9fbdyq
---

# I. Transformation

## 1. Transform Definition

Describes the geometric information of units in the scene, generally including location, rotation and zoom

![](../../../images/1d4ef7750794160f.png)

*Location*: Position in world coordinate system

*Rotation*: Rotation in world coordinate system

*Zooming*: The magnification ratio of the object

*\*Lock Transform*: An editing attribute. If this attribute is "enabled", the transform information of the entity cannot be modified

## 2. Node Graph Related

Location information can be obtained through node graph query

![](../../../images/b89bc0144eb30f5b.png)

# II. Native Collision

## 1. Definition of Native Collision

*Native collision* refers to the basic collision of objects, which fits the model more precisely compared to collisions added by *extra collision components*.

Conversely, as *basic information*, the shape of native collision cannot be modified, and players can only control the *initial effective* and *climbable* toggles.

![](../../../images/710d7dda8715712b.png)

*Initially Effective*: Whether native collision is enabled when the unit is initialized

*Climbable*: Whether the native collision can be climbed by characters, requiring the character to have climbing ability

*\*Native Collision Preview*: An editing feature that, when checked, allows you to preview the collision shape in the editor interface, see image above

*Camera can ignore collision:* When set to "No," collision with the current Object Entity may push the camera, causing stuttering or sudden changes in camera position. When set to "Yes," the camera ignores collision with this Object Entity. However, this may cause the camera to move inside the model, resulting in visual issues. Craftspeople should configure this setting based on the specific gameplay scenario

## 2. Node Graph Related

Modify Collision Switch

![](../../../images/b43b98c51c4f9ca4.png)

Modify Collision Climbability

![](../../../images/33e23509ab0c8cf7.png)

# III. Visibility

## 1. Definition of Visibility

This *basic information* determines whether the *entity*'s *model* is visible to players during runtime. It only affects the model, and does not impact *collisions*, *triggers*, *node graphs*, or other logic

It is recommended to create some functions related to hidden entities

![](../../../images/6de2d0df0f57d6cf.png)

## 2. Node Graph Related

![](../../../images/9f4d9f097fda60b8.png)

# 4. Create Settings

## 1. Create Settings Definition

Indicates whether the *entity* is created during stage initialization after being placed in the scene. If this toggle is "Disable," it must be dynamically created later via the node graph.

![](../../../images/ca1fad165bb6d991.png)

## 2. Node Graph Related

If an entity is destroyed or removed, this node can be used to recreate it

![](../../../images/863f133b48675705.png)
