---
title: Operation Nodes
path_id: mh0qfw9hirz6
updated_at: 2026-08-08 23:31:46
category: Node Introduction/Client Nodes/Character Skill Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0qfw9hirz6
---

# I. General

## **1. Enumeration Match**

![](../../../images/f60f74180f0440df.png)

**Node Functions**

After confirming the Enumeration type, determines whether the two input values are equal

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Enumeration 1 | Generic |  |
| Input Parameter | Enumeration 2 | Generic |  |
| Output Parameter | Result | Boolean | Output True if equal, False if not equal |

## **2. Equal**

![](../../../images/4cb5d729bd524a83.png)

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

## **3. Data Type Conversion**

![](../../../images/ffd7634c41f6eb2d.png)

**Node Functions**

Converts input parameter types to another type for output. For specific rules, see [Basic Concepts](/ys/ugc/tutorial//detail/mhk23ora1wom) - [Conversion Rules Between Basic Data Types]

In the client node, when converting a floating-point number to an integer, the number will be truncated.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Conversion Result | Generic |  |

# II. Math

## **1. Split 3D Vector**

![](../../../images/9e4a3f1fd3fbdfe8.png)

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

## **2. Orientation to Rotation**

![](../../../images/ca6b296f02c5a66b.png)

**Node Functions**

Converts a Direction Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |
| Output Parameter | Rotate | 3D Vector |  |

## **3. Multiplication**

![](../../../images/54e160d84c514316.png)

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

![](../../../images/b2f0ed345650306e.png)

**Node Functions**

Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **5. Arccosine Function**

![](../../../images/39ed87f9baf07cb5.png)

**Node Functions**

Calculates the arccosine of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **6. Arctangent Function**

![](../../../images/03b10c51387b929c.png)

**Node Functions**

Calculates the arctangent of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **7. Arcsine Function**

![](../../../images/3a5f75dac0ca8ee3.png)

**Node Functions**

Calculates the arcsine of the input and returns the value in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **8. Direction Vector to Rotation**

![](../../../images/f5f0bf5d17f6db75.png)

**Node Functions**

Converts the Forward Vector and Upward Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Forward Vector | 3D Vector | Represents the desired Orientation of the Unit |
| Input Parameter | Upward Vector | 3D Vector | Defines the Unit's Up direction (used to determine the rotation angle). Default is the positive Y-axis of the World Coordinate System |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Radians to Degrees**

![](../../../images/b69f22e38d08956e.png)

**Node Functions**

Converts radians to degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **10. Get Random Number**

![](../../../images/2d1645c41e16eddf.png)

**Node Functions**

Returns a random number in [Lower Limit, Upper Limit] (inclusive)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Lower Limit | Generic |  |
| Input Parameter | Upper Limit | Generic |  |
| Output Parameter | Random Number | Generic |  |

## **11. Addition**

![](../../../images/fe6f10c2241d07b2.png)

**Node Functions**

Adds two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **12. Subtraction**

![](../../../images/850164ed3956949b.png)

**Node Functions**

Subtracts two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **13. Degrees to Radians**

![](../../../images/be0fe9b2b39b27b9.png)

**Node Functions**

Converts degrees to radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Angle | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **14. Absolute Value Operation**

![](../../../images/704d984bc096d293.png)

**Node Functions**

Returns the absolute value of the input

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **15. Logical NOT Operation**

![](../../../images/9bcad50a57d21a5c.png)

**Node Functions**

Performs a logical NOT operation on the input Boolean value and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **16. Logical OR Operation**

![](../../../images/f099db7fbe62e0bf.png)

**Node Functions**

Performs a logical OR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **17. Logical XOR Operation**

![](../../../images/62fd4c8f1258ab7f.png)

**Node Functions**

Performs a logical XOR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **18. Logical AND Operation**

![](../../../images/e6e002972331a8e4.png)

**Node Functions**

Performs a logical AND operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **19. 3D Vector Normalization**

![](../../../images/5de662700e2d098a.png)

**Node Functions**

Normalizes the length of a 3D Vector and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **20. 3D Vector Addition**

![](../../../images/a676697c798e1f1a.png)

**Node Functions**

Calculates the sum of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **21. 3D Vector Angle**

![](../../../images/3273f1f29c312f8d.png)

**Node Functions**

Calculates the angle between two 3D Vectors and outputs the value in degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Angle (°) | Floating Point Numbers |  |

## **22. 3D Vector Subtraction**

![](../../../images/e45eba7fe404c710.png)

**Node Functions**

Calculates the difference of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **23. 3D Vector Modulo Operation**

![](../../../images/5887a614ef507816.png)

**Node Functions**

Calculates the magnitude of the input 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **24. 3D Vector Dot Product**

![](../../../images/29f7aca02a72292f.png)

**Node Functions**

Calculates the dot product of two input 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | Floating Point Numbers |  |

## **25. 3D Vector Zoom**

![](../../../images/6336be73878c567a.png)

**Node Functions**

Scales the input 3D Vector (scalar multiplication) and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **26. 3D Vector Cross Product**

![](../../../images/1d61bf93c5cd33ca.png)

**Node Functions**

Calculates the cross product of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **27. 3D Vector Rotation**

![](../../../images/e55e7a970e54663d.png)

**Node Functions**

Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Rotated 3D Vector | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **28. Greater Than**

![](../../../images/fd8f3cb99ad0f3c7.png)

**Node Functions**

Returns whether the left value is greater than the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **29. Greater Than or Equal To**

![](../../../images/896becd7f51f5fb4.png)

**Node Functions**

Returns whether the left value is greater than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **30. Less Than**

![](../../../images/5206fc759bee573f.png)

**Node Functions**

Returns whether the left value is less than the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **31. Less Than or Equal To**

![](../../../images/0149e3d96b149030.png)

**Node Functions**

Returns whether the left value is less than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **32. Cosine Function**

![](../../../images/4a95803e1cdc0c8d.png)

**Node Functions**

Calculates the cosine of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **33. Tangent Function**

![](../../../images/87eba3f7a238926b.png)

**Node Functions**

Calculates the tangent of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **34. Sine Function**

![](../../../images/190774b86c07afef.png)

**Node Functions**

Calculates the sine of the input in radians

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **35. Create 3D Vector**

![](../../../images/949402b284c57278.png)

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

![](../../../images/28b3a809cb795cab.png)

**Node Functions**

Converts screen coordinates to viewport coordinates (normalized from 0 to 1). Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Output Parameter | Viewport X | Floating Point Numbers |  |
| Output Parameter | Viewport Y | Floating Point Numbers |  |

## **37. Convert Viewport Coordinates to Screen Coordinates**

![](../../../images/77e42fe94c349e59.png)

**Node Functions**

Converts normalized viewport coordinates (0–1) to screen coordinates. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Viewport X | Floating Point Numbers |  |
| Input Parameter | Viewport Y | Floating Point Numbers |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

## **38. Convert Screen Coordinates to World Coordinates**

![](../../../images/ab315d0afdd405a3.png)

**Node Functions**

Add a depth value to the screen coordinates to convert them to world coordinates. Only available in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Input Parameter | Depth | Floating Point Numbers |  |
| Output Parameter | World Coordinates | 3D Vector |  |

## **39. Convert World Coordinates to Screen Coordinates**

![](../../../images/6939d4101e6a3ec1.png)

**Node Functions**

Convert world coordinates to screen coordinates. Only available in Beyond Mode.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | World Coordinates | 3D Vector |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

# III. Lists

## **1. Assembly List**

![](../../../images/c1fcb48ea9711fe6.png)

**Node Functions**

Assembles multiple Input Parameters of the same type (up to 10) into a single List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 0–9 | Generic | Assembles up to 10 parameters into a list |
| Output Parameter | List | Generic | The assembled list |

# IV. Structure

## **1. Split Structure**

![](../../../images/264ab99d56a52f85.png)

**Node Functions**

Get all parameters of the specified structure.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Structure | Structure |  |

## **2. Assemble Structure**

![](../../../images/9197e4cc0a0d0eb9.png)

**Node Functions**

Combine multiple parameters into a value of the structure type.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Structure | Structure |  |

# V. Dictionary

## **1. Create Dictionary**

![](../../../images/c995680d107af100.png)

**Node Functions**

Create key-value pairs according to the order of the input keys and values list.

This node will create a dictionary based on the shorter of the two lists, and any excess elements will be truncated.

If there are duplicate values in the keys list, the creation will fail, and an empty dictionary will be returned.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key List | Generic |  |
| Input Parameter | Value List | Generic |  |
| Output Parameter | Dictionary | Generic |  |

## **2. Assembly Dictionary**

![](../../../images/6fc2ff75438d2cde.png)

**Node Functions**

Combine up to 50 key-value pairs into a dictionary.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key 0–49 | Generic |  |
| Input Parameter | Key 0–49 | Generic |  |
| Output Parameter | Dictionary | Generic |  |
