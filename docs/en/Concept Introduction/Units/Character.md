---
title: Character
path_id: mhh7pxrmalzy
updated_at: 2025-10-21 19:26:41
category: Concept Introduction/Units
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhh7pxrmalzy
---

Unlike *player entities**,* *character entities* refer to the actual units that players control during the game, such as walking, running, climbing, and flying units with physical presence

# 1. Character Template

In Beyond Mode, players and characters are mapped one-to-one, so the *template configuration* of characters exists as part of the *player template*, which can be accessed under the character editing tab in the player template:

![](../../images/755c3b9eb359604f.png)

Tab Overview:

![](../../images/2af2b601077d6005.png): Basic Information Tab, where the Character section contains only sound effect-related information compared to other entities.

![](../../images/98d8f52d7b58aac8.png) Specialized Configuration Tab, where the Character section contains only combat-related parameters compared to other entities.

![](../../images/8dc3356103e1e158.png): Components tab, where you can add components to character entities or view existing components

![](../../images/45e4577d938bcb14.png): Node graph configuration tab, where you can add node graphs to character entities or view the node graphs that have been added

# II. Overview of Available Components for Character Entities

[Collision Trigger](/ys/ugc/tutorial//detail/mh8w69rzuc3i)

[Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica)

[Global Timer](/ys/ugc/tutorial//detail/mhawd6rl5kpy)

[Unit Status](/ys/ugc/tutorial//detail/mhd7nxrfa8im)

[VFX Playing](/ys/ugc/tutorial//detail/mh4ppo02m1o8)

[Custom Attachment Points](/ys/ugc/tutorial//detail/mhmshmimtegs)

[Collision Trigger Source](/ys/ugc/tutorial//detail/mhn95di01j84)

[Sound Effect Player](/ys/ugc/tutorial//detail/mhwiv89yra02)

[Inventory](/ys/ugc/tutorial//detail/mh5y5001vqd4)

[Loots](/ys/ugc/tutorial//detail/mh63ox06afy8)

[Nameplate](/ys/ugc/tutorial//detail/mh5n160t2b6w)

[Text Bubble](/ys/ugc/tutorial//detail/mhwtz297kp6a)

[Scan Tag](/ys/ugc/tutorial//detail/mhfc0lr1tcke)

[Mini-Map Marker](/ys/ugc/tutorial//detail/mh0pppib5eyc)

Additionally, there are equipment slot components that can only be added to characters

For details, please see [Equipment](/ys/ugc/tutorial//detail/mhg766rur2va)

# III. Runtime Characteristics

During gameplay, characters are dynamically initialized based on template configurations, therefore character entities do not have corresponding *GUID*Notably, when a character's HP reaches zero, the node graph on the character entity can receive both the *Entity Destroyed event* and the *Entity Removed/Destroyed* event. In contrast, when an object is destroyed, the event will be dispatched to the stage entity.During the Co-Op Mode gameplay, if a player actively returns to the lobby, the stage will receive the character's removal event
