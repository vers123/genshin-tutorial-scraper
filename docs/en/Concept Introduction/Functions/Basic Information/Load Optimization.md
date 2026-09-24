---
title: Load Optimization
path_id: mhqsjmittry4
updated_at: 2026-09-08 12:21:38
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqsjmittry4
---

During gameplay, when there are too many *entities* in the scene, it may cause the game load to exceed limits. When users encounter such issues, they can consider using *FOV Detection* for *load optimization*.

In simple terms, users can designate certain non-critical entities to be unloaded locally when the character is at a considerable distance, thereby saving the cost of these objects

# I. FOV Detection Parameter Configuration

There are two entry points for FOV Detection configuration:

## 1. Global Load Optimization Settings

In the stage settings interface, you can see the load optimization options

![](../../../images/6a4c6b024a02e9bd.png)

FOV Detection Status:

*Follow Entity Configuration*: When this option is selected, this load optimization will take effect according to the attribute configuration on the prefab/entity

*Disable*: When this option is selected, this load optimization feature will be disabled

## 2. Load Optimization Attributes

In the object's Basic Information tab, you can see the load optimization attributes. If set to "Enable", the object's entity will be subject to load optimization logic, which may result in *local destruction* when too far from the character

![](../../../images/ba9433e70d0b4718.png)

## 3. Creation-Specific Optimization Functions

![](../../../images/b13d1c5aef92d497.png)

**Out-of-Range Frequency Reduction**: This is a creation-specific optimization function that is enabled by default.

**Enabled**: During level runtime, if the creation entity exceeds a certain range from the character, it will run at a reduced frequency on the client side of that character.

**Disabled**: During level runtime, if the creation entity exceeds a certain range from the character, it will still run with normal logic.

## 4. Model Visibility Range & Precision

![](../../../images/462c78a35336e977.png)

The **Model Visibility Range & Precision** settings allow you to adjust the viewing distance and level of detail for a unit's model.  
(This setting can only be used after disabling **Do Not Run if Out of Range**.)

Default: No additional adjustments are made to the model's visibility range or quality.Always Visible: When the player moves beyond the unit's default visibility range, the unit model remains visible at the lowest level of detail instead of disappearing.Always Display at Maximum Precision: The unit model remains visible at all distances and maintains the highest level of detail.

# II. Rules for FOV Detection

## 1. Local Destruction State

The aforementioned "Local Destruction" state is different from the destruction of the entity, which can be understood as merely being "Do Not Show" on the client side, while the entity's logic still exists:

It can still be indexed and controlled logically through the node graph nodesWhen a player approaches a locally destroyed entity, the entity will be recreated locallyIn Co-Op Mode, locally destroyed entities may differ between different users based on their distance from the local characterWhen a local entity does not exist, certain purely local logic may not run, such as playing special effects

## 2. Destruction Rules (FOV Detection Grid)

### (1) Grid-Based Planar Division

Under the FOV detection load optimization rules, the actual gameplay scene will be divided into multiple square areas of the equal size. During runtime, character units and other entities in the scene will be placed into a unique grid:

![](../../../images/94740590b1520804.png)

Taking the grid where the character unit is located as the center, multiple surrounding grids form the "*FOV Detection Range.*" When FOV detection optimization is enabled, entities outside the vision detection range will be subject to "local destruction" and become invisible during gameplay. As shown in the graph below, assuming a FOV detection range of 3 × 3:

![](../../../images/2f1c898acf3413c5.png)

### (2) Character Cross-Grid

When the character's position changes, the FOV detection range will also change, and entities will be created or destroyed when entering/exiting the character's FOV detection range, as shown in the graph below:

![](../../../images/59d5264b96f58fdf.png)

### (3) Entity Cross-Grid

When entities cross grids through any Motion Device or Creation behavior, they will be created or destroyed if they trigger entering/exiting the character's FOV detection range:

![](../../../images/155484e081fd683d.png)

# III. FOV Detection Specifications in Beyond Mode

## 1. Grid Size

The grid square size in Beyond Mode is 40m x 40m

## 2. FOV Detection Range

In Beyond Mode, the actual FOV detection range extends to three grid spaces around your own grid position, as shown in the following graph:

![](../../../images/8879310af3190040.png)
