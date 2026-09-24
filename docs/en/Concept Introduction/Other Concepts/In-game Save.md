---
title: In-game Save
path_id: mh92u90ps98g
updated_at: 2025-10-21 11:05:22
category: Concept Introduction/Other Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh92u90ps98g
---

# I. Definition of In-Game Save Data

In-game save is a structure that stores player data generated within a specific stage. This data persists even after the player exits the stage, and will be carried over each time the player enters the stage. For example: you can save the list of items obtained by the player in a stage as an in-game save. Players can continue playing in the stage and whenever they re-enter the stage, they can bring back the items obtained from their previous playthrough

In-game saves require the use of [Structure](/ys/ugc/tutorial//detail/mh3fmi0t99ns) and [Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica)

# **II. In-Game Save Related Functions**

## 1. Data Structure of In-Game Save

In each stage, creators (Craftspeople) can configure multiple **in-game save templates**, but only one in-game save template can be enabled at a time as the current stage's in-game save template.

A game save template contains multiple game save data structures, with each game save being a fixed-length list of custom structures

Below is the configuration interface for the in-game save data structure and in-game save template

![](../../images/e435bfb720478856.png)

*In-game Save* *Structure* is used similarly to basic structures, but does not support certain data types

Here are the data types supported by in-game save data structures: (Entities, entity lists, dictionaries of all types, and structures are not supported in in-game save structures)

|  |  |
| --- | --- |
| **Data Type** | **List Data Type** |
| GUID | GUID List |
| Integer | Integer List |
| Boolean | Boolean List |
| Floating Point Numbers | Floating Point List |
| String | String List |
| Faction | Faction List |
| 3D Vector | 3D Vector List |
| Prefab ID | Prefab ID List |
| Configuration ID | Configuration ID List |

Below is the configuration interface for the in-game save structure, which follows basically the same configuration method as the basic structure

![](../../images/b3d0a05fcaad382a.png)

## 2. In-Game Save Data Writing and Reading

In-game saves rely on custom variables for writing and reading. After defining and enabling the in-game save template, each in-game save data structure in the template will generate a custom variable of the same name (called *in-game save variable*) on each player entity

**In-game save variables can be read and written using custom variable-related nodes, just like regular custom variables**

Since in-game save variables correspond one-to-one with in-game save definitions, player's in-game save variables cannot be modified directly

![](../../images/c740906eb00d15ea.png)

When a player enters a stage, based on their in-game save data, this in-game save data will be written to the in-game save variables on the player entity. This process is called *loading*

Note: The process of writing in-game save data to in-game save variables occurs before entity creation, so the entity creation event on the player entity can correctly query the in-game save variables on the player entity

When players exit the stage, the in-game save variables will be written to the in-game save file and carried away from the stage with the player. This process is called *saving*

## **3. In-Game Save Data Size Limitations**

The amount of in-game save data available for each stage is limited, determined by the member types of the structure that makes up the in-game save. Generally, string types and list types will generate larger data volumes.

If the total data volume in a stage exceeds the limit, you won't be able to playtest or publish it. You'll need to optimize the data structure of the in-game save.

### List Type Length Limit

Due to the overall data size limitation of in-game saves, all list-type data in in-game saves have maximum length restrictions (unlike custom variables)

During runtime, list data in in-game save variables can exceed the maximum length limit for storage, but when saving, list data that exceeds the length limit will be truncated to the maximum length limit (i.e., keeping the first several elements, while elements exceeding the length limit will be discarded)

This may result in some runtime player data not being saved to the in-game save file. It is recommended to validate the length of list-type data when writing to in-game save variables.

As shown in the following figure, when defining the in-game save structure, the length of all list-type data must be defined (in the figure, the affix ID list length is 10, meaning it can store up to 10 integers)

![](../../images/0c9a71c753a55407.png)

Additionally, each in-game save template, as a list of structures, has its own length limit. Any content exceeding this length will be truncated when saving.

![](../../images/53d54abb101dab2a.png)

## 4. In-Game Save Level Up

In-game saves can store persistent data generated during gameplay, so creators (Craftspeople) need to handle in-game save data carefully for published stages to prevent player data loss.

For a published stage, the in-game save can be upgraded in the following ways

Add in-game save data structures to the published in-game save template. When players enter the stage, the newly added in-game save data will be loaded with default values defined in the in-game save data structure.Add new members to the published in-game save structure. When players enter a stage, the newly added members will be loaded with default values defined in the structure.

The following in-game save operations are not recommended

Delete a published in-game save template, or replace it with a new in-game save template that has a completely different structure from the previous one.Reduce the maximum length of a published in-game save template. Modify the structure type referenced by in-game save files or delete existing in-game save files from published in-game save file templates.Modify or delete member data types of the published in-game save structure.

The above operations will cause the new in-game save structure to mismatch with the player's existing in-game save data, resulting in loading failure and resetting of the player's in-game save data

# **III. In-game Save Data Related Function Entry Points**

## 1. In-Game Save Data Structure Configuration

![](../../images/6c69fd0653ab91f2.png)

In-game save data structure has a similar configuration method to the basic structure (see [Structure](/ys/ugc/tutorial//detail/mh3fmi0t99ns))

![](../../images/6c2f562faa62b52d.png)

The main difference is that the list type members used in the in-game save structure need to have their length determined. The length needs to be determined by adding elements

![](../../images/aa01b96c5f7235e7.png)

## 2. In-Game Save Data Configuration and Save Templates Settings

You can find [Manage In-game Save] in the system menu

![](../../images/7283aa20bf0dde08.png)

### **(1) In-Game Save Edit**

On the left are all created in-game save templates. Creators (Craftspeople) can create multiple templates, but only one template can be used ultimately, which can be enabled by turning on the in-game save switch for the current template.

On the right side is the detailed configuration of this in-game save template. As mentioned earlier, each template contains multiple in-game save data entries. For each in-game save data entry, you can select the required in-game save structure and define its maximum length

![](../../images/d604d93a79f510ce.png)

### (2) Template Comparison Feature

You can use the template comparison feature to compare the differences between two templates. This is typically used for upgrading in-game save templates (upgrade requirements specify that the upgraded template must be purely incremental or identical to the pre-upgrade template, without any deletion or modification of data structures).

To use the comparison feature, you first need to set the in-game save template you want to compare as the comparison template. Right-click and select [Set as Compare Template]

![](../../images/c7aae11c66d67f92.png)

Then click "Compare Template" in the currently used template

![](../../images/bb7aef360634533e.png)

If the current template is not a correct upgrade of the comparison template (the in-game save data structure is identical, and the structure members are incremental), the following prompt will appear

![](../../images/2dfb54ce0b2909e9.png)
