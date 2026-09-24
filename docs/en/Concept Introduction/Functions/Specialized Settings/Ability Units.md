---
title: Ability Units
path_id: mh90vi0ifubs
updated_at: 2025-10-14 22:14:41
category: Concept Introduction/Functions/Specialized Settings
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh90vi0ifubs
---

# I. Definition of Ability Unit

## 1. What is an Ability Unit

Ability Units are a set of ability data predefined by creators (Craftspeople) during editing, which can be called by multiple other functional modules at runtime, such as *node graphs*, *on-hit detection components*, and *local projectiles*

Includes the following types:

|  |  |
| --- | --- |
| **Type** | **Description** |
| Hitbox Attack | Initiates a hitbox attack based on a specified target or location. When the attack hitbox collides with an entity's *hurtbox*, it launches an attack against that entity |
| Direct Attack | Perform a direct attack on the specified target |
| Play Special Effects | Play a *timed effect* based on a specified target or location |
| Create Local Projectiles | Create a *local projectile* based on a specified target or location |
| Add Unit Statuses | Add *Unit Statuses* to the specified target |
| Remove Unit Status | Remove *Unit Status* from the specified target |
| Destroy Self | *Destroy* self |
| Recover HP | Restore a certain amount of HP for the target |

## 2. How to Use Ability Units

Ability units are a set of pure data that has no functions on their own. Therefore, other systems are needed to call these ability units to achieve their corresponding effects

There are several entry points for ability unit call in the current mode. Note that each entry point has different types of ability units available

|  |  |  |
| --- | --- | --- |
| **Call Type** | **Description** | **Available Ability Unit Types** |
| Server Node Graph Direct Call | Directly initiate an ability unit call from the *server node graph*, and can only use attack-related ability units. | [Hitbox Attack]  [Direct Attack]  [Recover HP] |
| On-Hit Detection Component Hit Event Call | [On-Hit Detection](/ys/ugc/tutorial//detail/mh2pir0hat1s)When hitting an entity or scene, Ability Unit call can be triggered once | [Hitbox Attack]  [Direct Attack]  [Recover HP] |
| Local Projectile Hit Event Call | [When local projectile](/ys/ugc/tutorial//detail/mhciimiw86jg)hits an entity or scene, Ability Unit call can be triggered once | [Hitbox Attack]  [Direct Attack]  [Play Special Effects]  [Create Projectiles]  [Add Unit Status]  [Remove Unit Status]  [Destroy Self]  [Recover HP] |
| Local Projectile Destruction Event Call | [When local projectile](/ys/ugc/tutorial//detail/mhciimiw86jg) is destroyed, Ability Unit call can be triggered once | [Hitbox Attack]  [Direct Attack]  [Play Special Effects]  [Create Projectiles] |

# II. Editing Ability Units

## 1. Entry Point for Ability Units Editing

### (1) Entry Point for Specialized Settings Tab Editing

![](../../../images/138a8d44bb6e2acc.png)

Click "Advanced Editing" to enter the details interface

### (2) Entry Point for Local Projectiles Tab Editing

![](../../../images/cff428a013a3cc97.png)

Click "Advanced Editing" to enter the details interface

## 2. Editing Ability Units

![](../../../images/0896513812759a53.png)

On the ability unit details editor tab, click the "+" icon to add a new ability unit setting

![](../../../images/c1770be8f38c6eca.png)

You can then switch the ability unit type in the Ability Unit Type option

## 3. Ability Unit Effects

See [Ability Unit Effects](/ys/ugc/tutorial//detail/mhrvqvioautg)

## 4. Ability Unit Call

### (1) Server Node Graph Node Call

In the server node graph, you can call three ability units: [Hitbox Attack], [Direct Attack], and [Restore HP]

[Hitbox Attack] and [Direct Attack] are called using the [Initiate Attack] node

![](../../../images/cf0ff0197fd8566f.png)

Call the [Recover HP] behavior by calling the [Recover HP] node

![](../../../images/5e3fb4b5f4792dfb.png)

### (2) Called When On-Hit Detection Component Registers a Hit

The on-hit detection component can be configured with ability units that [Trigger on Hit]

![](../../../images/b3bb0bb7f534a765.png)

Click Details to enter the on-hit detection component details settings interface

![](../../../images/b657b034770469fe.png)

Click "Add Ability Units" to add pre-configured ability units

![](../../../images/ac39437bd790fe29.png)

When on-hit detection is successfully triggered, the configured ability unit will be called immediately

Compared to handling the same logic using the [When On-Hit Detection Is Triggered] event in the server node graph, configuring in [On-Hit Trigger Settings] allows ability units to trigger more quickly locally, reducing the impact of network latency

### (3) Called When Local Projectile Hits

In the [On-Hit Detection] component of local projectiles, you can also configure ability units that [Trigger on Hit]. Since local projectiles don't have node graph configurations, most of the logic for local projectiles needs to be written through hit trigger logic

![](../../../images/0d5cecafb1cf0efb.png)

![](../../../images/5f0c79dfb03dd63d.png)

As shown in the graph below, this is a common ability unit configuration where a local projectile hits, plays VFX, and finally destroys itself

![](../../../images/a3b921bab43f8f13.png)

Configure in order: the three ability units of Direct Attack - Play VFX - Destroy Self

Then configure in the On-Hit Trigger Settings to make the local projectile deal damage, play special effects, and finally make itself disappear upon impact

![](../../../images/0d6fcc60b8258930.png)

### (4) Called When Local Projectile Is Destroyed

In the [Behavior Settings at End of Life Cycle] on the base attributes tab of the local projectile, you can also reference a set of ability units

Typically used for behaviors executed when a local projectile is destroyed, such as initiating an attack upon destruction

![](../../../images/e254bc7bdb711b3e.png)
