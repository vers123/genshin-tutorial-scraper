---
title: Execution Nodes
path_id: mhw2560p865k
updated_at: 2026-09-18 19:54:13
category: Node Introduction/Client Nodes/Creation Status Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhw2560p865k
---

# I. General

## **1. Continue Executing Previous Frame Behavior**

![](../../../images/835ee9896feb3ba5.png)

**Node Functions**

If the Tactic executed in the previous frame has not finished, execution will continue until it completes

If the skill was executed in the previous frame, no process will happen

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **2. Execute Skill**

![](../../../images/36c1174bd7b6a816.png)

**Node Functions**

Execute the skill with the specified skill sequence number

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Skill ID | Integer |  |

# II. Tactics

## **1. Tactic: Ground Confrontation**

![](../../../images/4c8be76c1ad229d8.png)

![](../../../images/057787df5dd706b4.png)

**Node Functions**

The Creation executes a Paving Standoff. It uses four-direction Motion Tactics, with five directions: idle/forward/backward/left/right. Use this to simulate a sustained face-off with the Player.

You can use probability settings to create motion behaviors such as moving left and right around the Player, or preferring to move forward and avoiding moving backward. It also includes settings for adjusting distance to the Player and for obstacle avoidance.

Essentially, it just decides a direction; there is no specific Target Point

Execution Conditions:

Requires the unit or the target to be within the Territory RangeIf *Reachable via Pathfinding* is enabled and the unit is not airborne, Tactics will end when Pathfinding fails

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Inner Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Outer Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Direction Change Interval | Floating Point Numbers | Transition Time when changing directions. Default is 0. Each time the direction changes, the Creation stays still for the configured time, then switches to the new direction  Switching from another direction to Rest, or from Rest to another direction, does not count as an direction change |
| Input Parameter | Minimum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Maximum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Is Pathfinding Always Achievable? | Boolean |  |
| Input Parameter | Whether Restricted by Territory | Boolean | If set to Yes and there are no valid points within the Territory, this Tactic will end immediately |
| Input Parameter | Cancel Trigger Weight by Movement | Floating Point Numbers |  |
| Input Parameter | Forward Movement Weight | Floating Point Numbers | Affects Motion weights only in the Normal Mode. Even if you set the direction's weight to 0, the character may still move in that direction due to obstacle avoidance or unexpected conditions |
| Input Parameter | Backward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Leftward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Rightward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Lateral Obstacle Avoidance Distance | Floating Point Numbers | If the configured value is less than 0, the obstacle avoidance function will not run |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **2. Tactic: Ground Escape**

![](../../../images/cf55a37c1f4906e7.png)

![](../../../images/06769fa281b3ea45.png)

**Node Functions**

The Creation executes a Paving Escape, a tactic for fleeing from the Target. It attempts to turn its back to the Target and move farther away.

Allows you to configure multiple segments of Escape Motion. Each segment/run calculates one escape point.

Execution Conditions:

When the Creation is not in CD, and is inside its Territory, it will trigger fleeing behavior once their distance to the Target is less than *Flee Trigger Distance*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Escape Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Maximum Escape Angle | Floating Point Numbers | Uses twice the absolute value of the configured value as the actual flee point selection range |
| Input Parameter | Minimum Escape Segments | Integer |  |
| Input Parameter | Maximum Escape Segments | Integer |  |
| Input Parameter | Minimum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Escape Trigger CD | Floating Point Numbers |  |
| Input Parameter | Clear Aggro and Cancel Tactic After Countdown | Floating Point Numbers | If the value is less than 0, the Tactic will not be executed.  Otherwise, the timer starts from when the Tactics are entered. If it times out, battle will be forcibly ended.  After the Tactics execution ends, battle will be immediately ended |
| Input Parameter | Whether Restricted by Territory | Boolean | If set to Yes and there are no valid points within the Territory, this Tactic will end immediately |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **3. Tactic: Ground Idle Roaming**

![](../../../images/50c02b9b9898935f.png)

**Node Functions**

The Creation executes a Paving Roam, walking randomly within the AoE

Execution Conditions:

Affected by *Creation Underclock*, Creations that are too far from the Character will not enter this TacticSelect a suitable Target Point

Point Selection Rules:

Unlike most tactics, the point-selection logic for the *Paving Roam* tactic runs when it is **potentially** possible to execute *Paving Roam*, but before you Enter it

Because choosing the right Target Point is one of the requirements for entering this Tactic

