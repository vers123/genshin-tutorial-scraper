---
title: Extra Collisions
path_id: mhreraibgmak
updated_at: 2025-10-20 14:51:02
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhreraibgmak
---

# I. Functions of Extra Collision Component

Collision blocking, also known as collision detection, refers to the in-game functionality that simulates real-world physical object interactions.

In addition to *native collision*, the extra collision component supports flexible configuration of shapes, sizes and combinations, serving as the effective collision range during entity runtime, or as a climbable range.

Multiple *extra collision* components can be active simultaneously, with their effective ranges stacking cumulatively.

Each *Extra Collision* supports multiple collision ranges taking effect simultaneously, and their effective ranges will be stacked.

**Native Collision**

Native collision is the default collision that comes with prefabricated components.

You can configure whether the "native collision" is enabled through the "Initially Effective" setting

# II. Editing Extra Collision Components

## 1. Add Components

![](../../../images/a6a7ac72ddd3b88b.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click "Add Common Components" below, select and click "Extra Collision" to add it

When the "Extra Collision Component" is selected, the entity being edited will display the current effective range of the "Extra Collision" component in blue.

(3) Click "Advanced Editing" to expand the editing tab

**Initially Effective Extra Collision**

![](../../../images/ae4d641b9befda1a.png)

![](../../../images/d754438dc5634bb8.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Extra Collision* | Currently active extra collision configuration, corresponding to settings in the "Advanced Editing" tab |
| *Extra Collision Structure List* | Enumerated list of all extra collisions for editing the entity |

**Native Collision**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Enable Native Collision* | Configure whether the "Native Collision" is enabled in the Base Attributes tab |
| \**Native Collision Preview* | If enabled, blue dots will display the native collision range |

## 2. Editing Extra Collisions

![](../../../images/440dfebc2a1c4048.png)

Click ![](../../../images/95a83fc41e2a2913.png)to add "Extra Collisions".The newly added "Extra Collision" is Initially effective by default."ID: X", where X is the "Collision Area ID", can be used as a node input to adjust the parameters of extra collisions

![](../../../images/f9f7cc45d5d07702.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | Whether the extra collision is enabled along with the creation of the entity |
| *Climbable* | Whether the extra collision climbing function is enabled as well |
| *\*Native Collision* | Indicates whether native collision is active |
| *\*Native Collision Preview* | Enable to view the range of native collision |

Use "Add Extra Collisions" to add a basic shape

![](../../../images/a8d736020962392f.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Trigger Area Shape* | Supports three basic shapes: cuboid, sphere, and capsule  ![](../../../images/867d6b31c2472781.png) |
| *Center* | Offset relative to the entity/prefab center |
| *Zoom Multiplier* | Supports configuring shape scaling along different axes |
| *Rotation* | Supports orientation adjustment along different axes based on the center position |

# III. Managing Extra Collisions Through Node Graph

Activate/Disable Extra Collisions

Select an entity and enter the "Extra Collision ID" to adjust whether the extra collisions will take effect.

If ineffective, climbable attribute is also ineffective  
 ![](../../../images/139044eff3645200.png)

Activate/Disable Extra Collision Climbability

When extra collision is enabled, its climbing function can be adjusted separately

![](../../../images/48d368b38a5bac45.png)
