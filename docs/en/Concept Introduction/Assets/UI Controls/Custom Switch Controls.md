---
title: Custom Switch Controls
path_id: mhy48t9sr3ka
updated_at: 2026-05-13 22:54:54
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhy48t9sr3ka
---

# I. Custom Switch Features

*Custom Switches* can be toggled on and off either by clicking them or through their mapped custom variables, thereby triggering different functional logic  
  
Custom Switch interactions can send a *"When UI Control Group Is Triggered" event* to the node graph

# **II. Editing Custom Switches**

![](../../../images/148e764d38b82baf.png)

## **1. Add a Custom Switch**

In the *UI Control Group Editor window*, add the UI Control Template - Custom Switch

![](../../../images/09faf4d3a9336e87.png)

## 2. Custom Switch Settings

### (1) Basics

![](../../../images/2d0207ad21f78167.png)

### (2) Styles

![](../../../images/97e69ac71dfb3dc8.png)

*Style*: Available options are *Preset Style* and *Custom*

**Preset Styles**

![](../../../images/35cf1797172a2ad9.png)

Choose from a variety of preset button styles. Some preset styles support customizing the icon, color, text, etc.

![](../../../images/8725e6a0124e4f89.png)

![](../../../images/b89f4d544af1c552.png)

**Custom Styles**

![](../../../images/850b7fcfa42e5ada.png)

Assets for the Default, Hover, and Pressed states can be configured freely

|  |  |  |  |
| --- | --- | --- | --- |
| State | Description | Style Features | Example |
| On – Default | Non-interactive state | / | ![](../../../images/466db05e58264a9f.png) |
| On – Hover | When the cursor hovers over the button during keyboard and mouse input | Typically indicated by an outline, a slightly brighter color, or a subtle increase in size to signal that the button is interactive | ![](../../../images/9b2ad53dfb166cac.png) |
| On – Pressed | When the button is pressed during keyboard and mouse or touch input | Typically indicated by a color change and a slight decrease in size to show that the button is being interacted with. When released, it returns to the Default state | ![](../../../images/7808cb6ce69eb57d.png) |
| Off – Default | Non-interactive state | / | ![](../../../images/e3857ad2a48a0a96.png) |
| Off – Hover | When the cursor hovers over the button during keyboard and mouse input | Typically indicated by an outline, a slightly brighter color, or a subtle increase in size to signal that the button is interactive | ![](../../../images/f46b3ff4d432eff2.png) |
| Off – Pressed | When the button is pressed during keyboard and mouse or touch input | Typically indicated by a color change and a slight decrease in size to show that the button is being interacted with. When released, it returns to the Default state | ![](../../../images/83692e7df146fe47.png) |

### (3) Functions

**Key Settings**

![](../../../images/7ed14bef3b7eb6b2.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Switch Custom Variable Mapping* | Supports configuring a mapped Player Boolean Custom Variable  When the Custom Variable changes, the switch updates accordingly |
| *Key Mapping - Keyboard & Mouse* | Configure the PC shortcut mapped to this switch |
| *Button Hint Offset - Keyboard & Mouse* | Configure the display offset of the hint shown when the cursor hovers over the switch |
| *Key Mapping - Gamepad* | Configure the gamepad shortcut mapped to this switch |
| *Button Hint Offset - Controller* | Configure the display offset of the hint shown when the switch is focused with a controller |
| *Enable SFX* | Plays the configured sound effect when the switch is turned on |
| *Disable SFX* | Plays the configured sound effect when the switch is turned off |

**Click Response Area**

![](../../../images/30db0a92abc59d4a.png)

The click area can be configured only when the Style is set to Custom

The click area can be adjusted by dragging it directly in the editing window

The actual trigger area is determined by the configured range of the click area

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Clickable* | If disabled, this button cannot be clicked |
| *Click Area Preview* | When enabled, the light yellow area in the corresponding control in the editing window indicates the click area  ![](../../../images/c4785ebfebd5b98c.png) |
| *Area Range* | Supports using Match Button Size or Custom Size |
| *Location Offset* | When **Area Size** is set to Custom Size, you can configure the offset of the click area's center location |
| *Dimensions* | When **Area Size** is set to Custom Size, you can configure the click area dimensions |
