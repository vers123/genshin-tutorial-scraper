---
title: Model
path_id: mhqmzpipf2d0
updated_at: 2026-07-10 16:00:29
category: Concept Introduction/Functions/Basic Information
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhqmzpipf2d0
---

Indicates the features included in the unit model, including *preset status*, *unit attachment points* and *decorations*

For different models, their included functionalities also vary

# I. Preset Status

*Preset Status* is a unique attribute of objects, with each preset status representing a set of animation states for the object

Only some objects have preset status attributes

## 1. About Preset Status

### (1) Preset Status ID

*The preset status ID* represents a set of status definitions, such as the "Open - Close" state of a chest, "Lit - Extinguished" state of a torch, etc., and has the following characteristics:

All sub-states under each status ID are mutually exclusiveSub-states under each status ID can be switched between each other

### (2) Preset Status Value

Sub-states within each group of predefined states are referenced by *Status Values*. As shown in the graph, "0" represents the closed status of the floor spike trap, while "1" represents the open status of the floor spike trap

Each status value represents a specific animation state

When switching to different status values, the animation behavior will change, and some status value transitions will have corresponding animation transition effects

![](../../../images/ced416506127efd4.png)

![](../../../images/bcefe8ef8f3518be.png)

## 2. Node Graph Control Preset Status

When Preset Status Changes

![](../../../images/6e6cf26c4f53e986.png)

Set Preset Status

![](../../../images/f1972aa36eb99ed8.png)

Get Preset Status

![](../../../images/5fe5674f1eda4385.png)

# II. Unit Attachment Points

*Unit attachment points* are specific positions designated on the skeleton or structure of an *entity*, used for attaching other *units* or *special effects*.

## 1. View Default Attachment Points

You can view the preset *default attachment points*, including their names and positions, in the basic information bar of *prefab* or entities

![](../../../images/5686e0c70af9cc8a.png)

Each entity comes with a default basic attachment point: *center origin*, and the position of this attachment point is equivalent to the entity's location in the scene

Additionally, creation-type and character-type entities will have corresponding default attachment points based on their skeletal structure. The characteristic of such attachment points is that they move along with the skeletal position when the entity's bones move: for example, a character's hand attachment point can be used as the creation point for *local projectiles* in shooting actions

## 2. Adding Additional Attachment Points

Please refer to [Custom Attachment Points](/ys/ugc/tutorial//detail/mhmshmimtegs)

# III. Decorations

## 1. Concept of Decorations

### (1) Function of Decorations

Based on the creator's (Craftsperson's) needs, static object models can be attached to prefabs or entities to achieve more customized effects

### (2) Decoration Feature Definitions

a. Decorations are part of the basic information of prefabs (including objects and creations), and can also be used to modify entities in entity placement scenes

b. Decoration's configuration will not increase or decrease the number of prefabs or entities

## 2. Editing Decorations

### (1) Editing Interface Location

The entry point for "Decorations Editing" can be found under the "Model" section in the basic information of prefabs (or entities).

Under this section, you will see the main model, unit attachment points, and the decorations list editing interface.

Click "Decoration Editor" to open the decoration list.

![](../../../images/023552389cc45a79.png)

Click to select model assets to open the model asset library

![](../../../images/755656d7831f7e11.png)

Click on the model you want to add in the model asset library to add a decoration

![](../../../images/5c2efa8349a47e5d.png)

### (2) Decoration Attributes

a. Model

![](../../../images/a55f225d1086d2ad.png)

Select the model for this decoration

b. Transform

![](../../../images/6c2fffd68c0adef1.png)

Set which attachment point on the main model this decoration will follow, and configure additional position, rotation and zooming settings.

c. Native Collision

![](../../../images/75d4bc6230a2b0ef.png)

Set the collision toggle and whether it can be climbed.

# IV. Color and Material

*Color and materials* can be layered onto or replace the base color and material of a prefab or entity.

![](../../../images/94775f80599f9071.png)

## 1. Custom Color

Custom Color lets you layer a new color over a Component or Entity's original color, or replace the original color entirely.

![](../../../images/0fbe1cadddc11ca0.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Enable Custom Color* | **On:** Use a custom color to replace or overlay the object's original color. **Off:** Use the object's original color. |
| *Override Decoration Color* | **On:** Apply the main object's configured color to all attached decorations. **Off:** Decorations use their own original colors or any custom colors applied to them. |
| *Color* | Select a color using the color selector or by entering a color code. You can also adjust the opacity of the current custom color.  ![](../../../images/59a4fff4911ddb54.png) |
| *Node Graph Color Code* | The decimal value of the currently selected color, which can be referenced in the node graph. |
| *Color Blend Mode* | Choose between **Override** and **Multiply**.  ![](../../../images/bfeefb0863f2cc98.png)  *Override:* The custom color completely replaces the Entity's or object's original color.  *Multiply:* The custom color is blended with the original color. |

## 2. Custom Material

![](../../../images/117904a71738e59f.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Enable Custom Material* | **On:** Apply a custom material over the object's original material. **Off:** Use the object's original material. |
| *Override Decoration Material* | **On:** Replace the custom materials of all attached Decorations with the material configured for the main object. **Off:** Decorations use their own custom materials. |
| *Fill Material* | You can choose between **Ice** and **Stone** Material.  ![](../../../images/a9ded863a7bb9a92.png)  *Ice Material:* Gives the prefab or entity a frozen appearance.  ![](../../../images/9618c19ffb0e714a.png)  *Stone Material:* Gives the prefab or entity a petrified, stone-like appearance.  ![](../../../images/de23aa43ee0ecbf0.png) |
