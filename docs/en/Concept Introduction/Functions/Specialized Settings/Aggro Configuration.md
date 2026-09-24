---
title: Aggro Configuration
path_id: mhzwpk9o4t4y
updated_at: 2026-08-03 17:20:22
category: Concept Introduction/Functions/Specialized Settings
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhzwpk9o4t4y
---

# I. What is Aggro

*Aggro* is a function used by entities to select targets for their skills. The Aggro system selects a current skill target for creations based on certain rules (depending on the Aggro mode being used)

Generally speaking, creations will prioritize and continuously attack their current *Aggro Target*

# II. Aggro Modes

There are two Aggro modes for stage setting: *Default Aggro Mode* and *Custom Aggro Mode*. As shown in the figure below

![](../../../images/2489027f2397e0f8.png)

## **1. Default Aggro Mode**

Consistent with the creation aggro rules in Classic mode, the aggro target is independent of damage taken, and the aggro target will switch according to rules during combatAggro value is related to attack frequencyThe aggro value of the target decays over timeIf two aggroed targets have similar attack frequencies, they may switch targets periodically

## **2. Custom Aggro Mode**

Creations will generate *aggro values* based on factors such as damage dealt to them by other entities, healing done to allies, etc., and will select their aggroed target based on the ranking of these aggroed values.Supports configuration of aggro-related parametersSupports various operations on aggro values and aggro lists. Supports aggro-related behaviors like *taunt*Allow objects to use aggro functionality

Please note that the functions of these two modes are completely isolated. The parameter configurations and nodes set in the Custom Aggro Mode cannot be used in the Default Aggro Mode

# III. Functions of Custom Aggro Mode

## 1. Basic Concepts of Custom Aggro System

### (1) Aggro Owner and Aggro Target

*Aggro Owners*:

Holds an *Aggro List*, can select entities from the Aggro List as aggroed targets and perform related actions

Creations are Aggro owners by default, and their actions will target Aggroed targets

Objects can also be set as aggro owners, and their behavior logic can be determined based on their aggro list

Characters cannot be aggro owners

*Aggro Targets*:

All characters, objects, and creations from *hostile factions* relative to the aggro owner can become targets of their aggro

### (2) Aggro Value, Aggro List, and Aggro Target

Each Aggro owner maintains an Aggro list, which tracks all entities that have generated Aggro toward it, along with their respective Aggro values

When a battle begins, the Aggro owner sorts its Aggro list, designates the target with the highest Aggro as its primary target, and may switch targets later based on Aggro-transfer rules

For creation-type entities, the primary Aggro target is almost always their skill target, causing them to focus attacks on it

### (3) What Actions Generate Aggro Value

Generally speaking, there are four sources that generate Aggro value

Directly deal Damage to the aggro owner

