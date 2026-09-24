---
title: Skill Pre-Aim
path_id: mhzz64i25fm4
updated_at: 2026-07-10 18:53:52
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhzz64i25fm4
---

# I. What is Skill Pre-Aim?

The Skill Pre-Aim feature allows creators to configure the aiming phase for MOBA-style hero skills. Pre-aiming results can be queried through the relevant nodes in the skill node graph

There are two types of Skill Pre-Aim: Pre-Aim Before Cast, and Pre-Aim during Cast

Pre-Aim Before Cast can be configured for Instant Skills, Normal Skills, and Combo Skills

Pre-Aim during Cast can be configured for Normal Skills and Hold Skills

![](../../../images/820d59627eb5a6cb.png)

# II. Pre-Aim Before Cast

You can find this setting in the right panel under the corresponding skill type (Instant, Normal, or Combo Skills)

![](../../../images/3cb863a92a9f2f73.png)

## 1. Skill Pre-Aim

Once it is enabled, hold down the skill button to trigger the Pre-Aim function, then release it to cast the skill

![](../../../images/a144142f745694ba.png)

## 2. Detailed Settings

### (1) Basics

![](../../../images/7f0ad44b80f81a46.png)

#### a. Basic Settings

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Base Object* | Can be the skill owner or a specified entity; the center of the pre-aim maximum range is determined by this Base Object |
| *Aiming Area Changes Over Time* | When enabled, the maximum range will change according to the configured parameters over a specified transition time |
| *Radius* | Sets the radius of the maximum boundary cylinder |
| *Height* | Sets the height of the maximum boundary cylinder, extending vertically from the center of the Base Object |
| *Preview Max Pre-Aim Range* | Preview the maximum Pre-Aim range during editing. It will not be displayed during gameplay |
| *Always Show Cursor While Aiming* | When enabled, if the player is using keyboard and mouse, the cursor will appear when they enter Pre-Aim phase during gameplay, and they can aim by moving the cursor |
| *Ray Hit Layer* | Determines where the cursor ray registers hits. The ray only hits the selected hit layers |
| *Max Ray Length* | The maximum length of the cursor ray |

#### b. Aim Result Settings

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Limit Aim Duration* | When enabled, if a single hold reaches the specified maximum Pre-Aim duration, the pre-aim phase is forcibly ended and settled according to the Timeout Result Type |
| *Timeout Result Type* | Executes the corresponding result when the Pre-Aim action times out |
| *Trigger Skill on Completion of Pre-Aim* | Determines whether to trigger the skill through an additional filter judgment when pre-aim completes. If the filter judgment fails, the pre-aim is considered canceled, and the skill will not be triggered |

### (2) Aiming Area

The Aiming Area is mainly used for target filtering, and filtering results can be queried through nodes

A target must have a [Hurtbox] to be included as a valid target in the Aiming Area's filtering process

![](../../../images/7ff76e589c86f9fa.png)

#### a. Basic Settings

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Enable Aiming Area* | When enabled, this generates the corresponding target detection area based on the following parameters. Targets that meet the filtering rules are [Valid Targets], and the top-ranked among them is the [Optimal Target] |
| *Aiming Area Shape* | Sets the shape of the Aiming Area |
| *Aiming Area Changes Over Time* | When enabled, the maximum area will change according to the configured parameters over a specified transition time |
| *Radius* | Sets the radius of the maximum boundary cylinder |
| *Height* | Sets the height of the maximum boundary cylinder, extending vertically from the center of the Mount Target |
| *Mount Target* | Base Object: Sets the Base Object as the center of the Aiming Area.  Skill Owner: Sets the Skill Owner as the center of the Aiming Area.  Cursor Actual Mapped Position: Sets the cursor's actual hit point position on the hit layer as the center of the Aiming Area.  Cursor Mapped Position Within Range: If the cursor's actual hit point on the hit layer exceeds the maximum pre-aim range, a line is drawn to the Base Object. The center of the aiming area is then set to the intersection point of this line and the maximum boundary |
| *Y-Axis Rotation* | Sets the orientation of the Aiming Area  Fixed: Set to a specific angle  Follow Attach Point: Points to the forward direction of the attachment point  Orient to Cursor Mapped Position: Points to the position of the cursor's hit point (unavailable if no cursor hit point exist)  Orient to Cursor: Points to the intersection of the cursor and the plane where the character is located (remains available even if no cursor hit point exists)  Orient to Base Object: Points to the corresponding Base Object  Orient to Skill Owner: Points to the corresponding Skill Onwer |
| *Preview Aiming Area* | Previews the shape of the Aiming Area while editing. It will not display during actual gameplay |

