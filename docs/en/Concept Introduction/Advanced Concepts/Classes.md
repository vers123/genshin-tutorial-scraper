---
title: Classes
path_id: mhakeo0qiy6w
updated_at: 2026-09-16 17:47:06
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhakeo0qiy6w
---

# I. Definition of Classes

*Class* is a player attribute, but primarily affects the player's character. Class determines the initial attributes and skills of most player entities and character entities

Classes can be used to differentiate between player gameplay roles or categories, such as player abilities, character skills, and development paths

# II. Functions of Classes

The main function of a Class is to coordinate and encapsulate the functionality of multiple modules. Simply put, it packages a complete set of configurations and uniformly modifies them for both players and characters when switching classes. Except for the Class level, other data will only be overwritten once during class switching. Creators (Craftspeople) can still use Node Graphs and other methods to modify player and character data afterward. For example: when Class 1 is active for a player, the Normal Attack is replaced with Skill 1 by default, but you can still use Node Graphs to switch Skill 1 with other skills later

# III. Editing Classes

## 1. Entry Point for Editing

The entry point for editing classes can be found under the Class tab in Combat Preset, as shown in the graph:

![](../../images/ce404302daa0baa2.png)

## 2. Create New Class Templates

![](../../images/80db57c87bc5abb2.png)![](../../images/bbe8bcf1fec2d1e6.png)

Click the "Create Class" button and click Confirm in the pop-up to create a new class template

# IV. Class Parameter Settings

![](../../images/75cb90e99dbd359b.png)

## 1. Basic Settings

![](../../images/a1996556af28a593.png)

*Select Camera*: Choose a camera template. When the player switches to this class, the camera will be replaced with the template set here

*Select Layout*: Select a main screen layout. When the player switches to this class, the main screen layout will be replaced with the template set here

*Scan Tag Recognition Rules*: Rules for filtering active units from all available scannable objects

Distance From Center of FOV: In the screen coordinate system, the closer to the screen center, the higher the priority

*Actual Position Distance*: In the world coordinate system, the closer to the local character's position, the higher the priority

*Allow Jump*: Whether the character of this class can jump

*Allow Sprint*: Whether the character of this class can sprint

*Allow Climb*: Whether the character of this class can climb. Note that when climbing is disabled for this class, the character cannot climb even if the collision of objects is set to climbable

*Allow Glide*: Whether characters of this class can deploy wind gliders and glide in the air

## 2. Level Settings

The class *level* can be considered roughly equivalent to the character's level. When switching classes, the character's level will change accordingly. Class levels have the following characteristics:

Character level synchronizes with class levelDuring a single playthrough, players can switch between multiple classes. The levels of these classes will be recorded. For example: if Player 1's Class 1 is level 5, when switching to Class 2 and then back to Class 1, Class 1 will remain at level 5, and the class experience will be restored to its value before it was switchedThe initial class creation level can be overwritten once on the player template, and this level will be set for the player during stage initialization

![](../../images/7ff1a5993f1c6a3b.png)

The level module defines the level cap for this class, as well as the EXP configuration required for each level up

*Level*: The character's class level when a player first switches to this class during gameplay

*Maximum Level:* The highest level that this class can reach

*Level-up EXP*: Describes the experience required for each level-up in the class. Supports two configuration methods

*Linear Formula*: Provides a fixed formula where EXP needed for a level = current level × constant 1 + constant 2. Constants 1 and 2 are configurable

*List Configuration*: Use a two-dimensional table to precisely define the EXP required for each level, as shown below:

![](../../images/78e0c6bb363c7851.png)

## 3. Basic Battle Attributes

The class attributes will directly affect the corresponding Player's Character

And base Combat Attribute information cannot be configured on the player template

![](../../images/3c7f9fc4fa5883aa.png)

*Base HP*: The default HP value without attribute growth stacking

*Base ATK*: The default ATK without attribute growth stacking

*Base DEF*: The default DEF without attribute growth stacking

*Attribute Growth*: Defines how much attributes increase with level-ups. This currently supports three types:

*No Growth*: Attributes do not increase with level, meaning the attributes remain at their base values regardless of level*Default Growth Curve*: Uses the default growth curve, which can be previewed by viewing the growth curve, but cannot be modified

![](../../images/0dffa497ee9f582e.png)

The growth curve formula is as follows:

Final HP = Base HP × Level HP Multiplier

Final ATK = Base ATK × Level ATK Multiplier

Final DEF = Base DEF × Level DEF Multiplier

*Custom Growth Curve*: The calculation rules for custom growth curves are the same as the default curve, but creators (Craftspeople) can freely configure them through the [Edit Growth Curve] button

*Max Stamina*: The maximum value that this class's stamina can reach

## 4. Aggro Configuration

![](../../images/d6c4e0414b3a053a.png)![](../../images/a9eb0ed14fa3a12b.png)

If "Custom" is selected as the aggro type in stage settings, you can configure the aggro multiplier

## 5. Unit Status

