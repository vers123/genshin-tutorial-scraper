---
title: Character Control Skill
path_id: mhr0k3rc940e
updated_at: 2026-07-10 19:00:44
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhr0k3rc940e
---

# I. Definition of Character Control Skills

Character Control Skills are a special category of Character Skills that can only be used in the control state. They are configured similarly to Character Skills, but the Character does not display any skill animation while casting them.

Character Control Skills have the following features:

Custom Slot Duration: When editing a Skill, the Craftsperson can freely define the exact duration of an individual SlotTrigger Client Node Graph: Edit the events on the skill animation's *Node Graph Event Track* to trigger a specified Client Node Graph at a specific moment during the animationCharacter Skill subclass: Character Control Skills are still Character Skills. They are cast by the Character and share the same add/remove methods as Character Skills, and can also use all Node Graph Nodes, Unit Statuses, Skill Slots, and other features compatible with Character Skills.

# II. Editing Character Control Skills

## 1. Entry Point for Editing

The entry point for Character Control Skills is under the Skills tab in the Combat Preset tab

![](../../../images/85cd7147bc5caefc.png)

Click ![](../../../images/d971df92f0be6494.png)to open the Add Character Control Skills panel. From there, you can edit the Skill Name, Affiliated Tab, and Preview Object shown in the Editing interface  
![](../../../images/8db5e8ab61e802c5.png)

Preview Object: Defaults to an empty model. Any Prefab with a Control Motion Component attached can be selected as the Preview Object. This is for preview purposes only and does not affect actual Skill effects. During subsequent editing, you can switch the Preview Object using the [Preview Object] button at the bottom. The Preview Object's display height is automatically adjusted to match the height configured for the Entity Grounding Position in the Component.

Click [Confirm Creation] to finish adding the new Skill

## 2. Skill Parameters

The Parameter Configuration for Character Control Skills is shown in the graph below

![](../../../images/ef7ec01780649534.png)

*Configuration ID*: The unique identifier of the skill, referenced when modifying the corresponding skill configuration in the Node Graph

*Skill Types*: Currently includes three types

*Instant Skill*: Has no Skill Animation Slot and triggers its logic immediately when input is received

*Normal Skills*: Basic skill type

*Hold Skill*: Provides a Hold Slot and can respond with different branches based on how long the Player holds the input

### (1) Basic Settings

![](../../../images/059c31dec51f10d2.png)

*Skill Notes*: Describes the Skill's general purpose during editing

### (2) Numerical Configurations

![](../../../images/1cf57c1d55d61716.png)

Numerical parameters are the same as in Skill editing. For details, please see [Skill](/ys/ugc/tutorial//detail/mho81frl33im)  
![](../../../images/fa72ca04726a778a.png)

\*Skill Attribute Groups: Modify Skill Attribute Group values to dynamically modify some Skill behaviors. Character Control Skills only support adjusting the Cooldown Time Multiplier through the Attribute Groups

### (3) Life Cycle Management

![](../../../images/70063a6e1198f3ad.png)

*Destroy the skill when reaching the usage limit*: When enabled, usage limit can be configured

*Usage Limit*: The maximum number of times this skill can be used during its entire life cycle. When the skill reaches its maximum usage count, it will be automatically removed

### (4) Skill Pre-Aim Settings

![](../../../images/7dd4be42dc7088c9.png)

For Character Control Skills, Instant Skill and Normal Skill types support Skill Pre-Aiming. For details on Pre-Aiming, see [Skill Pre-Aiming](/ys/ugc/tutorial//detail/mhr3pdi50u1g)

## 3. Animation Editing for Character Control Skills

The workflow is the same as Normal Skill editing: After defining the cast conditions and cast logic, click [Animation Editor] to edit the subsequent logic. Note that the configuration approach for Character Control Skills differs slightly from that for Character Skills:

### (1) Normal Skills

Using Normal Skills as an example, this section explains the general configuration method for Character Control Skills. The preview model in the scene can be switched through the [Preview Object] mentioned above

![](../../../images/e6965704141f92a9.png)

#### a. Slot Editing

Unlike Character Skills, Creation Skills, and other Skill types with animation presentations, Character Control Skills are not associated with animations. They contain only one [Control Empty State Animation] slot where a custom duration can be entered

After a custom duration is set, it becomes the time scale for the entire *skill timeline*. Events can then be added at specific time points to synchronize skill logic with timing.

#### b. Editing Event Track

The Event Track is located at position "2" in the graph above. The time tracks for Character Control Skills are divided into three types:  
 *Start Event Track*: A point in time that is triggered immediately when the skill begins to be cast

*End Event Track*: The point in time triggered after all Skill actions finish playing

*Node Graph Event Track*: A track where you can add marks and Events based on Skill time progress. On this track, select a specific progress position and add a *Client Node Graph*, as shown below. When the animation reaches the configured progress, the Local Filter is triggered. The Node Graph timeline for Character Control Skills can also be configured as a Loop Section track. For details, see [Skill](/ys/ugc/tutorial//detail/mho81frl33im) - Skill Timeline Loop Segment Section

\*Character Control Skills only support adding *Client Node Graphs* whose node graph type is [Character Control Skill Node Graph]  
![](../../../images/af8257d88ea4653c.png)

### (2) Instant Skill

![](../../../images/1f24f00910bef7f5.png)

As shown in the graph above, all Instant Skill logic triggers at the moment the Skill is released, so only the Start Event Track is retained

### (3) Hold Skill

Hold Skill logic is similar to that of Character Hold Skills. It includes two Control Empty State Animations: a Hold Empty State Animation and a Hold End Empty Animation. Different logic is executed based on how long the player holds down the Skill button

![](../../../images/9466992ea6a7f855.png)

After entering the duration for each, when the Skill is actually cast:

If the Character keeps holding the input after entering this Skill, the Skill logic configured in the Hold State Empty Animation continues running, up to the duration entered by the Craftsperson

If the character does not maintain the hold input after entering this skill, the Hold State Empty Animation logic will be immediately interrupted, and the system will switch to the corresponding branch based on the *Branch Track* configuration

![](../../../images/6056d93af155a5fd.png)

#### a. Branches

Click the buttons in the graph below to add or remove Branches. Each Branch corresponds to the configuration logic for one End Empty Slot. During actual skill casting, the skill will transition to one of the Branches depending on when the player releases the hold input.

![](../../../images/75f05647cffd9313.png)

Each Branch has its own separate Control Empty State Animation

#### b. Branch Tracks

Branch tracks define specific rules for transitioning to different branches. Click the branch track to open the branch event editing interface on the right side of the screen

![](../../../images/de9bcc4bd1dc9ad0.png)

*Number of Branch Transitions*: The number of branch transition scenarios this skill supports. This configuration will divide the branch track into the corresponding number of segments

*Response*: Enables the Creator (Craftsperson) to configure the specific Branch to which each segment of the Branch Track transitions

On the Branch Track, the Creator (Craftsperson) can fine-tune Branch transition conditions by adjusting the length of each segment. During actual runtime, when the Player stops holding the input, the animation automatically transitions to the Branch configured for the response segment that contains the current Skill progress
