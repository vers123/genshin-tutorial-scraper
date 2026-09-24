---
title: Preset Points
path_id: mhsn6miaqazg
updated_at: 2025-10-21 23:04:22
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhsn6miaqazg
---

# I. What is a Preset Point?

A Preset Point is a data record of location and orientation within a Scene.

Preset Points can be referenced by features that require points data, such as Spawn Points, Revive Points, and Node Graph retrieval points.

# II. Editing Preset Points

## 1. Entry Point for Editing

![](../../images/edf86c251dc459f8.png)

## **2. Overall Editing Interface**

![](../../images/be77d0452727e6a5.png)

### (1) Preset Point Library

![](../../images/d1135a91d7e5e924.png)

All Preset Points are listed in this window.

![](../../images/155ec730fcfaffcc.png)Manage the visibility of the corresponding Preset Point in the Layout Scene

### **(2) Preset Point Visibility** in the Edit Window

![](../../images/92ccd1df30a026d3.png)

*Persistent Display Toggle On* Even if the Preset Point management tool is disabled, all Preset Points remain visible in the Edit Window

*Persistent Display Toggle Off*If the Preset Point management tool is disabled, all Preset Points become invisible

### **(3) Create Preset** Point

![](../../images/76684ad7da69f97d.png)

By clicking "Create Preset Point", a new Preset Point is generated at the center of the current Edit Window, with naming editing mode enabled automatically.

### **(4) Preset Point Parameters**

![](../../images/abbb28ae8e84a82b.png)

*Preset Point Name*The name of the Preset Point, which can be modified

*Preset Point Index* Used as an input parameter for Nodes and serves as the unique identifier of the Preset Point

![](../../images/834a31862a2e3a5e.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Lock Transform* | When checked, the Preset Point's position and rotation cannot be adjusted |
| *Display in Scene* | When unchecked, only the coordinate axes remain visible, and the Preset Point model will be hidden |
| *Location* | The Location data of the Preset Point |
| *Rotation* | The orientation data of the Preset Point |
| *Unit Tags* | Add units tags to preset points. See [Unit Tag](/ys/ugc/tutorial//detail/mhzldmiwdgu4) for more details. |
| *\***Reference Relationship* | ![](../../images/d0fa0e779a432ed5.png) |

# III. Referencing Preset Points

## 1. Spawn Point

In "Stage Settings" — Spawn Point configuration, you can *Select Point* to reference a Preset Point as the Spawn Point

![](../../images/13db684e5d2068a3.png)

## 2. Revive Points

In "Stage Settings" — Revive Point configuration, you can *Select Point* to reference a Preset Point as the Revive Point

![](../../images/6347e7d1bbd9ca98.png)

## 3. Node Graph

**Query Preset Point Position Rotation**

![](../../images/30bea10d3f0306a7.png)

Through the Preset Point Index, you can search for its location and rotation data

Click ![](../../images/2dc4deb92a9c3330.png)to expand all Preset Point enumerations for selection as input parameters

![](../../images/d6a81eec014225f6.png)

**Get Preset Point List by Unit Tag**

![](../../images/53a216495463dbfc.png)
