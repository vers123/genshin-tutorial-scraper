---
title: Unit Status Effect Pool
path_id: mhklw3rba8we
updated_at: 2026-09-18 15:06:23
category: Appendix
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhklw3rba8we
---

Final Value = (Base Value + Change Value) \* (1 + Adjustment Rate) \* Multiplier + Correction Value

"Change Value" indicates how much the base value changes  
"Adjustment Rate" is the coefficient for additional scaling  
"Multiplier" is the coefficient for overall scaling  
"Correction Value" is the final increment/decrement applied to the value

Note: Some unit states have dynamic variants. For information on modifying unit states dynamically using nodes, please refer to III. Unit Status Execution > 2. Manage with Server Nodes > Usage of Unit Status Parameter Dictionary on the corresponding documentation [Unit Status](/ys/ugc/tutorial//detail/mh6rh59iil2i) page

# I. Base Attributes

|  |  |  |
| --- | --- | --- |
| **Unit Status** | **Indication** | **Effect** |
| Interrupt Intake Multiplier | ![](../images/da53442f5b969012.png) | Influences the multiplier for interrupt value increase when attacked. When this value is 0, it means that taking damage does not increase the interrupt value, indicating that the entity has invincibility (or 'dominant body' status). |
| Fall Efficiency Change Value | ![](../images/1a79c981f5a47ed4.png) | Affects acceleration while falling. By default, all characters or creations have 200% fall efficiency; setting this to -200% allows characters or creations to ignore gravity. |
| Fall DMG Adjustment Rate | ![](../images/fad34fea273b5622.png) | Affects fall damage taken by characters. At -100, characters take no fall damage. |
| Max HP Adjustment Rate | ![](../images/3210e00f384fc63d.png) | Affects the entity's Max HP |
| Max HP Correction Value | ![](../images/186472c5751fd2fc.png) | Affects the entity's Max HP |
| Movement SPD Adjustment Rate | ![](../images/f07223d5147da3ce.png) | Affects the movement speed of characters and creations |
| Attack SPD Adjustment Rate (Not Active) | ![](../images/fa8084358738302c.png) | Affects character attack speed |
| Knockback Efficiency Adjustment Rate | ![](../images/e7d2a90bd1aa55cc.png) | When attacked, this value affects the magnitude of the knockback force, influencing the knockback distance or height. |
| Stamina Consumption Adjustment Rate | ![](../images/e3f654598a3e0407.png) | Adjusts Stamina consumption while running, swimming, and similar actions. A value of -100% removes Stamina cost for these actions |
| Shield Power Adjustment Rate | ![](../images/d97083349da97380.png) | When gaining a Shield, modifies the shield amount by the adjustment rate |
| Stamina Recovery Adjustment Rate | ![](../images/764be5a43d5ae388.png) | Adjusts Stamina recovery efficiency after Stamina is depleted. A value of -100% disables Stamina recovery |

# II. Damage Process

|  |  |  |
| --- | --- | --- |
| **Unit Status** | **Indication** | **Effect** |
| DEF Adjustment Rate | ![](../images/575b1f58a47f9dbf.png) | Affects the entity's DEF |
| DEF Correction Value | ![](../images/b98230e9a669e343.png) | Affects the entity's DEF |
| ATK Adjustment Rate | ![](../images/e68505446fb74c1b.png) | Affects the entity's ATK |
| ATK Correction Value | ![](../images/9ee215527f6572ce.png) | Affects the entity's ATK |
| CRIT Hit Trigger Change Value | ![](../images/70f7e0cb3cf0b5e7.png) | Affects the entity's CRIT Rate |
| Bloom Reaction RES Adjustment Rate | ![](../images/570886a1128d833e.png) | Affects the entity's Bloom Reaction RES |
| CRIT Hit RES Trigger Change Value | ![](../images/ba5311d66e58c0bc.png) | Affects the attacker's CRIT Rate when this entity is hit |
| CRIT DMG Change Value | ![](../images/6f63c7bdd54a402e.png) | Affects the entity's CRIT DMG |
| Attack DMG Boost Adjustment Rate | ![](../images/1aa20f1f0ed1d6ae.png) | Affects the entity's Attack DMG Bonus |
| Damage Reduction Adjustment Rate | ![](../images/0908f76e48036669.png) | Affects the entity's incoming DMG reduction |
| Recovery Effect Adjustment Rate | ![](../images/070812945bd8c431.png) | Affects the healing effect applied by the entity |
| Healing Effect Adjustment Rate | ![](../images/a9b8b0eaeea09217.png) | Affects healing effects received by the entity |
| Elemental DMG Bonus Adjustment Rate | ![](../images/b667a0d0d559477b.png) | Affects elemental damage dealt by the entity, including Physical and the seven elements |
| Elemental RES Adjustment Rate | ![](../images/ef9cab7202bcad54.png) | Affects elemental damage received by the entity, including Physical and the seven elements |
| Elemental Mastery Correction Value | ![](../images/bc3d6154bea1000b.png) | Affects the entity's Elemental Mastery |
| Transformative Reaction DMG Bonus Adjustment Rate | ![](../images/62852cf885123c2a.png) | Affects the damage of transformative reactions dealt by the entity  Includes the following reactions: Swirl, Superconduct, Electro-Charged, Firestarter, Frozen, Overloaded, Shatter, Bloom, Burgeon, Hyperbloom |
| Amplifying Reaction DMG Bonus Adjustment Rate | ![](../images/71e54e008f3a6eef.png) | Affects the damage of amplifying reactions dealt by the entity  Includes the following reactions: Vaporize, Melt |
| DEF Ignore Adjustment Rate | ![](../images/28c76b851aa968f7.png) | Affects the percentage of DEF ignored when entities deal DMG |
| DEF Ignore Correction Value | ![](../images/0c0fa87511373406.png) | The amount of defense ignored when an entity deals damage |
| Elemental DMG Immunity | ![](../images/4337c7b488bddf13.png) | When set to [Yes], grants immunity to damage of a specified element, including Physical and the seven elements |
| Skill Cooldown Efficiency Change Value | ![](../images/e647a5452a9c5310.png) | Affects the cooldown reduction efficiency of a character's skills; the higher this value, the faster skills cool down |
| Catalyze Reaction DMG Bonus Adjustment Rate | ![](../images/6f18afd5d9ae4578.png) | Affects the damage of Catalyze reactions dealt by the entity  Includes the following reactions: Aggravate, Spread |
| Aggro Multiplier Adjustment Rate | ![](../images/8ae035b6e16819f9.png) | Adjustment rate applied when gaining Aggro Value |
| Threat Multiplier Correction Value | ![](../images/ce586049a383cbdd.png) | Modifier applied when gaining Aggro Value |

# III. Special Functions

|  |  |  |
| --- | --- | --- |
| **Unit Status** | **Indication** | **Effect** |
| Creation Invisible | ![](../images/0bd4a149e37ffc7e.png) | When the Boolean local filter returns TRUE, the creation is not visible |
| Always Animate | ![](../images/10ff6f98b3d31838.png) | Animations will be fully calculated and played regardless of whether they are visible or within the camera view.  (By default, animations may stop playing for performance optimization reasons when they are not visible or not in the camera view.) |
| Trigger Skill on Timer | ![](../images/63aa9eecee9771c3.png) | Triggers the skill in the specified slot at regular intervals |
| Adjust Animation Speed | ![](../images/39182946f294d402.png) | Adjusts the animation speed of the specified attribute group |
| Adjust Cooldown | ![](../images/7943ff4c8add0f1f.png) | Adjusts the cooldown of the specified attribute group |
| Add Status to Status Display Area | ![](../images/e9e5ebec675b2083.png) | Select the corresponding Status Area Control to display the unit status information at that control's location. |
| Attack DMG Adjustment | ![](../images/2aeffb4857e181e7.png) | Mounted on the attacker entity, this is used to adjust effects before damage calculation for attacks that are initiated by the entity and meet specific criteria. Note: The three attack conditions (Attack Tag, Attack Type, and Local Filter) operate on an AND logic, meaning all three must be met to pass the check.  Attack Tag List: The tags of the initiated attack must be in the Attack Tag list.  Attack Type: The type of the initiated attack must be of the selected Attack Type.  Boolean Local Filter: A Boolean local filter may be configured here. If left unconfigured, this setting will not take effect.  Override Attack Element Type: Overrides the attack element type. You can choose not to override. If multiple different element overrides exist on the same attacker entity, the order of priority is undefined.  Override Whether It Is Absolute Damage: Overrides absolute damage status. You can choose not to override. If multiple different absolute damage override states exist on the same attacker entity, the order of priority is undefined.  "Extra CRIT" Parameters: For extra DMG bonus adjustment rate, extra CRIT Hit trigger, etc. Use these to modify the effects of the selected DMG instance before damage calculation takes effect. |
| DMG Taken Adjustment | ![](../images/e9f1755a2ddd49a2.png) | Mounted on the target entity, this is used to adjust effects before damage calculation for attacks that are received by the entity and meet specific criteria. Note: The three attack conditions (Attack Tag, Attack Type, and Local Filter) operate on an AND logic, meaning all three must be met to pass the check.  Attack Tag List: The tags of the received attack must be in the Attack Tag list.  Attack Type: The type of the received attack must be of the selected Attack Type.  Boolean Local Filter: A Boolean local filter may be configured here. If left unconfigured, this setting will not take effect.  "Extra CRIT" Parameters: For extra DMG bonus adjustment rate, extra CRIT Hit trigger, etc. Use these to modify the effects of the selected DMG instance before damage calculation takes effect. |
| Click to Release Skill | ![](../images/fecda08dca81b7d3.png) | Additional logic required for using the Always Show Cursor feature on mobile. |
| Control Motion Device Auto Advance | ![](../images/d97dfb22204074c7.png) | When a Unit Status Effect is added to a Control Motion Device, the device will automatically move forward upon activation |
| Control Motion Device's Movement Parameters | ![](../images/70e51c7e8575efcb.png) | When a Unit Status Effect is added to a Control Motion Device, its movement parameters can be increased by the specified value |
| Creation Levitation (Complex Creations Only) | ![](../images/4e5886ac073fc0ab.png) | Places the Complex Creation into an airborne state unaffected by gravity, without altering its animations  In this state, the Creation can execute Aerial Tactics, but cannot execute Ground Tactics. |
| Character Movement Disabled | ![](../images/5a122f0e625cd2c2.png) | Prevents player-controlled characters from moving via movement keys or control sticks |
| Mount Special Effects | ![](../images/293c8b8465ef2773.png) | Mount a looping effect on the entity; configuration is basically the same as for special effects |
| Elemental Effects | ![](../images/e062208403c1c5b9.png) | Applies a specific element to the entity. The element does not decay naturally, but is consumed by Elemental Reactions |
| Special Status: Invincible | ![](../images/bd7cb7e8778e750c.png) | Puts the entity into the Invincible state  While Invincible, the entity cannot take damage; being hit does not trigger the [When Attacked] event |
| Special Status: Cannot be Locked | ![](../images/7d530951319536a6.png) | Puts the entity into a Lock-On Disabled state  While active, auto-locking attacks and skills cannot lock onto this entity |
| Special Status: HP Locked | ![](../images/626c22d96bd6886d.png) | Puts the entity into an HP Locked state  While active, HP cannot decrease; being hit still triggers the [When Attacked] event |
| Special Status: Struggle | ![](../images/d9a64ef9724cc17d.png) | Puts the entity into a Struggle state  While active, the entity cannot act. Players can escape by rapidly tapping the Struggle key  Note: **This state is not available with some creations** |
| Special Status: Cannot recover HP | ![](../images/bf0bfbb4d0b1f834.png) | Puts the entity into a Cannot recover HP state  While active, the entity cannot restore HP |
| Special Status: HP Cannot Drop Below Specified Value | ![](../images/fb9c617ce9cb8407.png) | Puts the entity into a Minimum HP Threshold state  While active, the entity's HP cannot fall below the configured threshold percentage |
| Super Jump | ![](../images/4a96126eed23f8ed.png) | In this state, the character gains enhanced jumping ability  The xz multiplier controls horizontal jump distance; values greater than 1 increase horizontal jump distance  The y multiplier controls upward jump height; values greater than 1 increase vertical jump height |
| Prevent Elemental Attack Application | ![](../images/1a4a20f88ab3019b.png) | In this state, elemental attacks dealt by creations cannot apply elements |
| Immune to Taunt | ![](../images/5c5640242fdda1df.png) | Immune to taunts in Classic and Custom Aggro modes |
| Immobilize | ![](../images/27929ae4dc60fc49.png) | Restricts normal movement of creations; does not affect movement during skills or movement effects caused by skills  During the immobilization period, entities in the combat disengagement phase may be affected, potentially causing disengagement failure or other unstable state blockages. Creators (Craftspeople) are advised to manage movement restrictions by avoiding or monitoring disengagement states. |
| Jump Disabled | ![](../images/9fbc023411eb3ce3.png) | Prevents the character from jumping |
| Creation Silenced | ![](../images/a2e684a8f10abe55.png) | Prevents creations from casting skills  Custom skills for complex creations are not currently available; this feature will be supported in the next version. |
| Sprint Disabled | ![](../images/47a34d105ea0e8a9.png) | Prevents the character from sprinting |
| Disable Gliding | ![](../images/9268abc7252d1623.png) | Prevents the character from gliding |
| Monitor Elemental Reactions | ![](../images/b577dcfe47864441.png) | Set the event's send target and the reaction type to monitor for. When the entity undergoes the specified elemental reaction, it can trigger the node graph event [When Elemental Reaction Event Occurs] on the target entity |
| Shield | ![](../images/e07c4d9ac469b864.png) | Grants a Shield; parameters are referenced from the Shield configuration |
| Disable Climbing | ![](../images/31d930bfd22493fe.png) | Prevents the character from climbing |
| Monitor Movement Rate | ![](../images/a43fae2a8e0fbe45.png) | After adding, the node graph event [When Character Movement SPD Meets Condition] will be triggered when the condition is met. Additionally, the character with the added unit status can have their movement speed and direction obtained through the [Query Character's Current Movement SPD] node. |
| Hide Nameplate | ![](../images/15e1c4e578efec46.png) | Hides this unit's nameplate |
| Disable Struggle Button | ![](../images/3bc724339eb3689e.png) | When the character enters the Struggle state, they cannot escape early using the Struggle button |
| Keep hurtbox active during sprint | ![](../images/c56bb9d7aed65a9b.png) | During sprinting, the hitbox is not disabled. (By default, a character's hitbox is briefly disabled while sprinting) |
| Enable Outline Effect | ![](../images/dde0e291c13d2684.png)  ![](../images/d2f08259065531c1.png) | The edges of the entity will be outlined with the configured color  A Boolean filter can be configured  When the local Boolean filter returns TRUE, the outline will be applied on the entity |
| Hide Entity's Mini-Map Markers | ![](../images/324b78cf97b7626e.png) | Hides the entity's marker on the mini-map |
| Enable Transparency Effect | ![](../images/f97cbec134b71f8c.png)  ![](../images/2597e2c4e24f5fd3.png) | When the boolean local filter returns TRUE, and the mounted entity is obscured, the entity will be displayed with the configured color as if it were penetrating the obstruction |
| Character Hidden | ![](../images/7eb00050d4fcbbd7.png) | Semi-transparent and fully transparent are both states of concealment.  The evaluation result of a Boolean local filter can be understood as: [Whether the character mounted on the role is visible locally].  When both “Mute Effects” and “Mute Audio” are fully checked:  When viewed locally by a character mounted with this state: If the filter evaluates to true, the mounted character becomes semi-transparent with a blur effect; Mute Effects and Mute Audio do not take effect.If the filter evaluates to false, the mounted character is fully hidden.Effect masking takes effect; effects applied via effect components or effect unit states will not activate.Sound masking takes effect; walking/running/action sounds will not play, and sound effects will not activate. Whether to Mute Effects as well: The priority level of this unit’s state toggle is higher than the priority level of the VFX tools in the VFX Tool system |
| Object Invisible | ![](../images/13afbb3a5c932bb4.png) | When the Boolean local filter returns TRUE, the entity is not visible |
| Overwrite Scan Tag Data | ![](../images/77ccbc8e1424cfad.png)  ![](../images/f448ac6da3dc589c.png) | After adding, the character's scan tag component data will take effect according to the set parameters |
| Fix Mini-Map Orientation | ![](../images/897d4b01855d9491.png) | You can choose to set the character's facing direction as the top of the mini-map, or specify a certain angle of rotation to be the top of the mini-map |
