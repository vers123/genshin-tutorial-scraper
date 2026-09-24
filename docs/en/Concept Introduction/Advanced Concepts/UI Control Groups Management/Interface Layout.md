---
title: Interface Layout
path_id: mhb6mc085sjc
updated_at: 2026-08-06 15:40:09
category: Concept Introduction/Advanced Concepts/UI Control Groups Management
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhb6mc085sjc
---

# I. Definition of Interface Layout

The Interface Layout is the screen players use to obtain information and perform interactions during stage runtime.

In addition to the *Default Layout* with basic features, players can customize the Interface Layout.

The Interface Layout runs per player; during runtime, each player has exactly one active Interface Layout.

# **II. Interface Layout Management**

![](../../../images/3e5909eb71a569a3.png)

The Interface Layout is centrally managed via *Manage* *UI Control Groups — Interface Layout*.

Only supports editing and referencing the interface that is displayed during stage runtime, and does not support editing the interfaces for essential processes such as matching and settlement

**1. Default Configuration**

The Interface Layout used by players during Stage gameplay must be configured via *Class*.

Open the "Class" editing Interface, then use *Select Layout* to reference the Interface Layout.

![](../../../images/3164f2dca65c7995.png)

The Interface Layout parameter configuration window can also transit directly to this editing interface.

![](../../../images/ea3fe5b765387b3f.png)

## 2. Manage with Node Graphs

Switch Current Interface Layout

Use the Layout ID to switch the Target Player's current Interface Layout as needed.

