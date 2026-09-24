---
title: UI Animation Controls
path_id: mhxyow9ocdz6
updated_at: 2026-09-16 16:27:55
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhxyow9ocdz6
---

# I. UI Animation Features

*UI Animations* can be configured in the UI Layout and display the corresponding special effect asset in the UI Layout. It is a type of UI control used to beautify the interface and enrich its visual presentation

During stage runtime, UI Animation Controls can be triggered through Node Graphs

# **II. Editing UI Animation**

![](../../../images/78988d1b797d721e.png)

## **1. Add UI Animation**

In the *UI Control Group Editor window*, add the UI Control Template: UI Animation

![](../../../images/8f6e8a5e6c99588a.png)

## 2. UI Animation Settings

![](../../../images/0a909f9add298b16.png)

*Select UI Animation*: Select the special effect asset to be displayed in the UI Layout

*Play Sound Effect*: If set to Yes, the sound effect included with the asset will also play

*Layer*: Only supports Above All Controls and Below All Controls. The default is Above All Controls

## 3. Preview Settings

![](../../../images/1fffa40ca51f6277.png)

Enable this in the top-right settings to keep UI animations always visible in preview while editing, regardless of layer order

# III. Manage UI Animation through Node Graphs

Play UI Animation on Control

![](../../../images/24a007d5aad1faeb.png)

# IV. UI Animations in Client Controls

Client UI Animation controls can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `UIAnimationControl` in the API documentation to view the related APIs

![](../../../images/027764c4093ffb3e.png)

## 1. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation.

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/6a37dd1e767e5589.png)
