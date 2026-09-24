---
title: Character Disruptor Device
path_id: mhialcrh5l3q
updated_at: 2026-03-27 15:35:48
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhialcrh5l3q
---

# I. Functions of Character Disruptor Device Component

The Character Disruptor Device grants dynamic objects the ability to apply simulated physical forces to characters that collide with them.

Supports configuring multiple character disruptor devices simultaneously, but only one can be active at a time.

Character Disruptor Devices support usage of *local filters* to determine if they take effect

# **II. Editing Character Disruptor Device Components**

## 1. Add Components

![](../../../images/6da7b1dfb806094c.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click "Add Common Components" below, select and click "Character Disruptor Device" to add it

When "Character Disruptor Device" is selected, the entity being edited will display the current effective disturbance range of the "Character Disruptor Device" component in blue.

(3) Click "Advanced Editing" to expand the editing tab

## 2. Editing Character Disruptor Devices

![](../../../images/5d3723e4248028f7.png)

![](../../../images/4b3167a5721ce3b1.png)

Click ![](../../../images/4118fa6dd7960e0b.png)to add "Character Disruptor Devices".

If the current "Character Disruptor Device" group is empty, the added "Character Disruptor Device" will be enabled by default when initially activated.

"ID X", where X is the "Character Disruptor Device ID", can be used as a node input to adjust the parameters of the disruptor device

![](../../../images/9ed4076213fa31db.png)

Basic Settings

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | Whether to enable when the object is created |
| *Device Type* | Type of character disruptor device |
| *Device Rules* | Different disturbance types support different configuration parameters for disturbance rules |
| *Local Filter* | Can reference the Local Filter node graph to determine whether the disturbance device is in effect. Please refer to [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i)to understand the distinction and usage of both filters.  *Ejector*: Local filter will perform one check when a character enters the effective range  *Traction Device*: Local filter will perform one check when a character enters the effective range  *Force Field Device*: Local filter will continuously perform checks when a character enters the effective range  Explains basic nodes in the corresponding local filter node graph Obtain self entity Output parameter is the entity with character disruptor device component Obtain target entity Output parameter is the character entity in the effecive range of the tab Obtain current character Output parameter is local character |

![](../../../images/5f456bd976f203d3.png)

Trigger Areas

You can add basic shapes through "Add Trigger Areas". Multiple basic shapes form the trigger area of the Character Disruptor Device.

During editing, you can view the trigger area range on the edited entity in real-time in the editing interface.

Area Editing

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Trigger Area Shape* | Supports three basic shapes: rectangle, sphere, and capsule |
| *Center* | Offset relative to the entity/prefab center |
| *Rotation* | Supports orientation adjustment along different axes based on the center position |
| *Zoom Multiplier* | The trigger area's shape supports defining scaling along different axes |

## 3. Types of Character Disruptor Devices

### **(1) Ejector**

This force adds an additional configured value to the character's *velocity* in the configured direction.

During the ejector application, if a collision is detected in a certain direction, the ejector force applied in that component will be removed.

![](../../../images/ca1406d8193b313c.png)

**Device Rules**

![](../../../images/75ff17761dfaadf6.png)

When *Disturbance Direction* is set to *Specified Direction*, an additional parameter *Direction Vector* can be configured

By configuring this 3D vector, you can specify the direction of force applied by the ejector

When *Disturbance Direction* is set to *Associate Character Disturbance Direction*, additional parameters can be configured as *Direction Settings*

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Direction of Line From Character to Entity* | Line connecting the character and the entity center, pointing towards the entity center |
| *Direction of Line From Entity to Character* | Line connecting the character and the entity center, pointing towards the character |

Other configurable parameters are described as follows:

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Motion Velocity* *(m/s)* | When the character collision range takes effect, an additional ejector that can generate this speed will be applied |
| *Stable Phase Duration (s)* | The duration for which the character is affected by the ejector, during which the ejector's size remains constant |
| *Decay Phase Duration (s)* | The time it takes for the ejector affecting the character to gradually decrease to 0 after the Stable Phase Duration (s) ends |

**Local Filter Examples**

![](../../../images/b8f2f63c890c1bdb.png)

### **(2) Traction Device**

This force transforms the character into a sphere effect, dragging them towards the *traction destination* at the configured *speed* during the disturbance period.

![](../../../images/9cf539ec5aa9c387.png)

**Traction Destination**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Offset* | Position offset between the traction destination and the edited entity |
| *Radius* | When the character reaches within the radius distance of the traction destination, it is considered to have reached the destination |

**Device Rules**

![](../../../images/919627089191ff04.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Motion Velocity* *(m/s)* | When character collision is effective, an additional traction device that can generate this speed will be applied |
| *Stable Phase Duration (s)* | The duration for which the character is affected by the traction device, maintaining the speed during this period |
| *Decay Phase Duration (s)* | The time taken for the traction device's effect on the character to decay to zero after the disturbance period ends. |
| *Stop When Reaching the Destination* | If enabled, the force will end early when the character reaches the traction destination radius distance |
| *Can Be Interrupted by Jump* | If enabled, the character can end the force effect early by actively performing a jump during movement |
| *Ignore Scene Collision* | If set to Off, when the character collides with the scene during movement, the force effect can be terminated early |

**Local Filter Examples**

![](../../../images/19cbc0ad4803fade.png)

### **(3) Force Field Device**

This force continuously affects characters within its effective range, with different force effects that can be configured for different ranges.

The character will continuously experience corresponding forces while in different areas of the configured effective range.

![](../../../images/c1a74935361f4559.png)

**Logic Force Field Sphere**

The force field device is applied with this concentric sphere as the core

![](../../../images/6a7756b3e41a7087.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Inner Sphere Radius (m)* | Inner radius of the concentric sphere defining the force field's effective range |
| *Outer Sphere Radius (m)* | Outer radius of the concentric sphere defining the force field's effective range |
| *Offset* | Offset between the centre of the force field's logic effective sphere and the entity's position |

**Device Rules**

![](../../../images/c645794def14feb0.png)

When *Disturbance Direction* is set to *Specified Direction*, an additional parameter *Direction Vector* can be configured

By configuring this 3D vector, you can specify the direction of force applied by this force field device

When the *disturbance direction* is set to *"**Line Connecting Sphere Center and the Trigger Area Center**"*, additional parameters can be configured as *Inner Diameter Orientation* and *Outer Diameter Orientation*

![](../../../images/3ac4bcf689559202.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Inner Diameter Orientation* | Force direction of the inner sphere in the logic force field |
| *Outer Diameter Orientation* | Force direction of forces outside the logic force field beyond the sphere |

Each configurable parameter is divided into *towards the sphere center* and *away from the sphere center*

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Towards Sphere Center* | The line connecting the character and the sphere center of the logical force field, pointing towards the sphere center |
| *Away from Sphere Center* | The line connecting the character and the sphere center of the logical force field, pointing towards the character |

Other configurable parameters are described as follows:

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Inner Diameter Velocity (m/s)* | Additional force field device that can apply this speed within the inner sphere radius |
| *Outer Diameter Velocity (m/s)* | Additional force field device that can apply this speed outside the outer sphere radius |

**Local Filter Examples**

When a character is within the force field device's effective range, the local filter will continuously monitor and any changes in results will take effect immediately

![](../../../images/2bad415fbe429369.png)

**Force Field Device Effect Description**

Players will only be affected by the force field device effect when they enter the configured force field range.

The force effect and its configuration are related to the inner sphere radius and the outer sphere radius, with specific effects as follows

Let's explain in detail with a 3D graph

![](../../../images/02aae8bd8093960b.png)![](../../../images/97a6408fcf898eb3.png)

The player within the inner radius range experiences the force effect configured for the inner sphere radius.The player between the inner and outer radii experiences a transitional force effect between the inner and outer radii.The player outside the outer radius experiences the force effect configured for beyond the outer sphere radius.

# III. Important Notes

When the character is in a flying state and under additional forces, they are not affected by gravity.

This feature can be used to create horizontal force fields.

For the upward force of the force field device to take effect, the character must be in a flying state.

Characters cannot jump in place and take off while in the force field device

The inner radius velocity within the force field device is too high, and when the direction is set to "Line Connecting Sphere Center and the Trigger Area Center - Towards Sphere Center", if a character enters the range while flying or falling, they may be unable to escape this state

# IV. Manage Character Disruptor Devices Through Node Graphs

During entity runtime, character disruptor devices can be managed through node graphs

Set Character Disruptor Device

Adjust character disruptor devices affecting running entities

If the ID is empty or configured with non-existent IDs, all character disruptor devices will not take effect

![](../../../images/532ae695aedbcd6d.png)
