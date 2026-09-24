---
title: Floating Interaction Page Controls
path_id: mhp5msi2uryk
updated_at: 2026-08-06 19:52:49
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhp5msi2uryk
---

# I. Floating Interaction Page Features

![](../../../images/6328ea237cde9957.png)

*Floating Interaction Page* UI controls provide a range of advanced configuration options, such as tabs and single-choice windows, making it easier for Craftspeople to configure more complex related interfaces. They also support adding various buttons and switches to enrich functionality and presentation

During stage runtime, the Floating Interaction Page can be triggered through Node Graphs

It supports player interaction and, based on the Craftsperson's static configuration, can trigger Server Node Graph Events when tabs or single-choice windows are opened or closed

If the Floating Interaction Page encounters an abnormal condition such as disconnection or reconnection, it will not be restored

# **II.** Editing the **Floating Interaction Page**

![](../../../images/167ab551f4b10e14.png)

## **1. Add a Floating Interaction Page**

In the *UI Control Group Editor window*, add the UI Control Template - Floating Interaction Page

![](../../../images/a2727d5d26c3a083.png)

## 2. Floating Interaction Page Settings

### (1) Basics

![](../../../images/fb45d8660ed2b886.png)

### (2) Styles

![](../../../images/26ed82e249ce4537.png)

*Use Preset Background*: When enabled, you can choose a preset background. When disabled, the default background is used

*Select Preset Style*: Select one of the preset styles

*Page Container*: A container is used to organize the information structure of UI controls within a Floating Interaction Page. Containers can be divided based on the interface's information structure, and each container can be treated as a separate page

*Initially Effective*: Determines which containers are initially effective

*Window Container List*: Displays all current containers

Click [Details Editing] to enter the *Floating Interaction Page editing interface*

![](../../../images/5f83b1f6bf2cdee3.png)

### (3) Functions

![](../../../images/4be1fed99fc75b51.png)

*Pause Game on Page Open in Single-Player Mode:* If enabled, opening the Floating Interaction Page in a single-player stage will pause the game while the page is being used

Note: When the game is paused, Sound Effect Assets in the Sound Effect Library under Environment, Creature & Enemy Sounds, Character Actions, Combat, and Objects will also pause with the game. However, Sound Effect Assets included in UI Sound Effects will not pause and will continue playing

![](../../../images/c421450cecace06f.png)

*Controller Initial Selected Control*: Select one from the UI controls configured in the Floating Interaction Page editing interface

*Enable SFX*: The Sound Effect Asset triggered when the Floating Interaction Page is opened

*Disable SFX*: The Sound Effect Asset triggered when the Floating Interaction Page is closed

*Formal Variable Management*: Each Floating Interaction Page supports configuring a set of formal variables. If a corresponding formal variable is referenced in the Asset Library, the value configured in the current Floating Interaction Page will be used

For formal variable mapping, ensure that the data types match

![](../../../images/e44fbfd714881efa.png)

# III. Floating Interaction Page Editing Interface

![](../../../images/26e5af8d0eda4cf2.png)

A Floating Interaction Page functions as a new "UI Layout." You can add UI controls to this page and modify their settings accordingly

The difference is that some UI controls are exclusive to the Floating Interaction Page

## 1. Interaction Page Close Button

![](../../../images/0d9c1e655362adb7.png)

The Interaction Page Close Button is included by default in the Floating Interaction Page. Clicking it closes the entire Floating Interaction Page and all controls within it

The Interaction Page Close Button cannot be removed from the Inherent Container

If the Inherent Container is not enabled in the Floating Interaction Page, meaning the Close Button is not included, the page can still be closed with Esc on PC or the exit button on a controller. On mobile, the Floating Interaction Page must be closed through Node Graphs

### (1) Basics

![](../../../images/f9c47dcd0186f112.png)

### (2) Styles

![](../../../images/202d82da4ece9cad.png)

*Style*: Available options are *Preset Style* and *Custom*

**Preset Styles**

![](../../../images/4c8593dc8a045cbe.png)

Choose from a variety of preset button styles. Some preset styles support customizing the icon, color, text, etc.

![](../../../images/6a1af5c080711fb8.png)

![](../../../images/e6bd70a27c584772.png)

**Custom Styles**

![](../../../images/ef20b7d8deafeeee.png)

Assets for the Default, Hover, and Pressed states can be configured freely

### (3) Functions

**Key Settings**

These key settings cannot be modified. They correspond to the close function on PC and controller

![](../../../images/2582076981a40351.png)

**Click Response Area**

![](../../../images/c37f8b5f4fd2cd1f.png)

The click area can be configured only when the Style is set to Custom

The click area can be adjusted by dragging it directly in the editing window

The actual trigger area is determined by the configured range of the click area

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Clickable* | If disabled, this button cannot be clicked |
| *Click Area Preview* | When enabled, the light yellow area in the corresponding control in the editing window indicates the click area  ![](../../../images/74c655a8fbab1299.png) |
| *Location Offset* | Offset of the click area and its center point  Only available for Custom Buttons. The Close button cannot be modified |
| *Dimensions* | Size of the click area  Only available for Custom Buttons. The Close button cannot be modified |

