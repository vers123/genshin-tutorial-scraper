---
title: Control Motion Device
path_id: mhztm7ixqq10
updated_at: 2026-07-10 16:46:49
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhztm7ixqq10
---

# 1. Functions of the Control Motion Device

Attaching the Control Motion Device component to a Prefab/Entity allows you to control the movement of the Prefab/Entity, cast skills, and more via joystick input at runtime.

The Control Motion Device is mutually exclusive with other types of Motion Devices.

It is recommended to use uniform scaling (e.g., 1:1:1) for the controlled entity. Non-uniform scaling may cause the entity to deform when moving on slopes.

When creating complex controlled entities, we recommend you to use a uniformly scaled empty model as the main object, while adjusting the scale of decorative objects.

# II. Editing the Control Motion Device Component

![](../../../images/f2ab0b05d9568806.png)

(1) In the Entity/Prefab editing interface, open the Edit Component tab.

(2) Click "Add Common Component" below, select and click "Control Motion Device" to add it.

(3) Click "Advanced Editing" to expand the editing page.

# III. Parameter Configuration

## 1. Basic Settings

![](../../../images/93550c0232320a77.png)

### (1) Entity Grounding Position

*Entity Ground Position* defines the position where the controlled entity contacts the ground at runtime.

*Offset:* The offset value based on the bottom position of the controlled entity.

![](../../../images/abd5c0d001aec001.png)

### (2) Character Exit Point

*Character Exit Point* defines the ejection position of the operator when leaving the controlled entity.

*Character Exit Point:* Attachment point of the controlled entity

![](../../../images/05b091cd29787236.png)

### (3) Control Entity Collision

*Control Entity Collision* defines the collision box size of the control entity.

For elements or entities with the Control Motion Device component attached, their runtime collision is determined by the Control Entity Collision. Native and additional collisions will not take effect.

Note: If the controlled entity's collision is lower than the entity's grounded position at runtime, abnormal behavior will occur due to squeezing against the ground.

It is recommended to use a capsule or sphere as the collision shape, placing it in the upper half of the entity model to effectively prevent certain abnormal collision behaviors.

![](../../../images/3629a1e949ae2edf.png)

Click "Edit Details" to expand the edit page.![](../../../images/3ff15d44753f8f4e.png)

#### a. Default Entity Collision

*Default Entity Collision* defines the default collision of controlled entities, as well as other collision detection criteria during runtime.

![](../../../images/eeeb59eece1374b7.png)

|  |  |
| --- | --- |
| Configuration Parameter | Description |
| *Trigger Area Shape* | Only supports the basic capsule shape |
| *Center* | Offset relative to the ground position |
| *Radius* | Capsule radius  At runtime, the tilt angle is calculated based on the average ground normal using the radius as a reference.  The radius is used in physics collision detection. |
| *Height* | Capsule height  During runtime, height is used as the baseline to detect traversable obstacles, determine the airborne state, and calculate other physics-related properties |

#### b. Controlled Entity Collision Area

![](../../../images/e931db3c0a817294.png)

You can add basic shapes via "Add Collision Area".

