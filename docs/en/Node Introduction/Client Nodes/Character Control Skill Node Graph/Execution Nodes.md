---
title: Execution Nodes
path_id: mhmsr1i3dfxw
updated_at: 2026-09-18 13:52:28
category: Node Introduction/Client Nodes/Character Control Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhmsr1i3dfxw
---

# **I. Character Skills**

## **1. Traverse Entity List**

![](../../../images/be4f0c05f883c4f7.png)

**Node Functions**

Iterates through each Entity in the input Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity List | Entity List |  |
| Output Parameter | Current Entity | Entity |  |

## **2. Play Timed Effects**

![](../../../images/d96455b5c2493e89.png)

**Node Functions**

Plays Timed Effects at the specified world Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Special Effects Asset Configuration ID | Config ID |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Number |  |
| Input Parameter | Play Default Sound Effect | Boolean |  |

## **3. Fixed-Point Projectile Launch**

![](../../../images/524f842e22a5745d.png)

**Node Functions**

Spawns a Local Projectile at the specified Location in the World Coordinate System

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Projectile's Prefab ID | Prefab ID |  |
| Input Parameter | Create Location | 3D Vector |  |
| Input Parameter | Create Rotation | 3D Vector |  |
| Input Parameter | Track Target | Entity |  |
| Input Parameter | Projectile Faction | Faction |  |

## **4. Fixed-Point Displacement**

![](../../../images/f05ef4d4e8df546a.png)

**Node Functions**

Moves from the current Location to the Target Location

Supports configuring movement duration and speed; if both are set too low, the movement may not reach the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Displacement Duration | Floating Point Number |  |
| Input Parameter | Displacement Attenuation Duration | Floating Point Number |  |
| Input Parameter | Displacement Speed | Floating Point Number |  |
| Input Parameter | Displacement Target Location | 3D Vector |  |
| Input Parameter | Terminate Displacement on Collision | Boolean |  |

## **5. Camera Orientation Detection Data**

![](../../../images/ca2a0f5d2bb326f2.png)

**Node Functions**

Casts a ray from the Camera to the launch location and returns the Rotation and Location of valid Targets along the path

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Type | Enumeration |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Nearest Distance | Floating Point Number |  |
| Input Parameter | Furthest Distance | Floating Point Number |  |
| Output Parameter | Target Rotation | 3D Vector |  |
| Output Parameter | Target Location | 3D Vector |  |

## **6. Set Own Attack Target**

![](../../../images/fd30bbaaf0652f62.png)

**Node Functions**

Sets the Target Entity as its Attack Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Turn Immediately | Boolean |  |

## **7. Add Unit Status**

![](../../../images/9d3d7a62a35dee5d.png)

**Node Functions**

Applies the Unit Status corresponding to the configuration ID to the Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Application Target | Entity |  |
| Input Parameter | Stacks | Integer |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **8. Trigger Hitbox at Specific Location**

![](../../../images/45a39b11f4ce5c07.png)

![](../../../images/dadac966a047cf01.png)

![](../../../images/87a2207b57d5c53e.png)

**Node Functions**

Initiates a Hitbox Attack at the specified Location in the World Coordinate System, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Intput Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Intput Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Intput Parameter | Radius of Sphere Hitbox | Floating Point Number |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impluse | Floating Point Number |  |

## **9. Notify Server Node Graph**

![](../../../images/f54a42ffabeb50f4.png)

**Node Functions**

Notifies the Server Node Graph, supporting up to three String parameters

When executed, this node passes the logic to the server node graph and triggers the "When Skill Node Is Called" event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | String 1 | String |  |
| Input Parameter | String 2 | String |  |
| Input Parameter | String 3 | String |  |

## **10. Player Turning**

![](../../../images/4d59b4ccd704ce03.png)

**Node Functions**

Allows the player to turn using the configured turning mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Turning Mode | Enumeration | Includes: Target First Input Next, Input Orientation, Target Orientation, Target First, Lens Second, Lens Orientation, Input First Target Next |

## **11. Set Attack Weight**

![](../../../images/2c392e14d79bad11.png)

**Node Functions**

Allows you to set the current attack target's weight

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Current Attack Target Weight | Floating Point Number |  |
| Input Parameter | Forcibly Select a Target Once | Boolean |  |

## **12. Remove Unit Status**

![](../../../images/a679198dbfe08e6e.png)

**Node Functions**

Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Remove Target | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **13. Remove Specified Character Disruptor Device**

![](../../../images/350fc8a827cdaa6d.png)

**Node Functions**

Removes the specified type of Character Disruptor Device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Disturbance Device Type | Enumeration | Includes: Force Field Device, Ejector, and Traction Device |

## **14. Trigger Hitbox at Specified Attachment Point**

![](../../../images/6639b834399e6f28.png)

![](../../../images/c707692624d12daa.png)

![](../../../images/3fa833d4dba00239.png)

**Node Functions**

Initiates a Hitbox Attack at a specified Attachment Point, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Number |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **15. Recover Character's HP**

![](../../../images/fca857dc44755375.png)

**Node Functions**

