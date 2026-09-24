---
title: Terrain Editing
path_id: mh7mw90erg1s
updated_at: 2026-08-03 16:54:18
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7mw90erg1s
---

Use Terrain Editing to create scene effects within a stage.

# I. Terrain Editing

## 1. Entry Point

![](../images/82a8c5067f7d56e4.png)

Access Terrain Editing from the first button in the top tab bar; click to toggle it.

## 2. Initial Creation

When a stage saving is created, a 100 × 100 Terrain is generated automatically at world coordinates (0,-1.25,0).

## 3. Operating Units

In Terrain Editing, the smallest operable unit is a single-layer area (size 5 × 5; layer height 2.5).

## 4. Main Interface

![](../images/805eef02e8e84b26.png)

### (1) Assets Bar

How to open: Use the upper-left button![](../images/5e3083e29e85f68e.png)to toggle open and close.

Function: Select assets to create.

Asset List

![](../images/58dfd4044fb41198.png)

Area Material (Click to enter [Terrain Editing → Terrain Modification → Free Edit](/ys/ugc/tutorial//detail/mhwe1n94b1x6#NBO-buadXaGfdfOtGMnUhI))Custom Prefab (click to create)Prefabricated Components (click to create)Asset Library

### (2) Details Panel

How to open: Use the upper-right button![](../images/f891a7d88a2c2e3c.png)to toggle open and close.

Function: Manage terrains within stages.

Terrain List:

![](../images/3f2e4556bbb891e1.png)

Features

Rename (double-click the name![](../images/894076ac1a7f8cfe.png)to enable) - Modify the name of the selected TerrainFocus (click button![](../images/7e0783c305a3f43c.png)to enable) - Positions the camera at the terrainCreate Terrain (Click ![](../images/d8368c0daa0d45a3.png) button to enter) - Enter [Terrain Editing - Terrain Creation](/ys/ugc/tutorial//detail/mhwe1n94b1x6#N4xdsTIf2xzL6jrANA6X91)

Terrain Details:

![](../images/2c0efd4089cf6b01.png)

Activation Requirements: Select any terrain using the pointer or Terrain List (does not work with multiple selections).

Features

Modify Terrain Position (Input) - X value, Y value, Z valueModify Terrain Rotation (Input) - Y valueArea Material (Click the button![](../images/4239e4f2774fd258.png) to open the Replace panel) – Replace the selected material in the terrain with another material, or remove it. Note: Clicking![](../images/51a40addbf159c92.png)the button clears all areas of that material.![](../images/5032519f9fee1853.png)

### (3) Pointer

![](../images/92feaffb6436348c.png)

Opening: Available only when the Edit Mode is not active.

Function: Select one or more items (same logic as object selection). Toolbars change based on the current selection.

Selectable Content and Selection Functions

Terrain (For detailed functionality, see below: [Terrain Editing - Terrain Modification](/ys/ugc/tutorial//detail/mhwe1n94b1x6#Nm9GQGnLWXlPXcbdJBZU6M) )Static Objects, Dynamic Objects, and Creations (functions: modify position data or open the editor)

# II. Terrain Creation

## 1. How to Enable

Left Assets Bar

After entering [Terrain Editing - IV. Terrain Modification](/ys/ugc/tutorial//detail/mhwe1n94b1x6#NPvJ8GZc-Cm4qoP_c5auWx) , click the [Created Based on Grid Lines] ![](../images/252c31fe209bec1c.png) button in the lower right corner.

Right Details Panel

From the Main Interface, go to Details Panel > Terrain List > Create Terrain.

## 2. Creation Mode

![](../images/41d3f0b952c1e044.png)

## 3. Creation Logic

With the selected material in the material panel, the canvas height set by the right-side height scale, and the brush mode chosen in the bottom toolbar, use the pointer/brush at the current position to paint and create areas. Click End Drawing X on the top-right corner to generate terrain from the painted content.

## 4. Available Functions

### (1) Material Panel

Function

Switch Brush Material: Click to choose the brush's terrain material (two options available). (7 types in total)

![](../images/8b273f1ac924c015.png)

### (2) Height Scale

Function: Controls the canvas height used for terrain creation;

Move the slider![](../images/20afa3341c876f1e.png) to change the canvas height.Click the slider![](../images/38ea657ab921b15a.png)to enter a value and change the canvas height.Focus ![](../images/9c7d015726428bac.png)on the canvas height.Increase/decrease ![](../images/d7b791b23804095e.png)canvas height by 20.

### (3) Bottom Toolbar

Function: Switches Brush Mode

Area Actions

![](../images/d368f73f14c9c59e.png)

Brush Layers: Set ![](../images/7eacb5b01b9d02da.png)the layer count per stroke.

Create: Raise the selected area by x layers (Note: after editing, the entire area stack adopts the current brush material).

Delete: Lower the selected area by x layers.

Level Out: Set the selected area to the specified height.

Slope Actions

![](../images/dbb043ec37c1a658.png)

Usage Condition: The brush can select only areas that already exist

Set Slope Direction: Forward/Left/Right

Slope Material: The slope material generated will vary depending on the area material.

Create Slope: Add one slope layer on top of the selected area; the arrow shows the higher end based on the chosen direction.

Delete Slope: Remove the selected slope.

Water Body Actions

![](../images/8e2607fdf86a10f2.png)

Usage Condition: The brush works only on existing areas or water bodies.

Create Water Body: Convert the top layer of the selected area to a water body.

Remove Water Body: Convert the top water layer of the selected area back to an area.

Path Operation

![](../images/73ae66b67816ce81.png)

Usage Condition: The brush affects only existing areas.

Create Path: Draw a path on the top surface of the selected area.

Delete Path: Remove the path from the top surface of the selected area.

### (4) Brush Actions

Tap: Apply the configured brush effect once at the current positionDrag: Apply the configured brush effect at each valid position the cursor passes over.

### (5) End Drawing

![](../images/183d36aed37086ef.png)

Function: Generate terrains from the content created on the canvas.

Terrain Generation Logic: All connected areas form a single terrain; disconnected areas in one operation create multiple terrains.

# III. Terrain Modification - Pointer Mode

## 1. How to Enable

![](../images/92feaffb6436348c.png)

Available only when the Edit Mode is not active (Main Terrain Editing interface).

## 2. Available Functions

Click content to select it; the bottom toolbar updates based on the selection.

### (1) Single Terrain Selection

![](../images/7c1f71ff0fe37ccf.png)

Transform Tools

![](../images/b8b926f4b8248768.png)

Motion: Change the terrain's position (X, Y, Z).

![](../images/32524fecfca44722.png)

Rotation: Change the terrain's rotation (Y value).

![](../images/acfab568750b5c54.png)

Switching: Click the Hotkey Space to cycle between Motion, Rotation, and Mixed Transform tools.

Layer Adjustment

![](../images/7f7831ff04e265cd.png)

Raise a Layer: Click to![](../images/fedd5115672a665f.png) raise all areas in the selected terrain by one layer.

Lower a Layer: Click to![](../images/c584f04bb91a4e3b.png) lower all areas in the selected terrain by one layer.

Area Selection

![](../images/b71ed287e0219949.png)

How It Works: Click to enter the Precise Editing mode for the selected terrain. Use the pointer to select areas; hold Shift and left-click areas to add them from the selection.

![](../images/c685eedcd5e8da49.png)

Raise: Click to ![](../images/0b15fe7519221414.png) raise the currently selected areas by one layer

Lower: Click to![](../images/e651356aed6fd478.png) lower the currently selected areas by one layer;

Split: Click to![](../images/86d2a60864387e90.png) detach the selected areas from the terrain and generate one or more new terrains based on the split content;

Precise Editing

![](../images/deca26d1b955dc12.png)

Enter Precise Editing for the selected Terrain[Terrain Editing - V. Terrain Modification](/ys/ugc/tutorial//detail/mhwe1n94b1x6#N2fYcEPsH6pb1jPSSY2sQO)

Delete Terrain

![](../images/b8cd11627c5a6ce0.png)

Delete all selected Terrains.

### (2) Multiple Terrain Selection

![](../images/3ca2a2b257ca2eb3.png)

How It Works: Act on all selected terrains simultaneously.

Available Functions

Transform Tools

![](../images/a97eced7121aa028.png)

Delete

![](../images/346af21b51ca152a.png)

### (3) Right-click Menu

![](../images/aabc4feda712f7bb.png)

Copy, Paste, Camera Focus, Delete, Assets Exporting, Character Dummy, Add to Entity Deployment Group

# IV. Terrain Modification - Free Edit

## 1. How to Enable

On the Main Terrain Editing interface (not in any Terrain Editing mode), click any material button in the Material Panel.

![](../images/bc1e23aed9eb0819.png)

![](../images/50b207561206b656.png)

## 2. How It Works

[🎬 视频](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/en-us/mh7mw90erg1s/5587e588-1f1f-4d21-bad9-482c49b3e4be.mp4)

In Free Edit, the cursor starts in the pointer mode for terrain selection. Click to select terrain, then the cursor switches to the brush mode. Using the material chosen in the Material Panel and the brush mode selected in the bottom toolbar, paint to create areas at the pointer/brush position. Clicking another terrain ends drawing for the current terrain, generates terrains from the painted content, then returns to terrain selection.

## 3. Available Functions

All available functions match Scene Creation, except the Height Scale.

### (1) Material Panel

Function: Change brush material; replace terrain material.

### (2) Bottom Functional Area

Functions: Area Actions, Water Body Actions, Path Operation.

# V. Terrain Modification - Precise Editing

## 1. How to Enable

In the pointer mode, select a terrain and use the bottom toolbar to enter Precise Editing for the selection.

![](../images/deca26d1b955dc12.png)

## 2. How It Works

[🎬 视频](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/en-us/mh7mw90erg1s/7ba21d5b-9bea-491a-a1df-78c67c9be17e.mp4)

In the Precise Editing mode, you can edit only the terrain selected before entering. The cursor switches to the brush mode; with the material from the Material Panel and the brush mode from the bottom toolbar, paint to create areas at the pointer/brush position. Click End Drawing to generate terrains from the painted content.

## 3. Available Functions

All available functions match Scene Creation, except the Height Scale.

### (1) Material Panel

Function: Change brush material; replace terrain material.

### (2) Bottom Functional Area

Functions: Area Actions, Water Body Actions, Path Operation.

# VI. Shortcuts

## 1. Activation Requirements

Available in any Edit Mode or when the toolbar is in Area Actions mode.

[Terrain Editing - II. Terrain Creation](/ys/ugc/tutorial//detail/mhwe1n94b1x6#NdXA7wklhb_3QyKepWV9Iv)[Terrain Editing - IV. Terrain Modification](/ys/ugc/tutorial//detail/mhwe1n94b1x6#NPvJ8GZc-Cm4qoP_c5auWx) [Terrain Editing - V. Terrain Modification](/ys/ugc/tutorial//detail/mhwe1n94b1x6#N2fYcEPsH6pb1jPSSY2sQO) 

## 2. Uniform Height

Function: Hold down the Alt key. The first click samples the area's layer count; subsequent clicks apply that height to each valid area the brush touches.

[🎬 视频](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/en-us/mh7mw90erg1s/5175ec17-9033-4629-a3a8-b9b532839c03.mp4)

## 3. Quick Generation

Function: Hold down the Shift key, click to place a start area at the grid position, hover to preview the end, then click the end to generate terrains.

[🎬 视频](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/en-us/mh7mw90erg1s/8f819fb0-57c3-4faf-b086-b0573e3a9e0f.mp4)
