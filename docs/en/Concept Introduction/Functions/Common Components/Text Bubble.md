---
title: Text Bubble
path_id: mhrpv4ika1gs
updated_at: 2026-01-06 21:54:41
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhrpv4ika1gs
---

# I. Functions of Text Bubble Component

*Text Bubble Component* provides text bubble functionality mounted on entities. It can reference *custom variable* data to display configured content during stage runtime.

The text bubble component needs to be mounted on entities. Supports usage of *objects* and *creations*.

The Text Bubble component can be configured with multiple text bubbles, but only supports one text bubble being active at a time.

Text bubbles can be enabled or disabled through default configuration, and can also be controlled through *node graphs* to switch specific active text bubbles; additionally, the visibility of specific text bubbles can be adjusted through *local filters*.

# **II. Editing** Text Bubble Components

## **1. Add Components**

![](../../../images/d418f13622d9abe6.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click **Add Components** below, select and click on the text bubble to add it successfully

When the text bubble component is selected, the entity being edited will display the current active text bubble effect.

(3) Click **Advanced Editing** to expand the editing tab

## **2. Editing** Text Bubble Components

![](../../../images/e24bcbbc8a2348d9.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective Text Bubble* | The dropdown menu provides text bubble enumeration  By modifying the checkbox behind, you can change the effective status. After modification, the effective status will be synchronized to the text bubble editing page  ![](../../../images/e27a7f7cc9761edc.png)![](../../../images/bfd9195a8bf39001.png) |
| *\*Text Bubble List* | Enumerates all text bubbles configured for the entity |

# **III. Editing** Text Bubbles

## 1. **Add Text Bubbles**

![](../../../images/abd3eaa0af3afd24.png)

Click ![](../../../images/1e4ddac0933deeac.png)to add a text bubble.

The added text bubble is **initially effective** by default

Bubble X, where X is the bubble **ID**, serves as a node input to adjust the initial activation parameters of the text bubble

## 2. Editing Text Bubbles

### (1) Basic Settings

![](../../../images/4462dd282cc08a46.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Select Attach Point* | Select the preset *attachment point* of the entity, or a custom creator attachment point.  Can be selected from the dropdown menu. The text bubble position will be adjusted based on this point as its base location | |
| *Offset* | Offset can be adjusted relative to the attachment point selected in basic settings | |
| *Font Size* | Font size configuration | |
| *Visible Radius (m)* | The effective distance of text bubbles. The text bubble logic will only run when the character and entity distance meets the configuration | |
| *Filter Node Graph* | Can reference local filter node graph to determine whether text bubbles are visible locally | |
| Selection Type: Boolean | When the local filter returns a value of "true", the text bubble will be visible locally |
| Selection Type: Integer  Effective Integer Range: Configure an integer list as needed | When the local filter returns a value within the effective integer range, the text bubble will be visible to the local client |
| Explains the basic nodes in the local filter node graph Get Self Entity Output parameter is the entity mounted with text bubble component Get Target Entity Output parameter is the character entity within active range of text bubble  Retrieval succeeds only if the character entity is the local character Get Current Character Output parameter is the local character | |
| *Loop Playback* | If enabled, the text bubble will play in a loop; if disabled, it will only play once. | |
| *Send End Event* | When enabled, an event will be sent to the node graph after the last dialogue line is completed  Only the entity node graph with this text bubble component mounted can receive it  When and only when this option is checked, the server will record the completion of bubble events by different characters. If a character re-enters the range or reconnects after a disconnect, the bubble will not be triggered again.  If this option is not checked, the bubble dialogue will be re-triggered when a character re-enters the component's trigger range, and it will also be re-triggered after a disconnect and reconnection. | |

### (2) Editing Text Bubble Text

#### **a. Add Text**

![](../../../images/e5c561e73b52dfb1.png)

By adding text, you can increase the number of configuration entries. The text bubble supports configuring multiple lines of text, which will be played in sequence.

#### **b. Editing Bubble Text**

Use ![](../../../images/8158d7970288103f.png) to copy, paste, delete and perform other operations on the selected items.

![](../../../images/9536a3adf005f74b.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Duration* | Display time for the current bubble text content |
| *Text Content* | Display text editing  Supports **variable insertion**, select custom variables from the specified entity, which will update in real-time in the text box  Text size depends on the font size in basic configuration  The actual size of the bubble adapts according to the text amount and font size |

#### **c. Preview Bubble Text**

Click **Preview** to use the current text bubble as reference (regardless of whether the configuration is initially effective).

In preview, the display will correctly display the text bubble's configured position, font size, duration of each text line, and loop playback setting![](../../../images/988b3e457731293a.png)

# **IV. Managing Text Bubbles Through Node Graph**

During entity runtime, its active text bubbles can be managed through the node graph

**Switch Active Text Bubble**

![](../../../images/066b426877609831.png)

**When Text Bubble Is Completed**

![](../../../images/8af8c27f14423c55.png)
