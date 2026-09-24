---
title: Event Nodes
path_id: mh9ji0030dzs
updated_at: 2026-09-16 18:10:39
category: Node Introduction/Server Nodes
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh9ji0030dzs
---

# I. Custom Variables

## **1. When Node Graph Variable Changes**

![](../../images/c80ebd1b5bcbdea1.png)

**Node Functions**

This event is triggered when a Node Graph Variable in the current Node Graph changes

The previous and current values are Generic. Determine the Generic type to correctly receive events for Node Graph Variables of the corresponding type

Vessel-type Node Graph Variables do not provide before-value and after-value Output Parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | The Entity associated with this Node Graph |
| Output Parameter | Event Source GUID | GUID | GUID of the Entity associated with this Node Graph |
| Output Parameter | Variable Name | String | Name of the Variable that was changed |
| Output Parameter | Pre-Change Value | Generic | The Variable's value before the change |
| Output Parameter | Post-Change Value | Generic | The Variable's value after the change |

## **2. When Custom Variable Changes**

![](../../images/82a4e1b8d8aa7e1f.png)

**Node Functions**

This event is triggered when the Custom Variable of the Entity associated with the current Node Graph changes

The previous and current values are Generic. Determine the Generic type before you can correctly receive events for Custom Variables of the corresponding type

Vessel-type Custom Variables do not provide before-value and after-value Output Parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | The Entity associated with this Node Graph |
| Output Parameter | Event Source GUID | GUID | GUID of the Entity associated with this Node Graph |
| Output Parameter | Variable Name | String | Name of the Variable that was changed |
| Output Parameter | Pre-Change Value | Generic | The Variable's value before the change |
| Output Parameter | Post-Change Value | Generic | The Variable's value after the change |

# II. Preset Status

## **1. When Preset Status Changes**

![](../../images/815b1305104e9d60.png)

**Node Functions**

This event is triggered when the Preset Status of the Entity associated with the Node Graph changes

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Preset Status ID | Integer |  |
| Output Parameter | Pre-Change Value | Integer |  |
| Output Parameter | Post-Change Value | Integer |  |

# III. Entity Related

## **1.** When Character Movement SPD Meets Condition

![](../../images/f91b3d799b030a24.png)

**Node Functions**

Adds the Unit Status effect [Monitor Movement Speed] to the Character Entity. This event is triggered when the conditions are met

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Condition: Comparison Type | Enumeration |  |
| Output Parameter | Condition: Comparison Value | Floating Point Numbers |  |
| Output Parameter | Current Movement SPD | Floating Point Numbers |  |

## **2. When Entity Is Created**

![](../../images/21ebfd13c9690ded.png)

**Node Functions**

This event is triggered when an Entity is created

All types of Entities can trigger this event. Stage Entities, Character Entities, and Player Entities trigger this event when entering a Stage

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

## **3. When Entity Is Destroyed**

![](../../images/3c2f5234469cd435.png)

**Node Functions**

This event triggers when objects and creations within the stage are destroyed. This event can only trigger on stage entities.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Destroyed Entity |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Location | 3D Vector |  |
| Output Parameter | Orientation | 3D Vector |  |
| Output Parameter | Entity Type | Enumeration |  |
| Output Parameter | Faction | Faction |  |
| Output Parameter | Damage Source | Entity |  |
| Output Parameter | Owner Entity | Entity |  |
| Output Parameter | Custom Variable Component Snapshot | Custom Variable Snapshot | On destroy, captures a snapshot of the Custom Variable component on this Entity. Use the Search Custom Variable Snapshot node to retrieve its Custom Variable values |

## **4. When Entity Is Removed/Destroyed**

![](../../images/f45cbd8f8ddce984.png)

**Node Functions**

This event is triggered when any Entity in the Stage is removed or destroyed, and it can only be triggered on Stage Entities

This event is triggered upon Entity destruction or removal. Therefore, when an Entity is destroyed, it triggers both the [On Entity Destroyed] and [On Entity Removed/Destroyed] events in sequence

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source GUID | GUID |  |

# IV. Faction Related

## **1. When Entity Faction Changes**

![](../../images/3a257541cc5b7e39.png)

**Node Functions**