Note: If the Mount Target or the Orientation Object does not exist, the Aiming Area will not be created

#### b. Pre-Aim Target Filtering

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Aiming Priority* | All valid targets in the Aiming Area are sorted based on the selected priority. After sorting, the top-ranked target is the [Optimal Target] |
| *Aiming Target Limit* | Affects the number of Objects shown as [All Valid Targets] in the aiming presentation. The node still returns all valid targets |
| *Can Target Base Object* | When enabled, if the Base Object meets the filtering conditions, it can be selected as a valid target by the pre-aiming area |
| *Can Target Skill Owner* | When enabled, if the Skill Owner meets the filtering conditions, they can be selected as a valid target by the pre-aiming area |
| *Filter by Faction Within Area* | Filters based on hostile or friendly Faction relationship. A target is valid only if it satisfies both the Faction Filter and the Tag Filter |
| *Filter by Tag Within Area* | Filters based on Unit Tags. You can add Unit Tags to character entities through [Add Unit Tag to Entity]  Whitelist: The entity must possess every tag on the whitelist  Blacklist: The entity will be filtered out if it matches any tag on the blacklist |

Note: Certain weapons and summons belonging to basic creations possess active hurtboxes and will be included in the filtering process in the current version. This will be resolved in a future update, after which they will no longer be included in filtering

### (3) Aiming Visuals

![](../../../images/1032c87f0c7faedf.png)

#### a. Range Preview

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Preview Max Pre-Aim Range* | Same as the Preview Max Pre-Aim Range switch in the basic settings |
| *Preview Aiming Area* | Same as the Preview Aiming Area switch in the Aiming Area section |

#### b. Max Pre-Aim Range Effects

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Show Max Pre-Aim Range Effects at Runtime* | When enabled, the corresponding effects circle is displayed at runtime according to the configured parameters, with its radius set to the max pre-aim range radius |
| *Attach Point Name* | Special Effects will be attached to the Attachment Point matching this name |
| *Offset* | The position offset relative to the designated Attachment Point |
| *Max Pre-Aim Range Effect Color* | Adjusting the opacity affects the brightness and thickness of the Special Effect edges |
| *Preview Max Pre-Aim Range Effect* | Previews the max pre-aim range effect while editing |
| *Translucent When Obstructed* | When enabled, it the special effect is obsctructed by other models, it will render as semi-transparent through the obstacles |
| *Show Red Warning When Canceling Pre-Aim on Mobile* | When enabled, moving a finger out of the pre-aim area on mobile devices will turn the max pre-aim circle red |

#### c. Pre-Aim Effects

During the pre-aiming phase, corresponding pre-aiming effects will be displayed according to the configurations (e.g., the maximum skill range indicator, aiming area range indicator, pre-aiming direction indicator, etc.)

