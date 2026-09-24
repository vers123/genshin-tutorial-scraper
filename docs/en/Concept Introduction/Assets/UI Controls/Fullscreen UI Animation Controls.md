---
title: Fullscreen UI Animation Controls
path_id: mhp02viyg2dg
updated_at: 2026-09-16 16:28:48
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhp02viyg2dg
---

# I. Fullscreen UI Animation Features

*Fullscreen UI Animations* can be configured in the UI Layout and display the corresponding special effect asset in the UI Layout. It is a type of UI control used to beautify the interface and enrich its visual presentation

During stage runtime, Fullscreen UI Animation Controls can be triggered through Node Graphs

# **II. Editing Fullscreen UI Animation**

![](../../../images/c3d5907afc4323e9.png)

## **1. Add Fullscreen UI Animation**

In the *UI Control Group Editor window*, add the UI Control Template - Fullscreen UI Animation

![](../../../images/f76f5b8fb38de3bc.png)

## 2. Fullscreen UI Animation Settings

![](../../../images/8ee0a3f8cfb6667f.png)

*Select UI Animation*: Select the special effect asset to be displayed in the UI Layout

*Play Sound Effect*: If set to Yes, the sound effect included with the asset will also play

## 3. Differences Between Fullscreen UI Animation and UI Animation

Fullscreen UI Animations are at the very bottom of all layers by default and cannot be changed

Fullscreen UI Animations cover the entire screen, and their effective range cannot be modified

Fullscreen UI Animations are generally used for on-screen atmospheric effects

# III. Manage UI Animation through Node Graphs

Play UI Animation on Control

![](../../../images/cfcb15f3e34b965b.png)

# IV. Fullscreen UI Animations in Client Controls

Client Fullscreen UI Animation controls can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `FullscreenUIAnimationControl` in the API documentation to view the related APIs

![](../../../images/395dec6fce7cf2a6.png)

## 1. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation.

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/73478b6cc30e2746.png)
