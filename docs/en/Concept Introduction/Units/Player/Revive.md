---
title: Revive
path_id: mh8enu00szzc
updated_at: 2026-03-27 14:56:52
category: Concept Introduction/Units/Player
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh8enu00szzc
---

# I. Character Defeat and Revive Description

During gameplay, when all of a *player's* *character entities* are *defeated* (known as the *When All Player's Characters Are Down* state), the revive process will begin.

For player and character entities, the following downed and revive mechanics apply:

*When the Character Is Down*: When a character's HP drops to 0 or when it is forcibly defeated. In Beyond Mode, this also means all player characters are down (because the player only has one character).

*When Character Revives*: A character is revived from the downed state. When all of a player's characters are down, reviving any character will release that player from the downed state.

*When All Player's Characters Are Down*: While the player entity itself cannot be defeated, there exists a concept of all of a player's character entities being downed. In Beyond Mode, having a single character down is the same as all characters being down (as mentioned above, this is because the player only has one character).

Similarly, since the player entity cannot be defeated, there is no concept of reviving the player entity.

# II. Character Revive Process

A typical revive process in Beyond Mode is shown as follows:

1. When a character's HP drops to 0 or it is defeated by other means, the When All Player's Characters Are Down state is triggered.

![](../../../images/de747677f97b3241.png)

2. Revive Interface

The functions of the interface are as follows:

[Revive After ()s] / [Revive at Revive Point]: When a *revive duration* is set in Revive Settings, you can click the [Revive] button after waiting for the specified number of seconds to revive your character at the *revive point.*.

![](../../../images/8bb6116dade6b4cd.png)

![](../../../images/a9d75ca6858e6f72.png)

3. Characters will revive at the revive point after clicking the [Revive] button, when an auto revive is triggered, or when forcibly revived via the server node graph.

At that time, HP will be set to the *HP Percentage After Revive (%)* configured in Revive Settings.

![](../../../images/4b49a8c9b2852a35.png)

# III. Revive-Related Settings

## 1. Revive Settings Entry-Point

![](../../../images/e6f3422866e6f313.png)

Please note that revive settings are set in the [Player Template], and because player entities are generated from player templates, this means different players can have different revive settings.

Example: Player 1 may have a limit of 3 revives, while Player 2 may have no revive limit but must wait 30 seconds between each revive.

## 2. Revive-Related Settings Options

![](../../../images/0b3fca57ba249cae.png)

|  |  |
| --- | --- |
| **Setting Options** | **Descriptions** |
| *Allow Revive* | When set to [No], this player cannot be revived.  Can be toggled dynamically using [Allow/Forbid Player to Revive] in the server node graph. |
| *Show Revive Screen* | When set to [No], the revive interface will not pop up when the player is down.  Note! This means the player cannot be revived through the game's built-in logic and will need custom logic to be revived (e.g., assistance from other characters). Otherwise, they cannot be revived and can only exit the current stage. |
| *Revive Duration (s)* | The time required for the player to revive. After being downed, players must wait for the configured revive duration before they can be revived.  When set to [Auto-Revive]: the player will be revived immediately once the revive duration has elapsed.  The next revive duration can be adjusted through the node graph's [Set Player Revive Duration] node. |
| *Auto Revive* | After being downed, automatically revive after the configured [Revive Duration] without requiring the player to press the [Revive] button. |
| *Revive Limit* | The maximum number of times this player can be revived. When the number of revives exceeds this limit, further revives will not be possible.  The remaining number of revives can be adjusted through the node graph's [Set Player's Remaining Revive Count] node. |
| *Revive Point List* | The default list of viable revive points for this player. When reviving, a revive point will be selected from this list according to the [Revive Point Selection Rules].  The player's revive point list can be dynamically adjusted via the [Activate Revive Point] and [Deactivate Revive Point] nodes in the node graph. |
| *Revive Point Selection Rules* | Determines the rules for selecting a revive point from the current [Revive Point List].  Available options:  Nearest Revive Point: Selects the nearest viable revive point from the downed location.  Most Recently Activated Revive Point: The most recently activated revive point. You can refresh a revive point's activation time by reactivating an already activated point.  Highest Priority Revive Point: Uses the viable revive point with the highest priority in the revive point list. Priority can be configured at each revive point. If multiple points share the same priority, one will be randomly selected.  Random Revive Point: Randomly selects a viable revive point from the revive point list as the revive location. |
| *HP Percentage After Revive (%)* | Character's HP percentage after revive; this value cannot be 0. |
| *Special Knockdown Damage - Max HP Deduction Percentage (%)* | HP percentage deducted when drowning or falling into a bottomless pit. These types of revives do not follow the standard revive process and will not consume revive attempts. |

# IV. Revive-Related Function Nodes

**Revive Character**

![](../../../images/c2e7b6dff80227ed.png)

**Node Type**: Execution

**Node Function**

