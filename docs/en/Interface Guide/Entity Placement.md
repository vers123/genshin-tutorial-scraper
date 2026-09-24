---
title: Entity Placement
path_id: mhyoa89ov4g2
updated_at: 2026-03-27 13:58:10
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhyoa89ov4g2
---

![](../images/c5f30d39ca81d833.png)

# I. Function Overview

Create and place entities needed in a stage, and edit entity data. Shares the same scene as Terrain Editing

# II. Function Entry Point

Click the second icon in the top tab bar to switch to Entity Placement

Some features are available only on the Entity Placement tab.

![](../images/8261bd45c946e4e2.png)

# III. Placement Process

## 1. Creating Object Entities from Assets Bar

Hold and drag an object from the Assets Bar with the left mouse button, then release to drop it into the scene; or left-click an object in the Assets Bar to create it at the center of the screen

(1) The dynamic units tab under the prefabricated tab creates dynamic entities. You can add components and node graphs to them; they are more performance-intensive and generally used for gameplay objects

(2) The static units tab under the prefabricated tab creates static entities. You cannot add components or node graphs to them, nor control them via node graphs; they are performance-efficient and generally used for scenery

(3) In the Custom tab, whether an object is dynamic or static depends on the type of Custom Prefab selected

![](../images/1130645b152a84d7.png)

Note: Dynamic Entities have GUIDs and can be controlled via node graphs; Static Entities do not have GUIDs

## 2. Basic Placement Actions

### (1) Single Selection

Left-click to select an object. The selected entity highlights with an outline, shows the Transform Tools and the toolbar, and expands the Details Panel on the right

![](../images/b3f718cf80b2761a.png)![](../images/2c21c2bc76c1d92c.png)

### (2) Multiple Selection

Hold the left mouse button and drag to box-select; hold Left Shift and left-click to add or remove from the selection

The Transform Tool appears at the center of all selected entities

Note: Some entities cannot be selected at the same time (e.g., Entity Models and Waypoint Models inside an Entity Motion Device Component)

![](../images/b305d4d13f8cb6bb.png)

### (3) Cancel Selection

Click an empty area to deselect

### (4) Move, Rotate, Scale

Use the Transform Tool to move, rotate, and scale entities. Click Space to switch tool types (All-in-One, Move, Rotate, Scale)

All-in-One Transform Tool: Provides a subset of Move/Rotate/Scale and supports relative-coordinate transforms only

![](../images/3177b452aee9197b.png)

Motion Transform Tool: Changes an object's location; supports World coordinates or Entity (local) coordinates

![](../images/0f51fc7d23799625.png)

Rotation Transform Tool: Changes an object's rotation; supports World coordinates or Entity (local) coordinates

![](../images/8398109aff06d4f7.png)

Scale Transform Tool: Allows you to change an object's scale, supports Entity (local) coordinates only

![](../images/b2f931cd28b67e5d.png)

Use each Transform Tool's step increments to perform precise actions (Movement Stepping, Rotation Stepping, Scale Stepping)

![](../images/3f6e7cb6c22e9cbc.png)![](../images/f509dd312edbd7fd.png)![](../images/49fd7075a8d82513.png)

### (5) Delete Entities

Click Delete to delete the selected entity

### (6) Copy and Paste Entities

Click Ctrl+C/Ctrl+V to copy and paste; the new entity appears at the cursor's position in the scene

Hold Alt and drag a Transform Tool axis to duplicate in place; the new object will appear at the original's scene position (copies per action can be set in Quick Settings → Other Settings → Alt Copy Quantity)

### (7) Copy and Paste Entity Data

Does not create new entities

Access this via the selected object's right-click menu

Pasting entity data overwrites the selected entity and updates its prefab reference; the entity's GUID does not change

You cannot paste entity data between objects and creations

### (8) Undo

Click Ctrl+Z to undo the previous action

Unavailable in some cases

### (9) Quick Save

Click Ctrl+S to save all data in the current stage. Unsaved data is not written to the Saving (save frequently)

Unavailable in some cases

## 3. Details Editing

Access this in the Details Panel on the right, under the Base Attributes tab (first on the left)

![](../images/29006e17f6779f74.png)

### a. Transform

