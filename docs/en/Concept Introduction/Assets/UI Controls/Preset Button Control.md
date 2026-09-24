---
title: Preset Button Control
path_id: mhdrjpitofuc
updated_at: 2026-09-16 16:12:43
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdrjpitofuc
---

# I. Preset Button Functions

![](../../../images/423ab4c16a38b016.png)

The *Preset Button* is a special Client Interactive Button that supports configurable icons and display text for four states

The Preset Button Control is a Client Control that can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `PresetButton` in the API documentation to view the related Script APIs

# **II.** Editing Preset Button Status

Preset Buttons can reference Client Controls in their child hierarchy to define the visual appearance of different Status Nodes

## 1. Create Child Controls for the Preset Button

Add any control, then drag it under the Preset Button in the hierarchy

![](../../../images/2bcf3c200373fa2f.png)

## 2. Configure References for Button Status Nodes

Click any Status Node, then select the control to reference from the pop-up list of child controls

![](../../../images/d0c1542a722aa3f1.png)

# III. Preset Button Configuration

![](../../../images/eec8f9aab2b6e408.png)

## 1. Button Settings

### (1) Raycast Target

When enabled, the Button can respond to cursor interaction events

### **(2) Button Enabled**

Determines whether interacting with the Button can trigger its associated Nodes and Client Scripts

### (3) Button Status Nodes

Defines the Button's visual references for its four statuses. Each Status Node can reference the same or a different child control

|  |  |
| --- | --- |
| Status | Description |
| *Default* | No interaction |
| *Hover* | The status when the pointer hovers over the Button during keyboard and mouse input |
| *Pressed* | The status when the Button is pressed during keyboard and mouse or touchscreen input |
| *Unavailable* | The status when Button Enabled is turned off |

Click the Play button for a configured status to preview the Button's appearance in that status

![](../../../images/cb7d5ab8ac073605.png)

### (4) Sound Effects

Plays the configured sound effect when the Button is pressed

## 2. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/376c335dd43f287f.png)
