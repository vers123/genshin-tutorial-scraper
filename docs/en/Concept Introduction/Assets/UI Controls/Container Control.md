---
title: Container Control
path_id: mhvorr09h31s
updated_at: 2026-09-16 15:03:39
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhvorr09h31s
---

# I. Container Control Functions

![](../../../images/7d442c25844459f9.png)

Primarily serves as an attachment point for other Client Controls. It can keep the cursor persistently visible and block key and click event passthrough

The Container Control is a Client Control that can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `ContainerControl` in the API documentation to view the related Script APIs

# II. Container Control Configuration

![](../../../images/755f33968016ed9c.png)

## 1. Function Settings

*IsolateNavigation:* *When navigating based on the nearest control, controller navigation cannot cross the Container boundary in either direction*

*disableKeyEventPassthrough:* Key events within the Container do not pass through to the interface outside it

*disableCursorEventPassthrough:* Cursor events within the Container do not pass through to the interface outside it

*showCursor:* Keeps the cursor persistently visible

## 2. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/a9394d29446ce31d.png)
