---
title: Stage Settings
path_id: mh7sg60j65mw
updated_at: 2026-08-03 16:57:32
category: Interface Guide
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7sg60j65mw
---

# I. Entry Point Location

![](../images/79232672f8074172.png)

Click the System Menu button (top-left) to open the menu interface

![](../images/cd6db90654323477.png)

Click [Stage Settings] to open the Stage Settings interface for overall stage configuration

# II. Feature Details

## 1. Basic

![](../images/ca2745e04fa83da5.png)

![](../images/7ae6419e65b93b28.png)

The [Basic] interface provides common stage settings for configuration

### (1) Effective Scene Range After Activation

![](../images/e62bfbf41236a2bd.png)

![](../images/4c5d8400d12b863e.png)

a. Edit the stage's effective range; content outside the range will not take effect

b. Click "Custom Range" to define the stage's effective range

### (2) Level of Stage Environment

![](../images/d126189888783816.png)

a. Environment Level affects the damage coefficient of certain Elemental Reactions triggered by non-Character sources — the higher the level, the higher the coefficient

b. Related Elemental Reactions include Overloaded, Superconduct, Electro-Charged, Burning, Swirl, Shatter, Bloom, Hyperbloom, Burgeon, Aggravate, and Spread

c. Range: 1 - 120. It's recommended to match Character Level and Monster Level

d. After enabling "Enable Full Bloom Damage", Bloom reactions will deal full damage to all units by default.

### (3) Current Number of Permitted Players

![](../images/b09439ae4177b560.png)

Jump to Player Count settings to configure how many players can enter the stage

### (4) Stage Entity

![](../images/420eb0f4a8a581ef.png)

![](../images/2125968abb06f9d6.png)

a. Objects created together with the stage cannot be added or removed. They are the only objects that can monitor Down events.

b. Click [View] to jump to the stage entity's location in the scene and edit it there

### (5) Time Settings

![](../images/1110d9f45a20860f.png)

Configure the initial time and time flow rate when the stage starts; time affects the environment

The maximum flow rate is 1 second = 60 minutes

### (6) Load Optimization

![](../images/9200caff9a587b58.png)

Used to determine load requirements for this Save; high load may prevent some devices from running normally

### (7) Do Not Run If Out Of Range

![](../images/0695d192d390ade7.png)

![](../images/57f56990025de66f.png)

a. While the stage is running, entities with [Load Optimization] enabled will stop running on the player's client when beyond a certain distance

b. Control whether an object is affected via [Object Editing] -> [Load Optimization]