![](../../../images/cf69c0a8d73975a4.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Pre-Aim VFX Player Asset* | Requires a Persistent VFX Tool. For specific creation steps, see the later section [Pre-Aim VFX Tool Editing] |
| *Mount Target* | Base Object: Sets the Base Object's position as the effect location  Skill Owner: Sets the Skill Owner's position as the effect location  Cursor Actual Mapped Position: Sets the cursor's actual hit point position on the hit layer as the effect location  Cursor Mapped Position Within Range: If the cursor's actual hit point on the hit layer exceeds the maximum pre-aim range, a line is drawn to the Base Object. The effect location is then set to the intersection point of this line and the maximum boundary  Optimal Target: Sets the Optimal Target's position as the effect location.  Each Valid Target: Sets each valid target's position as the effect location. If multiple valid targets exist, multiple effects will be created |
| *Orientation* | The Orientation of the special effects  Fixed: Set to a specific angle  Follow Attach Point: Points to the forward direction of the attachment point  Orient to Cursor Mapped Position: Points to the position of the cursor's hit point (unavailable if no cursor hit point exist)  Orient to Cursor: Points to the intersection of the cursor and the plane where the character is located (remains available even if no cursor hit point exists)  Orient to Base Object: Points to the corresponding Base Object  Orient to Skill Owner: Points to the corresponding Skill Onwer  Orient to Optimal Target: Points toward the Optimal Target Orient to Each Valid Target: Points toward each individual valid target. If multiple valid targets exist, multiple effects will be created |
| *Enable Outline for Mount Target* | When enabled, an additional outline is displayed on the Mount Unit |

Note: If the Mount Target or the Orientation Object does not exist, the Special Effect will not be created

# III. Pre-Aim During Cast

## 1. Location

Add the [Skill Aim] state to the State Track on the timeline for the corresponding Skill type (Normal Skill or Hold Skill)

When the timeline reaches the Skill Aim state, hold the skill button to pre-aim during the skill, then release to complete pre-aiming. Then this will trigger the corresponding Skill Node Graph

![](../../../images/5054fbff235261bd.png)

## 2. Setting Updates

For this feature, several parameters have been added under the [Basics] tab. All other configurations are the same as Pre-Aim Before Cast section

![](../../../images/ca591ac23164b7e6.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Limit Max Aim Success Count* | Each successful pre-aim completion increases the completed count by 1. Once the maximum success count is reached, the pre-aiming phase ends and cannot be triggered again |
| *Cost to Interrupt Aiming* | When enabled, if the player actively cancels the pre-aiming action, the completed count also increases by 1. Otherwise, canceling the action will not consume a count |
| *Character Skill Node Graph* | When pre-aiming is complete and passes the filter (if configured), the configured Character Skill Node Graph is then triggered |
| *Allow Active Cancellation While Pre-Aiming Is Enabled* | When disabled, triggering pre-aiming no longer displays the cancel area, and this pre-aiming action cannot be actively canceled |

# IV. Pre-Aim VFX Tool Edit

## 1. Location

In the VFX Tool Editing interface, create a Persistent VFX Tool and configure the corresponding effects along the effect timeline

![](../../../images/fe9c5349fa25c032.png)

## 2. Warning Effects Adapted for Pre-Aiming

Under Timeline Editing → Warning Special Effects, new warning effects adapted for pre-aiming have been introduced. These allow you to configure rules changing over time and enable translucency/transparency effect

(Adjusting the opacity of the special effect color will modify the brightness and thickness of the effect edges)

![](../../../images/fa6358d85bc658b2.png)

If the VFX Tool's mount target is set to the Cursor, the VFX filter will not execute

# V. Pre-Aim Nodes

Pre-Aim Nodes can be used in Character Skill Node Graphs and Character Control Skill Node Graphs

## 1. Query Nodes

(1) Query Pre-Aim Termination Cause

Returns three cause types: None, Completed, or Canceled

![](../../../images/bca1fdfb524f09b2.png)

(2) Get Current Active Pre-Aim ID

Returns the ID of the Pre-Aim currently in progress

![](../../../images/5b7d96e6f53bfeaa.png)

(3) Get Pre-Aim Duration

Returns the final aim duration of the specified Pre-Aim ID. If Pre-Aim is still in progress, the duration updates in real time

![](../../../images/abebc7550e093e19.png)

(4) Get Pre-Aim Result

a. On-Hit Location: The actual coordinates hit by the cursor

b. Position Within Range: If the cursor's actual hit point on the hit layer exceeds the maximum pre-aim range, a line is drawn to the Base Object. The return location is then set to the intersection point of this line and the maximum boundary

c. Optimal Valid Target: After sorting by priority, the top-ranked target in the valid target list is the Optimal Valid Target. If no Aiming Area exists, no target is returned

d. Valid Target List: Returns all valid targets. If no Aiming Area exists, no target is returned

![](../../../images/0e2daeb576c013c1.png)

(5) Get Pre-Aim Collision Detection Count

Returns the number of targets the cursor ray hits during the process

![](../../../images/64e65e3d5297e7ec.png)

(6) Get Pre-Aim Ray Hit Info

Returns the On-Hit Location and On-Hit Entity of the first hit result of the pre-aim cursor ray

![](../../../images/9b9937d1d8604396.png)

(7) Get Pre-Aim Stick Deadzone Status

Queries whether the player's pre-aim stick (mobile/controller) is within its dead zone (insufficient movement input)

![](../../../images/386b7f5fd1729357.png)

(8) Get Base Object for Specified Pre-Aim Target

Returns the corresponding Base Object

![](../../../images/b7afc4c7b99e23dd.png)

## 2. Execution Nodes

(1) Complete Current Pre-Aim

When executed, the current active pre-aim is counted as actively completed once

![](../../../images/bf54d7f1faf330ee.png)
