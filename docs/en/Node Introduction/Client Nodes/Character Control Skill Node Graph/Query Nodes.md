---
title: Query Nodes
path_id: mh4pz30j635c
updated_at: 2026-07-22 16:15:47
category: Node Introduction/Client Nodes/Character Control Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh4pz30j635c
---

# **I. List-Related Functions**

## **1. Get Corresponding Value From List**

![](../../../images/b4534851fff8ea74.png)

**Node Functions**

Returns the value at the specified index in the list. List IDs start from 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![](../../../images/a2e2209572f42d5e.png)

**Node Functions**

Returns the length of the list (the number of elements in the list)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/c4d9f0b71f283c07.png)

**Node Functions**

Applies only to Floating Point Lists or Integer Lists; returns the maximum value in the list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/b7678be9da7bbb9c.png)

**Node Functions**

Applies only to Floating Point Lists or Integer Lists; returns the minimum value in the list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Entity Type List**

![](../../../images/bd8c121b80bf12f1.png)

**Node Functions**

Creates a list containing the specified Entity types. Available types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

## **6. List Includes This Value**

![](../../../images/b900a88495402743.png)

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

## **7. Get Ray Filter Type List**

![](../../../images/e8f8a5cc40db8f6f.png)

**Node Functions**

Creates a list containing the specified Ray Filter Types. Available filter types include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

# **II. Custom Variables**

## **1. Get Custom Variable**

![](../../../images/3239858b94a8e37c.png)

**Node Functions**

Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the default value for its type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# **III. Preset Status**

## **1. Get Preset Status**

![](../../../images/8d37aa2c854496ca.png)

**Node Functions**

Returns the value of the specified Preset Status for the Target Entity. If the Entity does not have the specified Preset Status, returns 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# **IV. Entity-Related Functions**

## **1. Query Entity by GUID**

![](../../../images/3657654a7aae9b7e.png)

**Node Functions**

Queries the Entity using the specified GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

## **2. Get Entity Location**

![](../../../images/f4cc583a5a0aa882.png)

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **3. Get Entity Rotation**

![](../../../images/4213657c8127533a.png)

**Node Functions**

Returns the Rotation of the specified Entity in Euler angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **4. Get Self Entity**

![](../../../images/d6b39434d51a5859.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **5. Get Target Entity**

![](../../../images/fb45483e5afd7751.png)

**Node Functions**

Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **6. Get Unit Attack Target**

![](../../../images/df55c0be4e2e35c9.png)

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **7. Get Target Attachment Point Location**

![](../../../images/0e736a9a282200ff.png)

**Node Functions**

Returns the Location of the specified Attachment Point on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **8. Get Target Attachment Point Rotation**

![](../../../images/4608374ec9844b7b.png)

**Node Functions**

Returns the Rotation of the specified Attachment Point on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

## **9. Get Entity Type**

![](../../../images/2f1f4fe2a917d6e7.png)

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumerate |  |

## **10. Filter Entity List Within Spherical Range**

![](../../../images/da62c591ea15f67d.png)

**Node Functions**

Filters Entities within a spherical range according to specified rules and a maximum count, and returns a list of Entities that meet the criteria

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radius | Floating Point Number |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **11. Filter Entity List Within Square Range**

![](../../../images/55ce25fc77344019.png)

**Node Functions**

Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the criteria

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Width | Floating Point Number |  |
| Input Parameter | Height | Floating Point Number |  |
| Input Parameter | Length | Floating Point Number |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **12. Query If Entity Is on the Field**

![](../../../images/ce681e391234d3b9.png)

**Node Functions**

Checks whether the specified Entity is on the field

Note that Character Entities are still considered on the field even when they are downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **13. Check the Preset Status Value of the Complex Creation**

![](../../../images/68502d7596fbf46c.png)

**Node Functions**

Returns the Preset Status Value of the Target Creation at the specified Preset Status Index

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# **V. Faction-Related Functions**

## **1. Query Entity Faction**

![](../../../images/3c9a0ad529667463.png)

**Node Functions**

Returns the Faction of the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/79135ef11c47fa39.png)

**Node Functions**

Checks whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# **VI. Player and Character Related**

## **1. Get Character Entity of Specified Player**

![](../../../images/c9ebcda9f1315517.png)

**Node Functions**

Returns the Character Entity associated with the specified Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **2. Get Player Entity to Which the Character Belongs**

![](../../../images/711ed8702b210011.png)

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affiliated Player Entity | Entity |  |

## **3. Get List of Player Entities on the Field**

![](../../../images/5ab6638abed6534d.png)

**Node Functions**

Returns a list of all Player Entities currently on the field

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **4. Query GUID by Entity**

![](../../../images/ea2a7be08176f91a.png)

**Node Functions**

Returns the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **5. Query If Self Is in Combat**

![](../../../images/c1d26a92946078b5.png)

**Node Functions**

Checks whether the Entity associated with this Node Graph is in combat

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | In Combat | Boolean |  |

## **6. Get Current Character**

![](../../../images/629a8697dc186775.png)

**Node Functions**

Returns the Character Entity currently controlled by this Player's client

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **7. Get Player Client Input Device Type**

![](../../../images/ad5503db0b5fbbab.png)

**Node Functions**

Returns the Player's client input device type, as determined by the UI mapping method

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Device Type | Enumeration | Includes keyboard and mouse, controller, touchscreen |

## **8. Get Player Movement Input**

![](../../../images/d3bee1cd7af2be81.png)

**Node Functions**

Returns the current local Player's movement input direction and input strength

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Direction | Floating Point Number |  |
| Output Parameter | Input Strength | Floating Point Number |  |

## **9. Query Skill Variable Value**

![](../../../images/da744198ec77ee65.png)

**Node Functions**

Returns the variable value corresponding to the specified Skill Variable Config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Number |  |

## **10. Get Current Key Behavior**

![](../../../images/27a4aed19d88fee3.png)

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel, along with their corresponding entry times

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List | Floating Point List |  |

## **11. Get Current Key Behavior (High Precision)**

![](../../../images/cb36e0f3b3ca9495.png)

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel, along with their corresponding entry times. Use this node when higher-precision entry times are required due to floating-point precision limitations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List (s) | Integer List |  |
| Output Parameter | Entry Time List (ms) | Integer List |  |

## **12. Get Current Client Time**

![](../../../images/a953a3f86b5c3eda.png)

**Node Functions**

Returns the current client time

If this node's content will be shown to players, Craftspeople should inform players in advance in the description or other relevant areas about the effects of obtaining the client time

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time | Floating Point Number |  |

## **13. Get Current Client Time (High Precision)**

![](../../../images/4a19720dc12559f4.png)

**Node Functions**

Returns the current client time. Use this node when higher-precision client time is required due to floating-point precision limitations

If this node's content will be shown to players, Craftspeople should inform players in advance in the description or other relevant areas about the effects of obtaining the client time

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time (s) | Integer |  |
| Output Parameter | Client Time (ms) | Integer |  |

## **14. Query Whether Player Is Currently in Voice Chat**

![](../../../images/167eba6ed22a6adf.png)

**Node Functions**

Returns true when the player's client detects microphone input

Note: This node only functions in multiplayer modes (multiplayer test play and live Co-Op mode). It does not function in single-player modes (single-player test play or live single-player mode)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Currently in Voice Chat? | Boolean |  |

## **15. Get Skill Config ID by Skill Instance ID**

![](../../../images/2d5aa0c854fb014a.png)

**Node Functions**

Returns the Skill Config ID corresponding to the specified Skill Instance ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Skill Instance ID | Integer |  |
| Output Parameter | Skill Config ID | Config ID |  |

## **16. Query Skill Instance List by Specified Slot**

![](../../../images/b536dd271cd77d27.png)

**Node Functions**

Returns all Skill Instances in the specified slot

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer List |  |

## **17. Query Active Skill Instance List of Specified Slot**

![](../../../images/84f20fc199ce4859.png)

**Node Functions**

Returns the Skill Instance currently active in the specified slot

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID | Integer |  |

## **18. Get Skill Instance ID by Skill Slot and Skill Config ID**

![](../../../images/eca8962c3be77322.png)

**Node Functions**

Returns the Skill Instance ID corresponding to the specified Skill Slot and Skill Config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Intput Parameter | Skill Config ID | Config ID |  |
| Output Parameter | Skill Instance ID | Integer |  |

# **VII. Pre-Aiming**

## **1. Get Base Object for Specified Pre-Aim Target**

![](../../../images/1b973700d4448de3.png)

**Node Functions**

Returns the Base Object for the specified Pre-Aim ID. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Base Object | Entity |  |

## **2. Get Pre-Aim Result**

![](../../../images/034ef0e4187f7706.png)

**Node Functions**

Returns the On-Hit Location, Position Within Range, Optimal Valid Target, and Valid Target List for the specified pre-aim. Only available in Beyond Mode

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

![](../../../images/43260e5705be7a2e.png)

**Node Functions**

Returns the elapsed duration (in seconds) of the specified pre-aim. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Duration (s) | Floating Point Number |  |

## **4. Get Current Active Pre-Aim ID**

![](../../../images/c3794f127c23839d.png)

**Node Functions**

Returns the ID of the currently active pre-aim in the current skill context. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Pre-Aim ID | Integer |  |

## **5. Get Pre-Aim Collision Detection Count**

![](../../../images/807ce3aaa95d90ee.png)

**Node Functions**

Returns the number of collision detection results for the specified pre-aim. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Result Count | Integer |  |

## **6. Get Pre-Aim Ray Hit Info**

![](../../../images/9dd7db151b8091a7.png)

**Node Functions**

Returns the ray hit information for the specified pre-aim, including the On-Hit Location and On-Hit Entity. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

## **7. Get Pre-Aim Stick Deadzone Status**

![](../../../images/b91ce4652ff1b13c.png)

**Node Functions**

Returns whether the input stick for the specified pre-aim is within the deadzone. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Whether in Deadzone | Boolean |  |

## **8. Query Pre-Aim Termination Cause**

![](../../../images/40bb0f7cdc3c0081.png)

**Node Functions**

Returns the end reason of the specified pre-aim (None/Completed/Canceled). Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Pre-Aim ID | Integer |  |
| Output Parameter | Termination Cause | Enumeration |  |

# **VIII. Cursor**

## **1. Get Cursor Active Status**

![](../../../images/7bcc4d35fee27124.png)

**Node Functions**

Returns whether the local persistent cursor is active. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Activate | Boolean |  |

## **2. Get Cursor Hit Result**

![](../../../images/bb6f2df3abb93ab6.png)

**Node Functions**

Returns the hit results of the local persistent cursor, including the On-Hit Entity List, On-Hit Position List, and Hit count. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | On-Hit Entity List | Entity List |  |
| Output Parameter | On-Hit Location List | 3D Vector List |  |
| Output Parameter | Hits | Integer |  |

## **3. Get Cursor Screen Coordinates**

![](../../../images/d7bc6909f4bfa619.png)

**Node Functions**

Returns the X and Y screen coordinates of the local persistent cursor. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Screen X | Floating Point Number |  |
| Output Parameter | Screen Y | Floating Point Number |  |

## **4. Get Cursor Viewport Coordinates**

![](../../../images/e59661e6af07e69e.png)

**Node Functions**

Returns the X and Y viewport coordinates of the local persistent cursor. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Viewport X | Floating Point Number |  |
| Output Parameter | Viewport Y | Floating Point Number |  |

# **IX. Tags**

## **1. Get Entity's Unit Tag List**

![](../../../images/c13252b4514e71ca.png)

**Node Functions**

Returns a list of all Unit Tags attached to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | List | Integer List |  |

## **2. Get Entity List by Unit Tag**

![](../../../images/0482ec75224c0017.png)

**Node Functions**

Returns a list of all Entities on the field that have the specified Unit Tag

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Tag Index | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# **X. General**

## **1. Get Local Variable**

![](../../../images/97085f0cfbbf5ab6.png)

**Node Functions**

Returns the value of the specified local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# **XI. Custom Aggro**

## **1. Get the Aggro Target of the Specified Entity**

![](../../../images/07254ee63d7d2f6b.png)

**Node Functions**

Only available in Custom Aggro Mode

Returns the aggro target of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro Target | Entity |  |

## **2. Get the Aggro List of the Specified Entity**

![](../../../images/da2495a2e02f0e49.png)

**Node Functions**

Only available in Custom Aggro Mode

Returns the aggro list of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro List | Entity List |  |

## **3. Query If Specified Entity Is in Combat**

![](../../../images/d2317f167ae45349.png)

**Node Functions**

Only available in Custom Aggro Mode

Checks whether the specified Entity is in combat

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | In Combat | Boolean |  |

# **XII. Triggers**

## **1. Get All Entities Within the Collision Trigger**

![](../../../images/b802c59c01cc8427.png)

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to the specified ID in the Collision Trigger Component of the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# **XIII. Rays**

## **1. Get Ray Detection Results**

![](../../../images/4caeb93f1a6b76e2.png)

**Node Functions**

Returns the first target or on-hit location that meets the filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detect Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Number |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Intput Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, and Creation |
| Intput Parameter | Hit Layer Filter | Enumeration List | Includes Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# **XIV. Scan**

## **1. Get Entity Currently Scanned by Scan Component**

![](../../../images/b215723c7214e921.png)

**Node Functions**

Returns the Entities currently detected by the Scan Component. These Entities have the "Activated State" scan status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Corresponding Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **2. Get All Valid Entities That Are Scannable by Scan Component**

![](../../../images/5736ec306a947b3d.png)

**Node Functions**

