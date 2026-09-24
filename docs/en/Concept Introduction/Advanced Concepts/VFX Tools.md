---
title: VFX Tools
path_id: mh78er0n24r4
updated_at: 2026-03-30 18:51:15
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh78er0n24r4
---

# I. What Are VFX Tools?

*VFX Tools* are composite assets consisting of visual effects (VFX) and sound effects (SFX) managed via a timeline. Craftspeople can Play or Mount them the same way as regular special effects

# II. Accessing the VFX Tool Editor

As shown in the image below, navigate to the Combat Preset tab, select VFX Tool and click [New VFX Tool]

![](../../images/620fc6ed2d744058.png)

# III. Basic Concepts of VFX Tools

## 1. Classification of VFX Tools

Similar to standard special effects, VFX Tools are categorized into two types: Timed and Continuous

*Timed VFX Tools* are VFX Tools with a fixed duration. Once the playback reaches the *Duration*, the VFX Tool will automatically destroy itself. Timed VFX Tools can only be triggered via the [Play Timed Effects] node

*Persistent VFX Tools* are VFX Tools with an infinite duration and will not destroy itself. Similar to continuous effects, they can be destroyed in the Node Graph using either the Special Effects Asset Configuration ID or the Special Effect Instance ID. Persistent VFX Tools can only be mounted via the [Mount Looping Effects] node

Note: You must choose the VFX Tool type when you create it. It cannot be changed later

![](../../images/20661b0a754bd955.png)

After creating a Timed VFX Tool, you can enter the editing interface to adjust its duration

![](../../images/4f25aa753b177b2f.png)

## 2. Effect Tracks

A VFX Tool can consist of multiple Effect Tracks. Click [New Track] to add a track to the timeline

You can configure visual effects (VFX) or sound effects (SFX) on any track. At runtime, the system will play these effects at their designated time points along the timeline

![](../../images/6aea4c7ba2e5945b.png)

Click a specific track to modify its properties

![](../../images/83f533980d5ff32d.png)

### **(1) Visibility Settings**

These settings determine whether the effects within a track are visible to each player. If any single condition is not met, all effects within that track will be hidden

|  |  |
| --- | --- |
| Parameters | Description |
| *Visible Faction List* | This parameter checks the faction relations between the effect owner and the local player:  Hostile Faction: The local player can see the effects on this track when they are hostile to the effect owner  Allied Faction: The local player can see the effects on this track when they are friendly to the effect owner  Own Faction: The local player can see the effects on this track when they are in the same faction as the effect owner    By default, all options are selected, so all players can see the effects on this track |
| *Local Filter* | The effect track updates the Local Filter on each player's client at a fixed frequency. When the filter returns "True," the effect is visible; When it returns "False," the effect is hidden |

### **(2) Loop Segment Settings**

|  |  |
| --- | --- |
| Parameters | Description |
| *Enable Loop Segment* | When enabled, this track becomes a loop segment track. You can also create a loop segment track directly through [New Track] |
| *Loop Segment Start Time (s)* | Defines the start position of the loop segment on the timeline |
| *Loop Segment Duration (s)* | Defines the duration from the start position to the end position of the loop segment |
| *Infinite Loop* | When enabled, this loop segment will keep looping until the VFX Tool's Life Cycle ends |
| *Number of Loops* | Specifies the number of times this segement loops. This parameter can be configured when Infinite Loop is disabled |

When a Loop Segment is enabled, a special area will appear on the effect track (marked by a blue box). This represents the loop segment area

![](../../images/3c59a7f2ad3dbf3c.png)

If Infinite Loop is disabled, you must specify the Number of Loops. This segment will repeat on the track for the specified number of times

The image below illustrates a loop repeated 3 times

![](../../images/ea55df2b951da1f4.png)

When Infinite Loop is enabled, this segment will keep looping until the VFX Tool's lifecycle ends

The image below illustrates an Infinite Loop configuration

![](../../images/e47f043a1b4b6e7e.png)

Note: If the duration of a Timed VFX Tool is reached, any active effects within the loop segment will be cut off at the end of the Timed VFX Tool's lifecycle