Revive a specified characterIn Beyond Mode, similar to the [Revive All Player's Characters] function, this will revive the player's characters and remove the Down status from all player characters. This revive will not consume the player's revive uses.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | The specified character entity that needs to be revived |

**Revive All Player's Characters**

![](../../../images/d3b0c872aa133c5f.png)

**Node Type**: Execution

**Node Function**

Revive all of the player's characters.In Beyond Mode, similar to the [Revive Character] function, it will revive the player's characters and remove all characters' Down statuses. You can choose whether to deduct the player's revive uses.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Player entity that needs all characters to be revived. |
| Input Parameter | Deduct Revive Count | Boolean | If [Yes], deducts 1 revive count when reviving. If the revive count is less than 1, this node cannot be executed. |

**Defeat All Player's Characters**

![](../../../images/3b9bb6e04109c13c.png)

**Node Type**: Execution

**Node Function**

Defeating all of a player's characters will put the player in a "When All Player's Characters Are Down" state.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity |

**Set Player Revive Time**

![](../../../images/155ca08ce1a012bb.png)

**Node Type**: Execution

**Node Function**

Modify the specified player's **next revive** time.If the player is currently in the Revive Phase, the current revive duration will not be modified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity |
| Input Parameter | Duration | Floating Point Numbers | Set revive duration in seconds. |

**Set Player Remaining Revives**

![](../../../images/36900aef74bad28d.png)

**Node Type**: Execution

**Node Function**

Modify the remaining number of revives for the specified player.Setting it to 0 will prevent this player from reviving.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity |
| Input Parameter | Remaining Amount | Integer | Set remaining revive uses. |

**Allow/Forbid Player to Revive**

![](../../../images/b8336265e6ce3878.png)

**Node Type**: Execution

**Node Function**

Modify whether a specified player is allowed to revive.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity |
| Input Parameter | Allow | Boolean | Set whether or not reviving is allowed. |

**When All Player's Characters Are Revived**

![](../../../images/457d6a916d2d45b8.png)

**Node Type**: Event

**Node Function**

Triggered when all of the player's characters are no longer in the Down state and have revived. Note that this event will not be triggered if the player's Down state is removed due to character revival.Since the player's recovery from the Down state and revive will also cause characters to recover from the Down state and revive, the [When Character Revives] event will also trigger after this event.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity | Revived player entity. |

**When All Player's Characters Are Down**

![](../../../images/eb9cda93523ee99f.png)

**Node Type**: Event

**Node Function**

Triggered when all of the player's characters are downed.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity | Player entity with all characters down. |
| Output Parameter | Cause | Enumeration | Cause of all player characters being downed.  Including the following reasons  -Node Graph: Defeated by nodes in the node graph.  -Normal Defeat: All of a player's characters downed due to their HP being reduced to 0.  -Abnormal Defeat: Downed due to falling into a bottomless pit, drowning, or other similar reasons. |

**When Player is Abnormally Downed and Revives**

![](../../../images/a51ad00327825530.png)

**Node Type**: Event

**Node Function**

When players are defeated and revived due to falling into a bottomless pit, drowning, or other reasons.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity | Player entity that's defeated due to drowning, falling into a bottomless pit, or similar reasons. |

**When the Character Is Down**

![](../../../images/13a3a49b3a7a7d13.png)

**Node Type**: Event

**Node Function**

Event triggered when a character is downed.Because the player only has one character in Beyond Mode, it will subsequently trigger [When All Player's Characters Are Down]

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity | Character entity that has been defeated due to drowning, falling into a bottomless pit, or similar reasons. |
| Output Parameter | Cause | Enumeration | Causes of Character Down  Includes the following reasons:  -Node Graph: Defeated by nodes in the node graph.  -Normal Defeat: All characters in player team are defeated due to HP reaching 0.  -Abnormal Defeat: Downed due to falling into a bottomless pit, drowning, etc. |
| Output Parameter | Knockdown Entity | Entity | Entity that defeated this character |

**When Character Revives**

![](../../../images/af7c7b000edf671e.png)

**Node Type**: Event

**Node Function**

Events triggered when a character revives.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity | Revived Character Entity |

**Query If All Player Characters Are Down**

![](../../../images/fad2715557d3e31e.png)

**Node Type**: Query

**Node Function**

Check if all of the player's characters are downed.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity Queried |
| Output Parameter | Result | Boolean | Whether Full Team Down |

**Get Player Revive Time**

![](../../../images/d0fdb7237630b484.png)

**Node Type**: Query

**Node Function**

Get the specified player's revive duration.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity Queried |
| Output Parameter | Duration | Floating Point Numbers | Get revive duration. |

**Get Player Remaining Revives**

![](../../../images/df9f0198d0773366.png)

**Node Type**: Query

**Node Function**

Query the player's remaining revive uses.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Target Player Entity Queried |
| Output Parameter | Remaining Uses | Integer | Get remaining number of revive uses. |
