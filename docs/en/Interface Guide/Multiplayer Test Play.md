---
title: Multiplayer Test Play
path_id: mhpv84i3difg
updated_at: 2025-10-13 23:21:33
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpv84i3difg
---

# I. Function Overview

This feature simulates multiplayer scenarios in edited stages to quickly validate stage effects.

# II. Function Entry Point

System Menu — Multiplayer Test Play

![](../images/88543f7a8e01a46d.png)

# III. Multiplayer Test Play Room

After clicking [Multiplayer Test Play] (see above), the initialization runs (required checks and stage upload). When complete, you enter the Multiplayer Test Play Room interface.

Note: Each Multiplayer Test Play loads the most recently uploaded Saving. If you edit the stage, manually update the stage before playing the latest changes.

![](../images/a535c832fa50dc33.png)

## 1. Room Functions

### (1) Waiting Area

![](../images/e5e1fcd4cc7089b0.png)

Players who join the Test Play Room are placed in the first available Waiting Area seat. Players in the Waiting Area do not join subsequently started playtests. They can switch areas and seats by clicking any open seat in the [Waiting Area] or [Preparation Area].

![](../images/35e20ac189f70c47.png)

**Invited Players**

Invited Players can switch seats in the following two ways:

Click [Join Preparation Area] to take a remaining seat in the Preparation Area.Click an empty seat to switch.

### (2) Preparation Area

![](../images/da7bb4207ff9cafe.png)

Holds all players who intend to participate in Test Play. Invited Players download the stage here and get ready to play.

Preparation Area: Loads [Stage Settings] -> [Player Count Settings] (player count, groups).

![](../images/4ea7d7b7e4534522.png)

**Invited Players**

![](../images/cf5479657228b685.png)

While in the Preparation Area, Invited Players click the [Ready] button (bottom-right) to signal readiness to play the stage

![](../images/6225ef30a9111bdc.png)![](../images/0a1bf86e70ec4dcd.png)

After clicking Ready, the stage download starts; when complete, the player enters the Ready state.

Note: When the host starts the game, any player in the Preparation Area who is not in the Ready state is moved to the Waiting Area.

### (3) Player Invitation

![](../images/aef34ae28031df0b.png)

![](../images/c5e336b3a07665ac.png)

