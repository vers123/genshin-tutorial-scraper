---
title: Factions
path_id: mhhodorziqra
updated_at: 2026-01-06 21:43:35
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhhodorziqra
---

In order to create competitive gameplay, entities are divided into different groups where players belonging to the same group share the same game objectives. This group is called a *faction*

In team-based competitive games, factions can serve as criteria for settlement objectives or score calculation

![](../../../images/840bc86a82b47469.png)

# I. Global Definition of Factions

Before selecting a faction in *Basic Info*, you need to first define the required factions in the faction tab of the stage settings

![](../../../images/f4a9ed3dacf2ddf0.png)

*Faction Name*: The name given to this faction

*Default Faction Unit*: New players/objects/creations will be categorized into the corresponding default faction

*Players Included*: A list of players representing who initially belong to this faction

*Entities Included*: A list of objects and creations that initially belong to this faction

# II. Faction Relations

Between any two factions, there must exist two types of relationships: *Hostile* and *Friendly*, which can be configured through the *Faction Relations* in the stage settings

Note that faction relations are one-way. Faction 1 may be hostile towards Faction 2, but Faction 2 isn't necessarily hostile towards Faction 1. There could be situations where Faction 2 is friendly towards Faction 1, in which case only entities from Faction 1 can attack Faction 2, while entities from Faction 2 cannot attack Faction 1

For example, as shown in the graph: The initial player faction is hostile towards both the initial object faction and initial creation faction, therefore they can directly attack entities (characters, creations or objects) belonging to these two factions

![](../../../images/7848aa160baade8e.png)

In other systems, faction-related settings work according to the faction relations defined in the stage configuration. For example, the ability unit in the graph below will correctly target enemies from hostile factions

![](../../../images/8aff5f03129077ca.png)

# III. Default Faction Configuration

Each faction can be configured with a *default faction unit*. When an entity of this object type (such as players and objects shown in the image) is created with a default faction (faction value of 0), it will be assigned to the default faction for that entity type

![](../../../images/d18bc1a0d8ce35f5.png)

For example, in the graph above, if no faction is overridden for this Stone Ball prefab when it is created, it will be created with [Initial Object Faction] (because the default faction for objects is Initial Object Faction)

![](../../../images/a5f5e0fd261630ad.png)

# IV. Using Node Graph to Control Player Factions

Entity Faction Change Events

![](../../../images/35fe0aa65c622edb.png)

Modify Entity Faction

![](../../../images/bb149ea2a8cda952.png)

Query Entity Faction

![](../../../images/c7aa2485541331de.png)

# V. Factions in Classic Mode

Compared to Beyond Mode, factions in Classic Mode are subject to certain restrictions:

All players and their characters belong to the **Player Faction** and cannot be modified.

All creations belong to the **Creation Faction** and cannot be modified.

Objects can be configured to belong to the **Player Faction**, **Creation Faction**, **Object Faction 1**, **Object Faction 2**, or **Object Faction 3**.

All entities cannot dynamically change factions, so faction modification-related execution and event nodes cannot be used.

Relationships between factions cannot be modified.

**The relationships between factions in Classic Mode are as follows:**

Rows represent the initiating party, and columns represent the receiving party.

|  | Player Faction | Creation Faction | Object Faction 1 | Object Faction 2 | Object Faction 3 |
| --- | --- | --- | --- | --- | --- |
| **Player Faction** | Friendly | Hostile | Hostile | Hostile | Friendly |
| **Creation Faction** | Hostile | Friendly | Friendly | Friendly | Hostile |
| **Object Faction 1** | Hostile | Hostile | Friendly | Hostile | Friendly |
| **Object Faction 2** | Hostile | Hostile | Hostile | Friendly | Friendly |
| **Object Faction 3** | Friendly | Hostile | Friendly | Hostile | Friendly |

The hostile relationships between the various factions can be represented by the following directed graph.

![](../../../images/e78ccca800a25306.png)

Object Faction 3 is typically used for objects that are friendly to the Player Faction and can assist characters in attacking constructs. Object Faction 1 is used for regular objects. If objects need to be hostile to Object Faction 1, Object Faction 2 is generally used for this purpose.