![](../../../images/95fc59682758d304.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Target Player* | The Player Entity that needs to switch the Interface Layout |
| *Layout Index* | The ID of the specified layout in the UI Layout Management Tool  ![](../../../images/1e06d5f8fa4b7088.png) |

Get Current Interface Layout

At runtime, get the player's current Interface Layout ID.

![](../../../images/544d884f5548ca8e.png)

# **III. Interface Layout Adaptation Instructions**

## 1. Device Selection

Due to significant differences in Interface Layouts across devices (resolution and button arrangement), if you want to create Stages playable on *PC/Mobile/Console*, you need to adjust UI Controls' *Location, Size, and Anchor* for each device

There are two places where device settings can be adjusted:

(1) Top bar: Select device and resolution

![](../../../images/fbd4380b715ed630.png)

(2) UI Control Details — Transform: Click to select a device![](../../../images/45524e772c003f71.png)

Main interface styles for different devices in 16:9 resolution:

|  |  |  |
| --- | --- | --- |
| Selected Device | Icon | Main Interface Diagram (16:9 Resolution) |
| PC | ![](../../../images/0348c10d3e4da694.png) | ![](../../../images/65626319d1d36f81.png) |
| Mobile | ![](../../../images/52f4bdf20e2dd122.png) | ![](../../../images/a53a2d2d386813fa.png) |
| Console | ![](../../../images/2d2c3a174318f460.png) | ![](../../../images/39ba3e53955f8520.png) |
| Mobile Controller | ![](../../../images/34bc0c86e3bfb04e.png) | ![](../../../images/4238e9e7fb2f6c71.png) |

## 2. Adjust Location and Size

### (1) Location

Using the bottom-left corner of the canvas as the origin, displays the relative location of the UI Controls' center point to the origin

Each device needs to be set up separately

![](../../../images/134d678522d9eb6e.png)

### (2) Size

Adjust the current size of the UI Control. Click the chain button in the top right corner to lock the current aspect ratio. Some UI Controls cannot be resized

Each device needs to be set up separately

![](../../../images/e5ae285d2770603a.png)

## 3. Anchor

### (1) Definition

When resolution changes, UI Controls automatically adapt their location while maintaining their relative location to the set anchor

Take the selected quest text in the following graph as an example:

![](../../../images/9e7b92000ab4355d.png)

|  |  |
| --- | --- |
| Selected Anchor | After changing resolution to 21:9 |
| ![](../../../images/e06e84321c727d07.png) | ![](../../../images/9594b527967d620e.png) |
| ![](../../../images/7585a8fee482d81f.png) | ![](../../../images/640e5b42bb124fb1.png) |

### **(2)** **Anchor** **Se**l**ection Guidelines**

Based on UI Control Location: Select the anchor corresponding to the section of the nine-grid where the element is placed.

![](../../../images/0413dba3b1c4f538.png)

Based on functional areas: For example, anchor selections for quest descriptions and multiple text boxes should remain consistent.

![](../../../images/1282a334b0ca24db.png)

### (3) New Anchor Type: Stretch

A new Stretch anchortype has been added under Anchor Type. This allows UI elements to stretch and adapt according to changes in the size of the background or container

![](../../../images/438c82b2034c3403.png)

### (4) New Anchor Type: Follow Native Controls

The existing anchor feature for controls does not maintain alignment with certain native controls across different screen aspect ratios. For instance, while the text box shown in the illustration below aligns correctly with the slots in the Skill Area control at a 16:9 aspect ratio, it shifts relative to the Skill Area when the aspect ratio is switched to 19.5:9

![](../../../images/89c6da6afda095f6.png)![](../../../images/37a89e85287037c7.png)

However, with the new anchor configuration method, "Follow Native Controls," selecting the Skill Area as the target ensures the text box control remains correctly aligned with the skill slots even as the screen aspect ratio changes

![](../../../images/1d0193e806223d56.png)

### (5) Control Anchor Display

Control anchors can be displayed permanently on the editing canvas. Click and drag to adjust the anchor position

![](../../../images/69b7bb2b8b6add24.png)

## 4. Interface Dead Zone

The mobile Interface has the smallest screen. Use the 16:9 aspect ratio for mobile as the baseline to ensure clickable UI Controls are inside the red box

![](../../../images/afe5be1fe539c279.png)

# IV. Interface Specification Reference

## 1. Text Reference

### (1) Font Size

When entering text, please refer to the graph below to select font size. Size 20 is typically used

|  |  |
| --- | --- |
| Type | Recommended Font Size |
| Large Title | 36-32 |
| Subtitle/Button Text | 24 |
| Body Text (Most Common) | 20 |
| Secondary Text | 18 |
| Recommended Minimum Font Size | 16 |

### (2) Text Color

Use *<color=#FFFFFF>Text Content</color>* command to change the color of the text in between, where #FFFFFF can be replaced with the following color codes

|  |  |
| --- | --- |
| Dark background (in pop-ups/main interface) | |
| Title/Secondary Text | #D3BC8E |
| Normal Text | #FFFFFF |
| Keyword 1 | #FFCC33 |
| Keyword 2 | #37FFFF |
| Warning Text | #FF5E41 |

|  |  |
| --- | --- |
| Light Background (Tips etc.) | |
| Normal Text | #4A5366 |
| Secondary text (75% opacity) | #4A5366BF |
| Keyword 1 | #F39000 |
| Keyword 2 | #3399CC |
| Warning Text | #FF5E41 |

Other special colors:

|  |  |
| --- | --- |
| Elemental Type Colors | |
| Hydro | #80C0FF |
| Pyro | #FF9999 |
| Anemo | #80FFD7 |
| Electro | #FFACFF |
| Dendro | #99FF88 |
| Cryo | #99FFFF |
| Geo | #FFE699 |

Pop-up:

Subtitle — Font color #D3BC8E

Content — For emphasized text, preferably use yellow (#FFCC33). Leave one line break before starting a new paragraph

![](../../../images/b9da548ec1b0ae4c.png)

### (3) Text Outline Feature

All text entry controls now come with the text outline function

As shown in the image, for dark text displayed on light backgrounds, you can disable the "Enable Text Outline"option to enhance text readability

![](../../../images/9d89e5aa1d9dd830.png)![](../../../images/872f2e51c7adfe76.png)

## 2. Interface Layout Reference

### (1) Main Interface Quest

Quest: Main Quest Text Box font size 20. Side Quest font size 18. Anchor at top left

Multiple side quests:

![](../../../images/97ea327a16361d06.png)

Side quest success/failure conditions: Success text color #ACFF44, Failure text color #FFFFFFBF

![](../../../images/923c50ffac060ec7.png)

Quest Description: Text size 18, consider using size 16 if there is too much text

![](../../../images/0f195750e961677d.png)

Quest with tracking distance: The Distance display must insert a *Custom Variable* in the text

![](../../../images/660ff24aa7b92601.png)

### (2) Hint

Text Box font size 20, center-aligned, length 5,000 (adapts to various screen sizes without showing the Boundary). Anchor at the top

![](../../../images/e53a5d53e62f661c.png)

### (3) Window

Pop-up:

Subtitle — Font color #D3BC8E

Content — For emphasized text, preferably use yellow (#FFCC33). Leave one line break before starting a new paragraph

![](../../../images/b9da548ec1b0ae4c.png)