After the host clicks [Invite], the [Invite Players] panel opens on the right with three sections: [Search Invitation], [Today's Invites], and [Friends].

**Search Invitation**

![](../images/1f707a6f82868855.png)

Search for players by UID. After searching, send an invite with the [Invite] button; once accepted, the player joins the Test Play Room.

![](../images/9cff7ff77970befd.png)

**Today's Invites**

![](../images/872604dae46ea16e.png)

Switch to this tab to view players invited today. Use the Invite button to invite them again.

**Friends**

![](../images/a244ba9ef6727a9f.png)

View your account's friend list on this tab; click a friend's Invite button to send a Test Play invite.

**Invited Players**

Players have 15 seconds to respond to a Multiplayer Test Play invite; if they do not respond in time, the invite is automatically declined.

**Invitation Limits**

Invitation Limit: You can invite up to 16 players per day for Test Play. [Today's Invites] resets at midnight.Invited Players: Players currently in a Stage, Domain, or Editing cannot receive Test Play invites.

### (4) Start Test Play

![](../images/a535c832fa50dc33.png)

The host can start Test Play with the [Start Game] button (bottom-right). After Test Play begins, all seats in the Preparation Area become non-joinable and non-clickable; players who entered Test Play switch to the In-Game status, and the Cosmetic Display phase starts.

Note: Even if the host is not in the Preparation Area, Multiplayer Test Play can be started as long as the stage meets the required conditions (player count, groups, etc.). The host does not need to participate in the Multiplayer Test Play.

![](../images/992fb36f836bcb51.png)

If invited players are in the Preparation Area but not yet Ready, clicking [Start Game] prompts the host for confirmation. If confirmed, all players not in the Ready state are moved to the Waiting Area.

![](../images/b6c0cd4fe19e154d.png)

## 2. Test Play Settings

### (1) Update Stage

![](../images/0c65a5beb2cacd69.png)

Click to upload the most recently edited stage to the Multiplayer Test Play Room. This action moves all players to the Waiting Area, and they must get Ready again.

![](../images/512b88a98b603a16.png)

### (2) Generate Test Play Report

![](../images/9136b79ed888d9b6.png)

After enabling, all players participating in Test Play automatically generate a local report at the end of Test Play for viewing the [Load Calculation Function](/ys/ugc/tutorial//detail/mho2hirgodxi). Creators can import these reports to review each player's Dynamic Load for the session.

![](../images/66350909b8235543.png)

Storage path: C:\Users\%USERPROFILE%\AppData\LocalLow\miHoYo\Genshin Impact\BeyondLocal\(Player UID)\Beyond\_Performance\_Report

### (3) Character Display Settings

![](../images/f7f190bb4c652074.png)

When enabled, players entering a stage go through the Cosmetic Display phase, then proceed to the Loading Interface.

### (4) Enable Settlement

![](../images/6740fb53d788f02a.png)

To speed up testing and reduce steps, disable settlement-related steps via [Enable Test Play Settlement] under [Multiplayer Test Play].

### (5) Test Play Manekin

![](../images/2ba4b0eb572b0701.png)

Before starting a test play, creators can use [Test Play Manekin] in [Test Play Options] to set which Manekin body type is used.

### (6) Test Play Data Settings

![](../images/7873b284e11b7b4f.png)

Before test play starts, the host can configure per-seat data via the [Settings] button at the top-right of each seat.

Note: These settings are bound to the seat. Any player occupying that seat uses the same settings.

![](../images/9b39c38bab26c630.png)

### (7) Test Play Player Management

During Multiplayer Test Play, the host can remove invited players or move them to the Waiting Area using the button at the top-right.

![](../images/7873b284e11b7b4f.png)

**Remove Player**

![](../images/f7f5a86e27474253.png)

The host can remove a player from the Test Play Room. After successful removal, the player returns to their pre-invitation location.

Removal restriction: If a player is currently in Test Play, they are removed after their Test Play ends.

**Move to Waiting Area**

![](../images/ed0239c68d7739c6.png)

The host can move a player to an empty seat in the Waiting Area via [Move to Waiting Area].

### (8) Disbanding the Room

![](../images/a535c832fa50dc33.png)

![](../images/be219e5d61af9a38.png)

The host can disband the Multiplayer Test Play Room using [Dismiss]. After disbanding, all players return to their location prior to joining the room.

### (9) Room Collapse

![](../images/7f3976aceda30684.png)

The host can collapse the interface to the top Menu Bar with the [Collapse] button (top-right) and return to the editing interface. Note: The Multiplayer Test Play Room remains active; invited players stay in the room.

# IV. In-Game Controls for Multiplayer Playtest

The host can perform these actions: Retry Challenge, End Test Play.

Invited Players can perform this action: End Test Play.

## 1. Exit Button

While in playtest, open the [Test Play Controls] panel via the top-left button or the Esc hotkey.

![](../images/4d291f8bab50d038.png)

## 2. Test Play Controls

### (1) Retry Challenge

After clicking [Retry Challenge], all startup steps from the Cosmetic Display phase are re-run; when complete, a new playtest session starts.  
Note 1: If an exception prevents immediate restart, exit Test Play and start the Test Play flow again.

Note 2: In Multiplayer Test Play, if any player exits the current session early, Retry Challenge cannot be executed.

Note 3: During Multiplayer Test Play, only the host can use Retry Challenge.

![](../images/ae90577108b01f7b.png)

### (2) Abandon Challenge

Click to end the current Test Play immediately and trigger the corresponding non-standard settlement result.

![](../images/ffc77aecfb95993d.png)

# V. Multiplayer Test Play Settlement

When Test Play ends, the settlement flow runs and displays results according to the stage's settlement settings.

Creators (Craftspeople) can configure these settings in [Settlement] under [Stage Settings].

![](../images/587b1ef66a9b15a0.png)
