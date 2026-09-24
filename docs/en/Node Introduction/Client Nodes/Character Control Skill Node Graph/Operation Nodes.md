---
title: Operation Nodes
path_id: mhvrd29t9rjm
updated_at: 2026-08-07 11:56:42
category: Node Introduction/Client Nodes/Character Control Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhvrd29t9rjm
---

# **I. General**

## **1. Equal**

![](../../../images/026404f66367cd18.png)

**Node Functions**

Determines whether two inputs are equal

Some Parameter Types have special comparison rules:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **2. Data Type Conversion**

![](../../../images/cbee88cf136387bd.png)

**Node Functions**

For output, converts the input Parameter Type into another type. See [Basic Concepts](/ys/ugc/tutorial//detail/mhk23ora1wom) - [Conversion Rules Between Basic Data Types] for specific rules

In the Client Node, converting Floating Point Numbers to an Integer truncates the decimal part

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Conversion Result | Generic |  |

## **3. Enumeration Match**

![](../../../images/2bcf6f680381e611.png)

**Node Functions**

After confirming the Enumeration type, determines whether the two input values are equal

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Enumerate 1 | Generic |  |
| Input Parameter | Enumerate2 | Generic |  |
| Output Parameter | Result | Boolean | Output True if equal, False if not equal |

# **II. Math**

## **1. Addition**

![](../../../images/89e2e0bd816f8385.png)

**Node Functions**

Adds two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Subtraction**

![](../../../images/072ab332e3dd6e45.png)

**Node Functions**

Subtracts two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **3. Multiplication**

![](../../../images/4af80186e1664da6.png)

**Node Functions**

Performs multiplication, supporting Floating Point and Integer multiplication

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **4. Division**

![](../../../images/074a14fc281884ec.png)

**Node Functions**

Performs division, supporting Floating Point and Integer division. Integer division returns only the integer quotient

The divisor should not be 0, otherwise it may return an illegal value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **5. Absolute Value Operation**

![](../../../images/b8f50d1a60f66410.png)

**Node Functions**

Returns the absolute value of the input

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **6. Get Random Number**

![](../../../images/1ab4f4f0d879eba6.png)

**Node Functions**

Returns a random number in [Lower Limit, Upper Limit] (inclusive)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Lower Limit | Generic |  |
| Input Parameter | Upper Limit | Generic |  |
| Output Parameter | Random Number | Generic |  |

## **7. 3D Vector Angle**

![](../../../images/cbad2a5352b2cc0e.png)

**Node Functions**

Calculates the angle between two 3D Vectors and outputs the value in degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector2 | 3D Vector |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **8. 3D Vector Modulo Operation**

![](../../../images/e673f5fdd79c0f6c.png)

**Node Functions**

Calculates the magnitude of the input 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **9. 3D Vector Zoom**

![](../../../images/5a3abb3253e0a907.png)

**Node Functions**

Scales the input 3D Vector (scalar multiplication) and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **10. 3D Vector Rotation**

![](../../../images/d32cd8c9ee2c291d.png)

**Node Functions**

Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Rotated 3D Vector | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **11. 3D Vector Addition**

![](../../../images/1e802dd7250b87dd.png)

**Node Functions**

Calculates the sum of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector1 | 3D Vector |  |
| Input Parameter | 3D Vector2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **12. 3D Vector Subtraction**

![](../../../images/6e575f55036b1f8d.png)

**Node Functions**

Calculates the difference of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector1 | 3D Vector |  |
| Input Parameter | 3D Vector2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **13. 3D Vector Dot Product**

![](../../../images/b17fc295bf20b132.png)

**Node Functions**

Calculates the dot product of two input 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector1 | 3D Vector |  |
| Input Parameter | 3D Vector2 | 3D Vector |  |
| Output Parameter | Calculation Result | Floating Point Numbers |  |

## **14. 3D Vector Cross Product**

![](../../../images/a701747764be2f58.png)

**Node Functions**

Calculates the cross product of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector1 | 3D Vector |  |
| Input Parameter | 3D Vector2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **15. Direction Vector to Rotation**

![](../../../images/82d2ed2894b8770c.png)

**Node Functions**

Converts the Forward Vector and Upward Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Forward Vector | 3D Vector | Represents the desired Orientation of the Unit |
| Input Parameter | Upward Vector | 3D Vector | Defines the Unit's Up direction (used to determine the rotation angle). Default is the positive Y-axis of the World Coordinate System |
| Output Parameter | Rotate | 3D Vector |  |

## **16. Orientation to Rotation**

![](../../../images/ad4cf2acc0867fdb.png)

**Node Functions**

Converts a Direction Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |
| Output Parameter | Rotate | 3D Vector |  |

## **17. Split 3D Vectors**

![](../../../images/f8099c8dce9a01dc.png)

**Node Functions**

Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | X-Component | Floating Point Numbers |  |
| Output Parameter | Y-Component | Floating Point Numbers |  |
| Output Parameter | Z-Component | Floating Point Numbers |  |

## **18. Sine Function**

![](../../../images/974b1b05f525444c.png)

**Node Functions**

Calculates the sine of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **19. Cosine Function**

![](../../../images/8d086419ac65ffa5.png)

**Node Functions**

Calculates the cosine of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **20. Tangent Function**

![](../../../images/eec3d4b16078ff47.png)

**Node Functions**

Calculates the tangent of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **21. Arcsine Function**

![](../../../images/87e733088d6d24bf.png)

**Node Functions**

Calculates the arcsine of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **22. Arccosine Function**

![](../../../images/b9dda0500d6e9df0.png)

**Node Functions**

Calculates the arccosine of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **23. Arctangent Function**

![](../../../images/e590eee74ebc51f2.png)

**Node Functions**

Calculates the arctangent of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **24. 3D Vector Normalization**

![](../../../images/11cfa18dbdcfaba9.png)

**Node Functions**

Normalizes the length of a 3D Vector and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **25. Radians to Degrees**

![](../../../images/e6f6b52097076344.png)

**Node Functions**

Converts radians to degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **26. Degrees to Radians**

![](../../../images/603a0d08ce017287.png)

**Node Functions**

Converts degrees to radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Angle | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **27. Logical AND Operation**

![](../../../images/bf2d6693abe7ea40.png)

**Node Functions**

Performs a logical AND operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **28. Logical OR Operation**

![](../../../images/b764552eb041e770.png)

**Node Functions**

Performs a logical OR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **29. Logical NOT Operation**

![](../../../images/bfadd14a325e9df1.png)

**Node Functions**

Performs a logical NOT operation on the input Boolean value and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **30. Logical XOR Operation**

![](../../../images/9b9be5bbc42b858f.png)

**Node Functions**

Performs a logical XOR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **31. Greater Than**

![](../../../images/e6b15b5e9eefbf0b.png)

**Node Functions**

Returns whether the left value is greater than the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **32. Less Than**

![](../../../images/5dc8cb18fde29b92.png)

**Node Functions**

Returns whether the left value is less than the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **33. Less Than or Equal To**

![](../../../images/7962e23da8684a9c.png)

**Node Functions**

Returns whether the left value is less than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **34. Greater Than or Equal To**

![](../../../images/fe3c55e2d94b9b57.png)

**Node Functions**

Returns whether the left value is greater than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **35. Creating 3D Vectors**

![](../../../images/577d055d73436a90.png)

**Node Functions**

Creates a 3D Vector from x, y, and z components

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | X-Component | Floating Point Numbers |  |
| Input Parameter | Y-Component | Floating Point Numbers |  |
| Input Parameter | Z-Component | Floating Point Numbers |  |
| Output Parameter | 3D Vector | 3D Vector |  |

## **36. Convert Screen Coordinates to Viewport Coordinates**

![](../../../images/5f759107497176b6.png)

**Node Functions**

Converts screen coordinates into normalized 0-1 viewport coordinates. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Output Parameter | Viewport X | Floating Point Numbers |  |
| Output Parameter | Viewport Y | Floating Point Numbers |  |

## **37. Convert Viewport Coordinates to Screen Coordinates**

![](../../../images/b9539893c58d9e97.png)

**Node Functions**

Converts normalized 0-1 viewport coordinates into screen coordinates. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Viewport X | Floating Point Numbers |  |
| Input Parameter | Viewport Y | Floating Point Numbers |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

## **38. Convert Screen Coordinates to World Coordinates**

![](../../../images/1004c29128d13d18.png)

**Node Functions**

Converts screen coordinates plus a depth value into world coordinates. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Intput Parameter | Depth | Floating Point Numbers |  |
| Output Parameter | World Coordinates | 3D Vector |  |

## **39. Convert World Coordinates to Screen Coordinates**

![](../../../images/d4a00c73a130492f.png)

**Node Functions**

Converts world coordinates to screen coordinates. Only available in Beyond Mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | World Coordinates | 3D Vector |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

# **III. Lists**

## **1. Assembly List**

![](../../../images/8042b78bf2f1662d.png)

**Node Functions**

Assembles multiple Input Parameters of the same type (up to 10) into a single List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Generic | Assembled List |
| Input Parameter | 0~9 | Generic | Assembles up to 10 parameters into a list |

# **IV. Structures**

## **1. Assemble Structure**

![](../../../images/fe1f4fe69aef5222.png)

**Node Functions**

Combines multiple parameters into a single Structure-type value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Structure | Structure |  |

## **2. Split Structure**

![](../../../images/48ee8409a278c7c2.png)

**Node Functions**

Returns all parameters of the specified Structure

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Intput Parameter | Structure | Structure |  |

# **V. Dictionary**

## **1. Assembly Dictionary**

![](../../../images/e994befae3c224b2.png)

**Node Functions**

Combines up to 50 Key-Value Pairs into one Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Dictionary | Generic |  |
| Input Parameter | Key 0~49 | Generic |  |
| Input Parameter | Value 0~49 | Generic |  |

## **2. Create Dictionary**

![](../../../images/9b242751d98e9bd7.png)

**Node Functions**

Creates Key-Value Pairs sequentially from the input key and value lists.

This node builds the Dictionary using the shorter of the key and value lists; extra items are truncated

If duplicate keys are found in the key list, creation fails and returns an empty Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key List | Generic |  |
| Input Parameter | Value List | Generic |  |
| Output Parameter | Dictionary | Generic |  |
