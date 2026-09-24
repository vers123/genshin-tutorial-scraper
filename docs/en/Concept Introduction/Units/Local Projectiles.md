---
title: Local Projectiles
path_id: mhqbvvigln6s
updated_at: 2025-10-14 20:50:36
category: Concept Introduction/Units
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqbvvigln6s
---

# 1. Definition of Local Projectiles

Local projectiles are entities that are computed and rendered locally to simulate projectile effects and on-hit effects

# II. Characteristics of Local Projectiles

Local projectiles need to be predefined during editing before they can be referenced and created by skill node graphs. For skill-related information, please refer to [Skills](/ys/ugc/tutorial//detail/mho81frl33im)

During runtime, local projectile entities depend on the *projectile motion device* to determine their runtime rules, and rely on *on-hit detection* to determine their collision trigger rules and effects.

When a local projectile entity runs, it follows the configuration set in its "Life Cycle"

# **III. Editing the** Local Projectile

## 1. Create Local Projectiles

After entering the combat preset tab, you can select the local projectile tab, manage tabs as needed, and create corresponding local projectiles within the tab

![](../../images/57fe0cd6b7470556.png)

Click *"Confirm Create"* to create a new local projectile

![](../../images/f1d4b9a524ca282f.png)

## 2. Naming and Indexing

![](../../images/18e368b5bd8f0407.png)

Each predefined local projectile *name* must be globally unique and a globally unique *prefab ID* will be automatically generated.

## **3. Base Attributes**

The first column is for the Base Attribute

![](../../images/e2abd4c0049447f6.png)

### (1) Basic Settings

The model configuration used by the local projectile during runtime. Selectable models are sourced from the projectile model library provided by the editor.

Supports adjusting the scaling along the X, Y, and Z axes. The zooming values are preserved after switching models

![](../../images/2f5a0c02b0cb959e.png)

### **(2) Combat Parameters**

![](../../images/a164bc96b3611043.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Attribute Settings* | Provides 2 enumeration options, *Inherited from Creator* and *Independent*. Corresponding parameters below will differ based on the option selected  Inherited from Creator by default  Inherited from Creator: HP, ATK, and DEF are identical to the creator's  Independent: Configure HP, ATK, and DEF as needed  Corresponding parameters below will differ based on the option selected |
| *Whether Subsequent Settings Are Influenced by the Creator* | If enabled, certain unit status effects on the creator will be synchronized to the projectile  Only status effects that affect HP, ATK, and DEF will be synchronized |

### **(3) Life Cycle** Settings

![](../../images/a86541ed33f82c9f.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Permanent Duration* | If not enabled, you need to specify the *duration time* |
| *Duration* | The maximum time from initialization to destruction of this local projectile without other influencing factors |
| *X/Z Axis Destruction Distance* | Except for *Ability Units*, this is the highest priority condition for destroying local projectiles during runtime  Local projectiles will self-destruct when exceeding the maximum destruction distance during runtime |
| *Y-Axis Destruction Distance* |

### **(4) End of Life Cycle Behavior** Settings

When a local projectile's life cycle ends, it will execute the configured ability units in order from top to bottom.

The ability units referenced here are those defined within the local projectile's ability unit settings.

![](../../images/734f8962d0af4f63.png)

## **4. Common Components**

The second column is for common components

![](../../images/55a274909cb1b876.png)

![](../../images/8da4f96f41bc107d.png)

### **(1) VFX Playing** Component

For details, please see [VFX Playing](/ys/ugc/tutorial//detail/mh4ppo02m1o8)

### **(2) Projectile Motion Device** Components

For details, please see [Projectile Motion Device](/ys/ugc/tutorial//detail/mhaqt9rgqv4u)

### **(3) On-Hit Detection** Components

For details, please see [On-Hit Detection](/ys/ugc/tutorial//detail/mh2pir0hat1s)

## 5. Ability Units

The third column is for the ability units

![](../../images/76f50498186b87f1.png)

Local projectiles can reference ability units, which require predefined editing. For details, please see [Ability Units](/ys/ugc/tutorial//detail/mh0ucw9e76f6)

![](../../images/be5b8fe0574f7b39.png)

Ability units can be adjusted through "Advanced Editing"

In the *On-Hit Detection component*, predefined ability units can be referenced and executed once hit detection is triggered
