---
title: Mini-Map Marker
path_id: mhiwt0rysfg6
updated_at: 2025-10-21 23:44:07
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhiwt0rysfg6
---

# I. Mini-Map Marker Component Functions

The *Mini-Map Marker Component* supports displaying entities on the **prefabricated Mini-Map UI Controls** through visual indicators such as icons/ranges

The Mini-Map Marker Component needs to be mounted on entities; it supports *players*, *objects*, and *creations*

Mini-Map Markers can be enabled/disabled through their default settings, or be controlled through *node graphs*

# **II.** **Editing** Mini-Map Marker Components

## **1. Adding** Components

![](../../../images/aff73554b6ee7018.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Components" below, then select and click "Mini-map Marker" to add it

(3) Click "Advanced Editing" to expand the Editing Tab

## **2.** Basic Information of Mini-Map Marker **Components**

![](../../../images/2f20fba650694875.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | The drop-down menu provides a list of mini-map markers  Use the check box to toggle the marker's active state. Changes will be synchronized to the marker's Advanced Editing tab  ![](../../../images/c5db8213d4dcd210.png)![](../../../images/c4ee12b0d45e8181.png) |
| *\*Mini-Map Marker List* | Enumerates all mini-map markers for entity configuration |

## 3. **Add Mini-Map Markers**

Click "Advanced Editing" to edit the Mini-Map Marker

![](../../../images/b5008d0a9c2eee0b.png)

Click ![](../../../images/39eb982686c863ef.png) to add mini-map markers.

The added mini-map marker is **initially effective** by default.

*Marker X*, where X is an ID, can be used as a node input to adjust the initial activation parameters of the mini-map marker.

## 4. Mini-Map Marker Parameter Descriptions

### (1) Display Settings

![](../../../images/14733e105db31dc6.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Initially Visible to All Players* | When enabled, the marker will be visible on the mini-map of all eligible players once it becomes active | |
| *Follow Object Visibility* | If enabled, when the entity is hidden, the mini-map marker will be hidden as well | |
| *Display Priority* | When Mini-Map Markers overlap at the same location, the marker with the higher priority will appear on top. A larger number indicates a higher priority | |

### (2) Marker Style

![](../../../images/9308ca2b179c26e6.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Select Type* | It is divided into several types: icon, range, marker, player's marker, and creation icon. Each type will have different configuration parameters. |
| *Show Height Difference* | When enabled, entities with height differences exceeding 10m will be marked on the mini-map as well |

### (3) Classification of Selection Types

Icons

![](../../../images/e3dc1e42ade2ff64.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Selec Icon* | ![](../../../images/632bdb059fea22fd.png)  Offers a variety of icons to choose from |
| *Background* | ![](../../../images/f974e67d66c3a619.png)  Options: None, Circle |
| *Background Border Color* | ![](../../../images/601c811cb365230e.png)  Icon background color supports specific colors as well as logic-driven colors  Logic-driven colors include  [Hostility] Enemies in red, friends in green, and self in blue  [Follow Own Faction] Based on the current faction's colors  [Follow Owner's Faction] Based on the current entity owner's faction colors |
| *Clickable* | When enabled, open the map and click on the marker to display its settings information |
| *Text Content* | ![](../../../images/dbfee5cce2957991.png)  Click to set the text on the right |

AoE

![](../../../images/8d650b9872abd8f3.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Area Style* | ![](../../../images/831d22351ab4b8f2.png)  Area's border can be displayed as a solid line or a dotted line |
| *Color* | ![](../../../images/f401c8c432069acf.png)  Icon background color supports specific colors as well as logic-driven colors  Logic-driven colors include:  [Hostility] Enemies in red, friends in green, and self in blue  [Follow Own Faction] Based on the current faction's colors  [Follow Owner's Faction] Based on the current entity owner's faction colors |
| *Area Size (m)* | Displays proportionally in the Mini-Map UI Controls according to the configured dimensions |

Marker

![](../../../images/7c24154a5b29bf6a.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Style Preview* | Displays the point style which cannot be modified. Points are not clickable on the world map |
| *Color* | ![](../../../images/f401c8c432069acf.png)  Icon background color supports specific colors as well as logic-driven colors  Logic-driven colors include:  [Hostility] Enemies in red, friends in green, and self in blue  [Follow Own Faction] Based on the current faction's colors  [Follow Owner's Faction] Based on the current entity owner's faction colors |

Player's Marker

![](../../../images/07529641dca17ce4.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Style Preview* | The preview icon shows the creator's (Craftsperson's) current icon. This icon needs to be passed through nodes. Player markers cannot be clicked on the world map |
| *Background Border Color* | ![](../../../images/a2a313cf6b166bcd.png)  Icon background color supports specific colors and logic-driven colors  Logic-driven colors include:  [Hostility] Enemies in red, friends in green, and self in blue  [Follow Own Faction] Based on the current faction's colors  [Follow Owner's Faction] Based on the current entity owner's faction colors |

Creation Icon

![](../../../images/c61b88628e3996e4.png)

|  |  |
| --- | --- |
| *Icon Preview* | This can only be set for creations. Preview only, not editable |
| *Background Border Color* | ![](../../../images/f401c8c432069acf.png)  Icon background color supports specific colors and logic-driven colors  Logic-driven colors include:  [Hostility] Enemies in red, friends in green, and self in blue  [Follow Own Faction] Based on the current faction's colors |
| *Clickable* | When enabled, open the map and click on the marker to display its settings information |
| *Marker Name* | Name of the marker |
| *Text Content* | Click to set the text on the right |

# **III. Managing Mini-Map Markers Through Node Graphs**

**Modify Mini-Map Marker Activation Status**

Batch modify the Mini-Map Marker states of target entities through the input list of mini-map marker IDs.

![](../../../images/41e029a531a402f0.png)

**Modify Player List for Visible Mini-Map Markers**

![](../../../images/f4a1ca61f314303b.png)

**Modify Player Markers on the Mini-Map**

![](../../../images/1afb207ad96f4049.png)

**Modify Mini-Map Zoom**

![](../../../images/0c6539521e7861e5.png)

**Modify Player List for Tracking Mini-Map Markers**

![](../../../images/7a9c0c12238ffd5d.png)

**Query Specified Mini-Map Marker Information**

![](../../../images/a0dd68c70b562ac7.png)

**Get Entity's Mini-Map Marker Status**

![](../../../images/09c791b9b2b3c64d.png)