**Controller Navigation**

![](../../../images/38657626dd0b4d6b.png)

Supports configuring a navigation hint when a button is focused with the controller joystick

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Selectable via Controller Joystick Navigation* | If enabled, the configured hint will be displayed when the button is focused through controller navigation |
| *Controller Navigation Hint Style* | Supports selecting a preset style |
| *Navigation Hint Target* | Can be set to Up, Down, Left, or Right. See below for the display effect:  ![](../../../images/77298037c567ea11.png) |
| *Navigation Hint Offset* | Supports configuring X/Y offset values |
| *Left/Right/Up/Down* | When controller focus moves from this control in the selected direction, it will prioritize snapping to the configured target  By default, focus snaps to the nearest control  Supports selecting controls from all configured containers |

## 2. Tab

### (1) Basics

![](../../../images/a7cd0aaf9ab0296c.png)

### (2) Styles

![](../../../images/69528cf460a71193.png)

*Style*: Available options are *Preset Style* and *Custom*

Both styles require configuration of the scroll direction

**Horizontal**

![](../../../images/6467b1673cf39b1d.png)

**Vertical**

![](../../../images/076aa157b558fd08.png)

**Preset Styles**

![](../../../images/d4f5382030accb5d.png)

Different preset styles can be selected

![](../../../images/e734041b578bca88.png)

**Custom Styles**

![](../../../images/aa0e918a0df8d633.png)

Supports adding styles to preconfigure multiple tab item styles

Each style allows the assets for the Default, Hover, Pressed, and Selected states to be configured freely

### (3) Functions

#### **a. Tab Settings**