## 3. Effect (SFX) Blocks

You can place Effect (SFX) Blocks anywhere along an effect track. Each block references a effect asset (sound asset) and configure its duration (Life Cycle) within the track

The effect asset can be either a Timed Effect or a Continuous Effect

### **(1) Life Cycle Settings for Effect (SFX) Block**s

![](../../images/2346286c0e900df6.png)

When Continuous Playback is enabled, the effect will play until it naturally finishes (Timed Effect) or until the VFX Tool is destroyed.

When Continuous Playback is disabled, you must configure the Duration. The effect will be destroyed once the duration is reached. However, if the VFX Tool is destroyed before the duration ends, the effect will be destroyed immediately

After selecting the Effect Asset and clicking [Set to Asset Duration], you can set the effect's duration to the Effect Asset's duration. (Because the effect's actual playback duration can vary somewhat randomly, this setting cannot guarantee that the effect won't be reclaimed earlier before its presentation concludes)

### **(2) Behaviors of Effects on Destroy / on Hide**

Both Regular and Warning Effects can be configured for their behavior when they are Destroyed or Hidden

*Behavior When Destroyed*: Defines the behavior of the effect asset when the VFX Tool is destroyed (for example, when it is removed through the Node Graph or when the VFX Tool's owner is destroyed)

*Behavior When Hidden*: Defines the behavior of the effect asset when the VFX Tool is hidden (for example, when Unit Status - Hidden Character causes all VFX Tools mounted on the owner to be hidden)

![](../../images/a7ab0f15e4258b11.png)

The configurable settings for this option depend on the type of effect asset selected:

**Timed Effects**

![](../../images/532073dd3378f5d2.png)

When "Has Behavior on Destruction" is enabled, the available options for "Behavior When Destroyed" are: Stop Particle Emission and Stop and Clear Effects

*Stop Particle Emission*: Stops particle emission for the current effect, but particles that have already been emitted will continue until the end of their Life Cycle. This is typically used to create a natural fade-out for some effects. Note that this option only affects effect assets containing particles. Otherwise, this option functions the same as Stop and Clear Effects

*Stop and Clear Effects*: Stops particle emission for the current effect and removes all visual presentation. It allows you to instantly remove all visual presentation

When "Has Behavior on Destruction" is disabled, the Timed Effect is not affected when the VFX Tool is destroyed and will continue playing until it completes its configured lifecycle

Special Notes: In all of the cases above where an effect is triggered to be destroyed, the system only attempts to destroy it. If the effect is a Timed Effect and its "Has Behavior on Destruction" is disabled, that Timed Effect cannot be destroyed. As a result, it may continue to play according to its Life Cycle settings even after the VFX Tool is destroyed

![](../../images/c750d5db714ba8a0.png)

The available options for "Behavior When Hidden" are: None and Destroy Effect

*None*: When the VFX Tool is hidden, the effect is not affected

*Destroy Effect*: When the VFX Tool is hidden, the effect is destroyed. When the VFX Tool is visible again, the effect will not resume or restart

**Looping Effects**

![](../../images/49ddd7da3abf6e4e.png)

You must configure a Behavior When Destroyed for looping effects: Stop Particle Emission or Stop and Clear Effects

*Stop Particle Emission*: Stops particle emission for the current effect, but particles that have already been emitted will continue until the end of their Life Cycle. This is typically used to create a natural fade-out for some effects. Note that this option only affects effect assets containing particles. Otherwise, this option functions the same as Stop and Clear Effects

*Stop and Clear Effects*: Stops particle emission for the current effect and removes all visual presentation. It allows you to instantly remove all visual presentation

![](../../images/b158051173b5fb2c.png)

The available options for "Behavior When Hidden" are: None and Sync Hidden Effects

*None*: When the VFX Tool is hidden, the effect is not affected

*Sync Hidden Effects*: When the VFX Tool is hidden, this looping effect is hidden automatically. It will reappear when the VFX Tool is visible again

### **(3) Regular Effect Blocks**

To add a Regular Effect Block, right-click the track and select [Add Event], then choose [VFX Effect]

![](../../images/4c9686788ec37268.png)

The available configuration parameters may vary slightly depending on the specific Effect Asset selected

![](../../images/c21b3dcfed0d2ebf.png)

![](../../images/e5f7b0fb8881139d.png)

|  |  |
| --- | --- |
| Parameters | Description |
| *Effect Asset* | You can select any Regular Effect Asset (Timed Effect / Looping Effect) |
| *Play VFX Default Sound Effect* | When enabled, the effect's built-in default sound effect will play simultaneously when the effect plays. When disabled, the default sound effect will not play |
| *Additional Element Type* | Only available for some effects  Modifies the visual style of the effect to match a specific Elemental Type  ![](../../images/8c072ad6e7b8cc76.png)![](../../images/f35b571ba892870e.png) |
| *Effect Playback Speed* | Only available for some effects  Adjusts the playback speed multiplier for this effect. The default is 1 (plays at its original speed)  Note: Adjusting this value does not affect the playback speed of the effect's default audio |
| *Offset* | A general effect parameter. Adjusts the location offset relative to the VFX Tool's origin |
| *Rotation* | A general effect parameter. Adjusts the rotation offset relative to the VFX Tool's origin |
| *Zoom* | A general effect parameter. Adjusts the scale of the effect relative to the VFX Tool. Only uniform scaling is supported |

### **(4) Warning Effect Blocks**

To add an Warning Effect Block, right-click the track and select [Add Event], then choose [VFX Effect]

![](../../images/6bba878314021207.png)

Warning effects are a category of effects that allow for the free configuration of static parameters. They are available in three shapes: circular, rectangular, and sector.

All warning effects are timed effects, and you can also call them directly as timed effects

**Circular warning effects**

![](../../images/8ee63bb57d819906.png)

![](../../images/63fcbd30f9a494c8.png)

|  |  |
| --- | --- |
| Parameters | Description |
| *Outer Radius (m)* | The outer radius of the circular warning area (when Zoom is set to 1) |
| *Inner Radius (m)* | The inner radius of the circular warning area (when Zoom is set to 1). If set to 0, the effect will expand outward from the center point |
| *Fill Time (s)* | The time required for the effect to expand from the inner radius to the full circular area |
| *Duration* | The amount of time the warning effect remains fully filled after the expansion is complete |
| *Ground Height* | If the distance between the effect and any surface below it is less than this value, the effect will snap onto that surface  If there is no valid surface below the effect within this range, the effect will not be shown |
| *Fill Color* | The color of this warning effect |
| *Offset* | A general effect parameter. Adjusts the location offset relative to the VFX Tool's origin |
| *Rotation* | A general effect parameter. Adjusts the rotation offset relative to the VFX Tool's origin |
| *Zoom* | A general effect parameter. Adjusts the scale of the effect relative to the VFX Tool. Only uniform scaling is supported |

**Rectangular warning effects**

![](../../images/80a2ea0c71acbdb3.png)

![](../../images/6e80dd6c0d08e00b.png)

|  |  |
| --- | --- |
| Parameters | Description |
| *X-Axis Length (m)* | The length of the rectangle along the X-axis (when Rotation is (0,0,0) and Zoom is 1) |
| *Z-Axis Length (m)* | The length of the rectangle along the X-axis (when Rotation is (0,0,0) and Zoom is 1) |
| *Fill Direction* | Linear Fill: Fills alongs the negative Z-axis  Inside Out: Fills outward along the X-axis from the center |
| *Fill Time (s)* | The time required to fill the entire rectangle |
| *Duration* | The amount of time the warning effect remains fully filled after the expansion is complete |
| *Ground Height* | If the distance between the effect and any surface below it is less than this value, the effect will snap onto that surface  If there is no valid surface below the effect within this range, the effect will not be shown |
| *Fill Color* | The color of this warning effect |
| *Offset* | A general effect parameter. Adjusts the location offset relative to the VFX Tool's origin |
| *Rotation* | A general effect parameter. Adjusts the rotation offset relative to the VFX Tool's origin |
| *Zoom* | A general effect parameter. Adjusts the scale of the effect relative to the VFX Tool. Only uniform scaling is supported |

**Sector warning effects**

![](../../images/e31a64d0a2d12a03.png)

![](../../images/ef5138c553f30eaa.png)

|  |  |
| --- | --- |
| **Parameters** | **Description** |
| *Outer Radius (m)* | The outer radius of the sector (when Zoom is 1) |
| *Inner Radius (m)* | The inner radius of the sector (when Zoom is 1) |
| *Sector Angle* | The angle of the sector |
| *Fill Direction* | Clockwise: Fills in a clockwise sweep. The sweep starts from the negative X-axis and ends at a position determined by the sector angle  Counterclockwise: Fills in a counterclockwise sweep. The sweep starts at a position determined by the sector angle and ends at the negative X-axis  Inside Out: Fills outward from the inner radius to the outer radius |
| *Fill Time (s)* | The time required to fill the entire sector |
| *Duration* | The amount of time the warning effect remains fully filled after the expansion is complete |
| *Ground Height* | If the distance between the effect and any surface below it is less than this value, the effect will snap onto that surface  If there is no valid surface below the effect within this range, the effect will not be shown |
| *Fill Color* | The color of this warning effect |
| *Offset* | A general effect parameter. Adjusts the location offset relative to the VFX Tool's origin |
| *Rotation* | A general effect parameter. Adjusts the rotation offset relative to the VFX Tool's origin |
| *Zoom* | A general effect parameter. Adjusts the scale of the effect relative to the VFX Tool. Only uniform scaling is supported |

### **(5) SFX Blocks**

To add an audio block, right-click the track and select [Add Event], then choose [SFX]

![](../../images/94d8785da976094f.png)

![](../../images/d0f5b1e446451d92.png)

|  |  |
| --- | --- |
| Parameters | Description |
| *Sound Effect Asset* | References a sound effect asset |
| *Volume* | Adjusts the playback volume of this sound effect |
| *Playback Speed* | Adjusts the playback speed of the sound effect |
| *Loop Playback* | When enabled, after the sound effect finishes playing, it will restart from the beginning after the loop interval |
| *Loop Interval (s)* | The interval between two loop cycles |
| *3D Sound Effect* | When enabled, this sound effect is a 3D sound effect based on the VFX Tool's origin |
| *Range Radius (m)* | The radius within which this sound effect can be heard |
| *Attenuation Mode* | Determines how the sound effect attenuates over distance |
| *Offset* | A general effect parameter. Adjusts the location offset relative to the VFX Tool's origin |

# III. How to Use VFX Tools

VFX Tools are used in exactly the same way as regular effects. You can play a VFX Tool anywhere that supports regular effects

Take the [Play Timed Effects] node as an example:

![](../../images/ef1b5ba6f22afa38.png)

In the effect asset selection box, you can enter the configuration ID of the VFX Tool

![](../../images/43199f3bdc60fe4b.png)

Or use the search box to find a configured Timed VFX Tool

![](../../images/d0b694feb493025a.png)

When the effect asset is a VFX Tool, the [Play Timed Effects] node supports the following features:

|  |  |
| --- | --- |
| **Parameters** | **Description** |
| *Effect Asset* | Select a VFX Tool |
| *Target Entity* | The owner entity of the VFX Tool |
| *Attachment Point Name* | The attachment point used by the VFX Tool. Its origin will be placed at the corresponding attachment point position |
| *Move With the Target* | Determines whether all effects within the VFX Tool follow the target's motion |
| *Rotate With the Target* | Determines whether all effects within the VFX Tool follow the target's rotation |
| *Location Offset* | The offset of the VFX Tool's origin relative to the attachment point |
| *Rotation Offset* | The rotation of the VFX Tool relative to the attachment point |
| *Zoom Ration* | Applied together with the zoom rotation in the VFX Tool |
| *Play Built-In Sound Effect* | When set to Yes, each effect in the VFX Tool uses its own [Play VFX Default Sound Effect] setting to determine whether to play its default sound effect  When set to No, no effects in the VFX Tool will play their default sound effects |