Fine-tune location, rotation, and scale

![](../images/54599daf697282f8.png)

After enabling Lock Transform, the locked entity's position, rotation, and scale cannot be changed via Transform Tools, preventing accidental edits

### b. Model

Replace the main object's model, view attachment points, and add decorations

![](../images/27b97aace7eea07d.png)

### c. Native Collision

Initially Effective: When enabled, the object's Native Collision box is enabled

Climbable: When enabled, the entity can be climbed

![](../images/e3aeef27cc6994c0.png)

### d. Visibility

Model visibility affects only the model's display and does not impact the entity's other logic

![](../images/73899db41771bdff.png)

### e. Create Settings

When Initial Create is disabled, the entity is not created at the start and can be created dynamically via node graphs

![](../images/732f6d9be7099c6d.png)

### f. Faction

You can set the entity's faction

![](../images/6f975424cd0eb3b2.png)

### g. Unit Tags Management

Add tags and search for tagged entities within the node graph

![](../images/39961f8988942a56.png)

### h. Entity Deployment Group Management

Manage an object's Entity Deployment Group

![](../images/2c128691b48d36cc.png)

### i. Load Optimization

Controls whether an object runs on the owning player's Local when it is far from the character

![](../images/a5463671aebe1513.png)

### j. Sound Effects

Determine whether the entity plays its own sound effects

![](../images/30cbff7f52d0f015.png)

### k. Reference Source

View the prefab referenced by the entity

![](../images/0e85242649371cf1.png)

### l. Notes

For inputting text notes

![](../images/8cc628acf6a393bd.png)

## 4. Quick Placement

Use Quick Settings (gear icon, top bar) to toggle related options

![](../images/b36a964d4d24d869.png)

### (1) Camera Settings

Adjust camera horizontal and vertical speed; click Reset to restore defaults

When Horizontal Lock is enabled, camera height can be adjusted only with E and Q.

### (2) Ground-Level Placement

When Ground Placement is enabled, drag the Transform Tool's pivot to place objects on the ground

### (3) Surface Adhesion

Snap objects to any of the six faces of their bounding box

### (4) Normalize Position After Surface Adhesion

Corrects an object's orientation after Surface Adhesion to align objects neatly

Adjusts the angle between objects to one of 0°, 90°, 180°, and 270°

### (5) Center Align

Aligns the centers of two objects

### (6) Show Distance When Moving

Displays the current movement distance while dragging with the Motion Transform Tool

### (7) Display Settings

Toggle persistent display of Creations Entering Battle Range, Preset Points, Empty Objects, and Path Waypoints

### (8) Alt Copy Quantity

Sets the number of objects created when copying with Alt

### (9) Environment Settings

Change the preview environment while editing

### (10) Edit Hotkeys

View the hotkeys for the editing interface

# IV. Entities, Prefabs, and Overwrites

## 1. Entities and Prefabs

Objects dragged from the Object Placement panel are entities. View the linked prefab via [Details Panel > Object Attributes > Reference Source]

Entity data references the prefab; edits made on the entity overwrite the referenced data

Deleting a prefab removes all of its entities

![](../images/462a11fd92520981.png)

## 2. Overwrite Prefab Data on an Entity

Non-overwritten fields receive updates pushed from the prefab (after clicking Overwrite Save)

Overwritten fields do not receive pushed updates (these fields are highlighted in blue in the Details Panel)

![](../images/ab9f9aa6ba861ec4.png)

## 3. Modify Prefabs

Prefabs can be edited directly in [Prefab Library][Prefab Library](/ys/ugc/tutorial//detail/mhwp5h9d4h3e)

Entities in the Entity Placement panel can push data back to the prefab and overwrite prefab data via the right-click menu [Overwrite and Save Prefab]

[Save As Prefab] creates a corresponding new prefab

![](../images/cf37eb02899d11db.png)

## 4. Restore Entity to Prefab Data

### (1) Restore All

Click the objects icon on the top bar to open more options, then choose [Restore to Prefab Data] to revert all entity data — except location and rotation — to match the prefab

![](../images/4561f06fd9f3b5a7.png)

### (2) Partial Restore

Each attribute card supports restoring its values individually

![](../images/10935b9502672a8e.png)