This event is triggered when an Entity's Faction changes

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Faction | Faction |  |
| Output Parameter | Post-Change Faction | Faction |  |

# V. Player and Character Related

## **1. When the Character Is Down**

![](../../images/1e5a338bbc6fa420.png)

**Node Functions**

When a Character is Downed, the Node Graph on the Character Entity can trigger this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |
| Output Parameter | Reason | Enumeration | Node Graph caused: the Character was Downed by the Destroy Entity node in the Node Graph  Normal Down: the Character was Downed because HP reached 0  Abnormal Down: the character was downed due to drowning, falling into an abyss, etc. |
| Output Parameter | Knockdown Entity | Entity |  |

## **2. When Character Revives**

![](../../images/01abdaaeba5a4cee.png)

**Node Functions**

When a Character is Revived, the Node Graph on the Character Entity can trigger this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **3. When Player Teleport Completes**

![](../../images/d70b61f49d0e112d.png)

**Node Functions**

This event is triggered on the Player Entity's Node Graph when the Player completes teleportation

This event is also triggered when a Player enters a Stage for the first time

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Player GUID | GUID |  |

## **4. When All Player's Characters Are Down**

![](../../images/9cd8fdd84c303cc0.png)

**Node Functions**

This event is triggered on the Player Entity's Node Graph when all of the Player's Character Entities are Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Reason | Enumeration | Node Graph caused: the Character was Downed by the Destroy Entity node in the Node Graph  Normal Down: the Character was Downed because HP reached 0  Abnormal Down: the character was downed due to drowning, falling into an abyss, etc. |

## **5. When All Player's Characters Are Revived**

![](../../images/2c2849aa05a39a87.png)

**Node Functions**

This event is triggered on the Player Entity's Node Graph when all of the Player's Characters are Revived

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |

## **6. When Player Is Abnormally Downed and Revives**

![](../../images/52f9078b76b06bcb.png)

**Node Functions**

This event is triggered on the Player Entity when a Character is Downed and then Revived due to drowning, falling into an abyss, or similar reasons

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |

## **7.** When the Active Character Changes

![](../../images/467547fdc627fabf.png)

**Node Functions**

Available only in Classic Mode. This event is triggered on the player entity when the active character changes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Player GUID | GUID |  |
| Output Parameter | Replaced Character Entity | Entity |  |
| Output Parameter | Current Active Character Entity | Entity |  |

# VI. Collision Trigger

## **1. When Entering Collision Trigger**

![](../../images/b4392914aad155c1.png)

**Node Functions**

The "Collision Trigger Source" range of a runtime entity A enters the "Collision Trigger" range of another runtime entity B

Node graph events will be sent to the entity B configured with "Collision Trigger"

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Entering Entity | Entity | Entity A (referenced above) |
| Output Parameter | Entering Entity GUID | GUID |  |
| Output Parameter | Trigger Entity | Entity | Entity B (mentioned above) |
| Output Parameter | Trigger Entity GUID | GUID |  |
| Output Parameter | Trigger ID | Integer | The trigger with the corresponding ID in Entity B's Collision Trigger Component |

## **2. When Exiting Collision Trigger**

![](../../images/4bb635faf0699393.png)

**Node Functions**

When the "Collision Trigger Source" range of active Entity A leaves the "Collision Trigger" range of active Entity B

Node graph events will be sent to the entity B configured with "Collision Trigger"

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Exiting Entity | Entity | Entity A (referenced above) |
| Output Parameter | Exiting Entity GUID | GUID |  |
| Output Parameter | Trigger Entity | Entity | Entity B (mentioned above) |
| Output Parameter | Trigger Entity GUID | GUID |  |
| Output Parameter | Trigger ID | Integer |  |

# VII. Combat

## **1. When HP Is Recovered**

![](../../images/1d02b83ba3b23ce7.png)

**Node Functions**

This event is triggered when an Entity's HP is restored

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Healer Entity | Entity |  |
| Output Parameter | Recovery Amount | Floating Point Numbers | Actual healing amount. If the Entity had not lost any HP prior to healing, the amount is 0 |
| Output Parameter | Recover Tag List | String List |  |

## **2. When Initiating HP Recovery**

![](../../images/ebb09b29292b71bb.png)

**Node Functions**

