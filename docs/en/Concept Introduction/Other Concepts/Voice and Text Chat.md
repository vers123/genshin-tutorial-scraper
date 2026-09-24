---
title: Voice and Text Chat
path_id: mhi706rk3afa
updated_at: 2026-04-02 21:26:09
category: Concept Introduction/Other Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhi706rk3afa
---

# I. Voice and Text Chat Features

The voice and text chat management provides gameplay-oriented chat features, supporting the configuration of multiple exclusive chat channels for different players or factions based on gameplay needs.

The same player can send messages in different chat channels simultaneously.

Supports real-time management of player chat channel permissions through node graphs.

# II. Voice and Text Chat Function Management

![](../../images/6ecbcfc37cc0e646.png)

You can manage the current level's chat channel through [System Menu] > [Manage Voice & Text Chat]

![](../../images/f3331893f48f95cb.png)

### Global Settings: Manage the overall availability of voice and text chat features.

Enable Real-Time Voice Chat?: Determines whether the voice chat function is enabled.

Enable team voice chat in-game: Determines whether team voice chat is allowed during the game.

Enable Text Chat?: Determines whether the text chat function is enabled.

Enable team text chat in-game: Determines whether team text chat is allowed during the game.

# III. Chat Channel Editing

Add Chat Channel

Click the [Add Channel] button to add new chat channels

The stage comes with a default global channel that applies to all players. While its configuration and name can be modified, it cannot be deleted.

![](../../images/8b00f42da70e715c.png)

Press the icon ![](../../images/f6ea9c646db1c5a5.png) to rename or delete the channel

Basic Information

![](../../images/912824cccba90dc3.png)

|  |  |
| --- | --- |
| Parameter | Description |
| *Index* | The unique identifier corresponding to the chat channel |
| *Text Chat Initially Active* | Determines whether the text chat function is enabled or disabled in the channel when the stage initially begins |
| *Channel Application Method* | Supports application by player/by faction  When the channel is applied by faction, chat channel membership can only be adjusted by switching player factions |
| *Apply to Player/Team* | Controls the initial coverage of the channel in the level, multiple selections allowed |
| *Display Priority* | Controls the display order of channels in the level chat system. Higher numbers appear at the top. |
| *Select Icon* | Controls the icon and color of the channel in the in-level chat system |
| *Voice Chat Initially Active* | Determines whether the voice chat function is enabled or disabled in the channel when the stage initially begins |
| *Limit Voice Chat Scope* | Determines whether the voice chat in the channel is restricted to a specific range |
| *Listening Radius (m)* | Sets the listening radius for voice chat in the channel, ranging from 1 to 100 meters |

Quick Message

![](../../images/8555d8a21363e202.png)

Control quick chat messages for corresponding channels within the level Click ![](../../images/6b5b3175c1603194.png) to add quick text, click ![](../../images/47d5a41696dadda3.png)to delete text. At least 1 default text must be kept

The corresponding in-game runtime display is shown in the figure below:

![](../../images/045c7afec792711a.png)![](../../images/b913309e1d3076ca.png)

# **IV. Controlling Text Chat Channels with Node Graph**

Set Chat Channel Switch

![](../../images/a023516b23cff23f.png)

Set Player's Current Channel

![](../../images/28fff272ce789e6d.png)

Modify Player Text Chat Permissions

![](../../images/64205b50e7be2142.png)

Set Player Voice Chat Range

![](../../images/78c3cd7097021893.png)

Set Player Voice Chat Permissions

![](../../images/8843297a9a1e3ae6.png)

Modify Player Channel Permission

![](../../images/a487b4f340c19f39.png)

Check if the player is currently in a voice chat

![](../../images/634f1e2677de8dbb.png)

Note: This node is only functional within multiplayer sessions (Multiplayer Test Play or Multiplayer Play). It will not execute in single-player modes (Single-player Test Play or Single-player Play)

# **V. Additional Note**s

In the current version, voice chat-related features have been added, and buttons to control voice chat during the game have been included in the interface layout.

To address the issue whereby some Craftspeople may have used interface controls that obscure the voice chat buttons in their stage designs, leading to players being unable to use the voice chat feature in the current version, we would like to remind all Craftspeople to adjust the position of their interface controls appropriately to ensure the normal use of this function.

The specific locations of the voice chat buttons on PC and mobile platforms are as follows:

![](../../images/af18ac038f59bfc2.png)

![](../../images/884cf8e43cf49d8e.png)