c. For detailed rules, see [Load Optimization](/ys/ugc/tutorial//detail/mhlb1vivioys)

### (8) Aggro Type

![](../images/92987d9c7d8336f3.png)

a. Default: Follows classic aggro rules. Nodes cannot query or modify aggro parameters

b. Custom: Allows aggro settings for objects, creations, classes, and ability units; nodes can query and modify aggro parameters

### (9) Shield Settings

![](../images/76ae885c401e5e4a.png)

Shared Calculation: Damage is absorbed by each unit status.

Individual Calculation: Each unit status calculates absorption separately; the highest absorption applies

### (10) Early Exit Protection

![](../images/789f81466003a5ce.png)

You can configure the corresponding exit protection based on gameplay requirements

Enter a value between 0-60 seconds, which will only take effect during actual gameplay

The actual duration of the exit protection is determined by the time when the stage is generated

### (11) Terrain Settings

"Reduce chance of gaps between terrain" is a **collider optimization toggle** within Terrain Settings

When enabled, this option reduces **the probability of gaps between adjacent terrain colliders**. This prevents issues such as characters getting stuck, sinking, or clipping at tile seams, ensuring smoother movement across terrain

![](../images/d5cd1070a3041679.png)

> **Note:**When this is enabled, **ray detection precision in the scene may be affected**. For stages that utilize rray detection logic (such as trigger sensing or skill hit detection), we recommend that you conduct practical testing after implementation to ensure that gameplay performance aligns with expectations

| Status | Effect |
| --- | --- |
| **On** | Reduces gaps between terrain colliders for smoother movement; however, may affect ray detection |
| **Off** | Maintains default collider precision, does not affect ray detection |

> We suggest that you enable this for stages that revolve around**terrain travel, parkour/platforming, and moving platforms**; as for stages that rely heavily on **ray detection**in their gameplay (such as arrow hit detection and visibility checks), we recommend that you turn it off or perform ample testing should you do choose to enable it

## 2. Faction

![](../images/a144308cb492830d.png)

Used to set the player's current faction. For details, see [Factions](/ys/ugc/tutorial//detail/mhe1ixri46ta)

## 3. Spawn Point

![](../images/a8a76003b552e69c.png)

Set the player's spawn point

### (1) Share Spawn Point

When enabled, different players may use the same spawn point

### (2) Spawn Point Name

You can customize the name of this spawn point to differentiate it from others

### (3) Apply to Character Template

Choose which player templates can use this spawn point

### (4) Select Point

Select a Preset Point in the stage and set it as the Spawn Point. For details, see [Preset Points](/ys/ugc/tutorial//detail/mhdyy7ico090)

### (5) Add Spawn Point

You can add additional Spawn Points; new Spawn Points function exactly the same as the default Spawn Point 1

## 4. Revive Point

![](../images/42dea09e89a6ca68.png)

Set the player's Revive Point. The Revive Points interface is empty by default. Click [Add Revive Points] to add Revive Point 1

(1) Priority: Revive Points with higher priority are used first; larger numbers indicate higher priority

(2) Select Point: Choose a Preset Point in the stage and set it as a Revive Point

## 5. Player Count Settings

![](../images/23de8dab6895c1d8.png)

Purpose of grouping:

1.During matchmaking, if a team exceeds the group's maximum player limit, the stage cannot be matched2.In a room, players must meet the required group size to start the game

Quick Apply Current Faction Data: After clicking Apply, groups are created based on the number of players in each faction

*Player Count Type*: Determines the player-count rule for this group

3.*Fixed Player Count*: The group size is fixed4.*Custom Player Count*: The group size can vary

![](../images/c4191ce9bc3cb5f6.png)

*Number of People*: The number of players in this group

*Players Included*: Configure players with the corresponding IDs for this group

*Required Group*: When disabled, the game can start even without this group

### Current Matching Strategy:

First, prioritize placing players into the necessary groups where the current number of players is closest to meeting the minimum player requirement.Then, prioritize placing players into the necessary teams.After all necessary teams are full, place players sequentially into the groups.

## 6. Loading Screen

![](../images/e63d696c8f4ee174.png)

Edit what appears on the loading screen when entering the stage  
*Select Resources:* Upload an image to use as the loading interface background

![](../images/5c5d70b71201a5b4.png)

*Title and Description*: Text displayed on the loading interface

![](../images/d7314f2845a02904.png)

## 7. Settlement

![](../images/b5e7f53c0f6da968.png)

Configure the Settlement Screen

Settlement Screen Type:

![](../images/93ee6566209a946c.png)

5.Personal Settlement: The settlement screen uses an individual performance layout6.Faction Settlement: The settlement screen uses a faction score layout

*Enable In-Game Ranking*: Determines the display order for Personal/Faction Settlement; ranking values are set via nodes

![](../images/71f7f876b51cb0ab.png)

*Related Node Graphs*: If a node graph configures settlement-related nodes, you can jump to it here

## 8. Terrain Navigation

![](../images/248e202b4f3864e2.png)

The navmesh affects the pathfinding capabilities of creations. It is recommended to re-bake the navmesh whenever you modify the terrain or placement of static objects.   
  
If there is no need for creation pathfinding, you can disable the upload switch

## **9. Optimization Option**s

![](../images/6a7fb6e330775df2.png)

Optimizes collision trigger detection for off-screen objects and unexpected player exits. This may increase overall system load
