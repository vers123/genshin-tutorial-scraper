---
title: Stage Settlement
path_id: mh1rck951c6a
updated_at: 2025-10-21 15:00:39
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh1rck951c6a
---

# I. Definition of Stage Settlement

*Stage Settlement* is an action triggered from the Node Graph. Once settlement is triggered, the entire stage will end, and the settlement result will be passed to the *Peripheral System* to update the data related to the *Leaderboard* and *Rank*

# II. Stage Settlement State

The stage settlement state can be dynamically updated during gameplay. After invoking the stage settlement node, results are settled based on each player’s current settlement state

The stage settlement state is a player attribute that consists of two fields

*Escape Validity*: When escape permitted is "False", the player's settlement state will be set to "Escape State"

*Settlement Status*: This field is only meaningful when escape permitted is "True". It has three possible states: "Victory", "Defeat", and "Undefined", which serve as the criteria for adding *rank points*

*Victory*: When settling a stage in this state, you will receive the victory points according to the corresponding scoring template

![](../../../images/8d68dbc601da8f15.png)

*Defeat*: When settling a stage in this state, receive the defeat score according to the corresponding scoring template

![](../../../images/81bd3ab99e18bdbf.png)

*Undefined*: The default state of players. Grants the undecided score defined by the corresponding scoring template when a stage is completed in this state

![](../../../images/53103aa6de3fa835.png)

# III. Stage Settlement Display

The stage settlement display determines how the match results will be presented. This is only shown during a match and does not affect the peripheral system

Click [Stage Settings] in the system menu to enter the Stage Settings interface

![](../../../images/8109affb50dab77b.png)

Configure stage settlement settings in the Stage Settings interface

![](../../../images/f6091ac1fb42dd1b.png)

*Settlement Screen Type*: Determines the interface display style during stage settlement, divided into faction settlement and personal settlement

*Faction Settlement*: Stage results are settled by faction

![](../../../images/2e661f357b1814c4.png)

*Personal Settlement*: Stage results are settled individually

![](../../../images/de3343b279027615.png)

*Enable In-Game Ranking*: When enabled, use the Ranking Settings node to edit the display order of individuals or factions during the settlement phase

*Ranking Value Comparison Order*: Determines the rule for displaying rankings, divided into ascending and descending order

*Low to High*: Lower ranking values are displayed at the top

*High to Low*: Higher ranking values are displayed at the top

# IV. Stage Settlement Management Using Node Graphs

Settle Stage

![](../../../images/4e39b3c2107b629f.png)

Set Player Settlement Ranking Value

![](../../../images/964ae530693fd8fa.png)

Set Faction Settlement Ranking Value

![](../../../images/9736bf388ee737fb.png)

Set Player Settlement Success Status

![](../../../images/53e8eff9f72cc489.png)

Set Faction Settlement Success Status

![](../../../images/1a5cb0745a894d4e.png)
