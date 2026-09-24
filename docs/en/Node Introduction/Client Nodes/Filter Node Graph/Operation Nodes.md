---
title: Operation Nodes
path_id: mhnemz9859q2
updated_at: 2026-08-07 16:44:27
category: Node Introduction/Client Nodes/Filter Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhnemz9859q2
---

# I. General

## **1. Enumeration Match**

![](../../../images/0755aa49e85d8f2a.png)

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

![](../../../images/3976f2ef10e9e4a5.png)

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

![](../../../images/4bd4d10e0801e110.png)

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

![](../../../images/bf33866e2796692f.png)

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

![](../../../images/7550120fc0617db9.png)

**Node Functions**

Converts a Direction Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |
| Output Parameter | Rotate | 3D Vector |  |

## **3. Multiplication**

![](../../../images/9c5859fce66d9fec.png)

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

![](../../../images/b4c5be4e20e97714.png)

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

![](../../../images/8767726ba13b032a.png)

**Node Functions**

Calculates the arccosine of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **6. Arctangent Function**

![](../../../images/a60ecc2e1c9d47f4.png)

**Node Functions**

Calculates the arctangent of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **7. Arcsine Function**

![](../../../images/98f2165dd7901f13.png)

**Node Functions**

Calculates the arcsine of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **8. Direction Vector to Rotation**

![](../../../images/17f8bf024d71522d.png)

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

![](../../../images/2377b4da79854372.png)

**Node Functions**

Converts Radian to degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **10. Get Random Number**

![](../../../images/fa3c6353220f0a14.png)

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

![](../../../images/5bbe80933744aac5.png)

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

![](../../../images/698a8a58d2fcd607.png)

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

![](../../../images/8e316bb4db9b0690.png)

**Node Functions**

Converts degrees to Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Angle | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **14. Absolute Value Operation**

![](../../../images/0d28e811a985524b.png)

**Node Functions**

Returns the absolute value of the input

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **15. Logical NOT Operation**

![](../../../images/16291563f14d99f9.png)

**Node Functions**

Performs a logical NOT operation on the input Boolean value and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **16. Logical OR Operation**

![](../../../images/ce526f03504817fb.png)

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

![](../../../images/db878b7ce14f8cba.png)

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

![](../../../images/dcb89fabfce80271.png)

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

![](../../../images/e798b07dff905422.png)

**Node Functions**

Normalizes the length of a 3D Vector and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **20. 3D Vector Addition**

![](../../../images/8292c5430ae19814.png)

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

![](../../../images/c873f10c81fc1332.png)

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

![](../../../images/adc44c39a2ff0911.png)

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

![](../../../images/2cf0a864e6baf14e.png)

**Node Functions**

Calculates the magnitude of the input 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **24. 3D Vector Dot Product**

![](../../../images/acd9fb2b4ce35ad4.png)

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

![](../../../images/1f3639a45dcbf7d0.png)

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

![](../../../images/9dbb4aa0fc977231.png)

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

![](../../../images/6b39c283378835db.png)

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

![](../../../images/e6a965379a98d41f.png)

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

![](../../../images/664c31fd4724663e.png)

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

![](../../../images/508bf4fe3eff8ac2.png)

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

![](../../../images/cd1f0b561d2ffa2d.png)

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

![](../../../images/ec981b88b1f7c89c.png)

**Node Functions**

Calculates the cosine of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **33. Tangent Function**

![](../../../images/ff29c0e8ce6a2876.png)

**Node Functions**

Calculates the tangent of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **34. Sine Function**

![](../../../images/608eb5769d344dde.png)

**Node Functions**

Calculates the sine of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **35. Create 3D Vector**

![](../../../images/f37eebacbb1bc075.png)

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

![](../../../images/6cf6b997715a27a6.png)

**Node Functions**

Converts screen coordinates to viewport coordinates (normalized to 0–1). Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Output Parameter | Viewport X | Floating Point Numbers |  |
| Output Parameter | Viewport Y | Floating Point Numbers |  |

## **37. Convert Viewport Coordinates to Screen Coordinates**

![](../../../images/ff2c0e0aa53c82f3.png)

**Node Functions**

Converts viewport coordinates (normalized to 0–1) to screen coordinates. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Viewport X | Floating Point Numbers |  |
| Input Parameter | Viewport Y | Floating Point Numbers |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

## **38. Convert Screen Coordinates to World Coordinates**

![](../../../images/985d5ee41082ea9c.png)

**Node Functions**

Converts screen coordinates to world coordinates and adds a depth value. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Screen X | Floating Point Numbers |  |
| Input Parameter | Screen Y | Floating Point Numbers |  |
| Input Parameter | Depth | Floating Point Numbers |  |
| Output Parameter | World Coordinates | 3D Vector |  |

## **39. Convert World Coordinates to Screen Coordinates**

![](../../../images/1cc99eef5bddc7d6.png)

**Node Functions**

Converts world coordinates to screen coordinates. Available only in Beyond Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | World Coordinates | 3D Vector |  |
| Output Parameter | Screen X | Floating Point Numbers |  |
| Output Parameter | Screen Y | Floating Point Numbers |  |

# III. Lists

## **1. Assembly List**

![](../../../images/622c1127bdd4f379.png)

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

![](../../../images/e058fccbbe68f21c.png)

**Node Functions**

Get all parameters of the specified structure.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Structure | Structure |  |

## **2. Assemble Structure**

![](../../../images/49dc9814347c491e.png)

**Node Functions**

Combine multiple parameters into a value of the structure type.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Structure | Structure |  |

# V. Dictionary

## **1. Create Dictionary**

![](../../../images/f32acce739bfcfd7.png)

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

![](../../../images/9298683fe5261a8f.png)

**Node Functions**

Combine up to 50 key-value pairs into a dictionary.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key 0–49 | Generic |  |
| Input Parameter | Key 0–49 | Generic |  |
| Output Parameter | Dictionary | Generic |  |
