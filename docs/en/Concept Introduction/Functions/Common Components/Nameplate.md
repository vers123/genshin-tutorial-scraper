---
title: Nameplate
path_id: mh0oh59a6d2i
updated_at: 2026-04-02 17:23:46
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0oh59a6d2i
---

# 1. Functions of Nameplate Component

*Nameplate Components* support displaying visual information for the specified entities during stage runtime, providing specific information such as entity *HP*, *level*, and other details, as well as directional guidance, distance display, and other visual indicators.

## **1. Overview**

The nameplate component needs to be mounted to entities. Supports usage of *characters*, *objects*, and *creations*.

The nameplate component allows multiple nameplates to be active at the same time.

Nameplates can be enabled or disabled via default configuration, or controlled individually through the *node graph*; the visibility of the specific nameplates can also be adjusted using the *local filter*.

## **2. Details**

**The actual nameplate display** includes both the *nameplate* and the *navigation indicator*

**Nameplates**

Can be occluded by the environment

On the same physics layer as the entity

**Navigation Indicator**

Not occluded by the environment

Above Interface Layout layer

# **II. Editing** Nameplate Components

## **1. Add Components**

![](../../../images/32acac8e898bf170.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click **"**Add Components**"** below, select and click "Nameplate" to add it

When the nameplate is selected, the entity being edited will display all currently active nameplates of the nameplate component and their stacking behavior.

(3) Click **"**Advanced Editing**"** to expand the editing tab

## **2. Editing** Nameplate Components

![](../../../images/a765d8929bbe3aba.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Nameplate* | The dropdown menu provides nameplate enumeration  By modifying the checkbox behind, you can change the effective status. After modification, the effective status will be synchronized to the nameplate editing tab  ![](../../../images/c6b65553aff1eda1.png)![](../../../images/2ee78df18da46883.png) |
| *\*Nameplate List* | Enumerates all nameplates configured for the entity |

# **III. Editing** Nameplates

## **1. Adding** Nameplates

![](../../../images/33f878a9928526de.png)

Click ![](../../../images/0b7f16e013763ebc.png)to add a nameplate.

The added nameplate is **initially effective** by default.

Nameplate X, where X is the nameplate ID, can be used as a node input to adjust the initial activation parameters of the nameplate.

## 2. Editing Nameplates

### (1) Select the Nameplate submenu

![](../../../images/96da4c3e57d4fa16.png)

### (2) Basic Settings

![](../../../images/9c3ebadd11e47f37.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Select Attachment Points* | Select the preset *attachment point* of the entity, or a custom creator attachment point.  Can be selected from the dropdown menu. The nameplate position will be adjusted based on this point as its base location. | |
| *Visible Radius (m)* | The effective range of the nameplate. The nameplate logic will only run when the character and the entity are within this configured distance. | |
| *Filter Node Graph* | Can reference the local filter node graph to determine whether the nameplate is visible on the local client. For the specific distinctions and usage of the two filters, see [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i). | |
| Selection Type: Boolean | When the local filter returns a value of "true", the associated nameplate will be visible to the local client |
| Selection Type: Integer  Effective Integer Range: Configure an integer list as needed | When the local filter returns a value within the effective integer range, the associated nameplate will be visible to the local client |
| Explains the basic nodes in the local filter node graph Get Self Entity Output parameter is the entity with nameplate component mounted Get Self Entity Output parameter is the character entity within effective range of nameplate  Retrieval succeeds only if the character entity is equal to the local client character Get Current Character Output parameter is the local character | |
| *Initially Effective* | Whether to enable simultaneously with object creation  If multiple nameplates are enabled simultaneously, overlapping may occur. | |

### (3) Nameplate Content

The nameplate offers the following independent types of editable content and supports both individual and combined use of these content types, with adjustable position, size, and detailed data for each item.

![](../../../images/48660c7905a69a60.png)

You can add content items to the nameplate with **"Add Content"**.

Use ![](../../../images/04c1cef8268a712b.png)to adjust the visibility of the specified items in the edit mode.

Use ![](../../../images/c45f140af47eb611.png) to copy, paste, delete and perform other operations on the selected items.

#### **a. Text Box**

![](../../../images/39f3183677516d03.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings |
| *Size* | Adjust the size of text box |
| *Background Color* | ![](../../../images/445e2401aa7c2624.png)  Supports setting a transparent or black semi-transparent background color |
| *Font Size* | Font size configuration |
| *Text Content* | Display text editing  Supports adjusting the alignment of the text content  Supports **variable insertion**. Selecting a custom variable for the specified entity will update it in real time within the text box  ![](../../../images/456ce205ec4def5d.png)  If the configured text content exceeds text box range, it will not be displayed  Insert the referenced custom variables in rich text format, using the following format:  **{Type:Prefix.VariableName}**  Type:  1: When referencing a custom variable of the entity itself.  2: When referencing an attribute of the entity.    Prefix:  s: When the billboard is attached to a non-character/player entity.  a: When the billboard is attached to a character entity.  p: When the billboard is attached to a player entity.    Variable Name:  When referencing a custom variable, use the name of the custom variable you want to reference.  When referencing an entity's attribute, use the following variable names:  Current HP: HpCur  Maximum HP: HpMax  Current ATK: AtkCur  Current DEF: DefCur  Current Level: LvCur  Player Nickname: PName  Distance to Player: PDist |

#### **b. Icons**

![](../../../images/8e8ce46f8cf4c3a0.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings | |
| *Size* | Adjust the size of the icon | |
| *Icon Type* | Custom Icon | Icon must be additionally selected for usage  ![](../../../images/baa52f1f78ee0aeb.png) |
| Use Faction Icon | Repeated icon selection unnecessary. The entity's Faction Icon will be read and applied accordingly |

#### **c. Progress Bar**

![](../../../images/7b42a8b21334483b.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings | |
| *Shape* | Horizontal | ![](../../../images/156f70c5fe78a3ee.png)  Supports setting width and height |
| Vertical | ![](../../../images/8076dcfbac27a9c5.png)  Supports width and height configuration |
| Ring | ![](../../../images/f1791eb34e4eda2a.png)  Supports diameter configuration |
| *Size* | Progress bar size adjustment | |
| *Progress Bar Style* | Percentage | Displays progress as a percentage based on 1:1 scale, with integer precision  ![](../../../images/2a28ae1c824377c7.png) |
| Do Not Show | Hide progress hint text  ![](../../../images/06eaad4e74b6cc35.png) |
| Current Value | Display current value in real-time  ![](../../../images/15ada4a519bbf571.png) |
| 1:1 Scale | Display actual ratio in real-time  ![](../../../images/ebe2eef20ec412a3.png) |
| *Color* | Can be selected from preset colors | |
| *Current Progress Value* | ![](../../../images/70f05e3dac53f6a4.png)  Supports selection of custom variables for the mounted entities and stages | |
| *Minimum Value* | Supports selection of custom variables for the mounted entities and stages | |
| *Maximum Value* | Supports selection of custom variables for the mounted entities and stages | |
| *Progress Bar Smooth Transition* | When enabled, the progress value change will be animated over the transition duration. | |
| *Transition Duration (s)* | When the current progress value changes, the visual transition will be complete within the configured time. | |

#### **d. Timer**

![](../../../images/a2293ccb3b2c0391.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings |
| *Type* | Stopwatch, Countdown |
| *Specify Timer* | Enumerates all predefined global timers that match the specified type |

#### **e. HP and Shield**

![](../../../images/a0ccb419e0dc603a.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings | |
| *Size* | Adjust HP bar size | |
| *HP Display Style* | Do Not Show | Hide HP bar |
| Progress Bar | ![](../../../images/06eaad4e74b6cc35.png) |
|  | Progress Bar + Value | ![](../../../images/ebe2eef20ec412a3.png)  Value is precise to two decimal places |
| *HP Color* | ![](../../../images/1895b367f197e63c.png)  The progress bar will display with the color configured in the settings. | |
| *Shield Display* | Do Not Show | Only show HP bar |
|  | Display Separately | ![](../../../images/4f5f8d3534bbb400.png)![](../../../images/095f532d5fc7af84.png)  If the shield is configured to display separately, the shield bar control will appear below the health bar. |
|  | Mixed Display | ![](../../../images/233dced2387d5f9e.png)![](../../../images/e33cd48ee353f6d5.png)  If configured for mixed display, the progress bar will show both the HP value and the shield value simultaneously, with the shield value displayed to the right and the HP value to the left, according to the deduction priority. |
| Show Shield Display Maximum Value |  | If checked, when the shield value exceeds the configured maximum, the shield bar will always display as full. |
| Shield Display Maximum Value |  | This configuration is only available when **Show Shield Display Maximum Value** is checked.  The shield display maximum value will be adjusted to the configured limit value. Any shield value exceeding this limit will continue to display as full.  The shield bar will show the deduction only when the shield value is less than the configured limit value. |

#### **f. Interrupt Intake Value**

![](../../../images/757149d54de06173.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Offset* | Offset can be adjusted relative to the attachment point selected in Basic Settings |
| *Size* | Adjust the size of the Interruption Gauge |
| *Interrupt Intake Value Calculation* | Can be increased or decreased |
| *Interrupt Intake Color* | Can select from preset colors |

## 3. Editing Navigation Indicators

### (1) Select the Navigation Indicator submenu

![](../../../images/2c92f00c9c865539.png)

### (2) Basic Settings

![](../../../images/36aed074197d6355.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Offset* | Adjustable offset based on the attachment point selected in basic settings |
| *Maximum Visible Radius (m)* | Maximum effective range of indicator |
| *Minimum Visible Radius (m)* | Minimum effective range of indicator |
| *Hide Indicators When Nameplate Is Displayed* | When enabled, the indicator will not be displayed when the nameplate is in effect, allowing for a smooth transition between nameplate and indicator display. |

### (3) Navigation Indicator Content

The navigation indicator provides two independent types of editable content, which can be used separately or in combination. Each type supports adjustments to position, size, and detailed data.

Use **Add Content**![](../../../images/2aeee1956c150083.png) to add items to the navigation indicator.

Use ![](../../../images/04c1cef8268a712b.png)to adjust the visibility of the specified items in the edit mode.

Use ![](../../../images/c45f140af47eb611.png) to copy, paste, delete and perform other operations on the selected items.

#### **a. Text Box**

![](../../../images/2cba04164675e38e.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Size* | Adjust the size of text box |
| *Background Color* | ![](../../../images/88477476233cf9b4.png)  Supports setting a transparent or black semi-transparent background color |
| *Font Size* | Font size configuration |
| *Text Content* | Display text editing  Supports **variable insertion**, select custom variables for the specified entities, which will update in real-time in the text box  Supports adjusting text alignment effects  If the configured text content exceeds the text box range, it will not be displayed |

#### **b. Icons**

![](../../../images/89222b7ee13901b1.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Size* | Adjust the size of the icon | |
| *Icon Type* | Custom Icon | Icon must be additionally selected for usage  ![](../../../images/ba8a84e094ccc28c.png) |
| Use Faction Icon | Repeated icon selection unnecessary. The entity's Faction Icon will be read and applied accordingly |

# **IV. Managing Nameplates Through Node Graph**

During entity runtime, its active nameplates can be managed through the node graph

**Set Entity Active Nameplate**

The Nameplate Config ID List entered through the node will completely override the target entity's active nameplate

![](../../../images/4cf03578e7f193ab.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Target Entity* | Entity | Runtime entity |
| *Nameplate Config ID List* | Configuration ID List |  |
