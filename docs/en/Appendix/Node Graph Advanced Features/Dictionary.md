---
title: Dictionary
path_id: mhbydx0u7cgw
updated_at: 2025-10-22 03:18:48
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhbydx0u7cgw
---

# I. What is a Dictionary

A *Dictionary* is a data structure used to represent a set of mapping relationships

For example, in a given gameplay, you may want to store the Scores of all Players on the Stage Entity

Without using a Dictionary, you would need to use multiple *Custom Variables* on the Stage Entity, each one storing a Player's Score (in Beyond Mode, up to 8 Custom Variables may be required)

This approach becomes cumbersome when you need to store Scores for more Entities. For instance, in a racing gameplay against Creations, each Creation would require an additional Custom Variable to record its Score

Using a Dictionary can effectively solve this problem:

On a Stage Entity, you can define a Dictionary mapping *Entity* to *Integer*. Each mapping in this Dictionary contains an Entity-type value and an Integer-type value. The Entity entry can be used to store Player Entities, while the Integer entry records their Scores

You can easily modify elements in a Dictionary using Dictionary Operation Nodes—for example, adding new elements or deleting existing ones

You can also package a data structure such as [Player's Score] into a Dictionary type for use and transfer

## 1. Definition of Dictionary

A Dictionary is a data structure that can be used in Server Node Graphs

Each Dictionary defines a mapping from data type A to data type B

Here, data type A is the *Key*, B is the *Value*, and each Key+Value combination is a *Key-Value Pair*. A Dictionary is simply a collection of Key-Value Pairs

A common Dictionary structure is shown below. This Dictionary maps *Strings* to *Floating Point Numbers*

|  |  |
| --- | --- |
| **Key** | **Value** |
| ABC | 1.3 |
| DEF | 1.8 |
| GHI | 20.5 |

## 2. Key Points of Dictionary Functions

**Dictionary Type Determination**

As explained in [Basic Concepts](/ys/ugc/tutorial//detail/mhk23ora1wom), Node Graphs are strongly typed, and a Dictionary's type is uniquely defined by its Key and Value types.

Therefore, a Dictionary of [String → Floating Point Numbers] type cannot be connected to a Dictionary of [String → Integer] type

**Dictionary Key Uniqueness**

A Dictionary cannot contain duplicate Keys. Each Key in a Dictionary must be unique

Therefore, Dictionary actions are centered around Keys, such as editing Values by Key or searching Values by Key

**Pass by Reference for Dictionaries**

Similar to Lists, Dictionaries in Node Graphs are passed by reference. As a result, Dictionary modification Nodes directly affect Dictionary data stored in *Custom Variables* and *Node Graph Variables*, as detailed in [Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica)

Similarly, in the *When* *Custom Variable Changes* Event, the fields [*Pre-Change Value*] and [*Post-Change* *Value*] are not provided. Use *Get Custom Variable* to obtain the updated Value

**Unordered Storage of Dictionary**

The Key-Value Pairs in a Dictionary are not stored in order. When using a Dictionary, do not rely on their sequence; treat them as unordered

**Available Data Types for Dictionaries**

The Dictionary Key types include:

|  |
| --- |
| **Data Types** |
| Entity |
| GUID |
| Integer |
| String |
| Factions |
| Prefab ID |
| Configuration ID |

The Dictionary values can include the following types:

|  |  |
| --- | --- |
| **Data Types** | **List Data Types** |
| Entity | Entity List |
| GUID | GUID List |
| Integer | Integer List |
| Boolean | Boolean List |
| Floating Point Numbers | Floating Point Numbers List |
| String | String List |
| Faction | Faction List |
| 3D Vector | 3D Vector List |
| Prefab ID | Prefab ID List |
| Configuration ID | Configuration ID List |
| Custom Structure | Custom Structure List |

# II. Using Dictionaries in Generics

In a Server Node Graph, a Dictionary is a special type of *Generic Pin*. To define a Dictionary type, select [Dictionary] in the Generic configuration, then specify its Key and Value types

For Generic Pins that support Dictionaries, the [Dictionary] option is available in the Generic dropdown menu

![](../../images/73d531fdfb836b93.png)

Upon being clicked, the Generic button next to [*Variable Value*] changes, indicating that this Pin is now a Generic Dictionary Pin

![](../../images/59621cbbe319474a.png)

Click the Generic button again to specify the Key and Value types for this Generic Dictionary

As described above, a Generic Dictionary's type is only fully defined once both its Key and Value types are specified

![](../../images/c2946489ade3f3f0.png)

# III. Dictionary-Related Nodes

## 1. Execution Nodes

**Set or Add Key Value Pair to Dictionary**

![](../../images/b1c3e87c029d9af0.png)

**Remove key-value pairs From cictionary by Key**

![](../../images/caff6e43074a1c6e.png)

**Clear Dictionary**

![](../../images/401eed8a48713ee6.png)

**Sort Dictionary by Key**

![](../../images/4f378ff85d87b2ec.png)

**Sort Dictionary by Value**

![](../../images/ca1dd683844aaeb7.png)

## 2. Query Nodes

**Query Dictionary Length**

![](../../images/4e98f5516a17ba5e.png)

**Query Dictionary Value by Key**

![](../../images/5f125bc54c41099c.png)

**Get List of Keys From Dictionary**

![](../../images/a8fc8a788b5d5d2b.png)

**Get List of Values From Dictionary**

![](../../images/200bebcb257cefc1.png)

**Query If Dictionary Contains Specific Key**

![](../../images/af0a015bd29ecfa9.png)

**Query If Dictionary Contains Specific Value**

![](../../images/7c2b247dfe56e52f.png)

## 3. Operation Nodes

**Create Dictionary**

![](../../images/bd8f3fb0d4bf6231.png)

**Assembly Dictionary**

![](../../images/526a5a33e6770513.png)
