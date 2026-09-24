---
title: Leaderboard
path_id: mht9eaisd5bw
updated_at: 2025-10-20 18:07:23
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mht9eaisd5bw
---

# I. Leaderboard Functions

The *Leaderboard* Function allows creators (Craftspeople) to record certain in-game information to the peripheral system. When other players browse the stage information from the lobby, they can view this leaderboard information, as shown in the graph below:

![](../../../images/c75abe59a71283f7.png)

![](../../../images/0e86cadb40074dda.png)

# II. Editing Leaderboard

Click [Manage Peripheral System] in the System menu to enter the Peripheral System Settings interface

![](../../../images/4e7ff2c9edf71137.png)

In the leaderboard tab of the peripheral system settings interface, you can perform settings related to the leaderboard.

Only the Leaderboard Function or the *Competitive* *Rank* Feature can be enabled. A stage can support multiple leaderboard templates. When configuring the data, you need to specify the leaderboard template ID. Click the "New Leaderboard" button in the lower right corner of the interface to add a new leaderboard template

![](../../../images/8bab50c99470a245.png)

*Leaderboard Settings*: Controls the overall logic and activation of Leaderboard Function

*Enable Leaderboard*: Choose to enable either the Leaderboard or Competitive Rank Function

*Enable In-Eoom Leaderboard Ranking*: Whether to allow setting leaderboard data when players play this stage through room teams rather than matchmaking

*Leaderboards*: Detailed settings for each leaderboard

*Leaderboard Name*: Can be customized, used by creators (Craftspeople) to distinguish between different leaderboards

*Index*: The identifier of this leaderboard, used for identifying when modifying leaderboard data via the node graph

*Display Priority*: When multiple leaderboards exist, those with higher priority are displayed closer to the top

*Display Format Selection*: Leaderboard scores are stored as numerical values on the server but can be displayed in different formats. The following formats are currently supported:

*Raw Numbers*: Display as a numerical value

*Time*: Display in duration format

*Percentage*: Display in percentage format

*Leaderboard Reset Type*: Rules for resetting leaderboards

*Do Not Reset*: The leaderboard remains persistent and will not be reset by external logic

*Reset With Season*: When a new season begins, the previous data will be reset

*Score Sorting Rule*: Defines how leaderboard values are sorted

*Lower Values First*: Players with lower values are ranked higher on the leaderboard

*Higher Values First*: Players with higher values are ranked higher on the leaderboard

Each leaderboard only records information for the top 1,000 players

# III. Node Graph Node Settings for Leaderboard Information

Leaderboard score settings are compatible with both floating point numbers and integer values

Set Player Leaderboard Score as Float

![](../../../images/adf10e2b95cce5ae.png)

Set Player Leaderboard Score as Integer

![](../../../images/80cbe06a617138c3.png)
