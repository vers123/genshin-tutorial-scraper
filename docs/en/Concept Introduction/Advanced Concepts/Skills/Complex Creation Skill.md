---
title: Complex Creation Skill
path_id: mhmhbh9hp07e
updated_at: 2026-04-03 14:57:11
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhmhbh9hp07e
---

# I. Definition of Creation Skills

*Creation Skills* are encapsulations that allow a Creation to execute the predefined behaviors. In the world of Teyvat, actions such as Hilichurls throwing Slimes or rocks are all considered skills.

Skills implement three core functions:

*Calling Creation Animations*: When editing a skill, Artificers can define the Creation animation effects that play after the skill is usedTrigger Client Node Graph: By editing events on the Skill Animation *Node Graph Event Track*, the specified Local Filter can be triggered at specific stages of the animationConfiguration *Skill Status*: During animation playback, specific time windows can be defined to apply persistent logic, such as playing special effects or setting Creation Orientation

# II. Editing Creation Skills

## 1. Entry Point for Editing

The Creation Skill Editor is located under the Skills Tab within the Combat Preset tab

![](../../../images/988a5145c1630423.png)

Click ![](../../../images/8db516a5f74ddc54.png), then select which Creation to create the skill for in the pop-up window. This determines which skill animations are available during editing.

Finally, click [Confirm Create] to complete adding the new skill

![](../../../images/eb9608b734645caa.png)

## 2. Skill Parameters

The skill parameters are configured as shown below:

![](../../../images/c4895a6ee2a7fff2.png)

*Configuration ID*: The unique identifier of the skill. This ID is referenced when modifying the corresponding skill configuration in the node graph

*Skill Type*: Currently divided into two types

*Instant Skill*: Animation editing is not supported. Logic is triggered immediately upon input

*Normal Skill*: The standard skill type

### (1) Basic Settings

![](../../../images/7f8632eb162b72b7.png)

*Model Attribution*: Different Creation models support different skill animations. Switching models clears all current Creation skill configurations

*Skill Notes*: Craftspeople can add custom notes to the skill

### (2) General Configuration

![](../../../images/8c8c79db94302143.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Can Interrupt Other Skills* | When enabled, this skill can interrupt and override other skills while they are being used |
| *Automatically Face Target* | When enabled, the skill automatically faces the target when used |
| *Continue Casting After Defeating the Target* | When disabled, the skill will not be used if the target no longer exists |
| *Cast Skill When Target Is Reachable* | When enabled, the skill is used if the target's location can be reached through normal pathfinding |
| *Cast Skill When Target Is Unreachable* | When enabled, the skill is used if the target's location cannot be reached through normal pathfinding |

# III. Animation Editing for Creation Skills

![](../../../images/b2df207b86aa746d.png)

After completing the general skill configuration, click Animation Editor to continue defining the logic executed after skill usage. Only Normal Skills support animation configuration

![](../../../images/6c080f71e899b830.png)

As shown above, configuration is performed using a timeline divided into an action track and a logic track. When the skill is used, animations on the action track and events on the logic track are triggered sequentially to produce the complete skill effect

### 1. Add Actions

First, add the required *actions*. The entry point is shown at position "1" in the graph above. Click to select from the currently available *Creation Animations*

![](../../../images/b577720e56e969c3.png)

The animation defines the scale of the entire *skill timeline*. The total length of the event track equals the sum of all animation durations. Adding events at the corresponding animation timestamps aligns visuals with logic

### 2. Editing Event Track

The event track is shown at position "2" in the graph above

*Event Track* includes four types:

*Start Event Track*: Triggered immediately when the skill begins to be used

*End Event Track*: Triggered after all skill actions have finished playing

*Node Graph Event Track*: A track that allows events to be added based on animation progress. At a selected animation progress point, a *Local Filter* can be added, as shown below. The Local Filter will be triggered when the animation reaches that point

![](../../../images/1d8ee59f959c17e1.png)

*Status Track*: Used to define non-triggered behaviors, such as continuous special effect playback. The start and end timestamps of the status can be freely configured

![](../../../images/e4fb5ecf63b23093.png)

Note: If multiple [Set Creation Orientation] events on the status track overlap, they will conflict with each other logically, and overlapping events will not be executed. As shown below, the second event will not be executed; only the first and third [Set Creation Orientation] events will be executed

![](../../../images/4196ac0f0eeb6259.png)

### 3. Instant Skills

![](../../../images/06fee887c7704c63.png)

As shown above, all logic for Instant Skills is triggered at the moment of usage, and no animations are played. As a result, Instant Skills cannot add actions and only retain the Start Event Track

# IV. Adding Creation Skills

In the specialized settings for Complex Creations, open Creation Skill Management and click Details Editing to enter the Details Interface

Click "+" under the referenced skills, then select a pre-defined skill from the tab that appears in the lower-left corner to complete the addition

![](../../../images/b9d61b78a2c07f45.png)
