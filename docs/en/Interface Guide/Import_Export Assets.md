---
title: Import/Export Assets
path_id: mh7y030nkv80
updated_at: 2025-10-21 23:14:30
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7y030nkv80
---

# I. Function Overview

The Import/Export Assets feature allows you to convert selected created content or content collections into a data archive that can be imported and reused later by yourself or others.

# II. Export Method 1 - Select in Stage

## 1. Entry Point

### (1) Right-click Menu

![](../images/e8a77eb1fa47d6a2.png)

Terrain Editing - Terrain Entities, Object Entities, Creation Entities.Entity Placement - Object Entities, Creation Entities.Prefab Library - Object Prefabs, Creation Prefabs.Miliastra Sandbox - Server Node Graph, Composite Nodes.

### (2) Right-click in Assets Bar

![](../images/5d927c256aa4e673.png)

Prefab Library - Object Prefabs, Creation Prefabs.Combat Presets - Skills, Status, Items

## 2. Function Logic

Generate an archive file (.gia) from the selected content.

## 3. Export Related Items

When exporting prefabsMounted Node Graphs are exported synchronously with the fileWhen exporting entitiesAssociated prefabs (if any) and mounted node graphs are exported synchronously

## 4. Action Flow

Select the content you want to export, then click Assets Exporting.

![](../images/62d1f5cc8102a011.png)

Choose a local folder for export and enter a file name.

![](../images/ca3bfe6348637a4c.png)

Wait for the file to be generated.

![](../images/d62648af371af0ff.png)

When the export finishes, the archive file is created at the chosen file path.

# III. Export Method 2 - Multi-Select Export in Stage

## **1. Entry Point**

![](../images/70be673147453a4c.png)

Terrain Editing - Terrain Entities, Object Entities, Creation Entities.Entity Placement - Object Entities, Creation Entities.Prefab Library - Object Prefabs, Creation Prefabs.

## **2. Function Logic**

When exporting multiple selections, they are exported as a combined asset into a single (.gia) file. After loading external assets, the package appears as a combined package on the [Import and Transfer] interface.

![](../images/ca65b0ffcde1c49c.png)

After transferring assets, the combined asset appears in the [Import Asset] section of the Assets Bar and is available for use.

## **3. Action Flow**

Its behavior is consistent with single-selection export in the stage

## **4. Export Related Items**

When exporting prefabsMounted Node Graphs are exported synchronously with the file.When exporting entitiesAssociated prefabs (if any) and mounted node graphs are exported synchronously.

# IV. Export Method 3 - UI Single/Multiple Selection Export

## **1. Entry Point**

System Menu - Asset Import/Export Tool

![](../images/9807f7319485ca7e.png)

## **2. Main Interface**

![](../images/2a9f0a58427d1522.png)

## **3. Function Logic**

This feature lets you quickly select and export multiple assets. You can choose from any asset type that supports individual export. Logic matches in-stage selection: when exporting multiple assets, they are combined into a single (.gia) file and remain usable as a combined asset unit thereafter.

![](../images/ca65b0ffcde1c49c.png)

## **4. Action Flow**

Click to select/deselect the assets you want to export.

![](../images/b8f1f6eb22b7923a.png)

Click the button to open the [Selected Content Management] panel.

![](../images/ed12ce0df8e3ba88.png)

After completing content selection, click the Export Assets button.

![](../images/7caf370cdbf6fb5c.png)

Review the prompt, then click Confirm.

![](../images/a95144a802780724.png)

Choose a local folder for export and enter a file name.

![](../images/ca3bfe6348637a4c.png)

Wait for the file to be generated.

![](../images/d3d40e0c2ade6b61.png)

# V. Local Asset Import/Loading Process

## 1. Entry Point

System Menu - Asset Import/Export Tool

![](../images/9807f7319485ca7e.png)

## 2. Function Logic

Load save files from the specified local folder into the Asset Library tab in Miliastra Sandbox for use during creation.

Each time local assets are imported, all content in the Asset Library tabs in Miliastra Sandbox is cleared and replaced with the newly imported content.

## 3. Auto Import

When opening the Miliastra Sandbox for the first time during an app session (resets after closing), local files are automatically loaded.

## 4. Action Flow

Switch to the Import and Transfer tab.Click Load External Assets in the bottom-right corner.In the prompt, click Load External Assets.

![](../images/2d32f7f487791674.png)

Wait for external assets to finish loading.

![](../images/a7016da3d95676d4.png)

A white text prompt will appear, indicating that all files were added successfully.

![](../images/507b0193846eadb1.png)

## 5. View Assets

![](../images/4a13604eb1faf5bf.png)

Creators (Craftspeople) can right-click an asset bundle to view all assets inside it.

![](../images/2a5c5c5622430177.png)

# VI. Asset Usage Process

## 1. Entry Point

Asset Types - Assets Bar - Asset LibraryNode Graph Manager/Node Explorer - Folders - Node Graph External Assets/Node External Assets

## 2. Function Logic

Prefab Asset Usage - Add Prefab assets to the specified Custom Assets Bar tab.Entity Asset Usage - Add entity assets to the stage.

## 3. Import Related Items

When using assets, related node graphs and prefabs are synchronously added to the default categorized tab or the Import Asset tab.

## 4. Action Flow

Left-click or select Transfer Assets from the right-click menu.

![](../images/d8ec188cdccfd0c8.png)

A tab selection confirmation pop-up appears.

![](../images/203473150ace7f40.png)

A white text prompt will appear, indicating the asset was used successfully.

# VII. Asset Usage Method - Combined Content

## **1. Entry Point**

Combined content appears simultaneously in the Assets Bar of all asset types contained within the [Combined Assets].

![](../images/6c0298d54dc956c0.png)

## **2. Function Logic**

When using combined assets, all assets within (e.g., prefabs, entities, and node graphs) are added synchronously.

## **3. Action Flow**

When using combined assets, you can choose to add all assets simultaneously to the [Default Tab] or the [Import Asset] tab. (Note: If the Import Assets tab does not exist, the system will create it automatically.)

![](../images/3f7d34df48532b6a.png)

# VIII. Reference Relationship Recovery

## **1. Function Logic**

When exporting combined assets via [Import/Export Assets - III. Export Method 2](/ys/ugc/tutorial//detail/mhxbd59urbfu#NvCw4TM8-sd3mDnaaUspEK) / [Import/Export Assets - IV. Export Method 3](/ys/ugc/tutorial//detail/mhxbd59urbfu#NcnPkUoM7qQNDjgY8BgnKE) , all reference relationships between assets within the combination are recorded. When the combined assets are used, the relationships formed by GUIDs are preserved via replacement. (That is, as long as the combined assets belong to the same batch, the relative reference relationships between assets remain consistent before import and after use)

## **2. Important Notes**

To ensure correct preservation of reference relationships, assets with references should be exported together as a combined asset before use.
