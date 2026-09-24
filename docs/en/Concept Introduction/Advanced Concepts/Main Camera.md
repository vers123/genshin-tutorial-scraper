---
title: Main Camera
path_id: mhapyl0uxns0
updated_at: 2026-09-16 16:55:34
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhapyl0uxns0
---

*Camera* is the tool that renders the player's perspective in the game. It determines what the player sees in the game.

In Beyond Mode, it supports creators (Craftspeople) to define camera rules by creating camera templates. Each template corresponds to a distinct Camera State.

# I. Definition of Camera Templates

Any *Camera Templates* available to players during gameplay must be edited in Manage Main Camera. The access path is shown below:

![](../../images/0c98962dd17e45b7.png)

At runtime, each player has only one active Camera Template assigned to them:

Different players can have different templates active at the same time. For example, in Co-Op Mode, Player A may have "Template 1" active while Player B has "Template 2" active simultaneously.

You can switch a specific Player Entity's active Camera Template at runtime through the Node Graph, but Template parameters themselves cannot be modified dynamically.

# II. Editing Camera Templates

After entering the Main Camera editor, you will see the interface divided into three sections:

![](../../images/99767f41b15b8e24.png)

1.Parameter configuration for the currently previewed Camera Template2.Preview of the relationship between the camera and character positions within the scene3.Real-time preview of the game screen during runtime

# III. Camera Template Parameter Configuration

## 1. Template Name

![](../../images/bc902ec2faa2eb40.png)

*Template Name*: The name of this Camera Template. It indicates the Template's role in gameplay and is also used as a reference when Node Graphs manipulate a player unit's main Camera Template

## 2. Location Information

![](../../images/c418b7fc0528a1ec.png)

Relative location between Camera and Character. These parameters are collapsed by default. They display relative coordinates between the camera and the character within the current preview Interface for reference during editing

## 3. Camera Basic Settings

![](../../images/7796f10ae252970c.png)

*Movement Mode*: The current version only supports camera following character entities. Future updates will expand support for other entity types such as vehicles, etc.

*Mode*: A crucial parameter that distinguishes camera template types. The mode determines the main camera rules, and the adjustable parameters for each camera will vary depending on the mode

*Default Effective Target*: The camera template, as a parameter attached to the player, can be modified directly during runtime for the corresponding player. However, during initialization, it must be assigned based on the player's class. This field can be used to set which classes the template should initially apply to

## 4. Camera Detailed Settings

Based on these different modes, the adjustable parameters exposed in the template settings will also vary

### (1) Classic Camera

Classic Camera is the camera used in the Classic Mode. Its parameters are grayed out. It only supports preview and cannot be edited, so its details are omitted for brevity

![](../../images/ebea6b7b152b19e2.png)

### (2) 3D Back Camera

3D back camera is an over-the-shoulder shot where the camera is positioned behind and to the right of the character, as shown in the following example:

![](../../images/f961413aac5b3631.png)

Detailed settings are shown in the image below:

![](../../images/6d7e49154bb38446.png)

*Camera FOV Detection*: Field of view (FOV) refers to the viewing cone range, as shown in the figure. Modifying the FOV will change the range of the FOV Cone

![](../../images/40e994f6e5049171.png)

*Camera can ignore collision:* When set to "No," collision with the current Object Entity may push the camera, causing stuttering or sudden changes in camera position. When set to "Yes," the camera ignores collision with this Object Entity. However, this may cause the camera to move inside the model, resulting in visual issues. Craftspeople should configure this setting based on the specific gameplay scenario

*Viewpoint Offset*: An additional location offset applied in the World Coordinate System after the Camera points to the target. The red box in the graph below shows the Viewpoint

![](../../images/91627c204cedbe09.png)

*Viewpoint Follows Rotation*: Whether the Camera rotates along with character rotation

*Default Line of Sight*: Initial distance between the camera and viewpoint

*Line of Sight Range*: The adjustable range of Line of Sight that can be modified through player input

*Horizontal Angle Range*: The range in degrees that the camera can be rotated left and right when the player moves the camera horizontally through input control

*Pitch Angle Range*: The range in degrees that the camera can be rotated up and down when the player moves the camera horizontally through input control

### (3) 2.5D Camera

The camera for traditional 2.5D games, as shown in the following reference:

![](../../images/0bc7c1c2e258d992.png)

The detailed settings are shown in the graph below:

![](../../images/a46cfba35935e172.png)

*Ignore Camera Collision*: When set to "No", the Camera may be pushed by collisions with entities in the scene, causing stuttering or sudden jumps. When set to "Yes", the Camera ignores collisions, but its position may move inside models, leading to poor visual performance. Therefore, creators (Craftspeople) need to customize this setting based on their actual gameplay scenarios

Other attributes: Already explained earlier so we won't repeat here

### (4) First Person Camera

The Camera is positioned at the character's eye level, simulating a first-person perspective view of the scene, as shown below:

![](../../images/b213c2b4dfc04d2b.png)

The detailed settings are shown in the graph below:

![](../../images/d8269a7cd9dbcde2.png)

### (5) Third Person Camera

Similar to the Classic Camera, but you can edit its detailed settings:

![](../../images/fa2a3fac83b4d2a5.png)

The detailed settings are shown in the graph below:

![](../../images/e83ba5dfa4907d41.png)

# IV. Camera Template Switching

You can use node graphs to dynamically switch Camera Templates at runtime. The target units are a *list of Player Entities*.

![](../../images/8fb3c3da542f3866.png)

# V. Object Camera

## 1. Basic Settings

![](../../images/061433790ce49cce.png)

*Mode*: Support has been added for Object Cameras to follow objects/creation entities. Currently, only Third Person Cameras are supported

*Movement Mode*: A crucial parameter that distinguishes camera template types. The mode determines the main camera rules, and the adjustable parameters for each camera will vary depending on the mode. Currently, only Follow Object/Creation is supported

## 2. Advanced Settings

![](../../images/02d1d9a1ebb44bd8.png)

Shares identical configuration logic with the character camera parameters

## 3. Movement Correction Settings

### (1) Camera Auto-Rotation Tracking

![](../../images/df49669445f8cb3d.png)

*Camera Auto-Rotation Tracking*: Determines whether the object camera adjusts and corrects its position after an offset occurs. When disabled, the following parameters are locked, and will not take effect

*Horizontal Correction Reference*: The baseline angle for correcting the object camera along the horizontal plane, relative to the object's forward direction (0 represents the object's forward direction)

*Pitch Correction Reference*: The baseline angle for correcting the object camera along the vertical plane, relative to the object's forward direction (0 represents the object's forward direction)

The value range for both Horizontal and Pitch Correction Speed is [0°,360°], while the range for both Horizontal and Pitch Correction Reference is [-180°,180°]

*Correct only while moving*: When enabled, the object camera will adjust based on the configured speed and reference angles only when the following conditions are met:  
1. The object to which the camera is attached moves   
2. The player is not moving or controlling the camera

*Camera Tracking Delay*: Determines whether the camera correction begins instantly after the player stops moving or controlling the camera

*Tracking Delay Duration*: The amount of time the system waits after the player stops moving the camera before initiating camera correction. Any new camera movement will reset this timer

### (2) Camera FOV Correction

![](../../images/76561917c62e7e07.png)

*Camera FOV Correction*: Determines whether the object camera's FOV scales dynamically based on the object's movement speed (commonly used for visual effects like acceleration). When disabled, the following parameters are locked, and will not take effect

*Max FOV Offset When Moving Forward*: The maximum FOV correction value applied when the object is moving forward at its max speed. At runtime, the actual FOV offset is interpolated based on the current speed within the range of [0, Max Speed]. When moving at maximum speed: Camera FOV = Configured Value + Correction Value

*Max Reference Value for Forward Velocity*: The forward speed reference used for FOV offset

*Max FOV Offset When Moving in Reverse*: The maximum FOV correction value applied when the object is moving in reverse at its max speed. At runtime, the actual FOV offset is interpolated based on the current speed within the range of [0, Max Speed]. When moving at maximum speed: Camera FOV = Configured Value + Correction Value

*Max Reference Value for Reverse Velocity*: The reverse speed reference used for FOV offset

### (3) Camera Movement Damping

![](../../images/44e454b34327fec1.png)

*Custom Action Damping*: Determines whether the camera's object-following damping coefficients are customized by the Craftsperson. When disabled, the damping coefficients for all three axes default to 1, resulting in an effective damping time of 0.15 seconds

*Movement Damping Coefficient*: The default value for each axis is 0, with an allowable input range of (0, 10]. Higher values introduce greater following latency relative to the object's movement speed. The effective damping time for a given axis is calculated as: Effective Damping Time = 0.15 seconds × Axis Damping Coefficient

## 4. How to Use Object Cameras

Add the universal component [Object Camera] into dynamic objects and creations, then select a pre-configured object camera template under Select Camera![](../../images/02da5439d28a49e0.png)

During stage runtime, use node graphs to switch to the corresponding camera

![](../../images/4b0d34d53c4c31f6.png)

![](../../images/239d04eb8c63b34c.png)