Upon entering a Tactic, execute the Motion quest immediately. Keep it running until the Motion stops (when you reach the destination or hit an obstacle). Then apply the CD and exit the TacticIf a Creation's current Location is already outside the *Roaming Radius* AoE, the *Paving Roam* Tactic selects a point in the direction from the current location toward the Spawn Point, at a distance equal to the *Roaming Radius*, as the Target PointIf Pathfinding is supported, it will be used to check whether the Target Point is valid

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Speed | Enumeration | Walk and Run |
| Input Parameter | Idle Roaming Radius | Floating Point Numbers | Farthest distance you can roam from the Spawn Point |
| Input Parameter | Minimum Idle Roaming Interval | Floating Point Numbers | The cooldown time between roaming behaviors. Each time roaming ends, the system randomly selects a CD between [Minimum Idle Roaming Interval, Maximum Idle Roaming Interval] and uses it as the new CD. This Tactic will not be executed during cooldown periods |
| Input Parameter | Maximum Idle Roaming Interval | Floating Point Numbers |  |
| Input Parameter | Single Minimum Idle Roaming Distance | Floating Point Numbers | Roam Distance from Current Point |
| Input Parameter | Single Maximum Idle Roaming Distance | Floating Point Numbers | Roam Distance from Current Point |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **4. Tactic: Ground Pursuit**

![](../../../images/22f85be33d424245.png)

![](../../../images/88ee4c539364b4d5.png)

**Node Functions**

The Creation executes a Paving Pursuit

Target Pursuit Tactic automatically selects a suitable location near the Target as the Target Point

Execution Conditions:

[Required]

1.Has a Target2.Not airborne3.This unit or the target is within the Territory Range

[Meet any one of the Conditions]

1.If this unit is not currently in this Tactic and the distance between the unit and the Target is within [*Minimum Pursuit Trigger Distance*, *Maximum Pursuit Trigger Distance*], the unit will enter this Tactic2.When already in the Tactic, the unit will continue to execute the Tactic only if the distance between this unit and the Target is greater than the *Stop Pursuit Distance*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Type** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Minimum Pursuit Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Pursuit Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Stop Pursuit Distance | Floating Point Numbers |  |
| Input Parameter | Outer Ring Pursuit Speed | Enumeration | Walk and Run |
| Input Parameter | Inner Ring Radius | Floating Point Numbers | Inner Ring Boundary Radius |
| Input Parameter | Inner Ring Pursuit Speed | Enumeration | Walk and Run |
| Input Parameter | Single Pursuit Duration | Floating Point Numbers | If value less than 0, do not execute the Tactic |
| Input Parameter | Tactical Instance CD | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **5. Tactic: Stand Still**

![](../../../images/1a34140644223f81.png)

**Node Functions**

The Creation executes the Idle behavior

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **6. Tactic: Return to Spawn Point After Leaving Battle**

![](../../../images/b745edcabdfb3c5a.png)

**Node Functions**

The Creation returns to the Spawn Point after leaving battle

A tactic that makes a unit return to the initial point when leaving battle. While this tactic is running, the Aggro system is disabled and will not be re-enabled until the tactic ends.

Execution Conditions:

3.This is only available in the pre-battle and out-of-battle phases. Place it first in your pre-battle Tactics so the Aggro system switches to it as soon as the battle ends

Select Target Points:

The Target Point is selected on the frame you enter the Tactic, and it will not be edited while the Tactic is being executed

Check the following conditions in order. When a condition is met, set the Target Point based on that item.

a.When the [Execute a Patrol] Tactic is performed and *Set End Point to Spawn Point* is enabled, the new Spawn Point will be used as the Target Pointb.Set the Spawn Point as the Target Point

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Movement Speed | Enumeration |  |
| Input Parameter | Teleport Back to Spawn Point? | Boolean |  |
| Input Parameter | Force Teleport Trigger Distance | Floating Point Numbers | Prerequisite: Set *Teleport Back to Spawn Point* to Yes  When this unit's distance from the Spawn Point is greater than or equal to the configured distance, a teleport will be forcibly triggered |
| Input Parameter | Force Teleport Trigger Time | Floating Point Numbers | Prerequisite: *Teleport Back to the Spawn Point* must be set to Yes  If the Tactic duration exceeds the configured timer and this unit has not yet returned to the Spawn Point, a teleport will be forcibly triggered |
| Input Parameter | Disable HP Recovery After Leaving Battle | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **7. Tactic: Rotate to the Target Entity**

![](../../../images/1fa73c095a1f4220.png)