**Aggro generated = (Actual DMG dealt × Attack's Aggro multiplier × Entity/Class Aggro Multiplier) + Attack's Aggro bonus**

Restore HP to entities currently on the aggro list

**Aggro generated = (Actual healing amount × Healing's Aggro multiplier × Entity/Class Aggro Multiplier) + Healing's Aggro bonus**

Use the aggro value operation nodes in the node graphWhen an aggro owner is not in battle and enters a battle through *FOV detection*, *range detection* or other methods, they will record 1 point of aggro towards the target that triggered the battle

### (4) Example of Custom Aggro Mode

Suppose Player 1's Character deals 10 DMG to a Hilichurl, Player 2's Character deals 20 DMG to the Hilichurl, and Player 3's Character heals Player 1 for 15 HP.

At the same time:

Three characters have 0 aggro value in the Hilichurl's aggro list before dealing damage/healingThe three characters' *class aggro multipliers* are 3.0, 2.0, and 1.0 respectively

Then the Hilichurl's Aggro list will record the following values:

|  |  |
| --- | --- |
| **Aggro Targets** | **Aggro Value** |
| Character 1 | 30（10×3.0） |
| Character 2 | 40（20×2.0） |
| Character 3 | 15（15×1.0） |

Since Character 2 has the highest Aggro value at this time, the Hilichurl will select Character 2 as the Aggro target (which is usually also the Hilichurl's skill target), until Aggro transfer or taunt-related actions occur

## 2. Aggro Transfer

In stage setting, you can set the global *Aggro Transfer Multiplier*

![](../../../images/add4cee3596e7eec.png)

When a target's Aggro value on the Aggro list is **≥ current target's Aggro value × Aggro transfer multiplier**, an *Aggro transfer* occurs, and that target becomes the new focus

In the above example, after executing the aforementioned actions, Character 2 becomes the Hilichurl's Aggro target with an Aggro value of 40

After Character 3 deals 30 DMG, the Aggro list becomes the following:

|  |  |
| --- | --- |
| **Aggro Targets** | **Aggro Value** |
| Character 1 | 30（10×3.0） |
| Character 2 (Current Aggro Target) | 40（20×2.0） |
| Character 3 | 15+30（30×1.0） |

Since Character 3's Aggro value (45 points) exceeds the current target's Aggro value (Character 2, 40 points) × Global Aggro Transfer Multiplier (assumed to be 1.10), the Hilichurl will switch its target to Character 3

## 3. Taunt

Taunt is a specific entity behavior that can be initiated by *Server Node Graph* or *Local Node Graph*

Taunting sets the taunter's aggro on the target's aggro holder to **current aggro target's aggro value × aggro transfer multiplier**. This triggers an aggro transfer, causing the taunted target to set the taunter as their aggro target, which typically results in creation attacking the taunter

Please note:

When the taunter is already the aggroed target, the taunt action will not cause any changes in aggro valueIf the taunted is not in battle, the taunt action will generate 1 point of aggro for the taunter, causing both the taunter and the target to enter the battle

## 4. Battle Entry and Exit

### **(1) Entering Battle**

Certain actions will cause entities to enter the battle state. For creations, entering a battle usually switches them to the battle behavior mode

For characters, they are considered to be in battle when the **character appears in any other entitiy's aggro list** (for example, when a character attacks a creation, it will cause the character to enter the battle)For objects/creations, when the **entity is the aggro owner and its aggro list is not empty**, it is considered to be in battle (for example, when a construct is attacked, the construct itself is considered to be in battle)

Any action that can generate aggro value may trigger battle entry, including:

Entering a battle when detected by creation's range detection or FOV detection (generates 1 point of aggro)Enter a battle by attacking other entitiesRestore health for entities in the aggro listTaunt into a battleForce battle entry by setting aggro value through node graph

### **(2) Leaving Battle**

Some actions can force entities to leave the battle. When creations leave the battle, they will instantly reset to their original positions and exit the battle mode

For any entity, it is considered to have left the battle when it is **not in any other entity's aggro list and its own aggro list (if it has one) is empty**

Certain actions can force battle exit, including:

The entity in the aggro list is not present (e.g., has been destroyed)The creation's pathfinding fails or it moves away from its own tethered areaUsed the [*Clear Aggro List*] node to clear the aggro list

Please note that you cannot leave the battle by setting aggro value to 0 using the [*Set Aggro Value*] related nodes (Aggro value during the battle must be at least 1, cannot be set to 0).

# IV. Aggro System Configuration Entry

## 1. Global Aggro Configuration

![](../../../images/1ea9344c0feb79e9.png)

In the stage settings, you can configure global aggro-related settings, including:

*Aggro Type*: Switch between Custom Aggro Mode or Default Aggro Mode. Note that after switching to Default Aggro Mode, custom Aggro-related features cannot be used

*Aggro Transfer Multiplier*: The Global Aggro Transfer Multiplier, default is 1.2 (meaning Aggro transfer occurs when exceeding 1.2 times the current target's Aggro value). This value cannot be less than or equal to 1

## 2. Aggro Parameter Configuration

### (1) Object Aggro Configuration

![](../../../images/542f547cff746c11.png)

*Aggro Generation Multiplier*: The multiplier at which this object generates aggro through dealing damage and healing actions

*Enable Aggro Record*: When enabled, this object will become an aggro owner and can obtain target entities through the node graph

*Synchronize Aggro Value*: Whether to synchronize the aggro values in this entity's aggro list to the local side (by default, aggro values are not synchronized, only aggro targets are synchronized). This is typically used when displaying aggro values in the UI. This button is only available when [Enable Aggro Record] is turned on

### (2) Class Aggro Configuration

![](../../../images/f8ddf8b5af943434.png)

*Aggro Generation Multiplier*: The multiplier for Aggro generated through attacks and healing actions by characters of this class

### (3) Creation Aggro Configuration

![](../../../images/64cd881a4c74bca0.png)

*Aggro Generation Multiplier*: The multiplier at which this creation generates aggro through dealing damage and healing actions

*Synchronize Aggro Value*: Whether to synchronize the aggro values in this entity's aggro list to the local side (by default, aggro values are not synchronized, only aggro targets are synchronized). This is typically used when displaying aggro values in the UI.

Please note that since aggro values are calculated on the server side, direct access to aggro values from any local side will be inaccurate

# V. Aggro-Related Nodes

## 1. Server Nodes

**Taunt Target**

![](../../../images/9f9526a2206029ef.png)

**Remove Target Entity From Aggro List**

![](../../../images/b5c6b924528fbb8e.png)

**Clear Specified Target's Aggro List**

![](../../../images/3b020c532bc97ff0.png)

**Set the Aggro Value of the Specified Entity**

![](../../../images/7b8e7aeb1339bf7e.png)

**When Aggro Target Changes**

![](../../../images/4fed4c896cf5e157.png)

**When Self Enters Combat**

![](../../../images/e53e75be476ef873.png)

**When Self Leaves Combat**

![](../../../images/da6ad7056b7b97fd.png)

**Query Global Aggro Transfer Multiplier**

![](../../../images/8b0567910e9950fc.png)

**Query the Aggro Multiplier of the Specified Entity**

![](../../../images/1c72624443b83f19.png)

**Query the Aggro Value of the Specified Entity**

![](../../../images/fa2620587affd41d.png)

**Query If Specified Entity Is in Combat**

![](../../../images/255e1bd37c048f64.png)

**Get List of Owners Who Have the Target in Their Aggro List**

![](../../../images/336969b033894c23.png)

**Get List of Owners That Have the Target As Their Aggro Target**

![](../../../images/c7a35e319914536e.png)

**Get the Aggro List of the Specified Entity**

![](../../../images/3a7369730991ef85.png)

**Get the Aggro Target of the Specified Entity**

![](../../../images/6875be4d7367c696.png)

## 2. Client Nodes

**Modify the Aggro Value of the Specified Entity**

![](../../../images/2fb169157c222f3b.png)

**Transfer the Aggro Value of the Specified Entity Proportionally**

![](../../../images/50d6bf67f47ae4ae.png)

**Taunt Target**

![](../../../images/947c5492ff2e85c1.png)

**Remove Target Entity From Aggro List**

![](../../../images/31b1724f86744a32.png)

**Clear the Aggro List of the Specified Entity**

![](../../../images/6eafa274ab386b86.png)

**Set the Aggro Value of the Specified Entity**

![](../../../images/249e0f1556cee47f.png)

**Modify the Aggro Value of the Specified Entity**

![](../../../images/3930728e4f642a5a.png)

**Query If Specified Entity Is in Combat**

![](../../../images/7f4c42675eb00830.png)

**Get the Aggro List of the Specified Entity**

![](../../../images/169b9305a4e90bd2.png)

**Get the Aggro Target of the Specified Entity**

![](../../../images/737f42588e7e15b8.png)
