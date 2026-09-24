---
title: Shield
path_id: mhju4irp8oyu
updated_at: 2025-10-22 02:50:52
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhju4irp8oyu
---

# I. Definition of Shield

A shield is an additional protective layer stacked on top of the unit's base HP which can absorb or block incoming damage

Shields can be added to objects, characters, creations, and other entities

Shield templates must be predefined before they can be applied to units

# II. Editing Shields

In the System menu, click [Shield Management] to open the shield management tool.

![](../../images/07373e81b58c3c66.png)

Click [Add Shield] to create a new shield template

![](../../images/bfcc6bdb18226f78.png)

*Shield Name*: Can be customized, used by creators (Craftspeople) to distinguish between different shield templates

*Configuration ID*: The unique identifier of this shield, which can be used in node graphs

*Elemental Damage Absorption Type*: Default is all; all types of damage will be absorbed.

*Remove when shield points are depleted*: Enabled by default. When disabled, even if the shield value is depleted, the unit status will retain at least 1 stack

*Show UI*: The shield bar will be displayed on the entity's nameplate component

*UI Color*: Shield bar color

*DMG Taken Ratio*: The proportion of damage applied to this shield when taking damage.

*Override Tags:* When adding unit status using nodes, if the key passed in the dictionary matches the overwrite label, the damage ratio should be overwritten with the value from the dictionary.

*Shield Point(s)*: The shield value provided by each stack of the unit status

*Ignore Shield Strength*: When adding shield value, determines whether to ignore the target entity's [Shield Strength Adjustment Rate] attribute

![](../../images/64596665077fad44.png)

*Infinite Absorption*: When enabled, the absorption ratio becomes infinite (i.e., only 1 shield point is deducted each time damage is absorbed)

*Absorption Ratio*: Damage absorbed per shield point

*Calculation Priority:* The priority order in which damage is absorbed when multiple shield unit statuses exist

*Effect applies to each stack*: If multiple unit status layers exist, only the shield value from the earliest layer takes effect.

*Absorb overflow damage*: Reduces unblocked shield damage to zero

*Attack Tags*: If not configured, this represents that the shield applies to all attacks. When configured, the shield only applies to attacks with the specified tags.

# III. Shield Usage

Shields must be added as unit status effects, with only one shield effect allowed per unit status

The shield configuration references the pre-configured shield template defined earlier

![](../../images/6eda5afe62d27d05.png)

# IV. Shield Settlement Mode

## 1. Shield Calculation Process for Single Unit Status

(1) The damage received by the unit is divided into [Shield Absorbed Portion] and [Shield-ignoring Portion] according to the [Damage Distribution Ratio].

(2) The [Shield Absorbed Portion] determines how much damage can be absorbed based on the effective [Shield Value] and [Absorption Ratio]. Any unabsorbed damage becomes [Overflow Damage].

(3) The [Shield-ignoring Portion] from step (1) and the [Overflow Damage] from step (2) above will be summed up as the final HP to be deducted (or absorbed by another shield, or set to zero according to the configuration)

## 2. Shield Settlement Mode

![](../../images/b73b90accd0e21cd.png)

Two types of stage global configuration

*Shared Calculation*: When multiple unit statuses have shields, they will absorb damage according to their settlement priority.

*Individual Calculation*: Damage is calculated separately for shields under each unit status, and the shield that absorbs the most damage is used.

# V. Shield Node Graph

[When Shield is Attacked] The following node graphs will receive this event:

Status Node Graph of the unit that owns the shieldEntity Node GraphPlayer Node Graph (when the target is a character)

![](../../images/eb3f7e27beab22a8.png)
