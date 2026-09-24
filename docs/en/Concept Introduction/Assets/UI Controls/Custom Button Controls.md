---
title: Custom Button Controls
path_id: mh72uu0inf60
updated_at: 2026-04-03 10:32:25
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh72uu0inf60
---

# I. Custom Button Features

*Custom Buttons* are a special type of Interactive Button whose icon and displayed text can be configured

The logic supported by Interactive Buttons also applies to Custom Buttons

# **II. Editing Custom** Button**s**

![](../../../images/274bf0d672227e5f.png)

## **1. Add a Custom Button**

In the *UI Control Group Editor window*, add the UI Control Template - Custom Button

![](../../../images/3322403f0dd04647.png)

## 2. Custom Button Settings

### (1) Basics

![](../../../images/48384b2d1d2740b3.png)

### (2) Styles

![](../../../images/cc7d29ce9da67e0e.png)

*Style*: Available options are *Preset Style* and *Custom*

**Preset Styles**

![](../../../images/95ee6834d7387505.png)

Choose from a variety of preset button styles. Some preset styles support customizing the icon, color, text, etc.

![](../../../images/cb449e1f2fe7b026.png)

![](../../../images/833bde274d4e0de3.png)

**Custom Styles**

![](../../../images/d39c8f2e0c77db21.png)

Assets for the Default, Hover, and Pressed states can be configured freely

Unavailable Assets can only be configured when Skill is selected under Functions - Key Type

|  |  |  |  |
| --- | --- | --- | --- |
| Status | Description | Style Features | Example |
| Default | Non-interactive state | / | ![](../../../images/f8c4781ed8699cea.png) |
| Hover | When the cursor hovers over the button during keyboard and mouse input | Typically indicated by an outline, a slightly brighter color, or a subtle increase in size to signal that the button is interactive | ![](../../../images/aedf64be6fdafc74.png) |
| Pressed | When the button is pressed during keyboard and mouse or touch input | Typically indicated by a color change and a slight decrease in size to show that the button is being interacted with. When released, it returns to the Default state | ![](../../../images/4ae457ec7669d1c9.png) |

### (3) Functions

**Key Settings**

When the Style is set to Preset Style, the Key Type is locked to Interactive Event and cannot be edited

When the Style is set to Custom, you can choose 1 of 3 Key Types: Skill, Interactive Event, or Item

![](../../../images/229e7ac3feadd54b.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Key Type* | Supports the following three options  Skill: Configure the corresponding skill slot  Interactive Event: Configure the cooldown time  Item: Configure the configuration ID of the corresponding item |
| *Key Mapping - Keyboard & Mouse* | Configure the PC shortcut mapped to this button |
| *Button Hint Offset - Keyboard & Mouse* | Configure the display offset of the hint shown when the cursor hovers over the button |
| *Key Mapping - Gamepad* | Configure the gamepad shortcut mapped to this button |
| *Button Hint Offset - Controller* | Configure the display offset of the hint shown when the button is focused with a controller |
| *Sound Effect* | Play the configured sound effect when the button is triggered |

**Click Response Area**

![](../../../images/bd4f5426c5cf608e.png)

The click area can be configured only when the Style is set to Custom

The click area can be adjusted by dragging it directly in the editing window

The actual trigger area is determined by the configured range of the click area

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Clickable* | If disabled, this button cannot be clicked |
| *Click Area Preview* | When enabled, the light yellow area in the corresponding control in the editing window indicates the click area  ![](../../../images/644560a644cb2f90.png) |
| *Area Range* | Supports using Match Button Size or Custom Size |
| *Location Offset* | When **Area Size** is set to Custom Size, you can configure the offset of the click area's center location |
| *Dimensions* | When **Area Size** is set to Custom Size, you can configure the click area dimensions |

### (4) Recommended Configuration

Button sizes can be defined based on functional priority. The recommended values are as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Button Priority (Lower number = higher priority) | Description | Recommended Size | Example |
| Level 1 | Core actions in the interface, such as upgrading equipment or enhancing characters | Width: As needed Height: 48–52 (Recommended Range) | ![](../../../images/76345d2facd7708b.png) |
| Level 2 | Secondary actions, such as viewing details | Width: As needed Height: 32–40 (Recommended Range) | ![](../../../images/4c362210685eae77.png) |
| Level 3 | Informational or hint buttons, such as [?] | Width × Height: Recommended 32 × 32 | ![](../../../images/f06304e832af1ae9.png) |

# **III. Additional Notes**

Custom Buttons cannot respond to multiple mappings that use the same key at the same time. By default, response priority is determined by creation order, with the most recently created button taking priority. If Custom Buttons are dynamically added or removed during stage runtime through Node Graph logic, this response priority will also change accordingly.
