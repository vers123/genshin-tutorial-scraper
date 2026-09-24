---
title: Rank
path_id: mhkas9r2gtq6
updated_at: 2025-10-20 18:11:18
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhkas9r2gtq6
---

# I. Rank Functions

The *Rank* Function allows creators (Craftspeople) to define player rank points within a stage. During stage settlement, players will receive different rank points based on different *settlement status*. The points for each state can be customized by the creator (Craftsperson).

When other players browse the stage information in the main hall, they can see recorded ranking information, as shown in the graph below:

![](../../../images/908e0628a8484748.png)

![](../../../images/96265bcf3587cfd8.png)

At the end of the match, players' rank points will be calculated accordingly

![](../../../images/1a127ae3e532fc3d.png)

# II. Editing Score Groups

Click [Manage Peripheral System] in the System menu to enter the Peripheral System Settings interface

![](../../../images/921f63c03586007a.png)

In the Peripheral System Settings interface, go to the Rank tab to configure Rankings-related settings

Rank points are modified through preset score group templates, with each player in the match using one score group template. Click the "New Scoring Group" button in the bottom right to create a new score group template

![](../../../images/c502e0d396fc904a.png)

*Enable competitive ranking?*: Choose to enable either the Leaderboard or Rank Function

*Enable in-room score calculation:* Whether to allow rank points adjustments when players play this stage through room teams instead of matchmaking

*Craftsperson's Message*: Allows creators (Craftspeople) to write detailed Rank Points Scoring Rules that will be displayed in the stage information interface outside of matches

![](../../../images/7ea7e4ebb710c73e.png)

*Score Group Settings*: Specific point value settings for each score group template

*Score Group Name*: Can be customized, used by creators (Craftspeople) to distinguish between different score groups

*ID*: The identifier for this score group, used to identify when modifying score group data within a node graph

*Victory Score*: Rank points earned when a player settles with the victory state

*Defeat Score*: Rank points earned when a player settles with the defeat state

*Undecided Score*: Rank points awarded when a player completes a stage in the undefined state

*Escape Score*: Rank points earned when a player settles with the escape state

*Players Included*: Which players this score group applies to

# III. Rank Score Template Configuration Suggestions

It is recommended to configure the scores according to the expected duration of the gameplay and the actual playing experience, referring to the following score table.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Expected Gameplay Duration (minutes) | Victory | Defeat | Undefined | Escape |
| 0-2 | 20 | -5 | 0 | -20 |
| 2-4 | 40 | -10 | 0 | -40 |
| 4-6 | 60 | -15 | 0 | -60 |
| 6-8 | 80 | -20 | 0 | -80 |
| 8-10 | 100 | -25 | 0 | -100 |
| 10-15 | 120 | -30 | 0 | -120 |
| 15-20 | 140 | -35 | 0 | -140 |
| 20-30 | 160 | -40 | 0 | -160 |
| 30-40 | 180 | -45 | 0 | -180 |
| 40-999 | 200 | -50 | 0 | -200 |

# IV. Special Situations for Rank Score Handling

## 1. Fleeing Penalties in Special Circumstances

Players may flee for various reasons, such as a large number of teammates fleeing or AFK, disconnection due to network issues, or the match becoming unplayable due to a significant power imbalance in the later stages. Creators (Craftspeople) can handle fleeing penalties based on the actual situation of the stage.

## 2. Win Streak

When players achieve consecutive wins, they can be given additional score rewards based on a certain percentage of their victory points.

## 3. Consecutive Escapes

When players escape consecutively, additional penalties can be applied.

## 4. Rank Protection

It is recommended to implement a rank protection mechanism. For example, if a player reaches the Silver rank and losing points would cause them to drop to the Bronze rank, they should be protected from dropping.

If any of the above special handling measures are implemented, it is suggested that creators (Craftspeople) explain them in the rank-related announcements.

# V. Node Graph Management of Score Group Data

Switch the scoring group that affects playher's competitive rank

![](../../../images/d730a33be6b7ae12.png)

Set Player Rank Score Change

![](../../../images/66f3dfc0d3634548.png)

Get Player Rank Score Change

![](../../../images/b887c7f83da7ae98.png)

Get Player Rank Info

![](../../../images/1a875ead9507e9de.png)
