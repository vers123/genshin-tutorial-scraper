---
title: Timer
path_id: mhk3sb99boca
updated_at: 2025-11-19 22:06:31
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhk3sb99boca
---

# I. Timer Functions

The *Timer* provides timing capabilities; it supports starting, stopping, pausing, and resuming timing operations, and also supports synchronizing UI controls to display timing information

# II. How to Use the Timer

Can only be created and used through node graphs, and must be explicitly assigned to an entity when created.

Supports timing in intervals, and the node graph will send events at each interval.

# III. Managing Timers Through Node Graphs

Start Timer

Start a timer on the target entity.

The timer is uniquely identified by a timer name.

The timer consists of a *Timer Sequence* that can be either looping or non-looping. The timer sequence should be a set of time points in seconds, arranged in ascending order (with a minimum interval of 0.03 seconds). When the timer reaches these time points, it triggers the [When Timer Is Triggered] event.

For example, [1, 3, 5, 7]: If such a timer sequence is provided, the [When Timer Is Triggered] event will be triggered at 1, 3, 5, and 7 seconds.

If the loop setting is "Yes," the timer will reset to 0 seconds after reaching the last time point and continue looping. For instance, with the timer sequence [1, 3, 5, 7], after reaching 7 seconds, the timer will reset to 0 seconds and start counting again.

![](../../../images/a86a929728bdc7f8.png)

Pause Timer

Pause an active timer at any time to temporarily stop its count

![](../../../images/e2043a7048006b51.png)

Resume Timer

During timer operation, if there was a previous pause, you can resume as needed to continue timing

![](../../../images/77ab7fd3ad2dcc7c.png)

Stop Timer

You can also terminate the created timer as needed

![](../../../images/2fead539a59ff495.png)

When Timer Is Triggered

When the timer is running and reaches a time period in the sequence, it will send an When Timer Is Triggered event to the entity node graph where the said timer is mounted

Timer Sequence ID: Represents the index of the timer sequence.

![](../../../images/ee60908928db863e.png)
