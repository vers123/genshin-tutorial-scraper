---
title: Query Nodes
path_id: mhwd900y1lbs
updated_at: 2026-08-07 16:08:01
category: Node Introduction/Client Nodes/Filter Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhwd900y1lbs
---

# I. List Related

## **1. Get Corresponding Value From List**

![](../../../images/ba0453e49addd17e.png)

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

![](../../../images/3410764edd17aa87.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/3304cfbebaedc28e.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/b209f87e47516f17.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![](../../../images/1f2a791115e6f43e.png)

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumerationd List |  |

## **6. Get Entity Type List**

![](../../../images/745b23c2c8d9a278.png)

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumerationd List |  |

## **7. List Includes This Value**

![](../../../images/9f55f0935a5f8bec.png)

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

![](../../../images/ae8c1a5008a6c830.png)

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

![](../../../images/362097ab3ccb7cc8.png)

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

## **1. Check the Preset Status Value of the Complex Creation**

![](../../../images/8b2d7fcbde36b4db.png)

**Node Functions**

Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **2. Query If Entity Is on the Field**

![](../../../images/78dd82955c186b28.png)

**Node Functions**

Check whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **3. Get Unit Attack Target**

![](../../../images/442de88bde8b88a7.png)

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **4. Get Target Attachment Point Location**

![](../../../images/8cfa8e1d510ddbc6.png)

**Node Functions**

Returns the Location of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **5. Get Target Entity**

![](../../../images/0b1158ec62203aa5.png)

**Node Functions**

Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **6. Get Entity's Type**

![](../../../images/4828996167a8b071.png)

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![](../../../images/e1890021452e9bda.png)

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![](../../../images/e9bd45b9481e9231.png)

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Self Entity**

![](../../../images/be75ccac6f27bde2.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **10. Filter Entity List Within Square Range**

![](../../../images/a39359357faad6eb.png)

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
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **11. Filter Entity List Within Spherical Range**

![](../../../images/a7c32857e048ce19.png)

**Node Functions**

Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Parameter | Radius | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **12. Query Entity by GUID**

![](../../../images/ff6fc102c8acbb22.png)

**Node Functions**

Search for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

# V. Faction Related

## **1. Query Entity Faction**

![](../../../images/5155eee3ee6b418d.png)

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/59ed9e30b6980408.png)

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VI. Player and Character Related

## **1. Query If Self Is in Combat**

![](../../../images/9ff8913f21463785.png)

**Node Functions**

Check whether the Entity associated with this Node Graph has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | In Combat | Boolean |  |

## **2. Get Player Client Input Device Type**

![](../../../images/45b442770d512753.png)

**Node Functions**

Returns the Player's local input device type, as determined by the Interface mapping method

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Device Type | Enumeration | Includes keyboard/mouse, gamepad, touchscreen |

## **3. Get Current Character**

![](../../../images/649f1f428e70135c.png)

**Node Functions**

Returns the Character Entity currently controlled by this Player's client

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **4. Get Player Entity to Which the Character Belongs**

![](../../../images/44e1a2b019b3984b.png)

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affliated Player Entity | Entity |  |

## **5. Get List of Player Entities on the Field**

![](../../../images/6b137e195b0d722e.png)

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **6. Get Character Entity of Specified Player**

![](../../../images/547bd5eacea9004d.png)

**Node Functions**

Returns the Character Entity of the specified Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **7. Query GUID by Entity**

![](../../../images/127ddea17e1b9db2.png)

**Node Functions**

Search for the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **8. Get Active Character of Specified Player**

![](../../../images/f622f984a7ba1134.png)

**Node Functions**

Available only in Classic Mode. Returns the on-field character in the player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **9. Check Classic Mode Character IDs**

![](../../../images/80bedde4d2a4b087.png)

**Node Functions**

Only available in the Classic Mode. Query the character ID of the Target Character. Check the appendix to see which Character it corresponds to[Classic Mode Character ID List](/ys/ugc/tutorial//detail/mh4imrrhzdzi)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Character | Entity |  |
| Output Parameter | Character ID | Integer |  |

## **10.** **Get Player's Character List**

![](../../../images/c75b89b84abeb2a3.png)

**Node Functions**

Returns a list of characters in the player's team. Available only in Classic Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character List | Entity List |  |

## **11. Get Player Movement Input**

![](../../../images/007ae0fb2e72c7a7.png)

**Node Functions**

Returns the Input Direction and Input Strength of the player's movement on the current client.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input Direction | Floating Point Numbers |  |
| Output Parameter | Input Strength | Floating Point Numbers |  |

## **12. Query Skill Variable Value**

![](../../../images/c865b09027e2023f.png)

**Node Functions**

Queries the corresponding Variable Value based on the Skill Variable Config ID.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

## **13. Get Current Key Behavior**

![](../../../images/9d90d13856214ebc.png)

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List | Floating Point List |  |

## **14. Get Current Key Behavior (High Precision)**

![](../../../images/8f4028c72e67b121.png)

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List (s) | Integer List |  |
| Output Parameter | Entry Time List (ms) | Integer List |  |

## **15. Get Current Client Time**

![](../../../images/1d1dbf2eb58cef96.png)

**Node Functions**

Returns the current client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time | Floating Point Numbers |  |

## **16. Get Current Client Time (High Precision)**

![](../../../images/072f01f459f5bdff.png)

**Node Functions**

Returns the current client time. Due to floating-point precision issues, use this node if you need greater granularity for the client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time (s) | Integer |  |
| Output Parameter | Client Time (ms) | Integer |  |

## **17. Query Whether Player Is Currently in Voice Chat**

![](../../../images/59f390418ff091db.png)

**Node Functions**

Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect in multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Currently in Voice Chat? | Boolean |  |

## **18. Get Skill Config ID by Skill Instance ID**

![](../../../images/b79714c2c322ec94.png)

**Node Functions**

Returns the corresponding Skill Config ID based on the Skill Instance ID provided

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Output Parameter | Skill Config ID | Config ID |  |

## **19. Query Skill Instance List by Specified Slot**

![](../../../images/74c518ed32b605f7.png)

**Node Functions**

Returns a list of all skill instances in the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer List |  |

## **20. Query Active Skill Instance List of Specified Slot**

![](../../../images/c88184f185712590.png)

**Node Functions**

Gets the skill instance currently in the foreground for the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer |  |

## **21. Query Skill Instance ID by Skill Slot and Skill Config ID**

![](../../../images/13b3e20264e9a69c.png)

**Node Functions**

Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Skill Config ID | Config ID |  |
| Output Parameter | Skill Instance ID List | Integer |  |

# VII. Attachment Points

## **1. Get Target Attachment Point Rotation**

![](../../../images/f7fd0361257911f8.png)

**Node Functions**

Returns the Rotation of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

# VIII. Triggers

## **1. Get All Entities Within the Collision Trigger**

![](../../../images/89986fe8d58bafa9.png)

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# IX. Rays

## **1. Get Ray Detection Result**

![](../../../images/edd54b5b1eb90152.png)

**Node Functions**

Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detect Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Options: Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# X. Scanning

1.

## Get All Valid Entities That Are Scannable by Scan Component

![](../../../images/8c9382c442ce06c9.png)

**Node Functions**

Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Object List | Entity List |  |

2.

## Get Entity Currently Scanned by Scan Component

![](../../../images/d0b44a7d4f439cc9.png)

**Node Functions**

Returns Entities currently detected by the Scan Component; these are Entities in the Active State

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Corresponding Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

3.

## Get Entity's Current Active Scan Tags

![](../../../images/7037dfda7c02bf7b.png)

**Node Functions**

Returns the Target Entity's Current Active Scan Tags

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **4. Get Entity's Scan Status**

![](../../../images/76b295306942a3b0.png)

**Node Functions**

Get Entity Scan Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Status | Enumeration | Options: Invisible, Current Scan Target, Candidate Target, Criteria Not Met |

# **XI**. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![](../../../images/5a8660f23406d3ab.png)

**Node Functions**

Check whether the specified Dictionary contains the specified Key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![](../../../images/0466f2a8d9fb1bb3.png)

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Check Dictionary Length**

![](../../../images/f3f700b60bfb299e.png)

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![](../../../images/71795108ae1fd3cd.png)

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![](../../../images/23690bb227704f5a.png)

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![](../../../images/337f1636024ffa7b.png)

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# **XII**. Unit Status

## **1. Whether the Entity has the Specified Unit Status**

![](../../../images/157c27c7da497910.png)

**Node Functions**

Check whether the Target Entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Config ID |  |
| Output Parameter | Has the Status | Boolean |  |

# **XIII. Pre-Aim**

## **1. Get Base Object for Specified Pre-Aim Target**

![](../../../images/3c966bf5fb9121cd.png)

**Node Functions**

Returns the reference object at the specified pre-aim index. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Base Object | Entity |  |

## **2. Get Pre-Aim Result**

![](../../../images/65efb57fb2ef8446.png)

**Node Functions**

Returns the on-hit location, position within range, optimal valid target, and valid target list for the specified pre-aim. Available only in Beyond Mode.

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

![](../../../images/e1da5019c61dbe36.png)

**Node Functions**

Returns the duration (in seconds) for which the specified pre-aim has been active. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Duration (s) | Floating Point Number |  |

## **4. Get Current Active Pre-Aim ID**

![](../../../images/1e20e2e6e7cea79e.png)

**Node Functions**

Returns the pre-aim ID currently active in the current skill context. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |

## **5. Get Pre-Aim Collision Detection Count**

![](../../../images/15fe195dffb8daff.png)

**Node Functions**

Returns the number of collision detection results for the specified pre-aim. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Result Count | Integer |  |

## **6. Get Pre-Aim Ray Hit Info**

![](../../../images/c6571dc697f0eb4c.png)

**Node Functions**

Returns ray hit info for the specified pre-aim, including the on-hit location and on-hit entity. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

## **7. Get Pre-Aim Stick Deadzone Status**

![](../../../images/92efaab6cb97559b.png)

**Node Functions**

Returns whether the input stick for the specified pre-aim is within the deadzone. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Whether in Deadzone | Boolean |  |

## **8. Query Pre-Aim Termination Cause**

![](../../../images/400a11779f2de0a3.png)

**Node Functions**

Returns the termination cause for the specified pre-aim (None/Completed/Canceled). Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Termination Cause | Enumeration |  |

# **XIV. Cursor**

## **1. Get Cursor Active Status**

![](../../../images/e0f91c93b7982727.png)

**Node Functions**

Returns the active status of the local persistent cursor. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Activate | Boolean |  |

## **2. Get Cursor Hit Result**

![](../../../images/eae535010a7ef95a.png)

**Node Functions**

Returns the hit results of the local persistent cursor, including the on-hit entity list, on-hit position list, and hits. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | On-Hit Entity List | Entity List |  |
| Output Parameter | On-Hit Position List | 3D Vector List |  |
| Output Parameter | Hits | Integer |  |

## **3. Get Cursor Screen Coordinates**

![](../../../images/3eeece6107ca9d55.png)

**Node Functions**

Returns the X and Y screen coordinates of the local persistent cursor. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Screen X | Floating Point Number |  |
| Output Parameter | Screen Y | Floating Point Number |  |

## **4. Get Cursor Viewport Coordinates**

![](../../../images/825d5dfcf06d20f9.png)

**Node Functions**

Returns the X and Y viewport coordinates of the local persistent cursor. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Viewport X | Floating Point Number |  |
| Output Parameter | Viewport Y | Floating Point Number |  |

#
