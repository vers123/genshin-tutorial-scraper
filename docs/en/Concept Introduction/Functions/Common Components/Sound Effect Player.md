---
title: Sound Effect Player
path_id: mhbx2pi8x190
updated_at: 2025-10-20 17:05:47
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhbx2pi8x190
---

# I. Sound Effect Player Component Functions

*Sound Effect Player Component* provides the ability for a Unit to play additional sound effects. The component supports two playback methods

1. When configured on the component by default, it plays automatically after the Unit that owns the component is created

2. Playback can be triggered via the Node Graph, but the Unit that plays the sound effect must have the Sound Effect Player component

# II. Editing the Sound Effect Player Component

## 1. Adding Sound Effect Player Component

![](../../../images/9ac3a92bbff010c1.png)

(1) Switch to the Components tab of the entity or prefab

(2) Find or create a Sound Effect Player component

## 2. Adding Sound Effect Player

![](../../../images/49b3678ae74a225e.png)

Click [Advanced Editing] to open the details editing tab

![](../../../images/e00922c72e131d5a.png)

On the details tab of the Sound Effect player group, click [Add Sound Effect] to create a new sound effect configuration

## 3. Configuring Sound Effect Player

![](../../../images/5a528f641db753a8.png)

*ID*: The identification ID of the Sound Effect Player

*Name*: Name of the player

*Sound Effect Assets*: Reference to the specific sound effect asset to play

*Volume*: Controls the playback volume of the sound effect

*Playback Speed*: The playback speed of the sound effect asset

*Loop Playback*: When enabled, the asset will play again after it finishes

*Loop Interval(s)*: Specifies the delay between the end of one playback and the start of the next when looping is enabled

*3D Sound* *Effects*: Determines whether the sound is 3D. When enabled, related configuration options become available

*\*Range Preview*: When enabled, shows the propagation range of the sound effect in the Scene

![](../../../images/dbfa40123d2f57a8.png)

*Range Radius (m)*: Configures the propagation radius of the Sound Effect

*Attachment Point*: Specifies an Attachment Point Location used as the Sound Effect's source

*Attenuation Mode*: When using 3D sound effects, the farther the listener (usually the character) is from the source, the lower the volume becomes. Once the distance exceeds the range, the volume drops to 0. The attenuation mode determines how the volume decreases over distance

*Linear Attenuation*: Volume decreases linearly with the listener's distance from the sound source

*Fast Then Slow*: Attenuates quickly near the source, then more slowly as distance increases

*Slow Then Fast*: Attenuates slowly near the source, then faster as distance increases

*Offset*: Offsets the sound source's location

# III. Using Node Graph to Control Sound Effects

Add Sound Effect Player

![](../../../images/07568a2557b4e165.png)

Adjust Specified Sound Effect Player

![](../../../images/d509e917633428c4.png)

Close Specified Sound Effect Player

![](../../../images/76ebbfe51ff2da2f.png)

Start/Pause Specified Sound Effect Player

![](../../../images/9dc7b32217912cf8.png)

Player Plays One-Shot 2D Sound Effect

![](../../../images/32eb4c04b5aebacb.png)
