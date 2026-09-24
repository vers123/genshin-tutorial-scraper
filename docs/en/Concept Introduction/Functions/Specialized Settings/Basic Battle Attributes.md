---
title: Basic Battle Attributes
path_id: mh8vbl0e14qo
updated_at: 2026-08-03 17:18:54
category: Concept Introduction/Functions/Specialized Settings
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh8vbl0e14qo
---

*Attributes* required for combat validation, such as ATK/DEF/HP, which may have different definitions depending on the entity type.

# I. Basic Battle Attributes for Objects

![](../../../images/03ede965ac85bd07.png)

*Level*: Default object level as set on its *prefab*/*entity*. This value can also be reassigned when creating objects using node graphs.

*Base HP*: The object's HP value. When HP is reduced to 0, the entity will be defeated, triggering destruction and removal events.

*Base ATK*: The base ATK of the object.

*Base DEF*: The base DEF of the object.

# II. Creation Base Battle Attributes

Unlike objects, from both level attributes and fixed attributes, it supports creators (Craftspeople) in adjusting parameters and planning growth curves for their creations.

![](../../../images/4c09725e60bf4097.png)

## 1. Level Attributes

![](../../../images/50c7738ba01b07f3.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Level* | The level at which the creation is created |
| *Base HP* | The creation's base HP. The actual HP is calculated by multiplying this value with the multiplier provided by *Attribute Growth* |
| *Base ATK* | The creation's base ATK. The actual ATK is calculated by multiplying this value with the growth rate provided by attribute growth. |
| *Base DEF* | The creation's base DEF. The actual DEF is calculated by multiplying this value with the growth rate provided by attribute growth. |
| *Attribute Growth* | A level-based numerical curve is an attribute curve that provides multipliers for health and attack power.  Provides three templates: *No Growth*, *Default* *Growth Curve*, *Custom Growth Curve*  ![](../../../images/d1ff9648a935ac3d.png) |

**(1) Attribute Growth Settings**

Attribute Growth Curve Enumeration Description

No Growth - All multiplier parameters are 1, meaning base attributes do not change with level.

Default Growth Curve - This curve is a predefined numerical curve. You can view the specific *growth multipliers* in the curve interface, but they cannot be modified.

Custom Growth Curve - Use a custom growth curve created by the creator (Craftsperson). You can click 'Edit Curve' to manually modify it, and it also supports importing and exporting curve properties.

Attribute Growth Curve Calculation Instructions

1.Take HP calculation as an example. Initial level is set to 1, base HP is changed to 200, select the Default Growth Curve.

![](../../../images/dfedb6eff062d14c.png)

Select "View Curve" to determine that when the level is 1, the *health multiplier* equals 5.938. Therefore, the actual health value of the creation during runtime should be 200 \* 5.938 = 1078.76.

In the top-right corner, select *"**Preview Result Values**"* to see the actual health value of 1078.76, which matches the calculated result.

The same principle applies to the calculation of other parameters.

![](../../../images/88cacdb652a4ac8d.png)

![](../../../images/8530d0d6c09ce743.png)

## (2) Attribute Growth Rules

*Actual HP* = Current Level HP Multiplier × Base HP

*Actual ATK* = Level ATK Multiplier × Base ATK

The base HP and base ATK are the values configured by the creator (Craftsperson) in the basic battle attributes.

The actual HP and actual ATK are the values that take effect during gameplay and may vary due to equipment, unit status, or other functionalities.

2.**Fixed Attributes**

The following fixed attribute parameters support overriding and will take effect for the creation during stage runtime. The configurable range for each parameter differs, as explained in the table below.

![](../../../images/9ec09c4af2e0811c.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Supports Configuring a Lower Limit | Supports Configuring an Upper Limit |
| *Elemental Mastery* | 0 | 3000 |
| *Various RES* | 0 | 3 |

# III. Node Graph

You can use the node graph to query the base combat attributes of creations or objects.

![](../../../images/f1665efe4e95382b.png)

![](../../../images/ecd3d1acf69ba3ad.png)

#
