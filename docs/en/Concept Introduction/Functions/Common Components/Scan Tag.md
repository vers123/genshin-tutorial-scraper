---
title: Scan Tag
path_id: mhrvf1ioor1w
updated_at: 2025-10-21 22:53:01
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhrvf1ioor1w
---

# I. What is the Scan Function

The scan function allows players to select an entity during gameplay by using the camera.

The scanned target can be configured to display special effects, such as unique icons or special effects.

In skill usage logic, scanned targets can also be retrieved via nodes from the relevant node graph, allowing selection of specific skill targets.

Whether an entity can be scanned and its status display after being scanned can be defined through *scan tags* and implemented through *scan components* to assign logic to prefabs and entities.

# II. Editing Scan Tags

A *scan tag* defines the filtering logic and display settings for a scannable object. It must be defined globally in advance. Access the scan tag definition interface via "Scan Tag Management" in the system menu

![](../../../images/aaefedb02c243b3f.png)

After entering the Scan Tag Definition interface, the editing interface will be divided into three main sections:

1. Scan Tag List

2. Scan Tag Effect Preview

3. Scan Tag Logic Configuration

![](../../../images/c45733fb991d7ba9.png)

## 1. Scan Tag List

All defined scan tags can be found in this interface, making it convenient for creators (Craftspeople) to filter and search globally

![](../../../images/fd69a72da61efdf7.png)

Click the "Create New Scan Tag Template" button to add a new scan tag

![](../../../images/691de3542ec4623e.png)

## 2. Scan Tag Logic Configuration

The configuration section determines the rules by which prefabs and entities with this tag will be scanned during gameplay, and their behaviors when scanned. It is divided into two tabs: "Status Performance" and "Effective Conditions"

### (1) Basic Definition

![](../../../images/db8efa9d970c4fa6.png)

*Scan Tag Name*: The name of the scan tag, used for identification only

*Configuration ID*: Data type serves as the configuration ID, which is the unique identifier of this scan tag, used to index this scan tag within the node graph

### (2) Status Performance

![](../../../images/52452871725d179c.png)

*Icon Settings*: When a prefab or entity with this scan tag is selected by the scan logic, a hint icon will appear. This section configures the related display properties of that icon

*Select Icon*: Configure an icon resource group corresponding to different selection states. This field can be left empty, in which case no icon will be displayed. Up to two icons can appear on-screen simultaneously

*Attachment Point*: The icon is displayed at the attachment point of the corresponding entity's name

*Offset*: The offset position of the icon

*Selection State*: For a scannable entity, there are three selection states. The icon display differs for each state

*Active State*: The state when currently selected by the scan function. Only one entity can be in the active state at any given moment

*Available State*: The state when active state conditions are met but not yet activated, usually due to the existence of other higher-priority targets that are already active

*Disabled State*: The state when effective conditions are not yet met

The corresponding runtime behavior is illustrated in the graph below:

![](../../../images/fee33a86bbc6a767.png)![](../../../images/74f095e211df96b8.png)![](../../../images/c98ff3bf75d5eb51.png)

**Special Effects Settings**

![](../../../images/3bdae5ef31eca001.png)

*Activated Status Effects*: Effect configuration that will be applied when an entity carrying the scan tag component is in the active state

*VFX Assets*: Creators (Craftspeople) can select a suitable special effect asset here to apply as the effect

*Attachment Point*: The effect is applied at the corresponding unit's attachment point and automatically follows its position and rotation

*Zoom Factor*: The actual scale at which the effect asset is played

*Offset*: Additional offset based on the above attachment point position

*Rotation*: Additional rotation applied relative to the attachment point above

![](../../../images/e35ddc0500dd15ee.png)

*Available Status Effects*: Effect setting that will be applied when an entity carrying the scan component is in the available state

The configurable parameters are consistent with the activated status effects

![](../../../images/17f8e479d1d3d06a.png)

*Disable Status Effects*: Effect configuration that will be applied when an entity carrying the scan component is in a disabled state

The configurable parameters are consistent with the activated status effects

### (3) Effective Conditions

The effective conditions describe the conditions which must be met to put a scannable entity into the available state

![](../../../images/3938dc65bb303f15.png)

*Local Filter*: Boolean filter and integer filter can be selected

*Filter Node Graph:*:Can be associated with a local filter node graph of the selected type. If the return value of the local filter does not meet the conditions, the entity will not participate in the state calculation and will be considered as a non-scannable object.

![](../../../images/61e731c74df225c9.png)