This event is triggered on the initiating Entity when an Entity restores HP to other Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Recover Target Entity | Entity |  |
| Output Parameter | Recovery Amount | Floating Point Numbers | Actual healing amount. If the Target Entity had not lost any HP prior to healing, the amount is 0 |
| Output Parameter | Recover Tag List | String List |  |

## **3. When Attack Hits**

![](../../images/e31f941e2da57715.png)

**Node Functions**

This event is triggered when an Entity's attack hits other Entities

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Hit Target Entity | Entity |  |
| Output Parameter | Damage | Floating Point Numbers | Actual damage dealt. If no damage is dealt due to Invincible or other reasons, the amount is 0 |
| Output Parameter | Attack Tag List | String List |  |
| Output Parameter | Elemental Type | Enumeration |  |
| Output Parameter | Elemental Attack Potency | Floating Point Numbers | Elemental Gauge in the Attack |

## **4. When Attacked**

![](../../images/6065cf0e6d8e1499.png)

**Node Functions**

This event is triggered when the Entity is attacked

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker Entity | Entity |  |
| Output Parameter | Damage | Floating Point Numbers | Actual damage dealt. If no damage is dealt due to Invincible or other reasons, the amount is 0 |
| Output Parameter | Attack Tag List | String List |  |
| Output Parameter | Elemental Type | Enumeration |  |
| Output Parameter | Elemental Attack Potency | Floating Point Numbers | Elemental Gauge in the Attack |

## **5. When Entering an Interruptible State**

![](../../images/fed92fc175289dd4.png)

**Node Functions**

Available only in Beyond Mode.

This event is triggered when an Entity is attacked and enters the Vulnerable Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker | Entity |  |

# VIII. Motion Device

## **1. When Basic Motion Device Stops**

![](../../images/e8ae317f765c87d8.png)

**Node Functions**

This event is sent to the Component Owner when a Basic Motion Device on the Basic Motion Device Component completes its movement or is disabled

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Component Owner |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Motion Device Name | String |  |

## **2. When Path Reaches Waypoint**

![](../../images/54a751a247b15641.png)

**Node Functions**

When the Pathing Motion Device reaches a Waypoint, it sends this event to the Owner of the Basic Motion Device Component. This event is triggered only if "Send Event on Waypoint Arrival" is enabled in the Waypoint settings

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Component Owner |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Motion Device Name | String |  |
| Output Parameter | Path Point ID | Integer |  |

# IX. Hit Detection

## **1. When On-Hit Detection Is Triggered**

![](../../images/a3ee674953d15f09.png)

**Node Functions**

This event is triggered when the On-Hit Detection Component's Owner hits other Entities or the Scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | On-Hit Hurtbox | Boolean | If set to False: The environment was hit  If set to True: An Entity was hit. Retrieve values from the Hit Entity output parameter |
| Output Parameter | On-Hit Entity | Entity | Hit Entity is only valid when a Hurtbox is hit |
| Output Parameter | On-Hit Location | 3D Vector |  |

# X. Timer

## **1. When Timer Is Triggered**

![](../../images/8504beb89dd1ec50.png)

**Node Functions**

This event is triggered when the Timer reaches the specified time node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Timer Name | String |  |
| Output Parameter | Timer Sequence ID | Integer |  |
| Output Parameter | Number of Loops | Integer |  |

# XI. Global Timer

## **1. When Global Timer Is Triggered**

![](../../images/06adafcbfda48f9a.png)

**Node Functions**

This event is triggered when the Global Countdown Timer reaches zero

The Global Stopwatch Timer does not trigger this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Timer Name | String |  |

# XII. UI Control Groups

## **1. When UI Control Group Is Triggered**

![](../../images/69c5d6edd056e557.png)

**Node Functions**

This event is triggered only by UI controls of the following types: Interactive Button, Item Display, Custom Button, and Custom Switch

This event can only be received by the Player Node Graph that triggered the interaction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | UI Control Group Composite Index | Integer | If the UI control that triggered this event forms a multi-control UI group with other controls, this output parameter returns the corresponding group value |
| Output Parameter | UI Control Group Index | Integer | If the triggering UI control is a single-control UI group, this value represents the ID of that UI control group  If the triggering UI control is part of a multi-control UI group, this value represents the ID of the control within that group |

