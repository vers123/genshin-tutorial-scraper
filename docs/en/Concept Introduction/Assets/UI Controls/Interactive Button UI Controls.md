---
title: Interactive Button UI Controls
path_id: mhj7wur7lume
updated_at: 2025-11-19 22:18:23
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhj7wur7lume
---

# I. Interactive Button Functions

![](../../../images/88c8c00a8c1ce627.png)

During stage runtime, clicks or external device inputs can trigger UI control interactions.

Supports player interaction. When selecting "Interactive Event," send a *When UI Control Group Is Triggered* event to the node graph after the interaction.

# **II. Editing Interactive Buttons**

![](../../../images/cf56ee8e7cc283be.png)

*Key Mapping - Keyboard & Mouse*

Choose a numeric key for input. The selected key will be displayed below the button in the edit window

![](../../../images/fbc6d91b4ef8b56f.png)

*Key Mapping - Gamepad*

![](../../../images/a74375022dffcfce.png)

*Size*

You can modify the size of the interactive buttons, with the larger ones being 64 x 64 and the smaller ones being 40.96 x 40.96.

![](../../../images/82389c41b02ff79f.png)

*Type*

![](../../../images/9bcd0431a34ffdb7.png)

*Button Skill*

You need to specify a skill. The corresponding icon and function details can be edited in the character skill editor. [Skills](/ys/ugc/tutorial//detail/mho81frl33im)

![](../../../images/a7a3de3f1a4605e8.png)

*Interactive Event*

![](../../../images/d91495c92e2ece3c.png)

Interactive event will send triggers to the node graph

*Skill Icon*

By operating ![](../../../images/26ffc65c95bc000b.png) you can configure the button's display graphics, which will be shown in real-time in the edit window.

![](../../../images/ce7d3d8c92dd21c4.png)

*Button CD*

Once a skill is used, you must wait for its configured cooldown to expire before it can be used again. During this time, the skill button will be grayed out

*Button Usage Limit*

If enabled, activates the configuration and functionality for displaying the usage count.

![](../../../images/7533dc837ebe37be.png)

![](../../../images/5d6400479e8cc8ab.png)

*Hide When No Usages Left*

Enable this to hide the button when the configured custom variable reaches 0

*Usage*

Available only when the usage limit is enabled.Different usage limits can be configured for each player, and these limits can only read the custom variables assigned to that player.The default count you configure will be displayed on the button in the edit window.To adjust the number of uses, modify the player's custom variable in the node graph. When this custom variable changes, the button's displayed usage count updates automatically.

*Use Items*

![](../../../images/98cd3293de0dbe48.png)

*Select Variable*

![](../../../images/d87d0a873ac1041c.png)

You can choose variables associated with the player's own entity

*Behavior when there are no items*

![](../../../images/0480b3f7bed4b1ae.png)

Divided into three types: : Icon Grayed Out, Do not show icon, and Hide button

# III. Managing Interactive Buttons Through Node Graphs

**When UI Control Group Is Triggered**

During stage runtime, when a player interacts with a button UI control group, it triggers the "When UI Control Group Is Triggered" event in the node graph. This event is sent only to the node graph of the *player* who performed the interaction

![](../../../images/b51343ec498b7ed0.png)
