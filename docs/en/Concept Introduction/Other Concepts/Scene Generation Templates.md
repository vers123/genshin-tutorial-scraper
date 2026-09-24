---
title: Scene Generation Templates
path_id: mhdipgirsolo
updated_at: 2026-02-06 17:41:04
category: Concept Introduction/Other Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdipgirsolo
---

# I. Function Overview

Scene Generation Templates let creators (Craftspeople) quickly generate large-scale scenes. These templates allow customization of what gets generated and their quantities, facilitating rapid construction of diverse scenes.

# II. Using Preset Templates

To facilitate direct use by creators (Craftspeople), we provide some preset templates.

## 1. Entry Point

Go to "Entity Placement". Open "Scene Generation Templates" → "Preset Templates", pick a template, then confirm to import.

![](../../images/f2a6a8e5947958ab.png)

## 2. Generate Entities

In the "Uncategorized" tab (or any tab created), click or drag a template to place an entity in the scene.

![](../../images/bdd70ec8173d40cd.png)

## 3. Adjust Entity Parameters

Select the new entity. In "Base Attributes", its generation rules and generation range are configurable.

![](../../images/3f50fbca9206280f.png)

Open "Asset Configuration" to fine-tune what gets generated (asset types, density, etc.). For specific parameter descriptions, see Part IV "Parameters Introduction".

![](../../images/006f88c371db1306.png)

## 4. Generate Scenes

After tuning parameters, click "Random Preview" to preview the result. If it looks good, click "Confirm Generation" to create the objects in the stage scene.

![](../../images/1dec74ffd03207f8.png)

## 5. Adjust Generated Objects

After generation, to move or delete everything together, use the upper-right button in the Scene Entity Group, then choose "Select All" or "Delete".

![](../../images/7765773bd3c7d181.png)

# III. Creating Scene Generation Templates

To create a custom generation template, follow these steps:

## 1. Function Entry Point

Go to "Entity Placement", open the "Scene Generation Templates" tab, then click "Manage Template".

![](../../images/a118af05c7854caf.png)

Or open the system menu and click "Scene Generation Template Management".

![](../../images/629ac620ce975bc5.png)

## 2. Create Templates

Click "New Scene Generation Template".

![](../../images/8f56ad55abafabf3.png)

## 3. Configure Parameters

Click "Asset Configuration" to set the parameters.

![](../../images/3018d8b019c750b4.png)

## 4. Complete

After saving the template, it is available in the Asset panel under the "Scene Generation Templates" tab.

![](../../images/f755f11f08f0cf73.png)

# IV. Parameters Introduction

## 1. Base Attributes Panel

The "Base Attributes" panel has two parts: Generation Rules and Generation Range.

![](../../images/c97481ab861a9807.png)

### (1) Generation Rules

**Scatter Rule Preset List:** Click "Random Preview" to preview the scatter. If satisfactory, click "Save Scatter Rule". The saved rule can then be selected from the "Scatter Rule Preset List" for generation.

![](../../images/777fe31346a79226.png)

**Lock Generation Result:** When enabled, every generation repeats the previous result exactly.

### (2) Generation Range

**Spawn Area Shape:** Sets the shape of the spawn area. Two options: Cuboid and Cylinder.

![](../../images/5e00807e08c21fec.png)

## 2. Asset Configuration Panel

In "Asset Configuration", creators (Artificers) can edit the parameters for each spawn layer.

There are five default layers: Rock, Building, Tree, Vegetation, and Decoration. Additionally, custom layers can be added.

![](../../images/ba33db43e645f53d.png)

### (1) Layer Parameters

**Generation Density:** Controls how crowded objects are in a layer. Lower values = sparser. Higher values = denser.

![](../../images/509bbbefa6425674.png)![](../../images/c9f331385c9ca5c2.png)

**Generation Randomness:** Controls sampling-point jitter for generated objects. 0 = more uniform. 1 = more chaotic.

![](../../images/76f680b22c6ce727.png)![](../../images/a18361e2a8a8e728.png)

**Generate Based on Terrain:** Rock Layer only. Controls whether rocks generate based on the scene terrain.

![](../../images/c964d6a6c73fa2ba.png)![](../../images/73fefc4419514678.png)

**Associated Range:** Vegetation Layer only. Defines the effective generation radius of objects in the Vegetation Layer, using objects in the Tree Layer as the center. Outside this range, nothing spawns.

If the **Generate Interval Distance** for Tree-Layer objects is set too large, or the **Associated Range** for the Vegetation Layer is set too small, the Vegetation Layer may fail to spawn any visible objects. It is recommended to optimize through the following two ways: a. Reduce the **Generate Interval Distance** of Tree-Layer objects (negative values are allowed); b. Increase the **Associated Range** of the Vegetation Layer.

![](../../images/8dfe05e31ccbd4f1.png)![](../../images/eb5c30e04465e728.png)

### (2) Detailed Layer Editing

To fine-tune a layer (asset types, weights, spawn interval distance, transform ranges), click "Details Editing" on that layer.

![](../../images/45c47d6361379423.png)![](../../images/9846a9bb2f3e642b.png)

**Weight:** Controls how often each model is chosen within the same layer.

![](../../images/6de5da3b492a9ac3.png)![](../../images/0021c55d44c67dde.png)

**Generate Interval Distance**: Controls the offset distance between the current model and the objects generated in the next layer, supporting both positive and negative values.

A circle is drawn with the current object's center as the origin, with a radius equal to the object's bounding box radius plus this value. Within the area defined by this circle, generation of objects in the next layer is prohibited.

![](../../images/d69ffab06bd53b0f.png)![](../../images/4fd11bf29262f513.png)

**Model Assets:** Click "Add Assets" to add more assets. Choose asset types from the "Model Asset Library".

![](../../images/51f439070460167d.png)

**Transform Range:** Sets the jitter range for location, rotation, and scale.

![](../../images/2023a07249b0a83c.png)

# **V. Special Notes**

1.Layers generate in order: Rock first, then Building, Tree, Vegetation, and so on. Except for Rock, layers follow the "Exclusion Rule": each layer generates only in empty space after excluding the previous layer's objects. (If a layer is too dense, later layers may have nowhere to spawn.)2.The Vegetation Layer is special. It follows the "Associated Rule" and spawns with the Tree Layer. If the Tree layer does not generate, then the Vegetation layer will not generate either.
