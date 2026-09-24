---
title: Ability Unit Effect
path_id: mhkgc6r6vjba
updated_at: 2025-10-21 19:59:17
category: Appendix
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhkgc6r6vjba
---

## 1. Hitbox

Initiates a Hitbox: Performs one attack against the entity that owns the Hurtbox colliding with the Hitbox

**Hitbox Configuration**

Configure Hitbox settings for this attack

![](../images/dbedaace0b0d5787.png)

|  |  |
| --- | --- |
| **Parameter Name** | **Description** |
| *Reference Position* | When set to Self, selects the entity's Attachment Point and performs an attack — commonly used for attacks initiated by the entity itself. When set to On-Hit Location, this is only meaningful when called from a Projectile's On-Hit Detection component; an attack is performed at the On-Hit Location |
| *Hitbox Shape* | Hitbox shape. Supports Cuboid, Sphere, and Cylinder |
| *Zoom* | Hitbox size (Cuboid: length/width/height; Sphere: radius; Cylinder: radius and height) |
| *Location* | Offset of the Hitbox relative to the Reference Position |
| *Rotate* | Rotation of the Hitbox relative to the Reference Position |

**Target Filter Configuration**

Filter targets hit by the Hitbox; Only Targets that meet the filter conditions are affected by the attack

![](../images/a948e65a70ad9dd3.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Filter Target Faction* | An attack usable only when the Target hit by the Hitbox meets the faction filter conditions.  **Options**  Don't Find Target: Cannot hit any Target  Allied Faction: Hits only entities in friendly factions, excluding the entity's own faction  Hostile Faction: Hits only entities in hostile factions  Self: Hits only self.  Own Faction: Hits entities in the entity's own faction  All: Hits all entities  All Except Self: Hits all entities except self  Allied Faction Self Included: Hits friendly factions and the entity's own faction | **Combat Faction Relationships**  Target Faction Filter uses *Combat Factions*, rather than the entity's [Faction] attribute  In Beyond Mode, factions follow these relationships:  Character->Creation: Hostile  Character->Object: Hostile  Creation->Object: Friendly  Object->Creation: Hostile  Creation->Character: Hostile  Object->Character: Hostile |
| *Entity Type Filter* | An attack usable only when the target hit by the Hitbox matches the selected entity type  **Options**  Object, Character, Creation |  |
| *Attack Layer Filter* | An attack usable only when the Hitbox hits the specified Attack Layer  **Options**  Only On-Hit Hurtbox: Usable only when hitting a Hurtbox  Only On-Hit Scene: Usable only when hitting the Scene  Hit All: Hits Hurtboxes, the Scene, and water and grass surfaces |  |
| *Trigger Type* | **Options**  Trigger Only Once per Lifecycle: Only one entity is affected regardless of how many entities the Hitbox hits. Commonly used for single-target attacks.  Triggers Only Once per entity: Affects all entities hit by the Hitbox |  |

**Attack Parameters**

Attack parameter configuration. Affects Damage and other values for this attack

![](../images/d18cd50aaadfa20a.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Damage Coefficient* | Coefficient used in damage calculation |  |
| *Damage Increment* | The incremental value used in damage calculation |  |
| *Elemental Type* | Includes seven *elements* and elementless type (i.e., *Physical* damage) |  |
| *Elemental Attack Potency* | The *Elemental Attack Potency* applied by this attack |  |
| *Hit Type* | The Hit Type of this attack affects:  - The hit *sound effect*.  - The base hit *visual effect*.  - Smash attacks additionally reduce *Geo* shields and trigger the *Shatter* reaction.  **Options**  None, Default, Slash, Smash, Projectile, Pierce |  |
| *Attack Type* | Attack Type for this attack; can be used as a condition in the *node graph*.  **Options**  None, Melee Attack, Ranged Attack, Default |  |
| *Interrupt Value* | The *Interrupt**Value* of this attack |  |
| *Is It True Damage* | Whether this attack deals True Damage.  True Damage is calculated from Damage Increment and ignores the attacker's ATK and the defender's relevant Defense attributes |  |
| *Damage Variation Curve* | The Damage Variation Curve is a distance-damage multiplier curve used for effects like long-range projectile damage falloff. The multiplier between any two distance nodes is linear  No Variation: Current damage does not use the Damage Variation Curve  Custom Variation Curve: Creators (Craftspeople) can define a custom curve  Preset Falloff Curve: A pre-made falloff curve for bow-and-arrow projectiles; linear falloff starts at 35 meters  Preset Growth Curve: A pre-made damage growth curve for reverse damage-increase attacks |  |
| *Damage Variation Distance Calculation Method* | Determines how distance is computed for the Damage Variation Curve  Distance from Current Position: Applicable to direct-damage falloff, such as some instant-hit ranged weapons  Distance from Creation Position: Applicable to projectile entities with a flight path |  |
| *Additional Shield Break* | Removes the target's *shield* *value* before shield calculations for this attack. |  |
| *Shield Pierce Rate* | The target's shield [DMG Taken Ratio] is reduced by [Shield Pierce Rate] to produce the final [DMG Taken Ratio], with a minimum of 0 |  |

**Aggro Configuration**

![](../images/29556419a816ce0c.png)

Enable this setting when Aggro Type in Stage Settings is set to Custom

**On-Hit Performance**

Configures parameters for effects when this attack hits entities or the Scene

![](../images/440e952b613fd616.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *On-Hit Scene Effects* | Configures effects when the Hitbox hits the Scene. Supports offset, rotation, and scale | Only *Timed Effects* can be used |
| *On-Hit Target Effects* | Configures effects when the Hitbox hits an entity. Supports offset, rotation, and scale | Only *Timed Effects* can be used |
| *Hit Reaction* | Select the type of Hit Performance; it affects *Hit Level*, *Horizontal Impulse*, and *Vertical Impulse* |  |
| *Hit Level* | Hit Performance Level produced when this attack lands, affected by the creation's *Super Armor*. |  |
| *Horizontal Impulse* | Affected by the selected Hit Performance type; can also be customized |  |
| *Vertical Impulse* | Affected by the selected Hit Performance type; can also be customized |  |
| *Knockback Orientation* | Direction in which the target is knocked back  Includes: Line Connecting Attacker and Hit Point; Hitbox On-Hit Orientation; Line Connecting Attacker's Owner and Hit Point; Tangent Line Between Attacker and Hit Point; Hit Orientation Reversed; Attacker's Facing Orientation; Opposite Orientation of the Line Connecting the Attacker and the Hit Point |  |
| *Mute Damage Pop-Up* | When checked, Damage Pop-Ups are not displayed for this attack |  |

**Attack Tags**

Configure tags carried by this attack. Tags have no inherent functionality; but can be used to implement custom logic by obtaining the attack's tags in the node graph

For example:

Here's how to implement instant monster elimination when it is hit by Explosive Barrel damage:

The Explosive Barrel's attack carries the tag "Explosive Barrel Explosion"

Some monsters check in their node graph's [When Attacked] event whether the Attack Tag equals "Explosive Barrel Explosion". If [Yes], immediately [Destroy Self]

Click to add multiple tags

![](../images/9df2a45a5f1cedfc.png)

On the target's node graph, use the [Attack Tag List] parameter to obtain the tags configured here

![](../images/af383723bad94648.png)

## 2. Direct Attack

Launch a direct attack against the specified target

Compared to Hitbox Attacks, Direct Attacks have fewer parameters; the configurations for [Attack Parameters], [Aggro Configuration], [On-Hit Performance], and [Attack Tags] are largely consistent

**Attack Parameters**

Attack parameter configuration is identical to [Hitbox Attack]

![](../images/8b94bd2babcdde7c.png)

**Aggro Configuration**

Same as [Hitbox Attack]

![](../images/0fb45e056f124b4a.png)

**On-Hit Performance**

Compared to [Hitbox Attack], it lacks [On-Hit Scene Effects] related parameters (because direct attacks are aimed at entities and won't hit the scene)

![](../images/5e8407b1bee8e041.png)

**Attack Tags**

Same with the [Hitbox Attack] configuration

![](../images/1a9583abb0dc6973.png)

## 3. VFX Playing

Play a Timed Effect at Self, or at the On-Hit Location.

![](../images/3d8c6e54c614b6d2.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Special Effects Asset* | Select a Timed Effect asset |  |
| *Play VFX asset sound effects?* | Turning it on will play the sound effects associated with the asset simultaneously |  |
| *Create Location* | Options: Self, On-Hit Location  Self: Play the effect at Self  On-Hit Location: Only meaningful when called in a Projectile's On-Hit Detection component; plays the effect at the On-Hit Location |  |
| *Zoom Factor* | Zoom Factor of the special effect when played |  |
| *Offset* | Relative offset of the special effect playback |  |
| *Rotate* | Relative rotation of the special effect playback |  |

## 4. Create Projectiles

Create a projectile entity at Self or at the On-Hit Location

![](../images/9ff400c8d3934c31.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Projectile Asset* | Select a predefined Projectile |  |
| *Create Location* | Options:  Self: Create the Projectile at Self.  On-Hit Location: Only valid when it is called within a Projectile's On-Hit Detection component; creates the Projectile at the On-Hit Location |  |
| *Offset* | Relative offset for the projectile's creation position. |  |
| *Rotate* | Relative rotation for the projectile's creation position. |  |

## 5. Add Unit Status

Add a unit status to entities hit by the Projectile.

![](../images/75464d9fceed7a9c.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Unit Status Asset* | Select a predefined *unit status*. |  |
| *Stacks* | Number of unit status stacks to apply |  |

## 6. Remove Unit Status

Remove the specified unit status from the entity hit by the projectile.

![](../images/9652196038e00fdd.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Unit Status Asset* | Remove the specified *unit status* |  |

## 7. Destroy Self

Destroy Self. Available only for Local Projectiles.

![](../images/0f747c32a1bd9783.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Delay Time* | After this Ability Unit is triggered, destroy self after the specified delay.  Typically used to allow VFX and other time-dependent elements to finish playing |  |

## 8. Recover HP

Restore a specified amount of HP to the target

![](../images/cc5adda048e3bb42.png)

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Description** | **Notes** |
| *Percentage Recovery Base Method* | HP recovery method  Includes Based on Target's Max HP, Based on Target's Current HP, Based on Caster's Max HP, and Based on Caster's ATK |  |
| *Percentage* | Percentage of HP restored based on the selected Percentage Recovery Base Method |  |
| *Additional Fixed Recovery Amount* | The fixed amount of HP restored to the target |  |
| *Ignore Recovery Adjustment* | Whether this recovery is affected by [Recovery Effect Adjustment Rate] and [Healing Effect Adjustment] in *Unit Status*. |  |
| *Healing Tag* | Healing Tag that can be obtained in the Server Node Graph to identify a specific healing instance |  |
