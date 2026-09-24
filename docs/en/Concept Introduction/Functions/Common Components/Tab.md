---
title: Tab
path_id: mhr3ngi2n74c
updated_at: 2025-10-16 17:01:07
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhr3ngi2n74c
---

# 1. Tab Component Functions

The Tab component enables players to configure and interact with dynamic objects and creations

After adding this component to an entity, it supports configuring and applying multiple tabs simultaneously

Each tab supports using a local filter to determine visibility for each player

The entity type that triggers the tab function is *Character*

# II. Editing Tab Components

## 1. Add Components

![](../../../images/9b4d68db396318c0.png)

(1) In the entity/prefab editing interface, open the Editing Components tab (A)

(2) Click "Add Common Components" below, select and click "Tab" to add (B), (C) successfully

When "Tab" is selected, the entity being edited will display the tab trigger area with a blue border

(3) Click "Advanced Editing" to expand the editing tab (D)

## 2. Editing Tabs

![](../../../images/20d4116506fb08e2.png)

### (1) Basic Tab Information

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Tab* | The dropdown menu provides tab enumeration  By modifying the checkbox behind, you can change the effective status. After modification, the effective status will be synchronized to the tab editing page  ![](../../../images/8b8dfff7bfef9751.png) |
| *\*Tab List* | Enumerate all tabs of entity configuration. |

Click to![](../../../images/046321f47bf5d9c3.png)![](../../../images/45aed179e22dfda9.png)toggle the visibility status of a tab in the editing window. Effective only during editing

![](../../../images/87bc4ee54eb42991.png)

Click "Advanced Editing" to enter the tab list and trigger area configuration interface

### (2) Tab List

![](../../../images/8683cc9632abf599.png)

Add New Tabs

![](../../../images/1846e59225f63cbf.png)

Click "Add Tabs" to create a new tab

Editing Tabs

![](../../../images/b03316e81c3f422c.png)

*Option ID* *ID**X*. Can be used for node graph input parameter to adjust whether tab is in effect

*Option Tab Icon* Click![](../../../images/3e0b8c52942a5102.png) to switch the icon in front of the tab.

![](../../../images/a8a9a8d6e225b72b.png)

*Initially Effective* If enabled, this option tab takes effect immediately upon entity creation. An effective tab is visible and can be selected for operation

*Sort Level* Controls the display order of option tabs. The higher the number, the further forward it appears

![](../../../images/096f07d0311b5033.png)

*Local Filter* There are two types of filters: Boolean filters and integer filters. See [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i) for details.

Filter Node Graph You can refer to the filter node diagram of the above selection types to determine whether the tab meets the display conditions.

The following is an example using a Boolean filter:

![](../../../images/b8c75d3b6187ad9c.png)

![](../../../images/7a697daa5c852553.png)![](../../../images/b1438cbf01602a9f.png)

The local filter continuously monitors while the character is within the effective range. If the result changes, it updates the display immediately.

Explains the basic nodes in the local filter node graph

Get self entity

The output parameter is the entity where the tab component is mounted

Get target entity

When the character is within range, this node outputs parameters for the character entity that is effective within the tab range

Get Current Character

Output parameter is the local character

Example

![](../../../images/cecae7f94461a3e0.png)

### (3) Trigger Option Area

![](../../../images/861a09b756d3dcd9.png)

Add Trigger Areas

![](../../../images/7a15c7e1142069c4.png)

Press the "Add Trigger Option Area" button to create a new trigger area

Trigger Areas

![](../../../images/3a7f0f5d5dedb737.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Trigger Area Shape* | Supports cuboid, sphere, and capsule shapes. Different size configuration parameters will be displayed based on the selected shape |
| *Center* | Offset relative to the entity/prefab center |
| *Rotation* | Supports orientation adjustment along different axes based on the center position |
| *Zoom Multiplier* | The trigger area's shape supports defining scaling along different axes |

# III. Manage Tabs Through Node Graph

Activate/Disable Tab

Enter the Tab ID to control whether the tab is enabled or not

![](../../../images/cbb29aa5cc9cf62c.png)

When the tab is selected

When the active tab is selected, it will send an event to the node graph

The entity node graph configured by the tab component will receive this event

![](../../../images/1fd1251ad0c462af.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Event Source Entity* | The entity where the tab component is mounted |
| *Event Source GUID* | The entity with mounted tab components, outputs 0 if none exists |
| *Tab ID* | Tab ID  ![](../../../images/e0394c5178631df4.png) |
| *Selector Entity* | Character entity that triggers tab |
