---
title: Query Nodes
path_id: mhdzd7i50td0
updated_at: 2026-09-18 21:14:24
category: Node Introduction/Client Nodes/Creation Status Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdzd7i50td0
---

# I. General

## **1. Check Target Position Pathfinding Availability**

![](../../../images/aa285aca831352b7.png)

**Node Functions**

Check whether a Creation can reach the current Target Point using normal pathfinding

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is Pathfinding Achievable? | Boolean |  |

## **2. Check the Coordinates When Entering Battle**

![](../../../images/7c4112eca36665ec.png)

**Node Functions**

Query the Coordinate Points when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Entering Battle Position | 3D Vector |  |
| Output Parameter | Entering Battle Rotation | 3D Vector |  |

## **3. Check If Entity Is on the Field**

![](../../../images/a721c132eb616cb2.png)

**Node Functions**

Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | On the Field | Boolean |  |

## **4. Check the Vertical Angle From Self to Target**

![](../../../images/2c1d654d0bc1fea2.png)

**Node Functions**

Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Angle | Floating Point Numbers |  |

## **5. Check the Vertical Distance From Self to Target**

![](../../../images/b8211163a9f4bfbd.png)

**Node Functions**

Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Distance | Floating Point Numbers |  |

## **6. Check the Distance From Self to Target**

![](../../../images/aec0205874d55177.png)

**Node Functions**

Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Distance | Floating Point Numbers |  |

## **7. Check the Horizontal Angle From Self to Target**

![](../../../images/dfff393cd8be9fa2.png)

**Node Functions**

Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Angle | Floating Point Numbers |  |

## **8. Check the Horizontal Distance From Self to Target**

![](../../../images/6494fa0a9bc7d080.png)

**Node Functions**

Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Distance | Floating Point Numbers |  |

## **9. Check Whether Self Is in Battle**

![](../../../images/fed53749ff25ccf5.png)

**Node Functions**

Check whether the Creation is currently in battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Whether in Battle | Boolean |  |

## **10. Check If Self Is in the Territory**

![](../../../images/c6e12e1175066e18.png)

**Node Functions**

Check whether this Creation's current location is within the Territory

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is in the Territory | Boolean |  |

## **11. Check Whether Self Is Using a Skill**

![](../../../images/7e74f6a97d985ac1.png)

**Node Functions**

Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is The Unit Using a Skill? | Boolean |  |
| Output Parameter | Skill ID | Integer |  |

## **12. Get Spawn Point Location Information**

![](../../../images/bd038e082b00f7b9.png)

**Node Functions**

Obtain the Creation's own Spawn Point information

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Spawn Point Coordinates | 3D Vector |  |
| Output Parameter | Spawn Point Rotation | 3D Vector |  |

## **13. Get Stage Entity**

![](../../../images/5443977116ff9c33.png)

**Node Functions**

Obtain Stage Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Stage Entity | Entity |  |

## **14. Get Target Level**

![](../../../images/35250f5f15a2769d.png)

**Node Functions**

Obtain the Target Entity's current level

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Current Level | Integer |  |

## **15. Get Target ATK**

![](../../../images/3815986baffc7943.png)

**Node Functions**

Obtain the Target Entity's ATK parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base ATK | Floating Point Numbers |  |
| Output Parameter | Current ATK | Floating Point Numbers |  |

## **16. Get Target HP**

![](../../../images/fa68bed89b82f531.png)

**Node Functions**

Obtain HP-related parameters for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base HP | Floating Point Numbers |  |
| Output Parameter | Max HP | Floating Point Numbers |  |
| Output Parameter | Current HP Percentage | Floating Point Numbers |  |

## **17. Get Target Entity**

![](../../../images/d1c069d95c247f2a.png)

**Node Functions**

Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **18. Get Previous Frame Execution Tactic**

![](../../../images/343b5ab457f3fc0e.png)

**Node Functions**

Obtain the Tactic executed by Creations in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Tactic Type | Enumeration |  |
| Output Parameter | Tactical Context | String |  |

## **19. Get Previous Frame Execution Status**

![](../../../images/c991d4759735dd9c.png)

**Node Functions**

Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **20. Get Entity's Type**

![](../../../images/ce9843ba7686fb8c.png)

**Node Functions**

