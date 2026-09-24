---
title: Prefab Group
path_id: mhrb64ieebm4
updated_at: 2025-10-20 11:27:39
category: Concept Introduction/Other Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhrb64ieebm4
---

# I. Functions of Prefab Groups

Prefab Groups can reference multiple Prefabs, including each Prefab's Location and Rotation (relative to the group center).

Prefab Groups can be created directly, or via the Node Graph during Stage runtime; this is equivalent to creating multiple Prefabs simultaneously.

Prefab Groups make Entity placement more convenient; when you edit the group's location, all Prefabs inside move accordingly

# II. Prefab Group Editing

## 1. Prefab Library Editing

In the Prefab Library, select multiple Prefabs and right-click to create a Prefab Group (or merge Prefab Groups). The group's center Location is calculated automatically.

![](../../images/fbef1908aa591cdc.png)

![](../../images/855fbcefe4ba2e7c.png)

## 2. Entity Placement Scene Editing

In the placement Scene, select multiple placed Entities, then right-click to create a Prefab Group (or merge Prefab Groups). The group's center Location is calculated automatically.

![](../../images/ef1e5e124289ede2.png)

# III. Edit Prefab Group Information

After selecting a Prefab Group, adjust each Prefab's Location and Rotation relative to the group's center

As shown in the figure, this is a Prefab Group containing two Prefabs

![](../../images/4850b619cf405cce.png)

# IV. Creating Prefab Groups with the Node Graph

Creating a Prefab Group directly via nodes is equivalent to creating each Prefab separately.

![](../../images/ebc4f18318108590.png)