**Node Functions**

The Creation rotates to face the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers |  |
| Input Parameter | Use Rotation Animation | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **8. Tactic: Rotate to the Specified Direction**

![](../../../images/2b4383f7c8ded6aa.png)

**Node Functions**

The Creation rotates to the Specified Orientation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Orientation | 3D Vector |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers |  |
| Input Parameter | Use Rotation Animation? | Boolean |  |
| Input Parameter | Rotation Direction | Enumeration | Default: use the shortest angle  Clockwise  Counterclockwise |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **9. Tactic: Rotate by Specified Angle**

![](../../../images/154f81b19e06b8d7.png)

**Node Functions**

The Creation rotates by the specified angle, and the Angular Velocity may have minor deviations during actual operation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Specified Angle | Floating Point Numbers |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers | If set to a positive value, rotates clockwise;  if set to a negative value, rotates counterclockwise; |
| Input Parameter | Use Rotation Animation? | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **10. Tactic: Move to the Target Position**

![](../../../images/7dd70ddf222c6056.png)

**Node Functions**

The Creation moves to the Target Point

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Position | 3D Vector |  |
| Input Parameter | Arrival Detection Range | Floating Point Numbers |  |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Turn Speed | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **11. Tactic: Move to the Target Entity**

![](../../../images/4adcdefc9983a3b5.png)

**Node Functions**

The Creation moves to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Arrival Detection Range | Floating Point Numbers | If the Distance to the Target Entity is less than or equal to the configured value, it is considered arrived |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Turn Speed | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **12. Tactic: Execute Patrol**

![](../../../images/bb261b0e8202dbbd.png)

**Node Functions**

A tactic setting where the Creation executes its patrol , using its configured Patrol Template to drive its motion.

Execution Conditions:

4.The Creation is configured with a Patrol Template5.Patrol Template referenced by Tactics; the referenced path data is not empty

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Patrol Template ID | Integer |  |
| Input Parameter | Start From the Nearest Waypoint? | Boolean |  |
| Input Parameter | Set End Point as Spawn Point | Boolean | Affects the *Return to Spawn Point After Leaving Battle* Tactic |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **13. Tactic: Aerial Landing**

![](../../../images/b83354cd9e76a762.png)

**Node Functions**

The creation performs an aerial landing action. It calculates a landing point based on the configured angle, then moves toward that point.

The tactic is considered complete when the vertical distance between the creation’s current position and the landing point is less than the *Height Threshold for Landing Detection*.

Execution Conditions:

The creation has the Unit Status Effect *Creation Levitation*.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean | Default: Yes |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |
| Input Parameter | Minimum Landing Angle from Horizontal | Floating Point Numbers |  |
| Input Parameter | Maximum Landing Angle from Horizontal | Floating Point Numbers |  |
| Input Parameter | Height Threshold for Landing Detection | Floating Point Numbers | Height Above Ground |
| Input Parameter | Movement SPD | Enumeration | Walk, Run |
| Input Parameter | Overwrite Movement SPD | Floating Point Numbers |  |
| Input Parameter | Override Turn Speed | Floating Point Numbers |  |
| Input Parameter | Maximum Descent Duration | Floating Point Numbers | If the value is less than 0, the tactic is not executed. |

## **14. Tactic: Aerial Pursuit**

![](../../../images/0ea3e8d80603463b.png)

**Node Functions**

The creation performs an aerial pursuit action.

While pursuing a target, the creation automatically selects a suitable position around the target as its destination.

Execution Conditions:

[Required]

1.The creation has the Unit Status Effect *Creation Levitation*2.The creation has a target3.An FOV Detection Area is configured in the creation's Entering Battle settings.

[Meet any one of the Conditions]