# XIII. Unit Status

## **1. When Unit Status Changes**

![](../../images/30bf229441fcd537.png)

**Node Functions**

This event is triggered when the Stack Count of a Unit Status changes

This event is triggered when Unit Status effects are applied or removed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Applier Entity | Entity |  |
| Output Parameter | Infinite Duration | Boolean |  |
| Output Parameter | Remaining Status Duration | Floating Point Numbers |  |
| Output Parameter | Remaining Status Stacks | Integer | Edited Stack Count |
| Output Parameter | Original Status Stacks | Integer | Previous Stack Count |
| Output Parameter | Slot ID | Integer | ID of the Unit Status slot that changed |

## **2. When Unit Status Ends**

![](../../images/5cc05d1912245ca3.png)

**Node Functions**

This event is triggered when a Unit Status is removed for any reason or when its Runtime Duration expires

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Applier Entity | Entity |  |
| Output Parameter | Infinite Duration | Boolean |  |
| Output Parameter | Remaining Status Duration | Floating Point Numbers |  |
| Output Parameter | Remaining Status Stacks | Integer |  |
| Output Parameter | Remover Entity | Entity |  |
| Output Parameter | Removal Reason | Enumeration | Status Replacement: The Unit Status was removed because it was replaced by another status  Duration Exceeded: The Unit Status exceeded its runtime duration  Dispelled: The Unit Status was removed directly  Status Expired: The Unit Status became invalid due to other reasons  Class Changed: The Unit Status was removed due to a class change |
| Output Parameter | Slot ID | Integer | ID of the Unit Status slot that changed |

## **3. When Elemental Reaction Event Occurs**

![](../../images/e5731be432102a50.png)

**Node Functions**

Adds the Unit Status effect [Monitor Elemental Reaction] to the Entity. This event is triggered when the conditions are met

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Elemental Reaction Type | Enumeration |  |
| Output Parameter | Triggerer Entity | Entity |  |
| Output Parameter | Triggerer Entity GUID | GUID |  |

## **4. When Shield Is Attacked**

![](../../images/31bb9e51be70e8f9.png)

**Node Functions**

Adds the Unit Status effect [Add Shield] to the Entity. This event is triggered when the Shield takes damage

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker Entity | Entity |  |
| Output Parameter | Attacker GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Pre-Attack Layers | Integer |  |
| Output Parameter | Post-Attack Layers | Integer |  |
| Output Parameter | Shield Value of this Unit Status Before Attack | Floating Point Numbers |  |
| Output Parameter | Shield Value of this Unit Status After Attack | Floating Point Numbers |  |

# XIV. Tabs

## **1. When Tab Is Selected**

![](../../images/7214d95d5a3046e4.png)

**Node Functions**

When the active tab is selected, it will send an event to the node graph

The Entity Node Graph configured by the Tab Component will receive this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Entity with the tab component mounted |
| Output Parameter | Event Source GUID | GUID | GUID of the Entity with the tab component mounted; outputs 0 if none exists |
| Output Parameter | Tab ID | Integer | ID of the tab |
| Output Parameter | Selector Entity | Entity | Character Entity that triggers the tab |

# XV. Creations

## **1. When Creation Enters Combat**

![](../../images/a3dec25016f44d69.png)

**Node Functions**

Only effective in Classic Aggro Mode

This event is triggered when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

## **2. When Creation Leaves Combat**

![](../../images/6dc9d4805ce38eb9.png)

**Node Functions**

Only effective in Classic Aggro Mode

This event is triggered when a Creation leaves battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

# XVI. Classes

## **1. When Player Class Level Changes**

![](../../images/515e18534cc7295c.png)

**Node Functions**

This event is triggered when a Player's Class Level changes and is sent to the corresponding Player. It can be received in that Class's Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Active Player Entity |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Level | Integer |  |
| Output Parameter | Post-Change Level | Integer |  |

## **2. When Player Class Changes**

![](../../images/794bfecd0308143f.png)

**Node Functions**

This event is triggered when a Player's Class changes and is sent to the corresponding Player. It can be received in the Node Graph of the new Class

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Modification Class Config ID | Config ID |  |
| Output Parameter | Post-Modification Config ID | Config ID |  |

## **3. When Player Class Is Removed**

![](../../images/fedd44330da348e2.png)

**Node Functions**

This event is triggered when a Player's Class is removed and sent to the corresponding Player. It can be received in the Node Graph of the previous Class

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Modification Class Config ID | Config ID |  |
| Output Parameter | Post-Modification Config ID | Config ID |  |

# XVII. Skills

## **1. When Skill Node Is Called**

![](../../images/a76295bc5fc4e066.png)

**Node Functions**

This event is triggered by the [Notify Server Node Graph] Node in the Skill Node Graph. Up to three strings can be passed in

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Caller Entity | Entity |  |
| Output Parameter | Caller GUID | GUID |  |
| Output Parameter | Parameter 1 | String |  |
| Output Parameter | Parameter 2 | String |  |
| Output Parameter | Parameter 3 | String |  |

# XVIII. Custom Aggro

## **1. When Aggro Target Changes**

![](../../images/e3ba6675e904c018.png)

**Node Functions**

Available only in Custom Aggro Mode

This event is triggered when the Aggro Target changes

This event can also be triggered when entering or leaving battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Aggro Target | Entity |  |
| Output Parameter | Post-Change Aggro Target | Entity |  |

## **2. When Self Enters Combat**

![](../../images/39964b7255b884a6.png)

**Node Functions**

Available only in Custom Aggro Mode

This event is triggered when the Entity itself enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

## **3. When Self Leaves Combat**

![](../../images/58a6457de192c9bb.png)

**Node Functions**

Available only in Custom Aggro Mode

This event is triggered when the Entity itself leaves battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

# XIX. Signals

## **1. Monitor Signal**

![](../../images/c9606b2298ec2dc0.png)

**Node Functions**

Monitors Signal trigger events defined in the Signal Manager

The Signal name to monitor must be selected first

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Signal Source Entity | Entity | The Entity that sent this signal using the Send Signal node |

# XX. Deck Selector

## **1. When Deck Selector Is Complete**

![](../../images/45aaad3916d3f1e5.png)

**Node Functions**

This event is triggered on the Player's Node Graph when the Player completes the Deck Selector, or when it is forcibly closed due to time constraints

The output parameters report the Deck Selector's result and the corresponding reason

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Player | Entity | Active Player Entity |
| Output Parameter | Selection Result List | Integer List | When a selection interaction is triggered, valid **selection results** are returned as this output parameter, and the completion reason is **Completed by Player**  When a **Full Refresh** pop-up selection is triggered, the complete **selection result list** is returned as this output parameter, and the completion reason is **Refresh All**  When a **Fixed-Quantity Refresh** pop-up selection is triggered, valid **selection results** are returned as this output parameter, and the completion reason is **Fixed-Quantity Refresh**  When the Deck Selector times out with no interaction, **the default selection is returned** is returned as this output parameter, and the completion reason is **Timeout**  When **Allow Discard Selection is enabled** and the Deck Selector is closed by the player, **the default selection is returned** as this output parameter, and the completion reason is **Closed** **Manually**  When the Deck Selector is closed via a Node Graph node, this output parameter is empty, and the completion reason is **Closed by Node Graph** |
| Output Parameter | Completion Reason | Enumeration | Six reason enumerations  **Completed by Player**, **Refresh All**, **Fixed-Quantity Refresh**, Timeout, Closed Manually, Closed by Node Graph |
| Output Parameter | Deck Selector Index | Integer | Referenced Deck Selector ID |

# XXI. Text Bubbles

## **1. When Text Bubble Is Completed**

![](../../images/18b09d2b281ba7b9.png)

**Node Functions**

This event can only be mounted by Text Bubble Components and is received by the Entity's Node Graph that completed the dialogue

Completion refers to when the final line of dialogue has finished playing

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Bubble Owner Entity | Entity | Runtime Entity with the Text Bubble component mounted |
| Output Parameter | Character Entity | Entity | Target Character of the current Bubble dialogue |
| Output Parameter | Text Bubble Configuration ID | Config ID | Currently active Text Bubble Config ID |
| Output Parameter | Text Bubble Completion Count | Integer | Number of times the currently active Text Bubble has been fully played for this dialogue Character |

# XXII. Shop

## **1. When Selling Inventory Items in the Shop**

![](../../images/88cc0cf7cdd5891f.png)

**Node Functions**

This event is triggered when Inventory items are sold in the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Buyer Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Purchase Quantity | Integer |  |

## **2. When Custom Shop Item Is Sold**

![](../../images/c74958b4dd839fb0.png)

**Node Functions**

This event is triggered when Custom items are sold in the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Buyer Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Shop Item ID | Integer |  |
| Output Parameter | Purchase Quantity | Integer |  |

## **3. When selling items to the shop**

![](../../images/cfba4a9f80f34f79.png)

**Node Functions**

This event is triggered when items are purchased by the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Seller Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Purchase Item Dictionary | Dictionary |  |

# XXIII. Equipment

## **1. When Equipment Is Equipped**

![](../../images/d69b3bd3c6048908.png)

**Node Functions**

This event is triggered when Equipment is equipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Holder Entity | Entity |  |
| Output Parameter | Equipment Holder GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **2. When Equipment Is Unequipped**

![](../../images/b18120a72885a8d7.png)

**Node Functions**

This event is triggered when Equipment is unequipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner Entity | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **3. When Equipment Is Initialized**

![](../../images/8445dd4266197aab.png)

**Node Functions**

When Equipment is first obtained and enters the Inventory, it is initialized. The event's output parameters return the unique ID of the Equipment instance. Use this ID to edit the Equipment dynamically. The Owner of the Equipment will receive this event. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **4. When Equipment Affix Value Changes**

![](../../images/d6101804a49fb04e.png)

**Node Functions**

This event is triggered when Equipment Affix values change. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |
| Output Parameter | Affix ID | Integer | The corresponding ID of this Entry within the Equipment Affixes |
| Output Parameter | Pre-Change Value | Floating Point Numbers |  |
| Output Parameter | Post-Change Value | Floating Point Numbers |  |

## **5. When Equipment is purchased**

![](../../images/6f32bc4e7b703c27.png)

**Node Functions**

The Inventory Owner Entity receives this event when it purchases equipment

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Purchasing Inventory Owner Entity | Entity |  |
| Output Parameter | Purchasing Inventory Owner GUID | GUID |  |
| Output Parameter | Equipment Index List | Integer List | List of Indices of the Purchased Equipment |

## **6. When Equipment is sold**

![](../../images/38302083916386cb.png)

**Node Functions**

The Inventory Owner Entity receives this event when it sells equipment

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Purchasing Inventory Owner Entity | Entity |  |
| Output Parameter | Purchasing Inventory Owner GUID | GUID |  |
| Output Parameter | Equipment Index List | Integer List | List of Indices of the Sold Equipment |

# XXIV. Items

## **1. When Item Is Lost From Inventory**

![](../../images/7a03e83fca4df406.png)

**Node Functions**

This event is triggered when an Item is removed from the Inventory (its quantity becomes 0). The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Quantity Lost | Integer |  |

## **2. When the Quantity of Inventory Item Changes**

![](../../images/fccb21da64aa0136.png)

**Node Functions**

This event is triggered when the quantity of Items in the Inventory changes. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Pre-Change Quantity | Integer |  |
| Output Parameter | Post-Change Quantity | Integer |  |
| Output Parameter | Reason for Change | Enumeration |  |

## **3. When Item Is Added to Inventory**

![](../../images/9e8eb1f866631ddd.png)

**Node Functions**

This event is triggered when a new Item is added to the Inventory. The Owner of the Inventory Component will receive it. This event is not triggered by quantity-only changes

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Quantity Obtained | Integer |  |

## **4. When the Quantity of Inventory Currency Changes**

![](../../images/003344dd61373505.png)

**Node Functions**

This event is triggered when the amount of Inventory Currency changes. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Currency Owner Entity | Entity |  |
| Output Parameter | Currency Owner GUID | GUID |  |
| Output Parameter | Currency Config ID | Config ID |  |
| Output Parameter | Currency Change Value | Integer |  |

## **5. When Items in the Inventory Are Used**

![](../../images/6ee85aa539780e17.png)

**Node Functions**

This event is triggered when an Item in the Inventory is used. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Amount to Use | Integer |  |

# XXV. Creation Patrol

## **1. When Creation Reaches Patrol Waypoint**