Initiates a one-time HP restoration for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Recovery Amount | Floating Point Number |  |
| Input Parameter | Ignore Recovery Adjustment Effect | Boolean |  |
| Input Parameter | Aggro Multiplier for This Healing | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Healing | Integer |  |

## **16. Player Turns to Face Set Direction**

![](../../../images/a69ba69926a7b679.png)

**Node Functions**

Allows the player to turn toward the direction specified by the configured 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |

## **17. Reset Skill Target**

![](../../../images/990bd27cd5c4e877.png)

**Node Functions**

Resets the Skill Target and reruns the skill selection logic to choose a new Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **18. Force Exit Aiming State**

![](../../../images/4cb5327d39cc94c4.png)

**Node Functions**

If the character is in Aiming State, forces them to exit the Aiming State

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **19. Trigger Spherical Hitbox at Specific Location**

![](../../../images/960fe5a256697922.png)

![](../../../images/8ebe47821c375612.png)

**Node Functions**

Initiates a Spherical Hitbox Attack at a specified location in the World Coordinate System, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Number |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **20. Trigger Rectangular Hitbox at Specific Location**

![](../../../images/9c50f49392302219.png)

![](../../../images/852e36846ee5982e.png)

**Node Functions**

Initiates a Rectangular Hitbox Attack at a specified location in the World Coordinate System, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Direction | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **21. Trigger Sector Hitbox at Specific Location**

![](../../../images/5cc0d7837ae595fb.png)

![](../../../images/56bf25fd84667bca.png)

**Node Functions**

Initiates a Sector Hitbox Attack at a specified location in the World Coordinate System, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **22. Trigger Spherical Hitbox at Specified Attachment Point**

![](../../../images/242656b8e4be1d00.png)

![](../../../images/729ddbc7a980aabe.png)

**Node Functions**

Initiates a Spherical Hitbox Attack at a specified attachment point, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Number |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **23. Trigger Rectangular Hitbox at Specified Attachment Point**

![](../../../images/b930edd51e5b1a1c.png)

![](../../../images/5f74a814b280292f.png)

**Node Functions**

Initiates a Rectangular Hitbox Attack at a specified attachment point, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |

## **24. Trigger Sector Hitbox at Specified Attachment Point**

![](../../../images/c8559c5dc6ebda41.png)

![](../../../images/af7b5d8142607d5e.png)

**Node Functions**

Initiates a Sector Hitbox Attack at a specified attachment point, supporting configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Number |  |
| Input Parameter | Damage Increment | Floating Point Number |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Number |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Number |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Number |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Number |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Number |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Number |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Number |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Number |  |

## **25. Interrupt Current Skill**

![](../../../images/0a30e9e0eb1e4478.png)

**Node Functions**

Interrupts the Skill currently being cast by the character

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **26. Set Skill Variable**

![](../../../images/d6d7cbf3725d3426.png)

**Node Functions**

Sets a value for the specified Skill Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Intput Parameter | Set Value | Floating Point Number | New Value |

## **27. Increase Skill Variable Value**

![](../../../images/02548644db601292.png)

**Node Functions**

Adds a value to the specified Skill Variable. The increment can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Intput Parameter | Increment | Floating Point Number | New Value = Original Value + Increment |

## **28. Character Blink**

![](../../../images/c41c8ec6a072563e.png)

**Node Functions**

Makes the character blink toward the Target Location. You can adjust the Orientation after the blink. Max Distance is 200 m

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Target Orientation | 3D Vector |  |

## **29. Add Key Behavior**

![](../../../images/eb57a64adb70e96d.png)

**Node Functions**

Adds a Key Behavior with the corresponding ID to the Key Behavior Log Panel and records the current Time with it. Up to 20 Key Behaviors can be recorded

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Key Behavior ID | Integer |  |

## **30. Clear Key Behavior Log Panel**

![](../../../images/e950d22117ea25d9.png)

**Node Functions**

Removes every recorded Key Behavior from the Key Behavior Log Panel

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **31. Cast Specified Skill Instance**

![](../../../images/8f0694c37cce951c.png)

**Node Functions**

Makes the Character cast the Skill tied to the specified Skill Instance ID

The button is available only when the Skill is bound to a button and currently active on field

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Intput Parameter | Check Key Availability | Boolean | Yes: Cast the Skill only when the current button is available  No: Cast the Skill regardless of current button availability |

## **32. Cast Skill From Specified Slot**

![](../../../images/64f76ea563883e61.png)

**Node Functions**

Makes the Character cast the on-field Skill in the corresponding Skill Slot

The button is available only when the Skill is bound to a button and currently active on field

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Check Key Availability | Boolean | Yes: Cast the Skill only when the current button is available  No: Cast the Skill regardless of current button availability |

# **II. General**

## **1. Finite Loop**

![](../../../images/748f849ce20fe6ab.png)

**Node Functions**

Starting from [Loop Start Value] and ending at [Loop Termination Value], it iterates through the range of values, incrementing by 1 each time. Each iteration executes the node logic connected to [Loop Body]. Upon completing the full traversal, it triggers the node logic connected to [Loop Complete].