Obtain the Target Entity's Type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Entity Type | Enumeration |  |

## **21. Get Entity Location**

![](../../../images/00cfac3eca54f928.png)

**Node Functions**

Obtain the Target Entity's Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Location | 3D Vector |  |

## **22. Get Entity Rotation**

![](../../../images/509daaa5e281d44a.png)

**Node Functions**

Obtain the Target Entity's Rotation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Rotation | 3D Vector |  |

## **23. Get Object Preset Status**

![](../../../images/cc83edf0bfd9d5b4.png)

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index from the Target Entity. If the Entity does not have the specified Preset Status, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **24. Get Custom Variable**

![](../../../images/d411c8d6054040c3.png)

**Node Functions**

Obtain the Variable Value of the specified Custom Variable from the Target Entity. If the variable does not exist, returns the default value for that type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

## **25. Get Current Execution Status**

![](../../../images/e303083d626b8cc8.png)

**Node Functions**

Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **26. Get Self Entity**

![](../../../images/381415c51c43ce98.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **27. Get Self Preset Status Value**

![](../../../images/7f05b7d3d2401487.png)

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **28. Query if Entity Has Unit Status**

![](../../../images/025d7eaf392278b3.png)

**Node Functions**

Check whether the target entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Has | Boolean |  |

# 

# II. Faction

## **1. Check Entity Faction**

![](../../../images/88dff507952b6513.png)

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/a573a52e555fc6ef.png)

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# III. Lists

## **1. Get Corresponding Value From List**

![](../../../images/929adba4a0aed4f3.png)

**Node Functions**

Return the value at the specified index in the Data List. Indexes start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![](../../../images/59ea02778cc2e130.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/9c6a6a4d67b973cf.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/7226eec44e74b38d.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. List Includes This Value**

![](../../../images/9e8901de19962535.png)

**Node Functions**

Check whether the specified list contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

## **6. Get Entity Type List**

![](../../../images/135f4a90f93c80d1.png)

**Node Functions**

Assemble the required entity types into a list.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 0 | Enumeration |  |
| Input Parameter | 1 | Enumeration |  |
| Input Parameter | 2 | Enumeration |  |
| Input Parameter | 3 | Enumeration |  |
| Input Parameter | 4 | Enumeration |  |
| Input Parameter | 5 | Enumeration |  |
| Input Parameter | 6 | Enumeration |  |
| Input Parameter | 7 | Enumeration |  |
| Input Parameter | 8 | Enumeration |  |
| Input Parameter | 9 | Enumeration |  |
| Output Parameter | List | Enumeration List |  |

# 

# IV. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![](../../../images/d069b4f263331b6a.png)

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

![](../../../images/c2f2de1e927a2dbb.png)

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Query Dictionary Length**

![](../../../images/1691ad2cf58fc877.png)

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![](../../../images/37ae8f011cc3337d.png)

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Query List of Values From Dictionary**

![](../../../images/aa2bb94a53dbf663.png)

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![](../../../images/6dba73a0dc46bcbf.png)

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# **V. Ray**

## **1. Get Ray Detection Result**

![](../../../images/d5806665f1547b69.png)

**Node Functions**

Get the ray detection result. Hits are evaluated from nearest to farthest, and the first target or hit position that meets the filter criteria is returned.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detect Initiator Entity | Enumeration |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Categories: Stage, Object, Player, Character, and Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Categories: Hurtbox, Environment, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Boolean |  |

## **2. Get Ray Filter Type List**

![](../../../images/cf4ca8fa09008ce1.png)

**Node Functions**

Assemble the required ray detection filter types into a list. Available filters include Hurtbox, Environment, and Object Self-Collision.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 0 | Enumeration |  |
| Input Parameter | 1 | Enumeration |  |
| Input Parameter | 2 | Enumeration |  |
| Input Parameter | 3 | Enumeration |  |
| Input Parameter | 4 | Enumeration |  |
| Input Parameter | 5 | Enumeration |  |
| Input Parameter | 6 | Enumeration |  |
| Input Parameter | 7 | Enumeration |  |
| Input Parameter | 8 | Enumeration |  |
| Input Parameter | 9 | Enumeration |  |
| Output Parameter | List | Enumeration List |  |
