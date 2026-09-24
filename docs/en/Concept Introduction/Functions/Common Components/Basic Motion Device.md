---
title: Basic Motion Device
path_id: mhi51frcqvim
updated_at: 2026-09-08 12:21:40
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhi51frcqvim
---

# I. Functions of Basic Motion Device Components

A *basic motion device component* gives *object entities* the ability to move according to set rules.

During Co-Op Mode, the basic motion device component prioritizes maintaining a consistent experience across all clients.

Basic motion device components support multiple basic motion devices working simultaneously. Their movements will be calculated simultaneously and stacked, although some basic motion devices are mutually exclusive.

# II. Editing Basic Motion Device Components

![](../../../images/f58f046d84a6cc2a.png)

(1) In the Entity/Prefab Editing interface, open the Edit Component tab.

(2) Click "Add Common Component" below, then select "Basic Motion Device" to add it.

(3) Press "Advanced Editing" to expand the editing page.

# III. Basic Motion Device Types

## 1. Uniform Linear Motion Device

*The* *uniform linear motion device* moves at a constant speed in a fixed direction based on the world coordinate system.

The parameters of the uniform linear motion device are shown in the figure below.

![](../../../images/95655d120709db75.png)

*Initially Effective*: When enabled, indicates that it takes place immediately once the entity is created.

*Effective Duration*: The motion device will automatically stop once the duration ends.

*Initial Speed*: Describes the entity's velocity along three axes.

*Velocity*: Initial speed after conversion to a 3D vector.

*\*Relative Location*: Has no meaning during runtime. During editing, it predicts where the entity will be located once the elapsed effect duration has ended when this motion device is acting independently.

## 2. Uniform Rotational Motion Device

Rotates at a constant speed around a fixed axis based on the the local coordinate system.

*Uniform rotational motion devices* are shown in the figure below:

![](../../../images/1af56f332146e9ff.png)

*Initially Effective*: When enabled, indicates that it takes place immediately once the entity is created.

*Effective Duration*: The motion device will automatically stop once the duration ends.

*Relative Rotation Axis Orientation*: Defines the axis of rotation.

*Angular Velocity*: Measured in degrees per second.

## 3. Target-Oriented Rotation-Based Motion Device

A motion device that rotates an object to a specified angle within a specified time.

*The parameters of the**Target-Oriented Rotation-Based Motion Device* are shown in the figure below:

![](../../../images/e0c58ace19d62217.png)

*Initially Effective*: When enabled, indicates that it takes place immediately once the entity is created.

*Effective Duration*: The motion device will automatically stop once the duration ends.

*Absolute Target Angle*: When the device takes effect independently, this is the expected orientation of the entity after the duration ends.

## 4. Pathing Motion Device

A device that moves objects along a specified path composed of multiple ordered waypoints.

![](../../../images/3d69f5228a61d741.png)

*Initially Effective*: When enabled, indicates that it takes place immediately once the entity is created.

*Loop Type*: Three loop types are provided:

*One-Way*: Stops moving upon reaching the path's endpoint and disables the motion device.*Round Trip*: Reverses direction and returns to the starting point upon reaching the path's endpoint.*Loop*: Upon reaching the path's endpoint, instantly teleport back to the starting point and restart the path.

*Waypoint List*:

*Time to Arrival*: Time required to move from the previous point to the current point.

*Movement Route*: Indicates the trajectory from the previous point to the current point.

*Relative Location**:* Path Point Relative to Entity Position.

*Absolute Rotation**:* Path Point Rotation Relative to World Coordinates.

*Notify Node Graph on Arrival*: When enabled, the object will send a "When Path Reaches Waypoint" event to its attached node graph upon reaching the corresponding waypoint.

## 5. Fixed-Point Motion Device

A motion device that moves an object to a specified position and rotates it.

![](../../../images/b25fd9f00c0d18cc.png)

*Initially Effective*: Takes effect immediately when the entity is created.

*Movement Type*: Provides the following two methods of motion.

*Uniform Linear Motion*: Moves to the target position and target rotation at a constant speed and turning rate.

*Arrive Immediately*: Ignores other motion description settings and immediately sets the object's coordinates and rotation to the target position and target rotation.

*Arrival Method*: Choose how to describe the movement rate.

*Fixed Speed*: Directly configure the specified rate.

*Motion Velocity (m/s)*: Enter the velocity value directly.

*Fixed Time*: Calculate the velocity based on the time required to reach the destination.

*Motion Duration (s)*: Enter the time required to reach the destination.

*Target Location*: The target position for the motion device.

*Target Rotation*: The target rotation for the motion device.

*Follow Rotation*: If configured, the motion device will not apply rotation changes to the object during motion unless set otherwise.

## 6. Stage Path Motion Device

A motion device that moves an object along a specified path, where the path is composed of multiple ordered waypoints. Unlike a regular path motion device, a stage path motion device references a stage path stored in a path management tool. When the motion starts, the object first moves to the first point of the path according to the configured method, and then continues along the path.

![](../../../images/c165af78c3c1ffd4.png)

Most of the configurations for the Stage Path Motion Device are the same as those for the Path Motion Device. The following focuses on the differences:

*Stage Path*: The referenced path. After selecting a path, the waypoint information will be automatically generated based on the waypoints configured in the path management tool.

*To Waypoint 1*: Unlike the Path Motion Device, the Stage Path Motion Device needs to describe how to move to the first waypoint.

*Movement Type*: Provides two methods of motion.

*Uniform Linear Motion*: Moves to the target position and target rotation at a constant speed and turning rate.

*Arrive Immediately*: Ignores other motion description settings and immediately sets the object's coordinates and rotation to the target position and target rotation.

*Arrival Method*: Choose how to describe the movement rate.

*Fixed Speed*: Directly configure the specified rate.

*Motion Velocity (m/s)*: Enter the velocity value directly.

*Fixed Time*: Calculate the velocity based on the time required to reach the destination.

*Motion Duration (s)*: Enter the time required to reach the destination.

*Notify Node Graph on Arrival*: When enabled, the object will send a "When Path Reaches Waypoint" event to its attached node graph upon reaching the corresponding waypoint. *\*Show Waypoint Information*: When enabled, detailed data for the waypoints will be displayed, but this information cannot be modified within the motion device.

# IV. Basic Motion Device States

The basic motion device has the following three states:

*Inactive***:** The default state of the basic motion device when initially configured on a component but not yet activated.*Running***:** The state when the basic motion device is functioning normally.*Paused***:** The state when the basic motion device is paused. Different from stopping, a paused motion device will record the current motion progress and continue the motion once resumed.

# V. Basic Motion Device Stacking Rules

## 1. Stacking of Same Type

When using basic motion devices of the same type, multiple movement motion devices can operate simultaneously and their effects will stack.

Only one basic motion device of other types can be active at a time.

## 2. Stacking Different Types

Different types of motion devices can stack.

Special Note: Rotational Motion Devices, Orientation Motion Devices, and Fixed Point Motion Devices cannot be stacked together.

Path Motion Devices and Stage Path Motion Devices cannot be stacked together.

For more detailed stacking rules, refer to the following 2D table.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Uniform Linear Motion | Uniform Rotational Motion | Rotate Towards Target | Path Movement | Fixed-Point Motion | Stage Path Movement |
| Uniform Linear Motion | Can Stack | Can Stack | Can Stack | Can Stack | Can Stack | Can Stack |
| Uniform Rotational Motion | Can Stack | Cannot Stack | Cannot Stack | Cannot Stack | Can Stack | Cannot Stack |
| Rotate Towards Target | Can Stack | Cannot Stack | Cannot Stack | Cannot Stack | Can Stack | Cannot Stack |
| Path Movement | Can Stack | Cannot Stack | Cannot Stack | Cannot Stack | Can Stack | Cannot Stack |
| Fixed-Point Motion | Can Stack | Can Stack | Can Stack | Can Stack | Cannot Stack | Cannot Stack |
| Stage Path Movement | Can Stack | Cannot Stack | Cannot Stack | Cannot Stack | Cannot Stack | Cannot Stack |

# VI. Conflict Rules for Basic Motion Devices

Basic motion devices use the *name* field as a unique reference method. Basic motion devices managed by a basic motion device component cannot have duplicate names. Conflicts occur when:

Enabled a motion device with the same name.The activated motion device type does not follow the stacking rules.

When checking for conflicts between basic motion devices, only devices that are running or paused will be considered. Inactive devices will not be taken into account.

When a newly activated motion device conflicts with an existing motion device, the existing device will be stopped (not paused), then the new device will be activated.

# VII. Using Node Graph to Control Basic Motion Devices

Activate Basic Motion Device

![](../../../images/11267f7feed5e73a.png)

Create Motion Device

Different nodes are available depending on the type of motion device.

![](../../../images/c3aa893af27c49d3.png)![](../../../images/c593dc4f85f749cc.png)![](../../../images/d57d15c31f966d6f.png)

Stop and Delete Basic Motion Device

![](../../../images/b7784a763a617108.png)

Pause Basic Motion Device

![](../../../images/0738e1674140242e.png)

Recover Basic Motion Device

![](../../../images/3465bf483e4208bd.png)

Event Node

![](../../../images/d5d5895c27e79f14.png)

![](../../../images/8e7f319367f4cd66.png)
