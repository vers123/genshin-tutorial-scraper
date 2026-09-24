---
title: Item Display UI Controls
path_id: mhtzuo0t4e1k
updated_at: 2026-08-03 18:22:49
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhtzuo0t4e1k
---

# I. Item Display Functions

![](../../../images/715aa0a062a84bbc.png)

During stage runtime, clicks or external device inputs can trigger UI control interactions.

Supports player interaction. When selecting "Player's Current Equipment" or "Template Item," send a *When UI Control Group Is Triggered* event to the node graph after the interaction.

# **II. Editing Item Display**

![](../../../images/62bbcdffa90db1aa.png)

*Interactable?*

When enabled, configures the interaction method

*Key Mapping - Keyboard & Mouse*

Provides PC key options to use as input interaction items. The selected key will be displayed below the key in the Edit window

![](../../../images/12809dd2a0a6d8ac.png)

*Key Mapping - Gamepad*

Provides controller button options to use as input interaction items. After selection, they will be displayed below the button in the Edit window

![](../../../images/b7079cb4c01055c7.png)

*Type*

Divided into three types: player's current equipment, template item, and items in inventory

![](../../../images/bcf14e2c4a7b824a.png)

*Player's Current Equipment*

![](../../../images/3292b03bc7576c57.png)

*Equipment Config ID Variable*

Allows selecting variables from the player

*Behavior When Unequipped*

Defines how this UI control behaves when no equipment is equipped

Two display modes are available: show empty slots or hide them

*Slot Cooldown (s)*

![](../../../images/d1668eca9b42a9d2.png)

Allows selecting the player, Players 1–8, or a custom variable from the Stage

*Slot Usage Count*

When enabled, allows configuring whether to hide the control when the count is zero and set the usage count

*Hide When No Usages Left*

When enabled, hides this control when no uses remain

*Usage*

Allows selecting the player, Players 1–8, or a custom floating-point variable from the Stage

![](../../../images/c0a2d1eadbbade93.png)

Template Item

![](../../../images/bc56994d6cd48f06.png)

*Item Config ID Variable*

Allows selecting the player, Players 1–8, or a custom variable from the Stage

*Item Quantity Display*

![](../../../images/31fd1b83f763a792.png)

When enabled, displays the current item quantity below the icon (shown as 00 in the image)

*Hide When Quantity Is Zero*

When enabled, hides the control when the item quantity is zero

*Item Quantity Variable*

Allows selecting the player, Players 1–8, or a custom variable from the Stage

*Slot Cooldown (s)*

Allows selecting the player, Players 1–8, or a custom variable from the Stage

Items in Inventory

![](../../../images/532fc6eb8e5e309d.png)

*Item Config ID Variable*

Allows selecting a custom variable from the player

*Behavior When There Are No Items*

Defines how this control behaves when no items are present

Two display modes are available: show empty slots or hide them

# III. Managing Item Display Through Node Graph

**When UI Control Group Is Triggered**

During stage runtime, when a player interacts with a button UI control group, it triggers the "When UI Control Group Is Triggered" event in the node graph. This event is sent only to the node graph of the *player* who performed the interaction

![](../../../images/b62cc22287575a1f.png)
