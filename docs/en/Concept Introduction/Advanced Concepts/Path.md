---
title: Path
path_id: mhavii0zcdd4
updated_at: 2025-10-21 03:09:27
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhavii0zcdd4
---

# I. Path Functions

Path is a feature that combines one or more *waypoints*, which contain only position and rotation information, into a set of path information.

The waypoint information in the path consists of world coordinates and rotation. Its data content will not be adjusted when referenced.

Paths can be referenced by any supported functionality, which currently includes the *Not-in-Battle - Patrol* feature of *creations* and the stage path movement of the basic motion device component.

# II. Path Management Tool Functions

*Paths* are managed uniformly through the Path Management Tool

Add or delete paths and edit the data within them

Manage the tabs that organize paths

# **III. Editing Paths**

## 1. Entry Points

Open the System menu in the top left corner and select *Path Management* to open the Path Management Tool

![](../../images/4541f737050bf807.png)

## 2. Tool Display Interface

Divided into the path management bar and the path configuration bar

![](../../images/2f4a6daa5e1feaf0.png)

### **(1) Path Management Bar**

![](../../images/04c81bb039f13f6a.png)

New Path

Create a new path by ![](../../images/21c35782ce8fd9d3.png) creating a path

Newly created paths are assigned to the *\*Uncategorized tab* by default

It uses the screen center point as the first waypoint of the path

![](../../images/46961f832c886227.png)

![](../../images/10e87146b66594fe.png)

Management Tabs

Select the *\*Uncategorized tab*'s ![](../../images/6ad7c5635cf5401d.png) to add a new tab and name it

![](../../images/077041723c4cda2e.png)

![](../../images/3a71b6015adb338e.png)

New tabs are empty by default. Assign paths to a tab and right-click *\*Change Tab* to adjust tabs where paths are located in for easier management

![](../../images/554f832763351751.png)

![](../../images/ae105dd1cb497848.png)![](../../images/f0fe51953d120597.png)

### **(2) Path Configuration Bar**

![](../../images/4045f049e24b133a.png)

Index and Name

![](../../images/3d07b4bbd69fff39.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *\*Name* | The path name used for identification must be unique and can be modified |
| *Index* | Unique identifier for the path, can be used as a node graph input parameter |

Basic Configuration

![](../../images/d6750cae69386c7a.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *\*Lock Transform* | When enabled, waypoints on this path can only be added or deleted; their information cannot be adjusted |
| *\*Display in Scene* | ![](../../images/52b3328891ea8561.png)  When enabled, all of a path's waypoints and their connection order will be shown in the scene |
| *\*Path Center Point Location* | The center point position of the path. This position maintains a constant relative distance to all waypoints. Therefore, modifying this position will affect the positions of all waypoints on the path |
| *\*Path Center Point Rotation* | The center point rotation of the path. This rotation maintains a constant relative angle to all waypoints. Therefore, modifying this rotation will affect the rotations of all waypoints on the path |

Waypoint List

![](../../images/7bec8013263fdda8.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Location* | Parameters can be manually adjusted to adjust waypoint position |
| *Rotation* | Parameters can be manually adjusted to adjust waypoint rotation |
| *\*Add Waypoint* | Click to create a new waypoint  ![](../../images/20708b19eec8fd02.png) |
| *\*Free Placement* | Clicking clears the interface. Place new waypoints in the scene using the left mouse button  ![](../../images/d0f2aafa8dec2255.png)Use![](../../images/9aa53f1a8cfaec63.png) to end placement |

Click the button on the right side of the waypoint![](../../images/cd689fdc4ad6a12f.png) to expand auxiliary editing

![](../../images/d67f153cd541be58.png)

![](../../images/bdfbe50d4ee888f5.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Tangent pointing to the destination* | Adjust waypoint rotation to point to the next waypoint |
| *Tangent pointing to the starting point* | Adjust waypoint rotation to point to the previous waypoint |
| *Select All Waypoints on Path* | Select all path points on this path. Disabled if no path points exist |
| *Add Waypoint toward the destination* | Adds a new waypoint after the selected point's number.  For example, adding a waypoint after waypoint 2 will create waypoint 3, and the previous waypoint 3 will become waypoint 4 |
| *Add Waypoint toward the starting point* | Adds a waypoint before the current point's number.  For example, when adding a preceding waypoint at waypoint 2, the new waypoint becomes waypoint 2, and the previous waypoint 2 becomes waypoint 3 |
| *Copy* | Copy the waypoint's coordinates and rotation information |
| *Paste* | Paste the copied waypoint's coordinates and rotation information |
| *Delete this waypoint* | Delete the specified waypoint |

Reference Source

![](../../images/9a0235348eea9318.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *\*Creation Reference* | Displays the number of references to this path  Can locate creations that reference this path |
| *\*Object Reference* | Displays the number of references to this path  Can locate objects that reference this path |

# III. Managing Paths Through Node Graphs

**Get Specified Waypoint Info**

![](../../images/5fd0a409c6a8ed43.png)
