---
title: Wonderland Task
path_id: mhbemn9wkzh6
updated_at: 2026-05-15 16:16:46
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhbemn9wkzh6
---

# 1. Functions of Wonderland Task

The Wonderland Task feature allows Craftspeople to set in-game objectives for players to complete and distribute rewards upon completion

These tasks can automatically refresh and reset on a cycle. If a player repeats the same stage within a single cycle, their task progress will continue to accumulate

Reward types and completion criteria are fully customizable by the Craftsperson

# II. Editing Wonderland Tasks

## 1. Wonderland Task Entrance

![](../../../images/5649c08390a6132d.png)

![](../../../images/6977b8ad1d976808.png)

You can open the Wonderland Task editing panel via the System Menu - "Wonderland Task"

Click "Create Task" to create a new Wonderland task. A single Wonderland supports up to 20 Wonderland tasks

## 2. Wonderland Task Global Settings

![](../../../images/85b05b0103d1369d.png)

Global Settings Switch:

*Enable in-game access to Wonderland Tasks*: When enabled, the Wonderland Task entrance will appear in the upper-right corner of the screen during gameplay  
*Allow in-room access and result finalization for Wonderland Tasks*: When players play this stage in a room party instead of matchmaking, this determines whether the node graph is allowed to set task progress

## 3. Editing Wonderland Task

![](../../../images/c95f932da2c95b84.png)

Basic Settings

*Refresh Type*: While a Wonderland task is active and in effect, periodically resets the task count and completion status. This can be divided into the following types

*Don't refresh*: Status does not change after completion

*Refresh daily*: Resets task status at 4:00 AM every day

*Refresh weekly*: Resets task status at 4:00 AM every Monday

*Refresh by season*: Resets task status when the season resets

*Task Description*: The task text displayed in the Wonderland task panel/Wonderland Details page

*Task Count*: A configurable value. Each player starts with a task count of 0, which is incremented via Node Graph logic during gameplay. Once the count reaches the specified value, the Wonderland Task is marked as complete

![](../../../images/ca0139a32980d321.png)

*Task Reward*: You can link up to three types of Wonderland Commendation Gift Boxes as rewards. Please note that a Wonderland task must be linked to a Wonderland Commendation Gift Box before it can take effect in-game

![](../../../images/8c0a26b513527e79.png)

Apply Settings:  
*Display Priority*: When multiple Wonderland Tasks are active, those with higher priority will appear at the top of the list

*Activate?*: Toggle to activate the Wonderland task. The task only takes effect when this is turned on  
*Permanent effect after activation?*: If disabled, you must specify the effective season. The available range starts from the current season to the next 10 seasons

# III. Managing Wonderland Task Data in the Node Graph

No. of Tasks Configured

![](../../../images/21af202e81bd0f80.png)

Function: Sets the designated task count for a specific player to a fixed value

Increase Task Count

![](../../../images/cf4915129e38bab4.png)

Function: Increases the designated task count for a specific player to a given value (can be negative)

Query Specified Task Count

![](../../../images/8d8cd350a0e3aa13.png)

Function: Query the current task count for a specific task of a specific player

Query If Specified Task Is Completed

![](../../../images/89c7af75289a13fb.png)

Function: Query the current completion status of a specific task for a specific player
