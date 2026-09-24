---
title: Execution Nodes
path_id: mhit7ur1q4rq
updated_at: 2026-08-08 23:34:49
category: Node Introduction/Client Nodes/Character Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhit7ur1q4rq
---

# I. Character Skills

## **1. Traverse Entity List**

![](../../../images/c028ae0872e6c1a6.png)

**Node Functions**

Iterates through each Entity in the input Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity List | Entity List |  |
| Output Parameter | Current Entity | Entity |  |

## **2. Play Timed Effects**

![](../../../images/c599d9ba7a0d1381.png)

**Node Functions**

Plays Timed Effects at the specified World Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Special Effects Asset Configuration ID | Config ID |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | Play Default Sound Effects? | Boolean |  |

## **3. Fixed-Point Projectile Launch**

![](../../../images/10659251bd44b9e8.png)

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

![](../../../images/69d56411b2087318.png)

**Node Functions**

Moves from the current Location to the Target Location

Supports configuring movement duration and speed; if both are small, the movement may not reach the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Displacement Duration | Floating Point Numbers |  |
| Input Parameter | Displacement Attenuation Duration | Floating Point Numbers |  |
| Input Parameter | Displacement Speed | Floating Point Numbers |  |
| Input Parameter | Displacement Target Location | 3D Vector |  |
| Input Parameter | Terminate Displacement on Collision | Boolean |  |

## **5. Recover Character's HP**

![](../../../images/15047d525d5a0bc7.png)

**Node Functions**

Initiates a one-time HP restoration for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Recovery Amount | Floating Point Numbers |  |
| Input Parameter | Ignore Recovery Adjustment Effect | Boolean |  |
| Input Parameter | Aggro Multiplier for This Healing | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Healing | Integer |  |

## **6. Camera Orientation Detection Data**

![](../../../images/969da1ad3a30d543.png)

**Node Functions**

Casts a ray from the Camera to the emission Location and returns the Rotation and Location of valid Targets along the path

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Type | Enumeration |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Nearest Distance | Floating Point Numbers |  |
| Input Parameter | Furthest Distance | Floating Point Numbers |  |
| Output Parameter | Target Rotation | 3D Vector |  |
| Output Parameter | Target Location | 3D Vector |  |

## **7. Force Exit Aiming State**

![](../../../images/365cd18866ded118.png)

**Node Functions**

When the character is in the aiming state, they will be forced to exit the aiming state.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **8. Set Own Attack Target**

![](../../../images/16c9055839898c12.png)

**Node Functions**

Sets the Target Entity as its Attack Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Whether to Turn Immediately | Boolean |  |

## **9. Trigger Hitbox at Specific Location**

![](../../../images/59a184d891b3cada.png)

![](../../../images/8d450d097289c1ff.png)

![](../../../images/1c49e6ca101ebb8a.png)

![](../../../images/5745634f84c36963.png)

**Node Functions**

Initiates a Hitbox Attack at the specified Location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Scene Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **10. Add Unit Status**

![](../../../images/8242153f37eeaeb1.png)

**Node Functions**

Applies the Unit Status defined by the configuration ID to the Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Application Target | Entity |  |
| Input Parameter | Stacks | Integer |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **11. Notify Server Node Graph**

![](../../../images/0a448e6b9ce73cc0.png)

**Node Functions**

Notifies the Server Node Graph; supports up to three String parameters

At runtime, forwards logic to the Server Node Graph and triggers the [On Skill Node Call] Event on the Server Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | String 1 | String |  |
| Input Parameter | String 2 | String |  |
| Input Parameter | String 3 | String |  |

## **12. Player Turning**

![](../../../images/401ab553168e1dcd.png)

**Node Functions**

Turns the Player using the configured turning mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Turning Mode | Enumeration | Includes: Target then Input, Input Direction, Target Direction, Target then Camera, Camera Direction, Input then Target |

## **13. Player Turns to Face Set Direction**

![](../../../images/070b25aae8d946e0.png)

**Node Functions**

Turns the Player toward the direction specified by the 3D Vector configuration

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |

## **14. Set Attack Weight**

![](../../../images/c53978072bd43ad8.png)

**Node Functions**

You can set the weight of the current attack target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Current Attack Target Weight | Floating Point Numbers |  |
| Input Parameter | Forcibly Select a Target Once | Boolean |  |

## **15. Remove Unit Status**

![](../../../images/2f001de83a192505.png)

**Node Functions**

Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Removal Target | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **16. Remove Specified Character Disruptor Device**

![](../../../images/3a2af195074caf71.png)

**Node Functions**

Removes the specified type of Character Disruptor Device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Disruptor Device Type | Enumeration | Includes: Force Field Device, Ejector, and Traction Device |

## **17. Trigger Hitbox at Specific Location**

![](../../../images/360f02de68d3ab57.png)

![](../../../images/0bfb654a16fe8691.png)

![](../../../images/76137054a5cb4110.png)

![](../../../images/ab62faffa6429497.png)

**Node Functions**

Initiates a Hitbox Attack at the specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Scene Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |
| Input Parameter | Hit Vertical Impulse | String List |  |

## **18. Reset Skill Target**

![](../../../images/0c37f681cc5efc0d.png)

**Node Functions**

Resets the Skill Target and reruns the Skill selection logic to choose a new Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **19. Trigger Rectangular Hitbox at Specific Location**

![](../../../images/688c6b8f08d1331c.png)

![](../../../images/e34737b3a099c35d.png)

**Node Functions**

Initiate a rectangular hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Integer |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **20. Trigger Spherical Hitbox at Specific Location**

![](../../../images/80038099c4b44d18.png)

![](../../../images/40379240b3f86565.png)

**Node Functions**

Initiate a spherical hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **21. Trigger Sector Hitbox at Specific Location**

![](../../../images/6a79be9da9349b62.png)

![](../../../images/1eb5c8641f896881.png)

**Node Functions**

Initiate a sector hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **22. Trigger Rectangular Hitbox at Specified Attachment Point**

![](../../../images/c89d109995cde89b.png)

![](../../../images/e2ab1193f1f5b8e7.png)

**Node Functions**

Initiate a rectangular hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **23. Trigger Spherical Hitbox at Specified Attachment Point**

![](../../../images/16de9f178b92057e.png)

![](../../../images/03a74556d6b1b3f6.png)

**Node Functions**

Initiate a spherical hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **24. Trigger Sector Hitbox at Specified Attachment Point**

![](../../../images/b47384f87a4c825d.png)

![](../../../images/020dc0e0c57391b8.png)

![](../../../images/0324312a6fbfef2b.png)

**Node Functions**

Initiate a sector hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **25. Interrupt Current Skil**l

![](../../../images/84730ed6569e588f.png)

**Node Functions**

Interrupts the skill currently being cast by the character

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **26. Set Skill Variable**

![](../../../images/37112174e0810d35.png)

**Node Functions**

Sets the value of the specified skill variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | The modified value |

## **27. Increase Skill Variable Value**

![](../../../images/73e558e68cd5be6b.png)

**Node Functions**

Increases the value of the specified skill variable. The increment can be a negative value.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | Modified Value = Original Value + Increase Value |

## **28. Character Blink**

![](../../../images/ad182a7467c7a12b.png)

**Node Functions**

Makes the character blink to the target position, with the direction they are facing post-blink adjustable. The maximum blink distance is 200 meters.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Target Orientation | 3D Vector |  |

## **29. Add Key Behavior**

![](../../../images/9e3468ec7958350b.png)

**Node Functions**

Adds a key behavior with the corresponding ID to the Key Behavior Log Panel, and records the current time along with it. The maximum number of key behaviors that can be recorded is 20.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key Behavior ID | Integer |  |

## **30. Clear Key Behavior Log Panel**

![](../../../images/799c982ae735c0f4.png)

**Node Functions**

Clears all recorded key behaviors from the Key Behavior Log Panel.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **31. Cast Skill From Specified Slot**

![](../../../images/549ab5e41fba1c8d.png)

**Node Functions**

Makes the character cast the skill corresponding to the specified Skill Instance ID.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Input Parameter | Check Key Availability | Boolean | Yes: The skill will only be cast when the current button is usable.  No: The skill will be cast regardless of whether the current button is usable. |

## **32. Cast Skill From Specified Slot**

![](../../../images/e2ff7c730f1003c3.png)

**Node Functions**

Makes the character cast the skill that is currently in the foreground for the corresponding skill slot.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Check Key Availability | Boolean | Yes: The skill will only be cast when the current button is usable.  No: The skill will be cast regardless of whether the current button is usable. |

# II. General

## **1. Set Local Variable**

![](../../../images/69f1e123ff13e1b6.png)

**Node Functions**

Sets the value of a local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Input Parameter | Variable Value | Generic |  |

## **2. Break Loop**

![](../../../images/7cd97f8bafe2f93e.png)

**Node Functions**

Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **3. Finite Loop**

![](../../../images/9558c9cf55689803.png)

**Node Functions**

From the [Loop Start Value] to the [Loop End Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loop Start Value | Integer |  |
| Input Parameter | Loop Termination Value | Integer |  |
| Output Parameter | Current Loop Value | Integer |  |

# III. Custom Aggro

## **1. Set the Aggro Value of the Specified Entity Proportionally**

![](../../../images/518117109f6a8389.png)

**Node Functions**

Available only in Custom Aggro Mode

Set the aggro value of the target entity for the specified aggro owner proportionally.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value Ratio | Floating Point Numbers |  |

## **2. Transfer the Aggro Value of the Specified Entity Proportionally**

![](../../../images/5bde22563c34bb12.png)

**Node Functions**

Available only in Custom Aggro Mode

Transfers a percentage of Aggro on the Aggro Owner from the Source Entity to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Transfer Target Entity | Entity |  |
| Input Parameter | Transfer Source Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Transfer Ratio | Floating Point Numbers |  |

## **3. Taunt Target**

![](../../../images/52b1ca2f772edd3f.png)

**Node Functions**

Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Taunter Entity | Entity |  |
| Input Parameter | Target Entity | Entity |  |

## **4. Remove Target Entity From Aggro List**

![](../../../images/6ab3132994ae4b6b.png)

**Node Functions**

Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |

## **5. Clear the Aggro List of the Specified Entity**

![](../../../images/000d706f58954885.png)

**Node Functions**

Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **6. Set the Aggro Value of the Specified Entity**

![](../../../images/6b61cac91281ef38.png)

**Node Functions**

Available only in Custom Aggro Mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value | Integer |  |

## **7. Increase the Aggro Value of the Specified Entity**

![](../../../images/6310fafebae2ebb6.png)

**Node Functions**

Available only in Custom Aggro Mode

Modify the aggro value of the specified entity for the aggro owner entity; the increase value can be negative.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Increase Value | Integer | Changed value = original value + increase value |

# IV. Signal

## **1.** **Send Signal to Server Node Graph**

![](../../../images/1e76fb4bb49a0efb.png)

**Node Functions**

Within the skill node graph, signals can be sent to the server node graph, and all server node graphs can listen for this signal.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Signal Name | String |  |

# V. **Pre-Aim**

## **1. Complete Current Pre-Aim**

![](../../../images/bc98a1a7f22e59f9.png)

**Node Functions**

Allows players to complete the current aiming phase early.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |
