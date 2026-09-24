---
title: Hurtbox Settings
path_id: mhqy3jiy8hj8
updated_at: 2025-10-14 22:02:23
category: Concept Introduction/Functions/Specialized Settings
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqy3jiy8hj8
---

# I. What is a Hurtbox?

The *hurtbox component* is a *component* used to perform hit detection, which can

When the *trigger area* defined by the component is hit by another entity's attack, it sends a hit event to the node graph

The hurtbox component is typically used as the receiver for attack events, determining hit detection and handling post-hit actions (e.g., dealing DMG or playing special effects) in the node graph of the attacked entity.

# II. Editing Hurtboxes

In the Specialized Setting tab of an *entity/prefab*![](../../../images/bf52cdf9155fc414.png)

Has a non-deletable hurtbox component by default.

![](../../../images/7d4a0b6ff344d263.png)

Click details to edit

![](../../../images/df6f3127240d31ab.png)

Multiple hit triggers are allowed under hurtbox settings. Creators (Craftspeople) can press A to add more hit triggers.

|  |  |
| --- | --- |
| **Parameter** | **Functions** |
| *Initially Effective* | Common component parameter used to set whether the component is initially effective. |

For each independent hurtbox trigger, creators (Craftspeople) can set whether it's initially active and add hurtbox trigger areas by pressing B.

Multiple hurtbox trigger areas will be combined through a union operation.

Creators (Craftspeople) can set the *trigger area shape*, with different shapes having different configurable parameters.

Cuboid: configurable center offset, rotation offset and absolute scaling.Sphere: configurable center offset and radius.Capsule: configurable center offset, rotation offset, capsule radius, and height.

# III. Operation of the Hurtbox Component

**[Node Graph Node] When Attacked**

![](../../../images/27233728e3de967d.png)
