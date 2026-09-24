---
title: VFX Playing
path_id: mh0ix895rnhe
updated_at: 2025-10-20 16:07:15
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0ix895rnhe
---

# 1. Functions of VFX Playing Components

The VFX Playing component contains two parts of functions

1. Effects played through the *node graph* must rely on the VFX playing component. Without this component, effects cannot be played through the node graph

2. Default *looping effects* can be mounted through components, and these effects will be created along with the entity

Multiple effects can be active simultaneously on the VFX Playing Component

# II. Editing VFX Playing Components

## **1. Adding** VFX Playing Components

![](../../../images/de85e0ad3258a3af.png)

(1) Switch to the Components tab of the entity or prefab

(2) Find or add a VFX playing component

The VFX Playing component is a default mounted component for all units (i.e., it is mounted by default when an entity is created). Therefore, for newly created entities or prefabs, you can find the Effect Player component directly in the Components tab

If it doesn't exist, you can add a new VFX playing component through the Add Common Components button

## **2.** Add VFX Play

On the "Details" tab of the VFX Playing component, press [Add Special Effects] to add a new effect configuration

![](../../../images/a66c149da4f26c81.png)

## **3.** Configure VFX Playing

![](../../../images/c91c47ce6706b19e.png)

|  |  |
| --- | --- |
| **Parameter Name** | **Parameter Description** |
| VFX Player ID | The sequence number of the VFX Player |
| VFX Player Name | The name of the VFX Player, which cannot be duplicated on the same entity |
| VFX Asset Type | Choose between *Looping Effects* and *Timed Effects*, which determines which effect asset library to use.  For effect-related assets, see [Special Effects](/ys/ugc/tutorial//detail/mhe1030vx380) |
| Special Effects Asset | You can select Special Effects Asset. After selecting a Special Effects asset, you can preview it in the scene![](../../../images/f474f8e3f1302422.png) |
| Follow Location | Whether to move along with the component owner |
| Follow Rotation | Whether to rotate with the component owner, only takes effect when [Follow Location] is set to [Yes] |
| Attachment Point | The attachment point where the effect plays. You can select either *built-in attachment points* or *additional attachment points* configured on the entity |
| Zoom Factor | Zoom multiplier of the effect |
| Offset | The offset of the VFX's playing position relative to the attachment point |
| Rotation | The rotation of the VFX's playing position relative to the attachment point |
| Local Filter | Refer to Local Filter Node Graph: Used to determine whether a specified effect should play. For the specific distinctions and usage of the two filters, see [Node Graphs](/ys/ugc/tutorial//detail/mhjwjrr5n73i). The local filter will continuously perform checks while the entity with the effect is present in the scene.  Here is an explanation of the basic nodes in the local filter node graph: Get Self EntityOutput parameter: The entity that has the effect group component mounted.Get Target EntityNo output parameter.Get Current CharacterOutput parameter: The local character. |
