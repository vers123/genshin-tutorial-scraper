---
title: Query Nodes
path_id: mh56b3rjj7ce
updated_at: 2026-05-07 19:14:32
category: Node Introduction/Client Nodes/Creation Status Decision Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh56b3rjj7ce
---

# I. General

## **1. Check Target Position Pathfinding Availability**

![](../../../images/f72fab6fd04d3883.png)

**Node Functions**

Check whether a Creation can reach the current Target Point using normal pathfinding

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is Pathfinding Achievable? | Boolean |  |

## **2. Check the Coordinates When Entering Battle**

![](../../../images/d75ca2560e99ecd8.png)

**Node Functions**

Query the Coordinate Points when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Entering Battle Position | 3D Vector |  |
| Output Parameter | Entering Battle Rotation | 3D Vector |  |

## **3. Check If Entity Is on the Field**

![](../../../images/75f244a370d9a0e4.png)

**Node Functions**

Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | On the Field | Boolean |  |

## **4. Check the Vertical Angle From Self to Target**

![](../../../images/18ef8aa7acb88668.png)

**Node Functions**

Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Angle | Floating Point Numbers |  |

## **5. Check the Vertical Distance From Self to Target**

![](../../../images/ea7dbb28a2a107e6.png)

**Node Functions**

Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Distance | Floating Point Numbers |  |

## **6. Check the Distance From Self to Target**

![](../../../images/f5b512b9d565f976.png)

**Node Functions**

Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Distance | Floating Point Numbers |  |

## **7. Check the Horizontal Angle From Self to Target**

![](../../../images/eb877f6d14faa3f8.png)

**Node Functions**

Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Angle | Floating Point Numbers |  |

## **8. Check the Horizontal Distance From Self to Target**

![](../../../images/d155b9d0fb8bc9a9.png)

**Node Functions**

Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Distance | Floating Point Numbers |  |

## **9. Check Whether Self Is in Battle**

![](../../../images/defe558e77f77e5e.png)

**Node Functions**

Check whether the Creation is currently in battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Whether in Battle | Boolean |  |

## **10. Check if Self Is in the Territory**

![](../../../images/6165e2d2e64588fb.png)

**Node Functions**

Check whether this Creation's current location is within the Territory

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is in the Territory | Boolean |  |

## **11. Check Whether Self Is Using a Skill**

![](../../../images/d23928ad70c75b78.png)

**Node Functions**

Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is the Unit Using a Skill? | Boolean |  |
| Output Parameter | Skill ID | Integer |  |

## **12. Get Spawn Point Location Information**

![](../../../images/205ae5bbc6bbf2f0.png)

**Node Functions**

Obtain the Creation's own Spawn Point information

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Spawn Point Coordinates | 3D Vector |  |
| Output Parameter | Spawn Point Rotation | 3D Vector |  |

1.

## Get Stage Entity

![](../../../images/772d1214b2f329be.png)

**Node Functions**

Obtain Stage Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Stage Entity | Entity |  |

## **14. Get Target Level**

![](../../../images/f56e9498b8308c4d.png)

**Node Functions**

Obtain the Target Entity's current level

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Current Level | Integer |  |

## **15. Get Target ATK**

![](../../../images/cb2dee06f001a981.png)

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

![](../../../images/3853be3b7e6cde2c.png)

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

![](../../../images/241c6073378da8c2.png)

**Node Functions**

Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **18. Get Previous Frame Execution Tactic**

![](../../../images/32d758a52af83d4f.png)

**Node Functions**

Obtain the Tactic executed by Creations in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Tactic Type | Enumeration |  |
| Output Parameter | Tactical Context | String |  |

## **19. Get Previous Frame Execution Status**

![](../../../images/399d931ba1174624.png)

**Node Functions**

Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **20. Get Entity's Type**

![](../../../images/86550aa92659a3af.png)

**Node Functions**

Obtain the Target Entity's Type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Entity Type | Enumeration |  |

## **21. Get Entity Location**

![](../../../images/f26f5f50d0fbf22d.png)

**Node Functions**

Obtain the Target Entity's Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Location | 3D Vector |  |

## **22. Get Entity Rotation**

![](../../../images/fe286f34b9f4104c.png)

**Node Functions**

Obtain the Target Entity's Rotation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Rotatation | 3D Vector |  |

## **23. Get Object Preset Status**

![](../../../images/aef3954c0fa35c12.png)

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

![](../../../images/03d6240d7c081634.png)

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

![](../../../images/901870cc2fbb3ce5.png)

**Node Functions**

Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **26. Get Self Entity**

![](../../../images/38ff64c2b9557d5f.png)

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **27. Get Self Preset Status Value**

![](../../../images/85b1f92c6db55f6d.png)

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# II. Faction

## **1. Check Entity Faction**

![](../../../images/b5f6429ac2c407c1.png)

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![](../../../images/2b94e8138eabaeee.png)

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

![](../../../images/bbf29d13ec8898e8.png)

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

![](../../../images/c4506cc3396ab21f.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](../../../images/aae46df041149ad9.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](../../../images/be8bac27eeef08d6.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. List Includes This Value**

![](../../../images/fc2cf3c5cd21d588.png)

**Node Functions**

Check whether the specified list contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# IV. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![](../../../images/81ef501df18727f8.png)

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

![](../../../images/45f517704ef6ee44.png)

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

![](../../../images/d8389b79ba59e0c7.png)

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![](../../../images/810961f3516d5009.png)

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Query List of Values From Dictionary**

![](../../../images/07993800b77cd366.png)

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![](../../../images/5caa698450629a0b.png)

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |
