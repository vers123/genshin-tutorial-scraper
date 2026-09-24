---
title: Execution Nodes
path_id: mh4v79raps66
updated_at: 2026-05-14 10:51:29
category: Node Introduction/Client Nodes/Creation Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh4v79raps66
---

# I. Skills

## **1. Traverse Entity List**

![](../../../images/6f185895edaeb076.png)

**Node Functions**

Iterates through each Entity in the input Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity List | Entity List |  |
| Output Parameter | Current Entity | Entity |  |

## **2. Play Timed Effects**

![](../../../images/5025ca8fd4f9fd04.png)

**Node Functions**

Plays Timed Effects at the specified World Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Special Effects Asset Configuration ID | Configuration ID |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | Play Default Sound Effect | Boolean |  |

## **3. Fixed-Point Projectile Launch**

![](../../../images/f2eb9f8268f0996d.png)

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

## **4. Complex Creation Directed Movement**

![](../../../images/b8a0b686e6874c5b.png)

**Node Functions**

Moves from the current Location to the Target Location

You can configure the Maximum Distance. If this value is too small, the object may not be able to move to the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Displacement Duration | Floating Point Numbers |  |
| Input Parameter | Max Distance | Floating Point Numbers |  |
| Input Parameter | Ignore Collision | Boolean |  |

## **5. Complex Creation Teleport**

![](../../../images/00356d41b67a557c.png)

**Node Functions**

Teleport from your current location to the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Target Rotation | 3D Vector |  |

## **6. Recover Creation's HP**

![](../../../images/d0bd004165032032.png)

**Node Functions**

Initiates a one-time HP restoration for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Recovery Amount | Floating Point Numbers |  |
| Input Parameter | Ignore Recovery Adjustment Effect | Boolean |  |

## 7. Set the Global CD of the Creation

![](../../../images/6938ed309353cc84.png)

**Node Functions**

Permanently changes the Creation's Global CD for this stage run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Cooldown | Floating Point Numbers |  |

## **8. Set the Current CD of the Creation Skill**

![](../../../images/2e0418a9037812cd.png)

**Node Functions**

Adjusts only the CD for this Creation Skill for this use. This is a one-time change and will not be saved

Note: When this Node runs, if the Target Skill is currently casting and is configured to trigger its CD when the Skill ends, the CD will be reset to the Skill's configured CD at End. Even if this Node successfully sets the Current CD, it will be overwritten by the CD triggered at Skill End.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |
| Input Parameter | Current Cooldown | Floating Point Numbers |  |

## **9. Set the CD of the Creation Skill**

![](../../../images/6f2c75a5bdee1bd0.png)

**Node Functions**

Permanently changes the Creation's Skill CD for this stage run

Note:

1.When this Node runs, it does not change the Target Skill's current remaining CD. It only affects the CD the next time the Skill enters CD2.If the Target Skill is being cast and is configured to Trigger CD on Skill End, then when the Skill ends, the CD that starts will use the time set by this Node3.Instant Skills have no duration, so their CD always starts counting when the Skill begins

For example:

4.Skill A has 5 seconds of CD remaining. At this moment, the Node's CD is set to 10 seconds. The Creation can use this Skill after 5 seconds, and after using it, this unit enters a 10-second CD5.Skill A is configured to trigger its CD when the Skill ends, with a 5-second CD. If a Creation is casting Skill A and this Node changes the CD to 10 seconds, the Skill will enter a 10-second CD immediately after it ends6.Skill A is an Instant Skill with a 5-second cooldown. If a Creation uses this Node in the Node Graph Logic for casting Skill A and changes it to 10 seconds, then, as in Example 1, Skill A will be available after 5 seconds. After you use it, it enters a 10-second cooldown

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |
| Input Parameter | Cooldown (CD) | Floating Point Numbers |  |
| Input Parameter | CD Variation Range | Floating Point Numbers |  |

## 10. Set the Current Time of the Creation Cooldown Group

![](../../../images/cb52836c4e1a6b4d.png)

**Node Functions**

Adjusts only this Creation's Skill Group CD for this session; changes are not saved

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | CD Group ID | Integer |  |
| Input Parameter | Current Cooldown | Floating Point Numbers |  |

## 11. Set the Time of the Creation Cooldown Group

![](../../../images/78334a92d2a463a7.png)

**Node Functions**

Permanently changes the Creation's Skill Group CD for this stage run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | CD Group ID | Integer |  |
| Input Parameter | Cooldown (CD) | Floating Point Numbers |  |
| Input Parameter | CD Variation Range | Floating Point Numbers |  |

## **12. Trigger Hitbox at Specific Location**

![](../../../images/a0747799cf7c6855.png)

![](../../../images/d64217a39400dcb1.png)

![](../../../images/f3000aeacce1de82.png)

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
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Offset | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **13. Trigger Rectangular Hitbox at Specific Location**

![](../../../images/fdb5f98cd384e2c4.png)

![](../../../images/35307d574ab0b52f.png)

**Node Functions**

Initiates a Rectangular HitBox Attack at a specified location in the World Coordinate System, with configurable attack parameters

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
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **14. Trigger Spherical Hitbox at Specific Location**

![](../../../images/fef0bdca991b7102.png)

![](../../../images/1cf4a4de20b4f0c9.png)

**Node Functions**

Initiates a Sphere Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

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

## **15. Trigger Sector Hitbox at Specific Location**

![](../../../images/49a425ffe890e2ff.png)

![](../../../images/b00386acb2f16a26.png)

**Node Functions**

Initiates a Sector Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

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

## **16. Add Unit Status**

![](../../../images/1586ff3a076cc2b6.png)

**Node Functions**

Applies the Unit Status defined by the configuration ID to the Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Application Target | Entity |  |
| Input Parameter | Stacks | Integer |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **17. Remove Unit Status**

![](../../../images/3bdba1008664d681.png)

**Node Functions**

Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Removal Target | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **18. Remove Specified Character Disruptor Device**

![](../../../images/a512d4b9698bfb02.png)

**Node Functions**

Removes the specified type of Character Disruptor Device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Disruptor Device Type | Enumeration | Includes: Force Field Device, Ejector, and Traction Device |

## **19. Resets the Creation's Skill CD**

![](../../../images/e480986aaf792f35.png)

**Node Functions**

Resets the Skill CD to 0. If the conditions are met, the Skill can be cast immediately

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |

## **20. Creation Turns to Face Set Direction**

![](../../../images/62039f443c21ae94.png)

**Node Functions**

Rotates the Creation to face the orientation of the specified 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |

## **21. Trigger Hitbox at Specified Attachment Point**

![](../../../images/60e69f3f56b19673.png)

![](../../../images/317c754f47f17b68.png)

![](../../../images/1c126795b4a78cc3.png)

**Node Functions**

Initiates a Hitbox Attack at a specified Attachment Point, with configurable attack parameters

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
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **22. Trigger Rectangular Hitbox at Specified Attachment Point**

![](../../../images/4d2bda17eb0fa719.png)

![](../../../images/3ed4f045e9e2c1ed.png)

**Node Functions**

Initiates a Rectangular HitBox Attack from the Specified Attachment Point, with configurable attack parameters

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

![](../../../images/916be43380e06abe.png)

![](../../../images/19ca4e7b469ef5fe.png)

**Node Functions**

Initiates a Sphere HitBox Attack from the Specified Attachment Point, with configurable attack parameters

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

![](../../../images/cbb40467a977b871.png)

![](../../../images/945fc37a8f4a17ec.png)

**Node Functions**

Initiates a Sector HitBox Attack from the Specified Attachment Point, with configurable attack parameters

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

## **25. Set Skill Variable**

![](../../../images/98637aff2b232c27.png)

**Node Functions**

Assigns value to specified Skill Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | New Value |

## **26. Increase Skill Variable Value**

![](../../../images/bafc5f7764e9ab50.png)

**Node Functions**

Adds the given value to the specified Skill Variable. Value can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Increase Value | Floating Point Numbers | New Value = Original Value + Increase Value |

# II. General

## **1. Set Local Variable**

![](../../../images/b40e1bb7a8c00a73.png)

**Node Functions**

Sets the value of a Local Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Input Parameter | Variable Value | Generic |  |

## **2. Break Loop**

![](../../../images/d4e40088115a5ae0.png)

**Node Functions**

Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **3. Notify Server Node Graph**

![](../../../images/d74bdf5c841a16ae.png)

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

## **4. Finite Loop**

![](../../../images/b63eea158daad443.png)

**Node Functions**

From the [Loop Start Value] to the [Loop Termination Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loop Start Value | Integer |  |
| Input Parameter | Loop Termination Value | Integer |  |
| Output Parameter | Current Loop Value | Integer |  |

# III. Signals

## **1. Send Signal to Server Node Graph**

![](../../../images/2564a645cddb71d0.png)

**Node Functions**

In the Skill Node Graph, you can send a signal to the Server Node Graph, and all Server Node Graphs can monitor that signal

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Signal Name | String |  |

# IV. Custom Aggro

## **1. Set the Aggro Value of the Specified Entity Proportionally**

![](../../../images/a9767564802da2bd.png)

**Node Functions**

Available only in Custom Aggro Mode

Set the Target Entity's Aggro Value toward the specified Aggro Owner proportionally

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value Ratio | Floating Point Numbers |  |

## **2. Transfer the Aggro Value of the Specified Entity Proportionally**

![](../../../images/f28a174bacea86dc.png)

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

![](../../../images/8942b901bffa24e0.png)

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

![](../../../images/79fa35271db1df49.png)

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

![](../../../images/ae7400326191b87e.png)

**Node Functions**

Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **6. Set the Aggro Value of the Specified Entity**

![](../../../images/1319e08578bc4235.png)

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

![](../../../images/e4616a5787d2e590.png)

**Node Functions**

Available only in Custom Aggro Mode

Edit the Aggro Value of the Specified Entity on the Aggro Owner, and the added value can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Increase Value | Integer | Edited Value = Original Value + Increase Value |

# 

##
