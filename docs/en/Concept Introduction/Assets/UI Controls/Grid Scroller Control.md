---
title: Grid Scroller Control
path_id: mhmvpn9nzh16
updated_at: 2026-09-16 15:58:39
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhmvpn9nzh16
---

# I. Grid Scroller Control Functions

![](../../../images/f41e4e0a078ee0d9.png)

The *Grid Scroller* can be used as a scrolling list for Item Inventories, product lists, and similar interfaces

The Grid Scroller Control is a Client Control that can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `GridScrollerControl` in the API documentation to view the related Script APIs

# II. How the Grid Scroller Works

The Grid Scroller uses a recycled list structure. For performance reasons, only List Items within the visible area are loaded

*When the Grid Scroller scrolls:* The List Item content is refreshed, triggering the corresponding callback. You can also use `RefreshItems` to trigger a refresh, ensuring that the correct List Item content is displayed at the corresponding scroll position

# III. Grid Scroller Configuration

![](../../../images/a70d28330d04de05.png)

## 1. List Settings

*Raycast Target:* Allows the Grid Scroller Control to respond to cursor interactions*Can Scroll:* When the List content extends beyond the Grid Scroller, scrolling can be used to display content that would otherwise be outside the visible area*Show Scrollbar:* Available when Can Scroll is enabled. Determines whether the scrollbar is displayed*Scroll Direction:* Determines whether the List scrolls horizontally (left and right) or vertically (up and down)

|  |  |
| --- | --- |
| Option | Description |
| *Horizontal* | The List scrolls left and right |
| *Vertical* | The List scrolls up and down |

List Item Size: Determines the width and height of each List ItemPadding: Determines the distance between the List content and the top, bottom, left, and right edges of the Grid Scroller ControlLayout Constraint and Preview Count: Displays the specified number of List Items in the interface to preview how the List will appear at runtime

|  |  |
| --- | --- |
| Option | Description |
| *Auto Wrap* | Automatically wraps List Items to the next row when they exceed the grid width |
| *Fixed Rows* | Automatically distributes List Items across each row based on the configured column count and Preview Count |

## 2. List Item Source

*Reference Control Template:* List Items in the Grid Scroller are displayed based on this Control Template*Note:* Only templates configured under *List Item Source* use the Grid Scroller's list-scrolling behavior. Controls placed directly under the Grid Scroller in the hierarchy do not use this behavior

## 3. Controller Navigation

### (1) General Controller Navigation Rules

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/296b67d664530ab9.png)

### (2) Grid Scroller Navigation Rules

If the List Items in the Grid Scroller can receive controller focus (that is, the controller navigation frame can move to the corresponding control), selecting the Grid Scroller Control focuses the first List Item by defaultWhen a List Item in the Grid Scroller has controller focus and there is no other List Item in the direction the joystick is pushed, focus moves to the control outside the Grid Scroller in that direction. For example, if the leftmost List Item is selected and the joystick is pushed left, focus moves to the control to the left of the Grid Scroller
