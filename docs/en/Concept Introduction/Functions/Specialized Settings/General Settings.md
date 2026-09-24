---
title: General Settings
path_id: mh029h9sjiq2
updated_at: 2025-10-21 23:35:29
category: Concept Introduction/Functions/Specialized Settings
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh029h9sjiq2
---

# I. Definition of General Settings

Creation-specific settings are divided into Behavior Modes, Not-in-Battle Behavior, and Battle Areas

![](../../../images/a107104d10f0a816.png)

# II. Edit General Settings

## 1. Behavior Mode

Supports Behavior Mode selection for Creation Entities. At runtime, Entities will autonomously perform actions such as movement, battle entry and exit based on the configured Behavior Mode

Creation Behavior Mode Full Enumeration Details: [Creation Behavior Mode Archive](/ys/ugc/tutorial//detail/mhyg4i0inazs)

![](../../../images/0fc7fff500c0ec2b.png)

The Behavior Modes of Creation Entities can be configured and switched through enumeration selection

![](../../../images/545a134a260ac69c.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Behavior Modes* | Can be selected from the enumerated options in the pre-provided behavior mode pool  Each Behavior Mode provides different optional actions for both in-battle and not-in-battle situations, causing the Creation to autonomously display different behaviors. |

## 2. Not-in-Battle Behavior

After selecting a Behavior Mode, you can choose the *Not-in-Battle Behavior*.

![](../../../images/035f2731635bee23.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Not-in-Battle Behavior* | Rules for creations while out of battle..  Each mode has its own Not-in-Battle behavior pool |

## 3. Battle Area

After selecting a Behavior Mode, you can choose the *Battle Area*.

![](../../../images/27a911fc363bca7b.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Battle Area* | An entity's autonomous detection of hostile entities. If detection succeeds, it enters battle with the detected entity as its target  All behavior modes include: *Range Detection* and *FOV Detection* |
| *\*Preview Battle Area* | Enable to observe Horizontal Range of Battle Area |
| *\*Behavior Description* | Behavior Mode Introduction  ![](../../../images/6de683008034293a.png) |

## 4. Details Editor

Through "Details Editor", you can adjust and configure more parameters for not-in-battle and battle behaviors.

![](../../../images/a01d4e45ed51c0c9.png)

### (1) Details Editor - Not-in-battle

Rules to be followed when a Creation Entity is running but has not yet entered the battle

For all not-in-battle behaviors, please refer to [Not-in-Battle Behavior](/ys/ugc/tutorial//detail/mhpsmb91keka)

Editable Not-in-Battle behaviors include *Wandering* *and* *Patrolling*

#### a. Wandering

![](../../../images/91053793b927df35.png)

A behavior supported by all Creations when not engaged in a battle

During stage runtime, when Creations are not in battle, they will move randomly within their *Territory* Range

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Movement Area* | A range centered on the creation's spawn coordinates  At runtime, the creation randomly moves to points within this range in its territory  Only spherical shapes are supported |
| *Area Radius (m)* | The radius of the spherical movement area |
| *\*Preview Movement Area* | When enabled, the configured Wandering Area Range can be viewed in the Editor Window |
| *Movement Interval (s)* | Randomly selected within the configured time interval. After each movement, waits for this duration before moving again |
| *Single Movement Distance (m)* | Randomly selected within the configured distance for each movement |

#### b. Patrol

Some Creations support configuring patrol behavior when not in battle

![](../../../images/2afe5dd74a4992f6.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Initial Effective Patrol Template* | The drop-down menu enumerates patrol templates for this creation  Use the checkbox to toggle whether it's active; changes sync to the Patrol Template Details Editing Tab  ![](../../../images/045f9cef5a833b02.png)![](../../../images/d9b71ccd28b1d3e1.png) |
| *\*Patrol Template List* | Enumerates all *patrol templates* configured for this creation |

Open the *Details Editing Tab* to create a new patrol template or edit the existing ones

**Add Patrol Templates**

![](../../../images/ff6ff15a8ba83c20.png)

Click ![](../../../images/7eb077d848738482.png) to add a patrol template.

For newly added patrol templates, Initially Effective is off by default.

*Template X*, where X is the ID; use it as a node input to switch patrol templates.

![](../../../images/c3ebeb76292d3a43.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Initially Effective* | If enabled, this patrol template takes effect when the creation is created  Only one patrol template can be active per creation at a time | |
| *Loop Type* | ![](../../../images/793bc60729ca3dd3.png) | |
| *One-Way* | The creation follows the path to the final waypoint, then stops patrolling |
| *Round Trip* | Upon reaching the final waypoint, the creation reverses and returns along the path; it does the same when it reaches the first waypoint |
| *Loop* | After reaching the final waypoint, the creation loops back to the first waypoint and continues |
| *Patrol Start Position* | ![](../../../images/bbe041855123165a.png)  Choose which waypoint the creation uses to begin its patrol | |
| *Nearest point* | The closest waypoint in the selected patrol template |
| *Starting point* | The first waypoint in the selected patrol template |

**Patrol Path Configuration**

![](../../../images/e59b8c39ac838119.png)

Select the pre-configured paths from [Path](/ys/ugc/tutorial//detail/mh333vim2h44)for reference.

**Editing Patrol Path Template**

![](../../../images/c69581683a0bef78.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Patrol Path* | Select the pre-configured paths from the path management tool | |
| *\*Open Path Management Tool* | Redirects to the Path Management Tool | |

**Patrol Path Waypoint Configuration**

![](../../../images/e59b8c39ac838119.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *\*Waypoint* | Waypoint X: Use X as a node parameter to read the waypoint's position/rotation, or to compare against the arrival point. | |
| *Travel Speed* | ![](../../../images/0b42959579df7782.png)  Offers **Walk and Run** as movement speed options | |
| *Arrival Detection Radius (m)* | If the creation is within the configured radius of a waypoint, it is considered to have arrived | |
| *Stay Duration(s)* | How long the creation remains in place after reaching the waypoint | |
| *Turn After Reaching Waypoint* | If enabled, the creation turns to match the waypoint's rotation upon arrival | |
| *Notify Node Graph on Arrival* | If enabled, upon arrival the creation sends a [Creation Reached Patrol Waypoint Event] to its mounted Node Graph | |
| *\*Show Waypoint Information* | ![](../../../images/4bd0bf3eb3d58a9b.png)  If enabled, you can view the waypoint's position and rotation; editing is not allowed | |

### (2) Details Editor - Combat

Rules for Creation Entity behavior when targeting a Character and preparing for/engaging in a battle

![](../../../images/3d9883e65a3f3ae1.png)

The basic configuration is consistent across different Behavior Modes, and here we'll explain all the parameters that have appeared so far.

#### **a. Battle Entry Settings**

At runtime, configure a creation entity's rules for how to detect hostile entities, detection distance, and relationship settings

![](../../../images/a86d39001e23a861.png)

**Detection Range**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Detection Range* | When hostile entities are within this range, the creation can obtain the corresponding entity information and target that entity to enter battle |
| *\*Preview Range* | When enabled, you can view the Detection Range of the edited creation entity in the Edit Window |

**FOV Detection**

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *FOV Type* | Provides *Full FOV* and *FOV Cone* enumerations, and shape editing parameters will change accordingly after selection |

![](../../../images/164a062115cd5333.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *FOV Cone - Cone Distance* | Configure the radius distance of the FOV Cone |
| *Full FOV - FOV Detection Radius* | Configure the sphere radius |
| *\*Preview Range* | When enabled, you can view the FOV Detection Range of the edited creation entity in the Edit Window |
| *Coordinated Engagement Distance (m)* | When a Creation enters a battle, other Creations within this distance that are not in battle will also join the battle |

#### **b. Battle Exit Settings**

When the creation entity is running, and has entered battle with hostile entities, configure the creation's automatic out-of-battle rule settings

![](../../../images/5c3e534d80286540.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Out-of-Battle Distance (m)* | When a creation is in battle, if the distance to its target entity exceeds the configured distance, the creation will leave battle |
| *\*Preview Out-of-Battle Distance* | When enabled, you can view the configured distance |
| *Leave Battle on Pathfinding Failure* | When a creation is in battle and there is no valid path to its target entity, the creation will leave battle |
| *Leaving Battle Delay (s)* | When a creation is in battle and there is no valid path to its target entity, it will leave battle after the configured Leaving Battle Delay |

#### **c. Territory Settings**

![](../../../images/3cdbdbf747bac5de.png)

![](../../../images/24ae182e44243fc8.png)

![](../../../images/ddf6a06e24e1bd0a.png)

![](../../../images/c15c39ad357cf30a.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Territory* | Supports configuration of none, sphere, or cylinder, with size parameters required  The Territory is centered at the created Location of the Creation and does not change the Location with Creation movement  The Creation's movement range is restricted within the Territory |
| *\*Preview Territory Range* | When enabled, you can view the configured Territory Range |
| *Leave Battle When Player Leaves Area* | When enabled, if the target entity leaves this area, the creation will leave battle |
| *Leaving Battle Delay (s)* | After the target entity leaves the territory range, the creation will leave battle after the specified delay |

### (3) Details Editor - Skills

**Basic Settings**

![](../../../images/cc3cbfff68feb937.png)

Some of the logic parameters of certain creations can be configured by the creator (Craftsperson) to adjust the behavior and logic during runtime.

For example, as shown in the figure for the [Abyss Mage], the *Powerful Elemental Ward* parameter is provided. By modifying this parameter, the creator can adjust the elemental value of the creation's Ward.

![](../../../images/9cd132ef5276e2b3.png)

**Skill Settings**

Enumerates some of the Creation's skills, which support a certain degree of adjustment to their cooldown times.

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *\*Skill Name* | Currently provides editing for some melee skills, ranged skills, and special skills |
| *Enable This Skill* | When enabled, if the Creation's Behavior Mode includes this skill, it will be used; otherwise, this skill will not be used |
| *Initial CD Range (s)* | A random time within the configured range will be set as the Effective Cooldown Time  After the creation is created, it will start using this skill only after the Effective Cooldown Time has elapsed |
| *Default CD Range (s)* | A random time within the configured range will be set as the actual cooldown time  After the Creation uses this skill, it cannot use it again during the actual cooldown time |

Complete enumeration details of Creation Skills:[Creation Skills Description](/ys/ugc/tutorial//detail/mhzys1ic5eok)

# III. Managing Creation Patrol via Node Graphs

1.

### **When Creation Reaches Patrol Waypoint**

If, in Patrol Template editing, the **Send Node Graph Event on Arrival Event** option is checked for a specified waypoint, the Node Graph Event will be received when the conditions are met

This Node Graph Event can only be received by the creation's node graph

![](../../../images/82fafb4c8159ac55.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Creation Entity* | Entity | The creation entity during runtime |
| *Creation GUID* | GUID | The GUID of the creation, outputs empty if not initially placed |
| *Current Patrol Template ID* | Integer | The currently active patrol template ID for the creation |
| *Current Global Path ID* | Integer | The Global Path ID referenced by the creation's currently active patrol template |
| *Current Waypoint ID* | Integer | The current waypoint ID reached by the creation |
| *Next Waypoint ID* | Integer | The waypoint ID the creation will move to next |

2.

### **Switch Creation Patrol Template**

![](../../../images/ba26262eeeec594a.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Creation Entity* | Entity | The creation entity during runtime |
| *Patrol Template ID* | Integer | The configured patrol template ID for the creation. If the template with the input ID does not exist, it will not take effect |

3.

### **Get Current Creation's Patrol Template**

![](../../../images/ee769dade29bead8.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Creation Entity* | Entity | The creation entity during runtime |
| *Patrol Template ID* | Integer | Currently active patrol template ID for the creation |
| *Global Path ID* | Integer | Global Path ID referenced by the creation's currently active patrol template |
| *Target Waypoint ID* | Integer | The waypoint ID the creation will move to next |

4.

### Get Aggro List of Creation in Default Mode

![](../../../images/ad6c2acb15713c97.png)

Output lists for this node are only correct when the hostility configuration is set to [Default Type].

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Creation Entity* | Entity | The creation entity during runtime |
| *Aggro List* | Entity List | Which entities the creation currently has hostility towards; this list is unordered. |

5.

### Get Creation's Current Target

![](../../../images/06e10e3b7927b35b.png)

Depending on the creation's current behavior, the target entities may differ.

For example, when the creation is attacking an enemy, the target is a specified enemy entity.

For example, when the creation is healing an ally, the target is a specified allied entity.

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Data Type | Description |
| *Creation Entity* | Entity | The creation entity during runtime |
| *Target Entity* | Entity | The creation's current AI selects the target entity |
