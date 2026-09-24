---
title: Copy and Paste Data
path_id: mhhtxlr3xgce
updated_at: 2025-10-16 11:48:13
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhhtxlr3xgce
---

# 1. Feature Overview

This function is used to copy data from the specified content and stores it in an independent clipboard (storing only one copy at maximum), which can then be used to paste and replace data in target content. After data replacement, the ID remains unchanged, not affecting node graph references, only replacing the functional data.

# II. Usage Restrictions

## 1. Asset Types

Only applicable to objects and creations.

## 2. Use Units

Prefab data can only be pasted onto prefabs.

Entity data can only be pasted onto entities.

# III. Copy and Paste Prefab Data

## 1. Entry Points

Right-click the menu in the Prefab Library scene

![](../../../images/96fc8645cda3e6d0.png)

Right-click the menu in the assets bar

![](../../../images/70e9a7f0cb2fcf0c.png)

Left-click the menu in the details bar

![](../../../images/210ab9d9818158ea.png)

## 2. Functional Logic

Copy prefab data to the clipboard, which can then be pasted to other prefabs of the same type to replace data of the target and associated entities.

## 3. Data Replacement

All data except name, prefab ID (identifier), and parent tab.All data of the affiliated entities.

## 4. Operation Process

Select the prefab you want to copy, and click "Copy Prefab Data".Select the prefab where you want to paste, click "Paste Prefab Data" to complete the replacement.

![](../../../images/a9cb3051815b4b16.png)

# IV. Entity Data Copy and Paste

## 1. Entry Points

Right-click the menu in the entity placement/prefab library scene

![](../../../images/e4f5e940fcbd4a8f.png)

Left-click the menu in the details bar

![](../../../images/a36deb2bea895483.png)

## 2. Functional Logic

Copy entity data to the clipboard and paste it to other entities of the same type to replace their data.

## 3. Data Replacement

All data except name, GUID (identifier), and parent tab.

## 4. Operation Process

Select the entity you want to copy, then click "Copy Entity Data".Select the entity you want to paste, click to paste the entity data, and the replacement is complete.

![](../../../images/bf6238a628010fae.png)