*Unit Status* added by the Class works as follows: when the Player switches to that Class, the configured Unit Status is automatically applied to the corresponding Character. For details about unit status and related configurations, please refer to the [Unit Statuses](/ys/ugc/tutorial//detail/mh6rh59iil2i) documentation

![](../../images/ca01403b6f58db85.png)

## 6. **Interrupt Resistance** Configuration

Characters have three interruption resistance statuses: **Interrupt Resistance Status, Interrupt-Vulnerable Status,** and **Protected Status**, as well as an *Interrupt Threshold* that affects status changes

**Interrupt Resistance Status**

When the Character is not being hit, the character's Interrupt Threshold starts at 0, and they are in an Interrupt Resistance Status

While in the Interrupt Resistance Status, when hit by any Interrupt attack (attacks with Interrupt Value greater than 0) that does not exceed the Interrupt Threshold limit, the character will only show hit reactions without being knocked back or launched. Meanwhile, the current Interrupt Threshold increases by the attack's Interrupt Value (the actual increase is also affected by the Interrupt Resistance multiplier of the unit's current status)

While in the Interrupt Resistance Status, the Interrupt Threshold will decrease according to the Interrupt Intake Decay Rate per second until it reaches 0

**Interrupt-Vulnerable Status**

When the Interrupt Threshold reaches its maximum, the Character enters an Interrupt-Vulnerable Status

In the Interrupt-Vulnerable Status, the Interrupt Threshold remains at its maximum value and will neither increase nor decrease

When hit by an Interrupt attack, the target may be knocked back or launched (depending on the launch force of that attack). The attack that causes the Interrupt Threshold to reach its maximum will also cause a knockback or launch effect

The Interrupt-Vulnerable Status lasts for several seconds, as set in the Interrupt Vulnerability Duration

**Protected Status**

After the Interrupt-Vulnerable Status ends, the Character enters the Protected Status

While in the Protected Status, the Interrupt Threshold remains at 0 and will not increase or decrease

When hit by an Interrupt Attack, you will not be knocked back or launched

The Protected Status lasts for several seconds, as set in the Invincibility duration

After the Protected Status ends, the Character enters the Interrupt-Vulnerable Status, then begins a new cycle of being in the Interrupt Resistance Status

![](../../images/14821f30e582ac4c.png)

*Interrupt Threshold*: Determines how much Interrupt Value Damage can be taken before entering the Interrupt-Vulnerable Status

*Interrupt Intake Decay Rate*: The amount of Interrupt Value that decays per second while in the Interrupt Resistance Status

*Interrupt Vulnerability Duration*: The duration of the Interrupt-Vulnerable Status, after which it enters the Protected Status. Can be 0

*Invincibility Duration*: The duration of the Protected Status, after which it will enter the Interrupt Resistance Status. Can be 0

# V. Class Skills

Class Skills are skills assigned to a Class. When a player switches to that Class, the character's skills are automatically switched to those configured for the Class

![](../../images/673dd93af04cbba7.png)

Note that skills configured in the Class Template are treated as the Class's default skills. After switching Classes, these skills can still be replaced with other skills through Node Graph nodes. However, when the Initialize Character Skill node is used, the character's skills are reset to those configured in the Class Template

Sprint Skill

The Sprint Skill can be customized. By default, it uses the standard sprint from Teyvat. When customized, a Custom Skill can be assigned as the Sprint Skill

Note: On PC, the Sprint Skill can be triggered by both the right mouse button and the Left Shift key. These bindings cannot be changed

Jump Skill

The Jump Skill can be customized. By default, it uses the standard jump from Teyvat. While airborne, the default Jump Skill deploys the Wind Glider. When customized, a Custom Skill can be assigned as the Jump Skill

Notes: 1. If no Custom Air Skill is configured, the character can use the default Jump Skill; 2. The Allow Jump/Glide toggle only affects the default Jump Skill

Air Skill

When the character meets the required airborne conditions, such as being a certain distance above the ground, the skill in the specified slot is forcibly replaced with the configured Air Skill. By default, Air Skills can be used while airborne

# VI. Class Components

To make editing between classes and characters more convenient, components have been added to classes as addable data

![](../../images/485e2ae0038799c2.png)

Components that can be added to the Player Entity: Custom Variable, Unit Status

![](../../images/4a8d5e2590a8dc81.png)

Components that can be added to the Character Entity: Custom Variable, Unit Status, Mini-Map Marker, Nameplate, Custom Attachment Point

# VII. Class Node Graphs

Class Node Graphs are Node Graphs attached to a Class. When switching to this class, the system will automatically apply the pre-configured node graphs to both the player and character, as defined in the template. The editing interface is located under the Node Graph tab:

![](../../images/feb892c90f23570b.png)

Class Node Graphs can be applied to both Players and Characters

# VIII. Using Node Graphs to Modify Classes

Related Event Nodes

![](../../images/b1cbd36cc8bb2c9e.png)

![](../../images/2d0a16981ce0d0c6.png)

Modify Class Experience

![](../../images/26e864960948c9d9.png)

![](../../images/8601ccce7207acdd.png)

Modify Player's Class

![](../../images/fc1763604091388c.png)

Query Class

![](../../images/6f76ddc618d4aff9.png)

![](../../images/ecc5be0ca2be9d5b.png)
