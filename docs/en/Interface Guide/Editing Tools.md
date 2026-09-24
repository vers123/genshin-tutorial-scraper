---
title: Editing Tools
path_id: mhqpg9r3fou6
updated_at: 2026-08-03 17:44:22
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqpg9r3fou6
---

# 1. Function Overview

Editing Tools collect several auxiliary editing functions, including bounding box display, array generation, symmetry editing, and 3D Notes.

# II. Array Generation

## 1. Function Overview

Quickly create copies in batches using either a Grid Array or a Ring Array.

## 2. Applicable Units

Object Entity

Creation Entity

Loot Entity

## 3.Function Entry Point

Select an Object → right-click menu → Array

![](../images/2751e3c81f73c388.png)

## 4. Grid Array

### (1) Function Descriptions

Generates an object array arranged by the specified Distance and count along the X, Y, and Z axes, following the configured Generation Rules.

### (2) Mode Features

- This is an exclusive mode; once entered, you cannot interact with other content.

- Click the "Exit" button in the upper-right corner, or press Esc, to leave the mode.

![](../images/092ad427d1ede8f1.png)

### (3) Array Settings

![](../images/5e86493583295ffa.png)

Array Interval: Indicates the spacing distance along the X, Y, and Z axes

Number of Arrays: Indicates how many objects to generate along the X, Y, and Z axes

### (4) Array Preview

![](../images/4c92cdcf5050b92e.png)

Click to preview the array effect without actually creating it.

### (5) Array Generation

Click [Confirm Create] in the lower-right corner to create the array result and exit the mode.

## 5. Ring Arrays

### (1) Function Descriptions

Generates objects in a ring arrangement around a center point at the set angular interval.

### (2) Mode Features

- This is an exclusive mode; once entered, you cannot interact with other content.

- Click the "Exit" button in the upper-right corner, or press Esc, to leave the mode.

![](../images/701e24e886bdcea7.png)

### (3) Array Settings

Generates the corresponding object entity instances from the content based on the target axis's start point location and orientation, plus the entered angle and count.

Example: Generate one entity every 80 degrees, for a total of 3

![](../images/337cce6d003bd8eb.png)

# III. Symmetry Editing

## 1. Function Overview

Quickly generate mirrored copies of content by defining a symmetry center, axis, or plane. Three modes are supported: Point Symmetry, Axis Symmetry, and Plane Symmetry.

## 2. Applicable Units

Object Entity

Creation Entity

Loot Entity

## 3. Function Entry Point

Select an Object → right-click menu → Symmetry

![](../images/bb966aeca4ba571f.png)

## 4. Mode Features

- This is an exclusive mode; once entered, you cannot interact with other content.

- Click the "Exit" button in the upper-right corner, or press Esc, to leave the mode.

## 5. Symmetry Operation Process

### (1) Select Symmetry Mode

Select one of the Symmetry sub-options from the right-click menu: Point Symmetry, Axis Symmetry, or Plane Symmetry.

![](../images/966c014a35787404.png)

### (2) Edit Symmetry Point, Axis, and Plane Information

![](../images/f349769bde9cd126.png)

### (3) Preview Symmetry Effect

![](../images/396070b5480e5552.png)

Click to preview the symmetry effect without actually creating it.

### (4) Generate Symmetry Result

Click [Confirm Create] in the lower-right corner to create the symmetry result and exit the mode.

## 6. Symmetry Method Descriptions

### (1) Point Symmetry

Calculates the new location and rotation in the opposite 180-degree orientation along the line between the symmetry point and the mirrored content.

![](../images/f349769bde9cd126.png)

### (2) Axis Symmetry

Uses the defined point as the pivot to form a symmetry axis along that axis's orientation, then calculates the location and rotation in the opposite 180-degree orientation.

![](../images/558e51b81ff577b2.png)

### (3) Plane Symmetry

Uses the defined point as the center to form a symmetry plane, then calculates the location and rotation in the opposite 180-degree orientation.

![](../images/0d4172186cfe3806.png)

## 7. Additional Description

Each time you enter Symmetry Mode, a new symmetry point is generated. Symmetry point data is not saved.

Symmetry point data is cleared when you exit the mode.

# IV. Bounding Box Display

## 1. Function Overview

This function makes it easier to measure content dimensions while editing, allowing for more precise edits.

## 2. Applicable Content

Object Entity

Creation Entity

## 3. Function Entry Point

Model - Display Type

![](../images/35a02041eac6e89d.png)

## 4. Display Type

Dimensions Only

![](../images/4a431add22736296.png)

Bounding Box and Dimensions

![](../images/db312c90b2c47904.png)

Collision and Dimensions (Objects Only)

![](../images/44d54cb0b6aaa523.png)

# V. Notes Function

## 1. Show Z-axis

### (1) Function Descriptions

Provides an additional UI Control showing the positive Z-axis orientation.

### (2) Function Entry Point

Details panel → Bottom → Editing Tools section

![](../images/a274a3ae3ea80ef9.png)

### (3) Visual Effect

![](../images/dfc28a427a594759.png)

## 2. 3D Notes

### (1) Function Descriptions

3D Notes consist of an Icon and Text, and are used to display notes information for objects in the editing scene.

### (2) Function Entry Point

Details panel → Bottom → Edit Tools section

![](../images/0f0815fa2c52eed7.png)

### (3) Visual Effect

![](../images/f2eabb33c5253fb8.png)

## 3. Global Notes Display Control

### (1) Function Descriptions

Controls whether note text for all content is always displayed through the option in Stage Settings.

### (2) Function Entry Point

![](../images/96e44f376c3e8110.png)

# VI. Model Data Copy and Paste

## 1. Function Description

Supports copying and pasting object model data, including the main model and all decorations. (For creations, only decoration content is copied)

## 2. Function Entry Point

Model - Copy

![](../images/0cd6b4014655a7fa.png)

# VII. Display Center Point Position for Multiple Selections

## 1. Function Description

In the Scene layer and Placement layer, position information can currently be displayed after multiple items are selected.

![](../images/fa738ac3e0115d18.png)

# VIII. Rangefinding

## 1. Overview

The rangefinding tool is a built-in feature that allows you to measure distances within the scene.

## 2. Accessing the Tool

Right-click Menu > Rangefinding Line > Add Rangefinding Line

Select Add Rangefinding Line to enter measurement mode. Left-click on the ground to place two points, and the distance between them will be displayed on screen.

![](../images/2bf3f9c04c98b4d6.png)

![](../images/2f2498c9c5e13d85.png)

## 3. Removing Measurement Lines

Option 1: Delete individual measurement lines

Option 2: Right-click Menu → Rangefinding Line → Remove All to remove all measurement lines

![](../images/ba4dba786fb714cb.png)

## 4. Editor Settings

You can choose whether rangefinding lines remain permanently visible via Quick Settings.

![](../images/3981cc149abfc902.png)