![](../../../images/a944dfc5348b26f9.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Trigger Area Shape* | Supports configuring three basic shapes: Box, Sphere, and Capsule  ![](../../../images/ab2ef08ad4eaa860.png) |
| *Center* | Offset relative to the center of the entity or part |
| *Rotate* | Supports adjusting the orientation on different axes relative to the center position |
| *Zoom Multiplier* | Box: Supports custom scaling of the collision shape on different axes.  Sphere: Supports uniform scaling of the collision shape by adjusting the radius.  Capsule: Supports custom scaling of the collision shape by adjusting the radius and height. |

### (4) Decoration Movement Performance

Decorative Object Performance defines which decorative parts of an interactive entity can play motion animations at runtime.

Recommended Workflow:

When editing model decorations, identify which decorations require motion effects (e.g., when editing a vehicle, ensure the four tires have motion effects)Add custom attachment points and attach the decorations to the corresponding attachment points (e.g., attach all individual decoration parts of the tire to the same attachment point)Add decoration movement, reference the corresponding attach point, and edit the movement settings (e.g., reference the tire's attach point and edit the movement settings)

How Decorative Object Motion Works: By rotating the referenced attachment point, all decorative objects attached to it inherit the corresponding motion animation.

![](../../../images/e1889dc39dc8aeb7.png)

Click "Edit Details" to expand the editing page.

![](../../../images/abfdd129ea380ec5.png)

#### a. Add Decoration Movement

Click ![](../../../images/483e130bbe345016.png) to add a new "Decoration Movement".

![](../../../images/4a243507edd11b22.png)

#### b. Movement Performance Settings

![](../../../images/04b3406ec05b8fbf.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Motion Type* | Currently, only tire motion behavior can be configured.  *Tire:* Simulates the rolling and left/right steering effects of tires when the vehicle is moving or turning.  ![](../../../images/e1e9724046c8a291.png) |
| *Rotate with Forward/Backward Input* | When enabled: Decorations with this movement behavior will continuously rotate forward or backward relative to the controlled entity, based on the movement speed of the Control Motion Device.  When disabled: No forward/backward rotation behavior. |
| *Rotation Speed Calculation Rules* | *Default:* Automatically calculates rotation speed based on the distance from the decoration's attachment point to the ground contact point.  *Custom:* A maximum rotation speed can be configured. The automatically calculated rotation speed will not exceed this maximum value.  ![](../../../images/88586013562cdd32.png) |
| *Max Rotation Speed* | Maximum forward and backward rotation speed of the decoration |
| *Rotation Axis Preview* | When enabled: Preview the rotation direction for forward/backward inputs (X-axis rotation). |
| *Rotate with Left/Right Input* | When enabled: Based on the current operator's left/right input, the decoration rotates left or right relative to its forward direction.  When disabled: No left/right deflection movement is displayed. |
| *Rotation Axis Preview* | When enabled: You can preview the rotation direction of left/right input (Y-axis rotation). |

#### c. Associated Decorations

*Associated Decoration* determines which decoration under a custom attachment point will exhibit the corresponding movement behavior at runtime.

![](../../../images/6906663555f7de5c.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Decoration Attachment Point* | Supports configuration of all custom attachment points  All decorations attached to the selected custom attachment point will apply the corresponding decoration movement behavior at runtime  ![](../../../images/207288549763cf3d.png) |
| *Attached Decorations* | Preview all decorations attached to the decoration attachment points |

![](../../../images/77dbbb508fff7406.png)

Click "Go to Decoration Editor" to open the Decoration Management page for the Prefab/Entity.

## 2. Movement Settings

![](../../../images/7f310a28fb6a32fb.png)

### (1) Control Input Settings

![](../../../images/219aa6645ff57776.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Directional Input Mode* | *Camera Direction:* The controlled entity always moves in the direction the camera is facing.  *Control Entity Direction:* The control entity moves in its model's forward direction.  ![](../../../images/80bcbcc5ff78df13.png) |
| *Forward Input Range* | When the joystick input falls within this zone, the controlled entity moves forward; otherwise, it moves backward.  The exact front of the input joystick is 0°, and the input angle is divided into symmetrical left and right zones centered at 0°.  PC inputs will be converted into joystick inputs. For example, W corresponds to the forward direction at 0°. |

### (2) Movement Area Settings

![](../../../images/1b891326078847dd.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Max Movement Slope Angle* | Determines the maximum slope angle that the control entity can climb. |
| *Tilt Along Slope* | Determines whether the control entity tilts to match the slope while moving across an inclined surface. |

### (3) Movement Settings

![](../../../images/362934cfa609fb2d.png)

|  |  |
| --- | --- |
| Configuration Parameter | Description |
| *Turn Velocity* | The speed at which the entity rotates around the Y-axis |
| *Forward Acceleration* | The forward acceleration provided to the entity when the input falls in the forward area. |
| *Max Forward Speed* | Maximum forward speed limit of the entity  Once the maximum forward speed is reached, input in the forward area will no longer provide acceleration to the entity. |
| *Separate Forward/Backward Speed* | When disabled: Forward and backward speeds are the same.  When enabled: Backward speed parameters can be configured separately. |
| *Backward Acceleration* | The backward acceleration applied to the entity when the input falls into the backward zone. |
| *Max Backward Speed* | The maximum backward speed limit of the entity  Once the maximum backward speed is reached, input in the backward zone will no longer provide acceleration to the entity. |
| *Resistance Deceleration* | The base resistance applied to the entity while moving  Resistance deceleration affects the actual movement speed, as well as how long it takes for the control entity to decelerate to a stop after input stops. |
| *Change with Movement Speed* | When enabled: The faster the entity moves, the greater the resistance it experiences. |
| *Deceleration Coefficient* | The greater the deceleration coefficient, the greater the resistance experienced by the entity when moving.  Formula: Base Resistance Deceleration + Deceleration Coefficient \* Speed Squared |
| *Max Speed Preview* | The final maximum speed the entity can reach, calculated based on its movement acceleration and resistance.  Note: During actual runtime, if the resistance coefficient is set too high, it may result in a situation where the max speed is not 0 but the entity cannot move. |

# IV. Character Control Skills

When a character is in the controlled state, normal character skills cannot be used; only character control skills can be used.

Skill editing is similar to character skills. For details, see [Character Control Skills](/ys/ugc/tutorial//detail/mhj4a0rzu4pi)
