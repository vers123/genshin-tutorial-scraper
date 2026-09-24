---
title: Entity Deployment Group
path_id: mhzr5n9jq3ju
updated_at: 2026-03-27 15:21:38
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhzr5n9jq3ju
---

# I. Functions of Entity Deployment Groups

*Entity Deployment Groups* can be used to quickly manage of multiple entities, and can batch create and batch destroy entities through related nodes.

You can use Entity Deployment Groups to quickly locate all units belonging to that Entity Deployment Group.

All unit types with physical entities in the scene can be assigned to an Entity Deployment Group, including: *Creations, Characters, and Objects*

Additionally, *terrains* can also be assigned to Entity Deployment Groups

The same entity can belong to multiple Entity Deployment Groups.

# II. Global Definition of Entity Deployment Groups

Before using the Entity Deployment Group, you need to define it globally in the Entity Deployment Groups Management Tool

In the system menu, click [Manage Entity Deployment Groups] to open the Entity Deployment Groups Management Tool

![](../../../images/8916991a6fe8b295.png)

The left side shows the Entity Deployment Groups Management bar, where you can browse existing Entity Deployment Groups or Click [Add Entity Deployment Groups] to create a new one.

After selecting an Entity Deployment Group, you can configure its settings in the details panel on the right and view the content list of that Entity Deployment Group

![](../../../images/e57e28a59418dac6.png)

The Entity Deployment Groups Management bar allows you to create new tabs and categorize Entity Deployment Groups by tabs

![](../../../images/5f85371d55a4eda4.png)![](../../../images/f2f5dc0dfd6626bc.png)

# III. Managing Entity Deployment Groups

## 1. Add Entities to Entity Deployment Group

In the Terrain Editing tab, right-click on the terrain to add it to the Entity Deployment Group from the pop-up menu.

![](../../../images/ab00b5e4fe29b6be.png)

In the Entity Placement tab, right-click an entity (hold Shift and left-click to select multiple entities) and choose Add to Entity Deployment Group from the pop-up menu.

![](../../../images/5cf1acc7e330fe50.png)

In the Entity Deployment Group Details interface, click [Select in Scene] in the bottom right corner to enter selection mode. You can quickly add entities to the current group by left-clicking to box select or clicking directly.

![](../../../images/4a211ea15683521b.png)

![](../../../images/356f9ec03409d511.png)

## 2. Entity Deployment Group Details Interface Settings

![](../../../images/b76251028089938b.png)

*Entity Deployment Group Name*: Can be customized to distinguish between different Entity Deployment Groups

*Index*: The unique identifier of this Entity Deployment Group, used for identification when modifying Entity Deployment Group data in a Node Graph

*Initial Create*: Determines whether the terrain and static objects within this Deployment Group are created alongside the stage.

Note: If either an Entity Group or an individual entity has **Initial Create** enabled, that entity will be created at the start of the stage.

Example: Entities A and B are both in Entity Group G. Entity A has **Initial Create** enabled, while Entity B does not.

If Entity Group G has **Initial Create** enabled, both A and B will be created alongside the stage.

If Entity Group G does not have **Initial Create** enabled, only Entity A will be created alongside the stage.

![](../../../images/f46ba8b39932f328.png)

*Content List*: Lists all units contained within an Entity Deployment Group

Right-click on a unit to remove it from the group or swap it to a different group

![](../../../images/8ed2281332bb3380.png)

# IV. Managing Entity Deployment Groups from the Node Graph

Get Currently Active Entity Deployment Group List

![](../../../images/6aae81216af4c62f.png)

Activate/Disable Entity Deployment Group

![](../../../images/d711a6a9612ac1ca.png)