Use [Break Loop] to terminate the iteration early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loop Start Value | Integer |  |
| Input Parameter | Loop Termination Value | Integer |  |
| Output Parameter | Current Loop Value | Integer |  |

## **2. Break Loop**

![](../../../images/1a935fba808ef01f.png)

**Node Functions**

Break out of a Finite Loop. The output pin must be connected to the [Break Loop] input parameter of the [Finite Loop] Node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **3. Set Local Variable**

![](../../../images/2ffb4042028278a2.png)

**Node Functions**

Sets the value of a Local Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Input Parameter | Variable Value | Generic |  |

# **III. Custom Aggro**

## **1. Set the Aggro Value of the Specified Entity**

![](../../../images/50ff762fb3af3fdf.png)

**Node Functions**

Available only in Custom Aggro mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value | Integer |  |

## **2. Increase the Aggro Value of the Specified Entity**

![](../../../images/ff050655f03c73bd.png)

**Node Functions**

Available only in Custom Aggro Mode

Edit the Aggro Value of the specified Entity on the Aggro Owner Entity; the Increase Value can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Increase Value | Integer | Edited Value = Original Value + Increment |

## **3. Set the Aggro Value of the Specified Entity Proportionally**

![](../../../images/8e58072d8247fcd8.png)

**Node Functions**

Available only in Custom Aggro Mode

Set the Target Entity's Aggro Value toward the specified Aggro Owner Entity proportionally

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value Ratio | Floating Point Number |  |

## **4. Transfer the Aggro Value of the Specified Entity Proportionally**

![](../../../images/fe0c48547f4ae857.png)

**Node Functions**

Available only in Custom Aggro Mode

Transfers a percentage of Aggro Value targeting the Transfer Source Entity from the Aggro Owner Entity to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Transfer Target Entity | Entity |  |
| Input Parameter | Transfer Source Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Transfer Ratio | Floating Point Number |  |

## **5. Clear the Aggro List of the Specified Entity**

![](../../../images/2906e8122bf65e87.png)

**Node Functions**

Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **6. Remove Target Entity From Aggro List**

![](../../../images/3c3c8c8f9a731cfd.png)

**Node Functions**

Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |

## **7. Taunt Target**

![](../../../images/ffea0be347a526ce.png)

**Node Functions**

Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Taunter Entity | Entity |  |
| Input Parameter | Target Entity | Entity |  |

# **IV. Signals**

## **1. Send Signal to Server Node Graph**

![](../../../images/1a40e0c0c6680efb.png)

**Node Functions**

In the Skill Node Graph, you can send a signal to the Server Node Graph, and all Server Node Graphs can monitor that signal

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Signal Name | String |  |

# **V. Pre-Aim**

## **1. Complete Current Pre-Aim**

![](../../../images/ba3ffd6522935392.png)

**Node Functions**

Allows the player to complete the Current Pre-Aim early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

# **VI. Motion Device**

## **1. Add Temporary Movement Parameters**

![](../../../images/1926b14cdc294578.png)

**Node Functions**

Adds Temporary Movement Parameters. These values take effect on the next frame, so their changes cannot be read in the current Execution Flow by querying the node.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Control Motion Device | Entity |  |
| Intput Parameter | Forward Acceleration | Floating Point Number |  |
| Intput Parameter | Reverse Acceleration | Floating Point Number |  |
| Intput Parameter | Turn Speed | Floating Point Number |  |
| Intput Parameter | Base Resistance Deceleration | Floating Point Number |  |
| Intput Parameter | Resistance Coefficient | Floating Point Number |  |
| Intput Parameter | Max Forward Speed | Floating Point Number |  |
| Intput Parameter | Max Reverse Speed | Floating Point Number |  |

## **2. Add Acceleration**

![](../../../images/3ac01c580d15101a.png)

**Node Functions**

Adds Temporary Speed. If the Vehicle is grounded, Speed is added only along the ground plane (its planar component)

The added Speed persists even after the Duration expires

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Control Motion Device | Entity |  |
| Intput Parameter | Speed | Floating Point Number |  |
| Input Parameter | Orientation | 3D Vector |  |
| Intput Parameter | Duration | Floating Point Number |  |

## **3. Add Temporary Acceleration**

![](../../../images/f1d3fb8264a5af95.png)

**Node Functions**

Adds temporary Acceleration. If the Vehicle is grounded, Acceleration is added only along the ground plane (its planar component)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Control Motion Device | Entity |  |
| Intput Parameter | Acceleration | Floating Point Number |  |
| Input Parameter | Orientation | 3D Vector |  |
| Input Parameter | Duration | Floating Point Number |  |

## **4. Set Control Motion Device to Not Grounded**

![](../../../images/885aa10c15ffcdca.png)

**Node Functions**

While grounded, the Control Motion Device continuously detects and snaps to the ground surface. To achieve airborne movement (such as jumping) by adding Speed, use this node to temporarily break out of the grounded state.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Control Motion Device | Entity |  |
| Input Parameter | Duration | Floating Point Number |  |