![](../../images/7d559f2d047a9af4.png)

**Node Functions**

When the **Send Node Graph Event on Arrival** option is enabled for a waypoint in the Patrol template, a Node Graph Event is triggered once the specified conditions are met

This Node Graph Event can only be received by the creation's node graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Creation Entity | Entity | Runtime Creation Entity |
| Output Parameter | Creation GUID | GUID | The GUID of the Creation. If it was not an initially placed Creation, the output is empty |
| Output Parameter | Current Patrol Template ID | Integer | The Patrol Template ID currently active on this Creation |
| Output Parameter | Current Path Index | Integer | The Path ID referenced by the Creation's currently active Patrol Template |
| Output Parameter | Current Reached Waypoint ID | Integer | The Waypoint ID the Creation has currently reached |
| Output Parameter | Next Waypoint ID | Integer | The Waypoint ID the Creation will move to next |

# XXVI. Creation Preset Status

1.

## When Complex Creation Preset Status Changes

![](../../images/5ef2a7c92db2eab5.png)

**Node Functions**

This event is triggered when the preset state of a complex creation is changed using the "Set the preset status value of the complex creation" node (the modified and unmodified values ​​must be different for this event to trigger).

This node graph event can only be received by the node graph of the complex creation.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Complex Creation Entity |
| Output Parameter | Event Source Entity GUID | GUID | Complex Creation GUID |
| Output Parameter | Preset Status Index | Integer |  |
| Output Parameter | Pre-Change Value | Integer |  |
| Output Parameter | Post-Change Value | Integer |  |

# XXVII. Floating Interaction Page

## **1. When Floating Interaction Page is Triggered**

![](../../images/174d9306189cb182.png)

**Node Functions**  
When the "Return to Server Event" option is enabled for a tab or single-choice window, confirming the interaction will trigger this event on the corresponding Player Entity's Server Node Graph.

When the player selects a Tab/Single-Choice Panel:

The Interactive Item Index is the index of the corresponding Tab/Single-Choice Panel, the List Index is the index of the corresponding Tab/Single-Choice Panel, and the Selected List Item is the index of the currently clicked item in the corresponding Tab/Single-Choice Panel.  
  
When the player clicks a button that has a Tab/Single-Choice Panel monitor configured:

The Interactive Item Index is the index of the corresponding Tab/Single-Choice Panel, the List Index is the list of indices of all Tab/Single-Choice Panels associated with the button, and the Selected List Item is the list of indices of the currently clicked items in the corresponding Tab/Single-Choice Panels.

After the interaction is confirmed, the corresponding player's server node graph will also receive this event for the following elements configured in the Floating Interaction Page: Interaction Page Close Button, Interaction Button, Item Display, Custom Button, and Custom Switch.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity | Active Player Entity |
| Output Parameter | Player GUID | GUID | GUID of the Active Player Entity |
| Output Parameter | Floating Interaction Page Index | Integer | Unique Identifier for the Floating Interaction Page |
| Output Parameter | Interactive Item Index | Integer | Index of the control that triggered this event |
| Output Parameter | List Index | Integer List | List of indices for the tabs or single-choice windows. Each List Index output parameter corresponds to a Selected List Item output parameter |
| Output Parameter | Selected List Item | Integer List | Each tab or single-choice window can have at most one selected item. Each Selected List Item output parameter corresponds to a List Index output parameter |

# XXVIII. **Control Motion Device**

## **1. When Player Leaves Control Motion Device**

![](../../images/a0ff00e717f91042.png)

**Node Functions**

Triggered when the player exits the Motion Device. The player will automatically exit the Motion Device when they become controlled or are teleported.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Leave Control Motion Device Entity | Entity |  |

## **2. When Player Follows Control Motion Device**

![](../../images/6c68928b93b8bc07.png)

**Node Functions**

Triggered when the player follows the Control Motion Device.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Follow Control Motion Device Entity | Entity |  |

## **3. When Player's Activated Control Motion Device List Changes**

![](../../images/695df79abf2a4b6d.png)

**Node Functions**

Triggered when the player follows the Control Motion Device.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | OldControl Motion Device Entity List | Entity List |  |
| Output Parameter | Current Activated Control Motion Device Entity List | Entity List |  |