Returns all valid objects that can be scanned by the Scan Component. Valid objects are units that have a Scan Component and whose filter returns true, regardless of their scannable status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Object List | Entity List |  |

## **3. Get Entity's Scan Status**

![](../../../images/cdfa814e13a235de.png)

**Node Functions**

Returns the scan status of the Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Status | Enumeration | Options: Invisible, Current Scan Target, Candidate Target, Condition Not Met |

## **4. Get Entity's Current Active Scan Tags**

![](../../../images/7a2cd7ae93f84551.png)

**Node Functions**

Returns the currently active scan tags of the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

# **XV. Dictionary**

## **1. Query Dictionary Value by Key**

![](../../../images/3e9e88e3fb3c84a3.png)

**Node Functions**

Returns the value corresponding to the specified key in the dictionary. If the key does not exist, returns the default value for its type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

## **2. Query If Dictionary Contains Specific Key**

![](../../../images/0cc9d5b3790e2bfb.png)

**Node Functions**

Checks whether the specified dictionary contains the specified key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Query If Dictionary Contains Specific Value**

![](../../../images/e5e6908047b6afe2.png)

**Node Functions**

Checks whether the specified dictionary contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **4. Check Dictionary Length**

![](../../../images/577d7807a44a8801.png)

**Node Functions**

Returns the number of key-value pairs in the dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **5. Get List of Values From Dictionary**

![](../../../images/b141577227556dee.png)

**Node Functions**

Returns a list of all values in the dictionary. Because key-value pairs in a dictionary are unordered, the values in the returned list may not be in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Get List of Keys From Dictionary**

![](../../../images/013dcb5cffc06cfa.png)

**Node Functions**

Returns a list of all keys in the dictionary. Because key-value pairs in a dictionary are unordered, the keys in the returned list may not be in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

# **XVI. Unit Status**

## **1. Whether the Entity Has the Specified Unit Status**

![](../../../images/47d89cebf9b9ad9d.png)

**Node Functions**

Checks whether the Target Entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Config ID |  |
| Output Parameter | Has the Status | Boolean |  |

# **XVII. Motion Device**

## **1. Get Currently Activated Control Motion Device List**

![](../../../images/3d8c143b79300db2.png)

**Node Functions**

Returns the list of currently activated control motion devices

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Control Motion Device List | Entity List |  |

## **2. Get Currently Followed Control Motion Device**

![](../../../images/7fc3d61f768e20dc.png)

**Node Functions**

Returns the currently followed motion device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Follow Control Motion Device | Entity |  |

## **3. Get Control Motion Device's Movement Parameters**

![](../../../images/931a183328273b60.png)

**Node Functions**

Returns the movement parameters of the specified control motion device, including temporary movement parameters. The addition of temporary values takes effect in the next frame, so changes to these values cannot be retrieved by a Get node within the current execution flow

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Control Motion Device | Entity |  |
| Output Parameter | Forward Acceleration | Floating Point Number |  |
| Output Parameter | Reverse Acceleration | Floating Point Number |  |
| Output Parameter | Turn Speed | Floating Point Number |  |
| Output Parameter | Base Resistance Deceleration | Floating Point Number |  |
| Output Parameter | Resistance Coefficient | Floating Point Number |  |
| Output Parameter | Max Forward Speed | Floating Point Number |  |
| Output Parameter | Max Reverse Speed | Floating Point Number |  |

## **4. Get Control Motion Device's Current Speed**

![](../../../images/d74fd83ca38ee25a.png)

**Node Functions**

Returns the current speed of the specified control motion device (speed magnitude and unit direction vector)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Motion Device | Entity |  |
| Output Parameter | Speed Magnitude | Floating Point Number |  |
| Output Parameter | Speed Direction | 3D Vector |  |

## **5. Get Control Motion Device's Forward Direction**

![](../../../images/52115b9950bf1ec5.png)

**Node Functions**

Returns the forward direction vector of the specified control motion device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Motion Device | Entity |  |
| Output Parameter | Forward Direction | 3D Vector |  |

## **6. Get Control Motion Device's Target Turn Direction**

![](../../../images/5a3ef37583a4c4db.png)

**Node Functions**

Returns the target steering direction of the control motion device (the movement joystick input converted into the control motion device's target steering direction)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Motion Device | Entity |  |
| Output Parameter | Target Steering Direction | 3D Vector |  |

## **7. Get Control Motion Device Grounded Status**

![](../../../images/4054ecec295ec1b5.png)

**Node Functions**

Returns whether the specified control motion device is currently grounded

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Target Control Motion Device | Entity |  |
| Output Parameter | Grounded | Boolean |  |
