---
title: Status Display Area Controls
path_id: mhy86mi516zg
updated_at: 2026-08-06 16:27:20
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhy86mi516zg
---

# I. Functions of the Status Display Area

*The Status Display Area* can be configured in the interface layout to monitor the unit status on entities and display them in a custom style

The Status Display Area controls are for information display only and are not interactive

Unlike the notification queue, status items do not have additional animation effects when added to or removed from the queue

# **II. Editing the Status Display Area**

![](../../../images/32152386c4152365.png)

## **1. Add Status Display Area**

In the *UI Control Group Editor Window*, add UI control template - Status Display Area

![](../../../images/e5290e2d75325925.png)

## 2. Status Item Style Settings

Similar to the Tab Controls and Single-Choice Window Controls, you can customize the style of status items in the style settings

![](../../../images/54de14b6d274873a.png)

Craftspeople can click "Edit Details" to add any assets to the status item's asset group. For example, UI animations can be added so that each time a new status item is added to the display area, the UI animation is triggered to indicate the status update

![](../../../images/1ab3ac72d49f4ab3.png)

## 3. Status Display Area Function Settings

![](../../../images/a98cf35bbc19cf4c.png)

Initial Fill Point:

The initial fill position when the first status item is added to the queue

![](../../../images/9e5355e28cc0315a.png)

Fill Direction:

The fill direction of the status item

![](../../../images/af6d72a04447ba55.png)

Insert New Status:

Can be combined with the "Fill Direction" and "Initial Fill Point" parameters to achieve different effects

![](../../../images/d40e46c7214cf754.png)

Example: When Layout Constraint = Auto Wrap:

If initial fill point = upper left, fill direction = vertical, and insert new status = back of queue, then when a status is added to the queue, it will be filled from top to bottom

If initial fill point = lower left, fill direction = vertical, and insert new status = front of queue, then when a status is added to the queue, it will be filled from bottom to top

Align:

![](../../../images/696fb319aaded4a5.png)

Similar to text box alignment, you can set the vertical and horizontal alignment of all status items relative to their parent controls

## 4. Notes

Unlike the Notification Queue Controls, the Layout Constraint parameters in the Status Display Area is affected by the fill direction of the status items

![](../../../images/33fb668c665ddca6.png)![](../../../images/dbb16ace50bb28a6.png)

When Layout Constraint = Fixed Rows, status items will fill the current column first before moving to the next column;

When Layout Constraint = Fixed Columns, status items will fill the current row before moving to the next row;

# **III. Steps for Displaying Status Items in the Status Display Area**

All three of the following conditions must be met simultaneously for this status to be displayed

## 1. Confirm the Monitored Entity

In the Status Item Configuration of the Function tab, first designate the entity to be monitored

![](../../../images/0c8d54eb7898b2bb.png)

## 2. Link Unit Status

Click Edit Details to open the interface, then click "Link Unit Status" to select the unit status to display

![](../../../images/591924043245a650.png)

## 3. Add Control Push in Unit Status

For unit status that needs to be displayed within a control, add the "Add Status to Status Display Area" effect in the settings, and select the target control to push to

![](../../../images/2663581885e7b95e.png)

# IV. Additional Notes

Classic Mode now also supports configuring Special Number controls

The Status Display Area control now includes a "DIsplayed as stacks when applied by different sources" option. When this option is disabled, unit states of the same type applied from different slots are displayed separately and it should be used together with the Monitor Parent Mode of the Special Number control

![](../../../images/223013cff64d4be4.png)
