---
title: Achievements
path_id: mhbc690cki4g
updated_at: 2025-10-20 18:25:58
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhbc690cki4g
---

# I. Achievement Functions

*Achievements* are used to record specific goals or milestones that players accomplish in the game

Achievement progress can be carried over across multiple playthroughs. When players replay the same stage, they can continuously accumulate achievement progress to unlock different achievements.

The number of achievements and completion conditions in a stage can be customized by creators (Craftspeople) through the Achievement module

# II. Editing Achievements

Click [Manage Peripheral System] in the System menu to enter the Peripheral System Settings interface

![](../../../images/fe0619a7f4ff174b.png)

Configure achievement settings in the Peripheral System Settings interface

A stage supports configuring multiple *regular* *achievements* and one *ultimate achievement*. The ultimate achievement will be automatically unlocked after all normal achievements are completed. The ultimate achievement will only be enabled when at least five normal achievements are set and their names and images are configured

![](../../../images/003eef674ed8d453.png)

*Achievement Settings*: Switch and Validity settings for the achievement system

*Enable Achievements?*: Enable or disable the achievement system

*Enable in-room achievement settlement*: Whether to allow setting achievement progress when players play this stage through room teams rather than matchmaking

## 1. Ultimate Achievement

![](../../../images/6a5e468213c668db.png)

*Ultimate Achievement*: Ultimate Achievement settings, click the edit button on the right to enter the Edit Details interface

![](../../../images/f182287d5737e643.png)

*Achievement Name*: The display name for the achievement. Can be modified in the Achievement Name field below

*ID*: The identifier used to distinguish this achievement when modifying achievement data in a node graph

*Achievement Icon*: Allows uploading a local image to serve as the achievement's icon

## 2. Regular Achievements

![](../../../images/977e4b74a091a6a7.png)

*Regular Achievements*: Click the New Achievement button in the bottom right to add a new normal achievement, then click the Edit button to modify its details

![](../../../images/c1ecbfb78e612691.png)

*Achievement Name*: The display name for the achievement. Can be modified in the Achievement Name field below

*ID*: The identifier used to distinguish this achievement when modifying achievement data in a node graph

*Rarity*: Creators (Craftspeople) can also customize an achievement's rarity, which is divided into *Glorious* *Gold**, Starsilver, and Bright* *Bronze*

*Achievement Counter*: A configurable value that starts at 0 for each player and gradually increases through Node Graph trigger logic during gameplay. The achievement is considered complete when the counter reaches this configured value

*Achievement Description*: The description displayed for this achievement

# III. Node Graph Achievement Data Management

Set Achievement Progress Tally

![](../../../images/18cfa9236378b2e0.png)

Change Achievement Progress Tally

![](../../../images/3be09aad7f338fb6.png)

Query If Achievement Is Completed

![](../../../images/765f03847c278d38.png)
