---
title: Notification Queue Controls
path_id: mhp9klrf4vdq
updated_at: 2026-05-14 13:03:21
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhp9klrf4vdq
---

# I. Functions of the Notification Queue

*Notification Queue* can be configured in the UI layout and push messages in designated styles in real time via a node graph

The Notification Queue Control is suitable for pushing and displaying various information during actual gameplay, such as scores, resource acquisition, and stage progress updates

The Notification Queue Control is for information display only and is not interactive

When notification items are added to or removed from the queue, additional animation effects will be applied

# **II. Editing the Notification Queue**

![](../../../images/cb8de308f9c16478.png)

## **1. Add Notification Queue**

In the *UI Control Group Editor Window*, add UI control template - Notification Queue

![](../../../images/f03c17bb332dd3e4.png)

## 2. Notification Item Style Settings

As with the Tab Controls and Single-Choice Window Controls, you can customize the style of notification item in the style settings

![](../../../images/5837a2a4113a79b6.png)

Craftspeople can click "Edit Details" to add any asset to the notification item's asset group. For example, UI animations can be added so that each time a new notification item is added to the display area, the UI animation is triggered to indicate the update of the new notification item

![](../../../images/807e4f22347281f9.png)

Note: When notifications are updated, they come with fade-in and fade-out animations by default. If a large number of notifications are updated simultaneously, there may be display delays caused by the animations

## 3. Notification Queue Function Settings

![](../../../images/f864e8b5695144ab.png)

Initial Fill Point:

The initial fill position when the first notification item is added to the queue

![](../../../images/f696121b4b2e4451.png)

Fill Direction:

The fill direction of notification item

![](../../../images/c515700ec1bbeede.png)

Insert New Notification:

Can be combined with the "Fill Direction" and "Initial Fill Point" parameters to achieve different effects

![](../../../images/5f93bac4a0d6f8a0.png)

Example: When Layout Constraint = Auto Wrap:

If initial fill point = upper left, fill direction = vertical, and insert new notification = back of queue, notifications will be filled from top to bottom when added to the queue

If initial fill point = lower left, fill direction = vertical, and insert new notification = front of queue, notifications will be filled from bottom to top when added to the queue

Align:

![](../../../images/9bb39a827ed92b6c.png)

Similar to text box alignment, you can set the vertical and horizontal alignment of all notification items relative to their parent control

## 4. Notes

As shown in the image, when the maximum number of notification queue entries exceeds the notification queue control's display range, the UI animations applied to the notification item asset group cannot be clipped

Therefore, it is **not recommended to set the maximum number of notifications in the notification queue to a value that exceeds the size of the notification queue control**

![](../../../images/eb7a8b85c6bec7b2.png)

![](../../../images/409b244d0dbde1c5.png)

# III. Notification Queue Update Methods

Use the Server Node - Refresh Notification Queue to implement the push notification function

Note that the notification queue can only be updated by pushing a single structure data as a whole

![](../../../images/ee042166c1e88a15.png)
