---
title: Global Timer
path_id: mh9bzc0r99i0
updated_at: 2026-04-02 16:42:38
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh9bzc0r99i0
---

# I. Global Timer Component Functions

*The* *global timer* component provides timing capabilities. It supports pausing, restarting, and modifying timers, and can synchronize with UI controls to display the timer's time.

The global timer supports configuring multiple sets of static timer data.

Global timers run independently on different active entities.

# II. How to Use Global Timers

There are two ways to use the global timer:

1. The entity editing component can have a reference timer set, which will be activated when the entity is created.

2. A node graph execution node can activate the timer when it is executed..

# III. Global Timer Management Tool

![](../../../images/a733622eb16be781.png)

You can predefine all global timers via the timer management tool.

![](../../../images/90e1277ba2e2cd5b.png)

Global Timer List

Enumerates all predefined global timers in the current stage.

![](../../../images/d572af0af793c62d.png)

# IV. Editing Global Timers

Add Timer

![](../../../images/dedec34c7ae2ace9.png)

Use the button shown above to add a new timer.

Name and ID

![](../../../images/65578d3b2f392faa.png)

Click ![](../../../images/7c6a258cdb7a79cc.png) the icon to rename or delete the specified timer.

![](../../../images/fe0f75d38b2b0647.png)

![](../../../images/ae23a8db5d0d24b7.png)

This name is the global timer's reference.

Basic Information

![](../../../images/0916d580aa56951e.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Global Timer Type* | Provides two types: *countdown and stopwatch*. |
| *Duration (s)* | When the timer type is countdown, a duration needs to be set. |

# V. Global Timer Reference

## **1. Referencing the Global Timer Through UI Controls**

Open[Interface Layout](/ys/ugc/tutorial//detail/mhozt0r74ng6)Management Tool, Select[Timer UI Controls](/ys/ugc/tutorial//detail/mhnrdor7uyra) "Timer" to execute its logic.

![](../../../images/596b9c40f8ad82ff.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Type* | Stopwatch, Countdown |
| *Specify Timer* | Will enumerate all predefined global timers that match the "Type". |
| *Source Entity* | Default configuration is stage entity. You can choose between stage entity or player entity |

The selected source entity needs to be configured with a global timer component.If the timer configured for the interface controls is not active when the source entity is running, the UI controls will display the default value 00:00.

When the source entity is running and the timer is active, the UI control shows the timer's current time.

## 2. Reference Global Timer Through Component

### (1) Add Component

![](../../../images/d8290a65e1a6f206.png)

a. In the entity prefab editing interface, open the Edit Component tab.

b. Click "Add Common Component", then select "Global Timer" to add it.

c. Press "Advanced Editing" to expand the editing page.

### (2) Reference Timer

![](../../../images/98de130d5cc1fc9e.png)

![](../../../images/ea49ad3bbb8cb5a7.png)

Click "Add Timer" to open a list of global timers, then you can select the desired global timer.

A global timer referenced by a component will be activated when the entity is created.

![](../../../images/2f44de269f685c7b.png)

Click "Manage Timer" to open the global timer management tool.

# VI. Reference Global Timer by Node Graph

Start Global Timer

Use the node graph to reference a global timer, with the running entity as the carrier.

Only timers predefined in the global timer management tool are valid as a reference.

![](../../../images/eb757d58eb44df42.png)

Stop Global Timer

Use the node graph to stop running a global timer early.

![](../../../images/dcbd372d53a6c86d.png)

Pause Global Timer

Use the node graph to pause a running global timer.

When paused, the UI controls linked to the timer will also pause their display.

![](../../../images/4da83e397f860109.png)

Recover Global Timer

You can resume a timer paused by "Pause Global Timer" via the node graph.

If a UI control references the timer, its display will resume as well.

![](../../../images/6c13513d7ceed1f4.png)

Increase Global Timer Value

You can adjust a running global timer via the node graph.

*Increase Value*: If the timer is counting down, a positive number will increase its remaining time, and a negative number will decrease its remaining time. For stopwatch timers, positive values increase the accumulated time, and negative values decrease it.

If the timer is paused first and then modified to reduce the time, the modified time will be at least 0 seconds.

For countdown timers, pausing followed by modifying the time to 0s will trigger the [When the Global Timer Is Triggered] event upon resuming the timer.

If the timer is paused first, then modified to 0s, followed by modifying the time to increase it, and finally resumed, the [When the Global Timer Is Triggered] event will not be triggered.

![](../../../images/89849742123b3dec.png)

When Global Timer Is Triggered

When the global timer's countdown ends, it will send an event to the node graph.

![](../../../images/b02e76f9b769cad2.png)

Get Current Global Timer Time

Use the node graph to get the current time of a running global timer.

*Current Time* If the timer is counting down, returns the remaining time.

If the timer is a stopwatch, it returns the accumulated time.

![](../../../images/f38afc6bcd7b91c8.png)
