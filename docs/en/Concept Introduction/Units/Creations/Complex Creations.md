---
title: Complex Creations
path_id: mh4ejirxhneu
updated_at: 2026-09-16 14:17:23
category: Concept Introduction/Units/Creations
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh4ejirxhneu
---

# I. Definition of Complex Creations

To meet the needs of Craftspeople who want greater freedom when customizing Creation models and behaviors, we have introduced some Creations that can have their autonomous logic edited and can have custom skills edited like characters. These Creations are referred to as *Complex Creations.*

# II. Creating Complex Creations

Like other Entities, open the Entity Placement Interface, select a specific item under the Complex Creations tab, then click it or drag it into the Scene to create the Complex Creation

![](../../../images/14cfc8068bb63a39.png)

# III. Differences Between Complex and Basic Creations

This section lists only the differences between Complex Creations and Basic Creations. For the definitions of all other parameters, refer to the [Creations](/ys/ugc/tutorial//detail/mhufqo0c0tqw).

## 1. Basic Information

### (1) Transformation

![](../../../images/3aecbdaf4a5ac95c.png)

Complex Creations support scaling, with an adjustment rate of 0.5–3.0.

### (2) Model

![](../../../images/f8d25f8f3e1a0ea6.png)

Complex Creations can adjust Preset Status. Preset Status affects various aspects of a Complex Creation, including but not limited to initial actions

## 2. Specialized Settings

### (1) Creation Status Decision Node Graph

![](../../../images/3d80421e0cf06a4b.png)

Complex creations can be configured with a *Creation Status Decision Node Graph*. Once configured here, Complex Creations will continuously access it and enter different autonomous logic statuses based on the configured conditions

In the *Creation Status Decision Node Graph*, you can reference the *Creation Status Node Graph*. In the Creation Status Node Graph, you can have Creations execute actual Skills and tactics.

### (2) Creation Skill Management

![](../../../images/99293ea54c54eaf8.png)

Complex Creations can use Custom Skills. Skills must be defined before they can be used in the Creation Status Node Graph.

Complex Creation Skills are edited similarly to Character Skills. Refer to [Skills](/ys/ugc/tutorial//detail/mho81frl33im).

The skill usage of Complex Creations is subject to three cooldown timers: *Global Skill CD, Skill CD, Skill Group CD*. A Skill can only be used when all three timers are ready

Click Details Editing to open the Skill Details Interface for Creations

#### a. Skills

![](../../../images/52ea684cc77f57a1.png)

**Basic Settings**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *ID* | Referenced in the Status Node Graph. Used when calling this Skill for actual execution |
| *Referenced Skill* | Custom Skills for Complex Creations can only reference Skills that they can use |

**CD Configuration**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initial CD Start Point* | Available Options:  **In Battle**: The initial cooldown starts when entering battle.  **Out of Battle**: The initial cooldown starts when exiting battle. |
| *Initial CD Range (s)* | Configure a random time within the specified range to be the effective cooldown time. After the Creation is created, it will start using the skill only after the effective cooldown time has passed. |
| *Default* *CD Range (s)* | Select a random time within the configured range as the Actual Cooldown Time.  After the Creation uses this Skill, it cannot use it again during the Actual Cooldown Time |
| *CD Group* | If a Skill is configured with a CD Group, it can only be used when its own Skill CD, Global Skill CD, and Skill Group CD are all ready |
| *CD Trigger Timing* | Select an enum value.  When Skill ends: Start counting CD after the Skill finishes.  When Skill starts: Start counting CD when the Skill starts |
| *Trigger Global Skill CD* | Whether this affects the Global Skill CD |
| *Ignore Global Skill CD* | If checked, ignore the Global Skill CD restriction in the skill usage conditions |

#### b. Cooldown Time

![](../../../images/95db2ec1f2a42559.png)

**Basic Settings**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Global CD (s)* | All Skills for the current Complex Creation are affected by the Global Cooldown Time |

**CD Group Configuration**

You can add CD Groups as needed by clicking [Add CD Group].

CD Group: Links the cooldown timers of multiple Skills. Skills in the same CD Group can only be used after their cooldown timers are ready

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *CD Group ID* | Can be referenced in Nodes at runtime |
| *CD Group Name* | Can be selected in the specified editor |
| *CD Range (s)* | Configure the cooldown time range |

### (3)**Autonomous Logic Parameter Settings**

![](../../../images/a14d8ce480bb1fa9.png)

Complex creations require the definition of *Autonomous Logic Parameter Templates*, which can be applied in the Creation Status Node Graph

These parameters are the basic requirements for the combat behavior of Complex Creations

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initial Effective Autonomous Logic Parameter Template* | The *Autonomous Logic Parameter Template* that is active by default at runtime. Maximum 1.  You can select an option from the dropdown enum to edit the active state. After editing, the active state is synced to the corresponding template's Editing Tab  ![](../../../images/d09de7a530249e7e.png)![](../../../images/0f70d6052bcd812a.png) |
| *\*Autonomous Logic Parameter Template List* | Lists all *Autonomous Logic Parameter Templates* configured for this Complex Creation |

Click Details Editing to open the Details Interface for *Autonomous Logic Parameter Templates*

![](../../../images/37923d69d2ba0f86.png)

Enumerate all *Autonomous Logic Parameter Templates* defined for this Complex CreationClick ![](../../../images/1704d94488cba320.png) to add an*Autonomous Logic Parameter Template*. It is inactive by default"Template\_X", where X is the *Autonomous Logic Parameter Template* ID. As a Node input, different Autonomous Logic Parameter Templates can be used to adjust states

#### a. Basic Settings

![](../../../images/f3783fae5b27a72a.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initially Effective* | If enabled, this *Autonomous Logic Parameter Template* takes effect immediately when the Complex Creation is Created |

#### b. Battle Settings

![](../../../images/05698cc9c0bc610a.png)

Range Detection

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Detection Range* | When Hostile Entities are within this range, the Creation can get their information and enter battle with them as Targets |
| *\*Preview Range* | When enabled, you can view the Detection Range of the Creation Entity in the Editing Interface |

FOV Detection

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *FOV Type* | Provides enums for FOV Cone and Full FOV. Selecting one also updates the range editing parameters |
| *FOV Cone - Cone Distance* | Configure the radius distance of the FOV Cone |
| *Full FOV - FOV Detection Radius* | Configure the sphere radius |
| *\*Preview Range* | When enabled, you can view the FOV Detection Range of the edited Creation Entity in the Editing Interface |

*Chain Battle Distance (m)*: When a Creation Entity enters battle, other Creation Entities within this area that are not in battle will also enter battle

*\*Preview Chain Battle Distance*: When enabled, you can view the chain battle area of the edited Creation Entity in the Editing Interface

#### c. Out-of-Battle Settings

![](../../../images/dbdc8e30b1d7fbab.png)

Rules that define when a Creation automatically leaves battle after engaging a hostile Entity during runtime

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Out-of-Battle Distance (m)* | When the distance between a Creation in combat and its target Entity exceeds the configured value, the Creation leaves battle |
| *\*Preview Out-of-Battle Distance* | When enabled, the editing interface displays the Out-of-Battle Distance of the Creation Entity currently being edited |
| *Leave Battle on Pathfinding Failure* | If no valid path exists between a Creation in combat and its target Entity, the Creation leaves battle |
| *Leaving Battle Delay (s)* | When there is no valid path between a Creation in combat and its target Entity, the Creation will leave battle following the specified delay |

#### d. Territory Settings

![](../../../images/13b92dd77693c200.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Territory* | Supports None, Sphere, and Cylinder configurations. Size parameters are required.  The Territory is centered on the Creation's spawn location and does not move with the Creation.  The Creation's movement range is constrained within the Territory. This restriction can be adjusted via Nodes.  ![](../../../images/e9fb4c2bf79279b1.png)  ![](../../../images/5089b60c7e14c0fb.png)  ![](../../../images/98c7ceee74fc7c9a.png) |
| *\*Preview Territory Range* | When enabled, the configured Territory range is displayed in the Editing interface |
| *Leave Battle When Player Leaves Area* | When enabled, the Creation leaves battle when the target Entity leaves the specified area |
| *Leaving Battle Delay (s)* | After the target Entity leaves the Territory range, the Creation leaves battle following the specified delay |

### (4) Patrol **Settings**

Please refer to the Patrol section under [General Settings](/ys/ugc/tutorial//detail/mh3rgo0c16c8)

# IV. Managing Complex Creation Behaviors Through Local Filter

## 1. Creation Status Decision Node Graph

The Construct State Decision Node Graph starts with the **Execute only by sequence** node. Each output pin connects to the **Switch to self execution status** node to execute different behaviors as needed. If the entry conditions of the preceding state are not met, it will first attempt to enter *Failed Execution*. If the conditions are still not met, it will try to execute the state of the next output angle. The Creation Status Decision Node Graph continuously executes. If the conditions of the preceding states are met, the complex creation will immediately switch execution states and execute the preceding state's node graph. If the conditions are not met, the complex creation may not execute any state node graph.

**Example**: During runtime, start from branch 1 and first evaluate node A. If node A's conditions are met and it executes successfully, nodes B and C will not be executed subsequently. If node A's conditions are not met, continue evaluating node B. If neither nodes A nor B meet the conditions, start evaluating node C from branch 2.

If the creation is currently executing the status node graph within node C, but the execution conditions of node A are met, the complex creation will immediately switch to executing the state node graph within node A.

![](../../../images/cf23dded090c29e1.png)

Execute only by sequence

![](../../../images/95d686ea8c321f03.png)

Switch to self execution status

![](../../../images/de66b5a8a16d141d.png)

## 2. Creation Status Node Graph

The input and output pins of the Creation Status Node Graph support only single-line connections

The Creation Status Node Graph represents continuous behavior. While a Complex Creation remains in a given execution state and is not switched by the Status Decision Node Graph, it continuously executes the configured behavior in the Creation Status Node Graph

For example, when a Complex Creation switches to the Creation Status Node Graph shown below via the Status Decision Node Graph, this Node Graph will continue its execution

![](../../../images/b381a2663ce8cace.png)

Tactic Nodes can be configured in a Creation Status Node Graph. They are divided into three types: Ground Tactics, Aerial Tactics, and General Tactics. Ground Tactics can only be executed when the Creation is on the ground, while Aerial Tactics can only be executed when the Creation is airborne. General Tactics are not affected by the Creation's airborne state and can be executed in either state

Whether a Creation is airborne is determined by whether it has the *Creation Levitation* Unit Status effect. A Creation with this Unit Status effect is considered airborne; otherwise, it is considered to be on the ground