*Obstacle Detection*: Obstacle detection is used to verify line-of-sight between the local-controlled character and scanned entities. It determines whether there are obstructions between the character and the scanned object. When enabled, if the ray detection fails, the entity will be disabled.

*Obstacle Detection Point*: The name of the unit attachment point on the scanned object. This serves as the target point for ray detection

*Ignore Water Surface*: When enabled, if a water surface collider is detected between the player and entity, it will be ignored and treated as if there is no obstruction

![](../../../images/b71158d38617680c.png)

*Distance Detection*: Used to define the available range of a scannable entity. This determines the distance within which the scannable object and local character are available

*Distance Detection Point*: Distance detection evaluation is based on the position of the configured unit attachment point

*Detection Range*: If the scanned entity is not within the configured range, it will be disabled. The range can be previewed directly in the scene

![](../../../images/a1e04e246387e6e0.png)

![](../../../images/3e791cb6887b68dc.png)

*Line of Sight Detection*: Line of sight detection is used to determine whether there are any obstacles between the local camera and the scanned object. When enabled, if the ray detection fails, the entity will be disabled.

*Line of Sight Detection Point*: The unit attachment point on the scanned object used as the target for ray detection

*Ignore Water Surface*: When enabled, if a water surface is detected between the local camera and entity, it will be ignored and treated as if there is no obstruction

*Ignore Obstacles*: When enabled, line of sight detection ignores all obstacles

![](../../../images/68275041b1715a3d.png)

*FOV Range Settings*: Requires that the scanned entity must be within an elliptical area at the center of the screen, otherwise the entity will be disabled

*FOV Detection Point*: Detection is based on the unit attachment point position as set on the entity

*Ellipse Horizontal Axis Ratio*: The ratio of the ellipse's left and right borders relative to the screen width

*Ellipse Vertical Axis Ratio*: The ratio of the ellipse's top and bottom borders to the screen height

Click "Preview FOV" below to visually preview the effective range, as shown in the following graph:

![](../../../images/6af152b940d338eb.png)

# III. Editing Scan Tag Components

## **1. Adding** Components

![](../../../images/ac58d4915a99883c.png)

(1) In the Entity or Prefab editing interface, open the Component Editing Tab

(2) Click "Add Components" below, then select and click "Scan Tag" to add it

## **2.** Scan Tag Component Settings

The scan tag component can be configured with multiple alternative scan tag templates, but only one scan tag can take effect during gameplay. This can be dynamically switched using node graphs

![](../../../images/2b3b869b1af446fd.png)

*Initially Effective*: Default active scan tag

*Scan Tag List*: All scan tags contained in this component

Click Advanced Editing to enter the editing interface

![](../../../images/b86f9128be95b38b.png)

In this interface, click the Add button to add a new scan tag and set its scan tag template reference

*Scan Tag ID*: Used as an identifier when switching node graphs dynamically

*Initially Effective*: Determines whether the scan tag is active initially. Only one scan tag can be active at a time

*Reference Scan Tag*: Select and reference pre-defined global scan tags

# IV. Scan Tag Filtering Logic

The previous section on Scan Tag Logic Configuration introduced under what conditions a single scan object would be considered available. When multiple available scan objects are present simultaneously, only one scan object will be set to the active state. The filtering rules are defined by the class attribute "Scan Tag Recognition Rules"

For more class information, please check [Classes](/ys/ugc/tutorial//detail/mhodlcrpht3q)

![](../../../images/57670a77938f03e0.png)

*Scan Tag Recognition Rules*: Rules for filtering active units from all available Scanned Objects

*Distance From Center of FOV*: Scan tags closest to the center of the view are prioritized for activation

*Actual Position Distance*: Gives priority to activating scan tags nearest to the player character

# V. Scan Tag Node Graph Nodes

## Server Nodes

Set Scan Tag Rules

![](../../../images/bd06412a7306a689.png)

Set Scan Component's Active Scan Tag ID

![](../../../images/752c9de686409044.png)

Get Current Active Scan Tag Config ID

![](../../../images/d58af37937502ce8.png)

## Client Node

Get All Valid Entities That Are Scannable by Scan Component

![](../../../images/cb2eef244773e9ad.png)

Get Entity Currently Scanned by Scan Component

![](../../../images/636d88fdc0cbfc2f.png)

Get Entity's Current Active Scan Tags

![](../../../images/7d069ba63a2be42d.png)

Get Entity's Scan Status

![](../../../images/021eb8a61906cc90.png)