1.This tactic is not currently active. The creation enters it only when the horizontal distance to the target is greater than *Horizontal Distance to Trigger Pursuit*, or the height difference is greater than *Height Difference to Trigger Pursuit*2.This tactic is already active. The creation continues executing it only when the horizontal distance to the target is greater than *Horizontal Distance to Stop Pursuit*, or the height difference is greater than *Height Difference to Stop Pursuit*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean | Default: Yes |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can skill be interrupted | Boolean | Default: No |
| Input Parameter | Horizontal Distance to Trigger Pursuit | Floating Point Numbers |  |
| Input Parameter | Horizontal Distance to Stop Pursuit | Floating Point Numbers |  |
| Input Parameter | Use Elevation Difference When Pursuing | Boolean | When set to No, both *Height Difference to Trigger Pursuit* and *Height Difference to Stop Pursuit* are ignored. |
| Input Parameter | Height Difference to Trigger Pursuit | Floating Point Numbers | If the value is less than 0, this setting is ignored. |
| Input Parameter | Height Difference to Stop Pursuit | Floating Point Numbers | Same as above. |
| Input Parameter | Minimum Vertical Offset from Target | Floating Point Numbers | Height offset range for the target point. |
| Input Parameter | Maximum Vertical Offset from Target | Floating Point Numbers | Same as above. |
| Input Parameter | Movement SPD | Enumeration | Walk, Run |
| Input Parameter | Overwrite Movement SPD | Floating Point Numbers |  |
| Input Parameter | Override Turn Speed | Floating Point Numbers |  |
| Input Parameter | Single Pursuit Maximum Duration | Floating Point Numbers | If the value is less than 0, the tactic is not executed. |
| Input Parameter | Tactical Instance CD | Floating Point Numbers |  |

## **15. Tactic: Aerial Escape**

![](../../../images/234ee91547352c0b.png)

**Node Functions**

The creation performs an aerial escape action. This tactic causes the creation to flee its target by attempting to turn away and move farther away.

You can configure multiple escape movement segments. The number of segments ranges from [*Minimum Escape Segments*, *Maximum Escape Segments*).

The system calculates an escape position for each segment or attempt. Both azimuth and pitch angle settings are supported.

Execution Conditions:

The creation has the Unit Status Effect *Creation Levitation*The tactic is not on cooldownThe creation is within its territoryThe distance to the target is less than *Escape Trigger Distance*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean | Default: Yes |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can skill be interrupted | Boolean | Default: No |
| Input Parameter | Escape Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Movement SPD | Enumeration | Walk, Run |
| Input Parameter | Overwrite Movement SPD | Floating Point Numbers |  |
| Input Parameter | Override Turn Speed | Floating Point Numbers |  |
| Input Parameter | Maximum Escape Azimuth | Floating Point Numbers | The actual escape point search range is twice the absolute value of the configured value. |
| Input Parameter | Minimum Escape Pitch Angle | Floating Point Numbers | Escape pitch angle range. Negative values indicate upward angles, while positive values indicate downward angles. |
| Input Parameter | Maximum Escape Pitch Angle | Floating Point Numbers | Same as above. |
| Input Parameter | Minimum Escape Segments | Integer |  |
| Input Parameter | Maximum Escape Segments | Integer |  |
| Input Parameter | Minimum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Upward Escape Weight | Floating Point Numbers |  |
| Input Parameter | Downward Escape Weight | Floating Point Numbers |  |
| Input Parameter | Turn Toward Target When Escape Ends or Is Blocked | Boolean | Default: Yes |
| Input Parameter | Escape Trigger CD | Floating Point Numbers |  |
| Input Parameter | Clear aggro and cancel tactic after countdown | Floating Point Numbers | If the value is less than 0, the tactic is not executed.  Otherwise, the timer starts when the tactic begins. When the time limit is reached, the entity is forced to exit combat.  The entity exits combat immediately when the tactic ends. |
| Input Parameter | Whether restricted by territory | Boolean | When set to Yes, the tactic ends immediately if no valid positions exist within the territory. |

## **16. Tactic: Aerial Confrontation**

![](../../../images/8000568d662bb27e.png)

**Node Functions**

The creation performs an aerial confrontation action. This multidirectional movement tactic allows the creation to randomly select a destination within the configured probability space around the target and move toward it.

Supports three-dimensional movement behaviors such as pursuing the player, moving away from them, and circling them from either side. It also provides settings to adjust the creation’s distance from the player and to avoid obstacles.

Execution Conditions:

The creation has the Unit Status Effect *Creation Levitation*The creation or its target is within the territoryThe creation's current Preset State supports six-directional movement

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean | Default: Yes |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can skill be interrupted | Boolean | Default: No |
| Input Parameter | Inner Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Outer Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Minimum Standoff Height | Floating Point Numbers | Height Above Ground |
| Input Parameter | Maximum Standoff Height | Floating Point Numbers | Same as above. |
| Input Parameter | Optimal Height Above Ground | Floating Point Numbers | The greater the difference between the optimal height and the actual height, the more likely the unit is to move in the opposite direction. |
| Input Parameter | Minimum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Maximum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Whether restricted by territory | Boolean | When set to Yes, the tactic ends immediately if no valid positions exist within the territory. |
| Input Parameter | Limit Height Based on Reference Ground | Boolean | *Minimum/Maximum Standoff Height* only takes effect when this setting is set to Yes, or when *Optimal Height Above Ground* is greater than 0. |
| Input Parameter | Cancel Trigger Weight by Movement | Floating Point Numbers |  |
| Input Parameter | Forward Movement Weight | Floating Point Numbers | This only affects movement weights in Normal Mode. Even if a direction's weight is reduced to 0, the unit may still move in that direction due to obstacle avoidance or exceptional circumstances. |
| Input Parameter | Backward Movement Weight | Floating Point Numbers | Same as above. |
| Input Parameter | Leftward Movement Weight | Floating Point Numbers | Same as above. |
| Input Parameter | Rightward Movement Weight | Floating Point Numbers | Same as above. |
| Input Parameter | Upward Movement Weight | Floating Point Numbers | Same as above. |
| Input Parameter | Downward Movement Weight | Floating Point Numbers | Same as above. |
| Input Parameter | Lateral Obstacle Avoidance Distance | Floating Point Numbers | If the configured value is less than 0, obstacle avoidance will not execute. |
| Input Parameter | Ascent Height for Obstacle Avoidance | Floating Point Numbers |  |
| Input Parameter | Maximum Obstacle-Avoidance Angle Relative to Vertical | Floating Point Numbers | When the angle between the movement direction and the vertical direction exceeds this value, the unit stops instead of flying upward to bypass the obstacle. |
| Input Parameter | Overwrite Movement SPD | Floating Point Numbers |  |
| Input Parameter | Overwrite Movement Rotation SPD | Floating Point Numbers |  |
| Input Parameter | Override On-The-Spot Turn Speed | Floating Point Numbers |  |
| Input Parameter | Movement SPD | Enumeration | Walk, Run |
| Input Parameter | Minimum Single Movement Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Single Movement Distance | Floating Point Numbers |  |

## **17. Tactic: Aerial Idling**

![](../../../images/ac6c323210565a01.png)

**Node Functions**

The creation performs an aerial idling action, moving randomly within a specified area.

Execution Conditions:

The creation has the Unit Status Effect *Creation Levitation*When affected by *Creation Frequency Reduction*, creations that are too far from the player character cannot enter this tacticA valid target point has been selected

Point Selection Rules:

Unlike most tactics, the target point selection logic for *Aerial Idling* runs when the tactic **may** be executable but has not yet been entered.

This is because selecting a valid target point is one of the conditions for entering the tactic.

Once the tactic is entered, the creation immediately begins the movement task. When the movement task ends, either because the creation reaches its destination or collides with an obstacle, the cooldown is applied, and the creation exits the tactic.If the creation’s current position is outside the *Idle Roaming Radius* or *Height Limit Relative to Spawn Point*, or if the tactic repeatedly fails to select a valid target point, *Aerial Idling* uses the default target point insteadDefault Target Point: A point whose height offset from the spawn position equals the average of *Minimum Height Relative to Spawn Point*and *Maximum Height Relative to Spawn Point*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean | Default: Yes |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can skill be interrupted | Boolean | Default: No |
| Input Parameter | Movement SPD | Enumeration | Walk, Run |
| Input Parameter | Overwrite Movement SPD | Floating Point Numbers |  |
| Input Parameter | Override Turn Speed | Floating Point Numbers |  |
| Input Parameter | Idle Roaming Radius | Floating Point Numbers | Maximum Idle Roaming distance from the spawn point. |
| Input Parameter | Minimum Height Relative to Spawn Point | Floating Point Numbers |  |
| Input Parameter | Maximum Height Relative to Spawn Point | Floating Point Numbers |  |
| Input Parameter | Minimum Idle Roaming Interval | Floating Point Numbers | Idle Roaming cooldown. Each time the tactic ends, a duration is randomly selected from [*Minimum Idle Roaming Interval*, *Maximum Idle Roaming Interval*] and used as the cooldown. This tactic cannot be executed during the cooldown. |
| Input Parameter | Maximum Idle Roaming Interval | Floating Point Numbers |  |
| Input Parameter | Single Idle Maximum Duration | Floating Point Numbers | A single Idle Roaming action automatically stops after exceeding this duration. |
| Input Parameter | Minimum Idle Roaming Distance | Floating Point Numbers | Idle Roaming distance from the current position. |
| Input Parameter | Maximum Idle Roaming Distance | Floating Point Numbers | Idle Roaming distance from the current position. |
