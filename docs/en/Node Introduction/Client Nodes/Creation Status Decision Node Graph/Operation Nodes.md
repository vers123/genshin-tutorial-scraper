---
title: Operation Nodes
path_id: mhw7p30tmvqo
updated_at: 2026-05-14 11:24:14
category: Node Introduction/Client Nodes/Creation Status Decision Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhw7p30tmvqo
---

# I. General

## **1. Enumeration Match**

![](../../../images/e9ae8d0a65fd604c.png)

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

![](../../../images/426a013ef7b0f0c5.png)

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

![](../../../images/5f21d7017956443a.png)

**Node Functions**

Converts input parameter types to another type for output. For specific rules, see [Basic Concepts](/ys/ugc/tutorial//detail/mhk23ora1wom)-[Conversion Rules Between Basic Data Types]

In the Local Node, converting Floating Point Numbers to an Integer truncates the decimal part

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Conversion Result | Generic |  |

# II. Math

## **1. Split 3D Vector**

![](../../../images/eede132c4fd33b72.png)

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

![](../../../images/2d262dd2d779b673.png)

**Node Functions**

Converts a Direction Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |
| Output Parameter | Rotation | 3D Vector |  |

## **3. Multiplication**

![](../../../images/80ddb3addb71b46b.png)

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

![](../../../images/fa2cf4df0eea3216.png)

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

## **5. Create 3D Vector**

![](../../../images/60ec5fae7d09f4eb.png)

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

## **6.. Arccosine Function**

![](../../../images/7b455cae484da727.png)

**Node Functions**

Calculates the arccosine of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **7.. Arctangent Function**

![](../../../images/8e872bf4f5d3256d.png)

**Node Functions**

Calculates the arctangent of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **8.. Arcsine Function**

![](../../../images/4704f483a734f05e.png)

**Node Functions**

Calculates the arcsine of the input and returns the value in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **9. Direction Vector to Rotation**

![](../../../images/b6d89ce952fd6649.png)

**Node Functions**

Converts the Forward Vector and Upward Vector to Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Forward Vector | 3D Vector | Represents the desired Orientation of the Unit |
| Input Parameter | Upward Vector | 3D Vector | Defines the Unit's Up direction (used to determine the rotation angle). Default is the positive Y-axis of the World Coordinate System |
| Output Parameter | Rotate | 3D Vector |  |

## **10. Radians to Degrees**

![](../../../images/7ebc50963d6aea26.png)

**Node Functions**

Converts Radian to degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **11. Get Random Number**

![](../../../images/88deecf9cd087b52.png)

**Node Functions**

Returns a random number in [Lower Limit, Upper Limit] (inclusive)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Lower Limit | Generic |  |
| Input Parameter | Upper Limit | Generic |  |
| Output Parameter | Random Number | Generic |  |

## **12. Addition**

![](../../../images/5369d1ac6647aea1.png)

**Node Functions**

Adds two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **13. Subtraction**

![](../../../images/8c88bea87fbfd2d4.png)

**Node Functions**

Subtracts two Floating Point Numbers or Integers

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **14. Degrees to Radians**

![](../../../images/f4f7e39109a6d3cf.png)

**Node Functions**

Converts degrees to Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Angle | Floating Point Numbers |  |
| Output Parameter | Radian | Floating Point Numbers |  |

## **15. Absolute Value Operation**

![](../../../images/bfd066a1f2afc9f6.png)

**Node Functions**

Returns the absolute value of the input

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **16. Logical NOT Operation**

![](../../../images/4f13e6a0bd1c6884.png)

**Node Functions**

Performs a logical NOT operation on the input Boolean value and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **17. Logical OR Operation**

![](../../../images/e35fa9dd20ae8b96.png)

**Node Functions**

Performs a logical OR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **18. Logical XOR Operation**

![](../../../images/459b91fd4760d6c1.png)

**Node Functions**

Performs a logical XOR operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **19. Logical AND Operation**

![](../../../images/3c3f1e51bcfe2ddf.png)

**Node Functions**

Performs a logical AND operation on the two input Boolean values and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Condition 1 | Boolean |  |
| Input Parameter | Condition 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **20. Assembly List**

![](../../../images/6f8d2433f2791c60.png)

**Node Functions**

Assembles multiple Input Parameters of the same type (up to 10) into a single List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 0–9 | Generic | Assemble up to 10 parameters into a list |
| Output Parameter | List | Generic | The assembled list |

## **21. 3D Vector Normalization**

![](../../../images/6c1b961868db10d7.png)

**Node Functions**

Normalizes the length of a 3D Vector and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **22. 3D Vector Addition**

![](../../../images/08235f9067d9779f.png)

**Node Functions**

Calculates the sum of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **23. 3D Vector Angle**

![](../../../images/cef3b9ae18fe02c1.png)

**Node Functions**

Calculates the angle between two 3D Vectors and outputs the value in degrees

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Angle | Floating Point Numbers |  |

## **24. 3D Vector Subtraction**

![](../../../images/9796c1870b942a9f.png)

**Node Functions**

Calculates the difference of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **25. 3D Vector Modulo Operation**

![](../../../images/2e2bae0732069ec3.png)

**Node Functions**

Calculates the magnitude of the input 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **26. 3D Vector Dot Product**

![](../../../images/e362f3d140223795.png)

**Node Functions**

Calculates the dot product of two input 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | Floating Point Numbers |  |

## **27. 3D Vector Zoom**

![](../../../images/35bfeb822a9e431e.png)

**Node Functions**

Scales the input 3D Vector (scalar multiplication) and outputs the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **28.. 3D Vector Cross Product**

![](../../../images/e637c0921797f5b9.png)

**Node Functions**

Calculates the cross product of two 3D Vectors

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Calculation Result | 3D Vector |  |

## **29. 3D Vector Rotation**

![](../../../images/89e8f392651c3f94.png)

**Node Functions**

Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Rotated 3D Vector | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **30. Greater Than**

![](../../../images/4ac7e7078f0aa2c1.png)

**Node Functions**

Returns whether the left value is greater than the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **31. Greater Than or Equal To**

![](../../../images/dba6cafc0bb66fe7.png)

**Node Functions**

Returns whether the left value is greater than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **32. Less Than**

![](../../../images/809fd84e36e7e3bf.png)

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

![](../../../images/8642b4c9468822e4.png)

**Node Functions**

Returns whether the left value is less than or equal to the right value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Boolean |  |

## **34. Cosine Function**

![](../../../images/bd96c8c27dd7ee97.png)

**Node Functions**

Calculates the cosine of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **35. Tangent Function**

![](../../../images/0204c817a4e27df2.png)

**Node Functions**

Calculates the tangent of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **36. Sine Function**

![](../../../images/183fb1faeea08cec.png)

**Node Functions**

Calculates the sine of the input in Radian

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

# III. Dictionary

## **1. Create Dictionary**

![](../../../images/0a8a4315ad061ecb.png)

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

## **2. Assembly Dictionary**

![](../../../images/0e722aab2a732c94.png)

**Node Functions**

Combines up to 50 Key-Value Pairs into one Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key 0–49 | Generic |  |
| Input Parameter | Value 0–49 | Generic |  |
| Output Parameter | Dictionary | Generic |  |

# IV. Structures

## **1. Split Structure**

![](../../../images/2abc6c02015591c3.png)

**Node Functions**

Returns all parameters of the specified Structure

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Structure | Structure |  |

## **2. Assemble Structure**

![](../../../images/e514f163ecb351a6.png)

**Node Functions**

Combines multiple parameters into a single Structure-type value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Structure | Structure |  |

#
