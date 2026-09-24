---
title: Query Nodes
path_id: mhmsfb9qifdm
updated_at: 2026-08-08 23:46:43
category: Node Introduction/Client Nodes/Creation Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhmsfb9qifdm
---

# I. Skills

## **1.** Get the Complex Creation's Current Using Skill

![](../../../images/5717b3872405b820.png)

**Node Functions**

Return to the ID of the Skill currently being cast by the current Complex Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Skill ID | Integer |  |

## **2. Query Skill Variable Value**

![](../../../images/fd0144a70c5212c1.png)

**Node Functions**

Returns the corresponding variable value based on Skill Variable Config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

# II. List Operations

## **1. Get Corresponding Value From List**

![](../../../images/f91c54bf60f72ad3.png)

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

![](../../../images/27dd45968cec533c.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/0fbc00caea9cebe8.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/2c0ef8ce0be78657.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![](../../../images/487a2604f4293816.png)

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

## **6. Get Entity Type List**

![](../../../images/1b59160a83a34de7.png)

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

## **7. List Includes This Value**

![](../../../images/02a17dec2f29bf16.png)

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# III. Custom Variables

## **1. Get Custom Variable**

![](../../../images/0b4067ce318ad0b5.png)

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

# IV. Preset Status

## **1. Get Preset Status**

![](../../../images/697f085be5b22710.png)

**Node Functions**

Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# V. Entity-Related

## **1. Check the preset status value of the complex creation**

![](../../../images/bfdec2f023ca7ee8.png)

**Node Functions**

Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **2. Query if Entity Is on the Field**

![](../../../images/a50817e129927507.png)

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

![](../../../images/d6970cc9787e2152.png)

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **4. Get Target Attachment Point Location**

![](../../../images/2c8d7b1211b0988a.png)

**Node Functions**

Returns the Location of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **5. Get Target Attachment Point Rotation**

![](../../../images/015fa83e7dd9d701.png)

**Node Functions**

Returns the Rotation of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

## **6. Get Entity's Type**

![](../../../images/380e6b4546721eb1.png)

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![](../../../images/3f5c5166c96ff086.png)

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![](../../../images/bcf52be24ea6114a.png)

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Creation's Current Target**

![](../../../images/0a33cb2e8103e6c2.png)

**Node Functions**

Return to the specified Creation's current target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Creation | Entity |  |
| Output Parameter | Target Entity | Entity |  |

## **10. Get Self Entity**

![](../../../images/9d5ae2657bf95421.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **11. Get Sub-Entity List**

![](../../../images/2a1447005c65a7be.png)

**Node Functions**

Return to the Target Entity's Sub-Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Sub-Entity List | Entity List |  |

## **12. Filter Entity List Within Square Range**

![](../../../images/806d2151c61c3a2d.png)

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

## **13. Filter Entity List Within Spherical Range**

![](../../../images/60939ed49e8c5918.png)

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

## **14. Query Entity by GUID**

![](../../../images/b99276a8a9664fd1.png)

**Node Functions**

Search for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

## **15. Get Player Entity to Which the Character Belongs**

![](../../../images/0e9a5743b988dced.png)

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affiliated Player Entity | Entity |  |

## **16. Get List of Player Entities on the Field**

![](../../../images/b4a66e57d73ac83f.png)

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **17. Get Active Character of Specified Player**

![](../../../images/de2535170b57119f.png)

**Node Functions**

Available only in the Classic Mode. Obtains the on-field character in the player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **18. Get Player's Character List**

![](../../../images/000117f285c35a91.png)

**Node Functions**

Available in the Classic Mode only. Returns a list of all characters in the Player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character List | Entity List |  |

## **19. Query GUID by Entity**

![](../../../images/340486231877fdd7.png)

**Node Functions**

Returns the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **20. Check Class Mode Character ID**

![](../../../images/bca476ccd99531f4.png)

**Node Functions**

Available in Classic Mode only. Returns the Character ID of the Target Character, and can be used to look up the corresponding character in the Appendix [Classic Mode Character IDs](/ys/ugc/tutorial//detail/mh4imrrhzdzi)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Character | Entity |  |
| Output Parameter | Character ID | Integer |  |

# VI. Faction-Related

## **1. Query Entity Faction**

![](../../../images/fe145e0e17fa5ad6.png)

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/8d219b02d81d715c.png)

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VII. Tags

## **1. Get Entity List by Unit Tag**

![](../../../images/04b14b04d597dceb.png)

**Node Functions**

Returns a list of all Entities in the scene that carry this Unit Tag

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Tag Index | Integer |  |
| Output Parameter | Entity List | Entity List |  |

## **2. Get Entity's Unit Tag List**

![](../../../images/436295e017ce50ee.png)

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

![](../../../images/6b5d6a1347099d95.png)

**Node Functions**

Returns the value of a specific local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# IX. Custom Aggro

## **1. Query If Specified Entity Is in Combat**

![](../../../images/dc3a4db3c724143a.png)

**Node Functions**

Available only in Custom Aggro Mode

Check whether the specified Entity has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | In Combat | Boolean |  |

## **2. Get the Aggro List of the Specified Entity**

![](../../../images/3cb2896ccb15bbe4.png)

**Node Functions**

Available only in Custom Aggro Mode

Get Specified Entity's Aggro List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro List | Entity List |  |

## **3. Get the Aggro Target of the Specified Entity**

![](../../../images/9e89eb727d6d536b.png)

**Node Functions**

Available only in Custom Aggro Mode

Get Aggro Target of Specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro Target | Entity |  |

# X. Triggers

## **1. Get All Entities Within the Collision Trigger**

![](../../../images/9c71be6498bb7775.png)

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

![](../../../images/e3bbb748047ba0df.png)

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

# XII. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![](../../../images/c1dbc0133823778f.png)

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

![](../../../images/96dd8dd5cd17d209.png)

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

![](../../../images/2e82ad2bc155c060.png)

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![](../../../images/123643ab8fc9f7cb.png)

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![](../../../images/26a70f37c4deff57.png)

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![](../../../images/9c719c429b64ffae.png)

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# **XIII**. Unit Status

## **1. Whether the Entity Has the Specified Unit Status**

![](../../../images/546cf72ed59e6b2a.png)

**Node Functions**

Check whether the Target Entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Configuration ID |  |
| Output Parameter | Has the Status | Boolean |  |

# **XIV. Cursor**

## **1. Get Cursor Active Status**

![](../../../images/5dd21cbaa175741a.png)

**Node Functions**

Get whether the local always-visible cursor is currently active. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Activate | Boolean |  |

## **2. Get Cursor Hit Result**

![](../../../images/55f77031e1f667e6.png)

**Node Functions**

Get the hit results of the local always-visible cursor, including the list of hit entities, list of hit positions, and hit count. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | On-Hit Entity List | Entity List |  |
| Output Parameter | On-Hit Entity List | 3D Vector List |  |
| Output Parameter | Hits | Integer |  |

## **3. Get Cursor Screen Coordinates**

![](../../../images/eff252da23e8ff1b.png)

**Node Functions**

Get the X and Y screen coordinates of the local always-visible cursor. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

## **4. Get Cursor Viewport Coordinates**

![](../../../images/4f16563223930cd9.png)

**Node Functions**

Get the X and Y viewport coordinates of the local persistent cursor. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Viewport X | Floating Point Numbers |  |
| Output Parameter | Viewport Y | Floating Point Numbers |  |