![](../../../images/bedd0fd1239f2b20.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Tab Item Size* | General settings for each tab item |
| *Spacing* | Spacing between tab items |
| *Padding* | Margin settings for the top, bottom, left, and right sides relative to the border |
| *Center If Content Doesn't Fill* | If enabled, the tab items will automatically be centered as a whole |

#### **b. Tab Item Configuration**

![](../../../images/cb2c1dcc6d5ec3a3.png)

Supports preconfiguring tab items, statically linking associated tab items, and adjusting displayed content through Node Graphs during stage runtime

Tab items support click feedback configuration, including opening tabs and toggling control visibility

Tab item settings vary slightly depending on whether the selected style is Preset Style or Custom

**Add Tab Items**

In the Edit Details interface, click the plus sign to add a new Tab Item

![](../../../images/c261c49aec282809.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Tab Name* | Name of the Tab Item |
| *ID* | Unique Identifier for the Tab Item |

**Basic Settings**

![](../../../images/de4d02f29636f886.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Tab Name* | Name of the Tab Item |
| *Tab Style* | Select a style configured in the Tab Style settings at the previous layer |
| *Preview Selection State* | If enabled, the default display configuration will be shown in the editing window |
| *Return to Server Event* | During stage runtime, clicking this Tab Item triggers the [When Floating Interaction Page is Triggered] Server Node Graph Event |

**Formal Variable Configuration**

![](../../../images/b439aeb32665dcc3.png)

Link formal variables to specified data or Player Custom Variables

If any assets in this tab item reference formal variables, they will use the real-time data of the corresponding configured custom variables

**Container Status Settings**

![](../../../images/a30f9fe57483402e.png)

Supports adding page containers and configuring whether each one is **shown or hidden**

When this tab item is selected, the configured page containers will be shown or hidden according to these settings

**Control Status Settings**

![](../../../images/e622036ed4260411.png)

Supports adding controls to page containers and configuring whether each one is **shown or hidden**

When this tab item is selected, the configured controls will be shown or hidden according to these settings

#### c. Interaction Settings

![](../../../images/7a579b959107a60e.png)

When the corresponding hotkey is enabled, this tab can be interacted with using the hotkey

Interacting with this tab triggers the configured sound effect

#### d. Controller Navigation

![](../../../images/fb2e55a2e42b6204.png)

When controller hotkeys are enabled for a tab, Controller Navigation cannot be triggered

If controller hotkeys are not enabled, refer to the corresponding configuration description for the Interaction Page Close Button

## 3. Single-Choice Window

### (1) Basics

![](../../../images/fafd7a7c21eeefb5.png)

### (2) Styles

![](../../../images/fe489b634340b45e.png)

Single-choice windows support only Custom Style

Styles can be added to preconfigure multiple tab item styles

Each style supports freely configuring the assets for the Default, Hover, Pressed, and Selected states

### (3) Functions

#### **a. List Settings**

![](../../../images/d842564a164fc015.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Scroll Direction* | Horizontal or Vertical |
| *List Item Size* | General settings for each list item |
| *List Item Spacing* | Spacing between list items |
| *Padding* | Margin settings for the top, bottom, left, and right sides relative to the border |
| *Center Align* | If enabled, the tab items will automatically be centered as a whole |
| *Layout Constraint* | Auto Wrap or Fixed Rows |

#### **b. List Item Configuration**

![](../../../images/388dd6f618653aa4.png)

Supports preconfiguring list items, statically linking associated list items, and adjusting displayed content through Node Graphs during stage runtime

List items support click feedback configuration, including opening tabs and toggling control visibility

**Add List Items**

In the Edit Details interface, click the plus sign to add a new List Item

![](../../../images/9833be532c0cfb17.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *List Item Name* | Name of the List Item |
| *ID* | Unique Identifier for the List Item |

**Basic Settings**

![](../../../images/2c757918e3f783c4.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *List Item Name* | Name of the List Item |
| *List Item Style* | Select a style configured in the List Style settings at the previous layer |
| *Preview Selection State* | If enabled, the default display configuration will be shown in the editing window |
| *Return to Server Event* | During stage runtime, clicking this List Item triggers the [When Floating Interaction Page is Triggered] Server Node Graph Event |

**Formal Variable Configuration**

![](../../../images/812e96a6d9fb6e01.png)

Link formal variables to specified data or Player Custom Variables

If any assets in this tab item reference formal variables, they will use the real-time data of the corresponding configured custom variables

**Container Status Settings**

![](../../../images/16b180e608286fc4.png)

Supports adding page containers and configuring whether each one is **shown or hidden**

When this tab item is selected, the configured page containers will be shown or hidden according to these settings

**Control Status Settings**

![](../../../images/6de0a962d6023795.png)

Supports adding controls to page containers and configuring whether each one is **shown or hidden**

When this tab item is selected, the configured controls will be shown or hidden according to these settings

#### c. Interaction Settings

![](../../../images/2e23f76dd7176aed.png)

Interacting with this single-choice window triggers the configured sound effect

#### d. Controller Navigation

![](../../../images/0b666ed9dc6a232a.png)

When the controller joystick hovers over a button, you can configure a navigation hint

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Selectable via Controller Joystick Navigation* | If enabled, the configured hint will be displayed when the button is focused through controller navigation |
| *Controller Selection Behavior* | Supports selecting **on focus change or after pressing Confirm** |
| *Controller Navigation Hint Style* | Supports selecting a preset style |
| *Navigation Hint Target* | Can be set to Up, Down, Left, or Right. See below for the display effect:  ![](../../../images/77298037c567ea11.png) |
| *Navigation Hint Offset* | Supports configuring X/Y offset values |
| *Left/Right/Up/Down* | When controller focus moves from this control in the selected direction, it will prioritize snapping to the configured target  By default, focus snaps to the nearest control  Supports selecting controls from all configured containers |

# IV. Manage Floating Interaction Pages with Node Graphs

The Floating Interaction Page includes some special controls. Among them, tabs and single-choice windows have similar features, and their parameters are managed in the same way. Therefore, when referenced in Nodes or Output Parameters, tabs and single-choice windows are collectively referred to as [List].

Show Floating Interaction Page

![](../../../images/a9292e86f01e0b2a.png)

Close Floating Interaction Page

![](../../../images/42b04d2dc4b8e9ed.png)

Update Floating Interaction Page List Data

![](../../../images/f413afa8c7f1f4d9.png)

When Floating Interaction Page is Triggered

![](../../../images/3c66cb64c40eed8a.png)

# V. Floating Interaction Page Controls & Controller Navigation

## 1. Controls That Support Controller Navigation

When an interactive UI control, such as an Interactive Button, Item Display, Custom Button, Custom Switch, etc., is added to a Floating Interaction Page, additional "Controller Navigation" settings become available. In addition, controls that can only be used on a Floating Interaction Page, such as a Tab, Single-Choice Window, Text Window, etc., also support "Controller Navigation" settings.

![](../../../images/588f0f6d15be4fb3.png)

## 2. Controller Navigation Hints

As shown in the image, the control types highlighted in the lower-left box can be configured as controller navigation targets. To allow a control to be selected using the controller joystick, enable the "Selectable via Controller Joystick Navigation" option.

Once a control is configured as a navigation target, a directional arrow will be displayed as shown in the image. You can customize the arrow style, direction, and position offset.

![](../../../images/bf23274ac9128078.png)

## 3. Controller Navigation Rules

Using the Left/Right/Up/Down parameters shown in the image, you can specify which control should receive focus when the controller navigation focus is on the current control and the player tilts the stick to the left, right, up, or down.  
By default, focus moves to the control whose center point is closest in the selected direction.  
You can also specify a target control from the control list or choose None.![](../../../images/10694484f6930f93.png)

## 4. Navigation Focus & Buttons

When a control other than a Tab or Text Window is configured as the navigation target, it can respond to the fixed Confirm button ![](../../../images/06d4d678ff8a953f.png) or ![](../../../images/e9929022e6175d48.png) (depending on the player's system button mapping). If the control also has a shortcut key configured, it can additionally respond to the corresponding controller shortcut.

## 5. Controller UI Design Guide

For more information on designing gameplay interfaces for controller users, please refer to the following tutorial:

[UI Controls — Controller UI Design Guide](/ys/ugc/tutorial/course/detail/mhjobxrdykym)
