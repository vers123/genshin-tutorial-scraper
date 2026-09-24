---
title: Query Nodes
path_id: mh9p1x07f3kw
updated_at: 2026-08-07 18:20:02
category: Node Introduction/Client Nodes/Character Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh9p1x07f3kw
---

# I. List Related

## **1. Get Corresponding Value From List**

![](../../../images/641adf4d6b1d37cb.png)

**Node Functions**

Returns the value at the specified ID in the List. IDs start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![](../../../images/70763701b9f3cd9e.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/8c58b5a12ba4eb80.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/d976801b55ff3778.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![](../../../images/273599a3e0bc4ae8.png)

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Complete list |  |

## **6. Get Entity Type List**

![](../../../images/7a33dfcd4b09690e.png)

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Complete list |  |

## **7. List Includes This Value**

![](../../../images/155d745c5dad3311.png)

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# II. Custom Variables

## **1. Get Custom Variable**

![](../../../images/ba9df4d2ca615bb3.png)

**Node Functions**

Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# III. Preset Status

## **1. Get Preset Status**

![](../../../images/2c9ff0244a2b409a.png)

**Node Functions**

Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# IV. Entity Related

## **1. Query If Entity Is on the Field**

![](../../../images/e2ef240f831bf28a.png)

**Node Functions**

Searches whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **2. Get Unit Attack Target**

![](../../../images/7777b3e094f721cc.png)

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **3. Get Target Attachment Point Location**

![](../../../images/86f428f0de3a9c51.png)

**Node Functions**

Returns the Attachment Point Location corresponding to the specified Attachment Point Name on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **4. Get Target Attachment Point Rotation**

![](../../../images/b8b2fe5bb101b6d2.png)

**Node Functions**

Returns the Attachment Point Rotation corresponding to the specified Attachment Point Name on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

## **5. Get Target Entity**

![](../../../images/9a0ee039c2bbb3a0.png)

**Node Functions**

Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **6. Get Entity‘s Type**

![](../../../images/c4743ac23ff49b51.png)

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![](../../../images/6b29472ea713430d.png)

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![](../../../images/e54c9f78e30b5821.png)

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Self Entity**

![](../../../images/d4d4c87a3d6f4026.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **10. Filter Entity List Within Square Range**

![](../../../images/e7d42a139eb94fde.png)

**Node Functions**

Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Width | Floating Point Numbers |  |
| Input Parameter | Height | Floating Point Numbers |  |
| Input Parameter | Length | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **11. Filter Entity List Within Spherical Range**

![](../../../images/ec5bd2b0a337130a.png)

**Node Functions**

Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Parameter | Radius | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **12. Query Entity by GUID**

![](../../../images/e6252b9b403ef5f2.png)

**Node Functions**

Searches for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

## **13. Check the Preset Status Value of the Complex Creation**

![](../../../images/5263e6f104ad71fd.png)

**Node Functions**

Query the preset state value of the target creation corresponding to the preset state index.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# V. Faction Related

## **1. Query Entity Faction**

![](../../../images/a6a8f3b0dab2dd15.png)

**Node Functions**

Searches Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/28567847f12d001b.png)

**Node Functions**

Searches whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VI. Player and Character Related

## **1. Query If Self Is in Combat**

![](../../../images/144cabd38d2b1d02.png)

**Node Functions**

Searches whether the Entity associated with this Node Graph has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | In Combat | Boolean |  |

## **2. Get Current Character**

![](../../../images/3806077d0b435deb.png)

**Node Functions**

Returns the Character Entity currently controlled by this Player's client

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **3. Get Player Entity to Which the Character Belongs**

![](../../../images/ca833501c00f6b43.png)

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affiliated Player Entity | Entity |  |

## **4. Get List of Player Entities on the Field**

![](../../../images/f41a5d47877ebe4c.png)

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **5. Get Character Entity of Specified Player**

![](../../../images/6c46d56506cc259b.png)

**Node Functions**

Returns the Character Entity of the specified Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **6. Query GUID by Entity**

![](../../../images/157ca3f4b92ad597.png)

**Node Functions**

Searches for the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **7. Get Player Client Input Device Type**

![](../../../images/2ab8e8c80768745c.png)

**Node Functions**

Returns the Player's local input device type, as determined by the Interface mapping method

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Device Type | Enumeration | Includes keyboard/mouse, gamepad, touchscreen |

## **8. Get Player Movement Input**

![](../../../images/974b0bd3aa5cd188.png)

**Node Functions**

Returns the Input Direction and Input Strength of the current client player's movement.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Direction | Floating Point Numbers |  |
| Output Parameter | Input Strength | Floating Point Numbers |  |

## **9. Query Skill Variable Value**

![](../../../images/fd6302d76ef1c4a9.png)

**Node Functions**

Searches for the corresponding variable value based on the Skill Variable Config ID.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

## **10. Get Current Key Behavior**

![](../../../images/6b878c971eefa8ff.png)

**Node Functions**

Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List | Floating Point List |  |

## **11. Get Current Key Behavior (High Precision)**

![](../../../images/bdc6c3b33838eeb5.png)

**Node Functions**

Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List (s) | Integer List |  |
| Output Parameter | Entry Time List (ms) | Integer List |  |

## **12. Get Current Client Time**

![](../../../images/0db702ac08681fe1.png)

**Node Functions**

Returns the current client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time | Floating Point Numbers |  |

## **13. Get Current Client Time (High Precision)**

![](../../../images/884f9038d4214da1.png)

**Node Functions**

Returns the current client time. Due to floating-point precision issues, use this node if you requite greater granularity for the client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time (s) | Integer |  |
| Output Parameter | Client Time (ms) | Integer |  |

## **14. Query Whether Player Is Currently in Voice Chat**

![](../../../images/4535ec161d6098c9.png)

**Node Functions**

Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect during multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Currently in Voice Chat? | Boolean |  |

## **15. Get Skill Config ID by Skill Instance ID**

![](../../../images/eb5141786f073ebf.png)

**Node Functions**

Returns the corresponding Skill Config ID based on the Skill Instance ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Output Parameter | Skill Config ID | Config ID |  |

## **16. Query Skill Instance List by Specified Slot**

![](../../../images/11d868139f070188.png)

**Node Functions**

Searches for all skill instances in the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer List |  |

## **17. Query Active Skill Instance List of Specified Slot**

![](../../../images/5b3f81212f1f0abd.png)

**Node Functions**

Returns the skill instance(s) currently in the foreground for the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer |  |

## **18. Query Skill Instance ID by Skill Slot and Skill Config ID**

![](../../../images/7cf9f6dbb764b3f8.png)

**Node Functions**

Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Skill Config ID | Config ID |  |
| Output Parameter | Skill Instance ID List | Integer |  |

# VII. Unit Tags

## **1. Get Entity List by Unit Tag**

![](../../../images/d6e131d4712e1bfe.png)

**Node Functions**

Returns a list of all Entities in the scene that carry this Unit Tag

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Tag Index | Integer |  |
| Output Parameter | Entity List | Entity List |  |

## **2. Get Entity's Unit Tag List**

![](../../../images/0375695036459599.png)

**Node Functions**

Returns a list of all Unit Tags carried by the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | List | Integer List |  |

# VIII. General

## **1. Get Local Variable**

![](../../../images/1b042cfb1325a15e.png)

**Node Functions**

Returns the value of a specific local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# IX. Custom Aggro

## **1. Query if Specified Entity is in Combat**

![](../../../images/381c2b3759fb2674.png)

**Node Functions**

Available only for Custom Aggro Mode

Searches whether the specified Entity has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | In Combat | Boolean |  |

## **2. Get the Aggro List of the Specified Entity**

![](../../../images/654e5aa72edbf466.png)

**Node Functions**

Available only for Custom Aggro Mode

Gets Specific Entity's Aggro List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro List | Entity List |  |

## **3. Get the Aggro Target of the Specified Entity**

![](../../../images/344e34e43b30d7fd.png)

**Node Functions**

Available only for Custom Aggro Mode

Gets Aggro Target of Specific Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro Target | Entity |  |

# X. Triggers

## **1. Get All Entities Within the Collision Trigger**

![](../../../images/48398e7cfa2fb630.png)

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# XI. Ray

## **1. Get Ray Detection Result**

![](../../../images/1fdb55a90b696c78.png)

**Node Functions**

Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detection Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Options: Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# XII. Scanning

## **1.** Get All Valid Entities That Are Scannable by Scan Component

![](../../../images/44d8a44e9e8ae8f3.png)

**Node Functions**

Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Object List | Entity List |  |

## **2.** Get Entity Currently Scanned by Scan Component

![](../../../images/268a909133e0c66a.png)

**Node Functions**

Returns Entities currently detected by the Scan Component; these are Entities in the Active State

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Corresponding Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **3.** Get Entity's Current Active Scan Tags

![](../../../images/bf7cf734eff65d02.png)

**Node Functions**

Returns the Target Entity's Current Active Scan Tags

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **4. Get Entity's Scan Status**

![](../../../images/6dd6d5cfc4c419e0.png)

**Node Functions**

Get Entity Scan Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Status | Enumeration | Options: Invisible, Current Scan Target, Candidate Target, Not Eligible |

# XIII. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![](../../../images/85d938fb5c596f05.png)

**Node Functions**

Query if the specified dictionary contains a specific key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![](../../../images/4cc749b0d98811fa.png)

**Node Functions**

Query if the specified dictionary contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Check Dictionary Length**

![](../../../images/f695376c33cfa360.png)

**Node Functions**

Query the number of key-value pairs in a dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![](../../../images/8107140e5eb05c9b.png)

**Node Functions**

Get a list of all keys in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of keys retrieved may not be in the order they were inserted.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![](../../../images/8f2a494f116cd8ed.png)

**Node Functions**

Get a list of all values in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of values retrieved may not be in the order they were inserted.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![](../../../images/8275b5c8c6f0f485.png)

**Node Functions**

Query the value corresponding to a key in the dictionary, and return the default value of the type if the key does not exist.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# XIV. Unit Status

## **1. Whether the Entity Has the Specified Unit Status**

![](../../../images/a22f14a04077e55f.png)

**Node Functions**

Query whether the entity has the specified unit status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Configuration ID |  |
| Output Parameter | Has the Status | Boolean |  |

# XV. Pre-Aim

## **1. Get Base Object for Specified Pre-Aim Target**

![](../../../images/5241bb2dbc2a3127.png)

**Node Functions**

Gets the reference object for the specified pre-aim index. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Base Object | Entity |  |

## **2. Get Pre-Aim Result**

![](../../../images/2cb23b06e8aa7504.png)

**Node Functions**

Retrieves the on-hit location, position within range, optimal valid target, and valid target list for the specified pre-aim. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | Position Within Range | 3D Vector |  |
| Output Parameter | Optimal Valid Target | Entity |  |
| Output Parameter | Valid Target List | Entity List |  |

## **3. Get Pre-Aim Duration**

![](../../../images/38eff5c353da784e.png)

**Node Functions**

Retrieves how long the specified pre-aim has been active (in seconds). Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Duration (s) | Floating Point Numbers |  |

## **4. Get Current Active Pre-Aim ID**

![](../../../images/cee768c48ce724ec.png)

**Node Functions**

Retrieves the currently active pre-aim index in the current skill context. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Pre-Aim ID | Integer |  |

## **5. Get Pre-Aim Collision Detection Count**

![](../../../images/5ff6d04a239c0d57.png)

**Node Functions**

Retrieves the number of collision detection results for the specified pre-aim. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Result Count | Integer |  |

## **6. Get Pre-Aim Ray Hit Info**

![](../../../images/0e5101d01cbe2add.png)

**Node Functions**

Retrieves the raycast hit information for the specified pre-aim, including the on-hit location and on-hit entity. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

## **7. Get Pre-Aim Stick Deadzone Status**

![](../../../images/3a13447f64b357ab.png)

**Node Functions**

Retrieves whether the input joystick of the specified pre-aim is currently in the deadzone. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Whether in Deadzone | Boolean |  |

## **8. Query Pre-Aim Termination Cause**

![](../../../images/a95ff36f4cb65235.png)

**Node Functions**

Queries the termination cause of the specified pre-aim (None/Completed/Canceled). Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Termination Cause | Enumeration |  |

# **XVI. Cursor**

## **1. Get Cursor Active Status**

![](../../../images/50ac721f627bd188.png)

**Node Functions**

Checks whether the local cursor is set to always be visible. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Activate | Boolean |  |

## **2. Get Cursor Hit Result**

![](../../../images/f3127d251a668a12.png)

**Node Functions**

Retrieves the hit results for the local always-visible cursor, including the On-Hit Entity List, On-Hit Position List, and number of hits. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | On-Hit Entity List | Entity List |  |
| Output Parameter | On-Hit Position List | 3D Vector List |  |
| Output Parameter | Hits | Integer |  |

## **3. Get Cursor Screen Coordinates**

![](../../../images/a4465001dd990d51.png)

**Node Functions**

Retrieves the screen X and Y coordinates of the local always-visible cursor. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

## **4. Get Cursor Viewport Coordinates**

![](../../../images/0bfd7105c5183510.png)

**Node Functions**

Retrieves the viewport X and Y coordinates of the local always-visible cursor. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |
