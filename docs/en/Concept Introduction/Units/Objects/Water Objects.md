---
title: Water Objects
path_id: mhg5eo0ktu6w
updated_at: 2026-05-14 13:04:09
category: Concept Introduction/Units/Objects
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhg5eo0ktu6w
---

# I. What Are Water Objects

Water objects are used for water-related scene decoration and gameplay functions.

A water object is a type of **special environmental object** that comes with multiple preset forms and supports free splicing, providing a realistic and interactive water body representation

All water objects have the **water interaction attribute**. Once a character enters the water area, they will automatically switch to the **Swim state**, gaining the corresponding movement method and behavior Logic.

# II. Water Object Editing Entrance

![](../../../images/1e645865ecd2e268.png)

Water objects can be found in the Entity Editing tab under Prefabricated > Dynamic Units > Other. Drag the corresponding object into the scene to use it.

# III. Water Object Types

## 1. Water Body

Standard 3D water body, suitable for creating enclosed or semi-enclosed water scenes such as **rivers, lakes, pools, and channels**

Two shape variants are provided:

| Shape | Description | Applicable Scenarios |
| --- | --- | --- |
| **Cylinder-Shaped Water Body** | Cylinder-shaped, with rounded edges | Wells, circular ponds, fountain bases |
| **Cube-Shaped Water Body** | Cube-shaped, with clean edges | Channels, troughs, square pools, moats |

![](../../../images/a3739695eef9d78f.png)

Both shapes support scaling adjustments, allowing the Craftsperson to freely adjust the depth and width of the water body. Characters who walk in from the side or jump in from above will both trigger the swim state.

![](../../../images/bc83c0444e8aef62.png)

The shallow water and deep water colors can be freely modified using the color picker.

## 2. Circular Water Body

A lightweight **planar water body** designed for small-scale shallow water scenes

It displays as a circular plane **in the editor** for easy placement and alignment. **During gameplay**, it renders water ripple effects when viewed from above, creating a realistic visual feel of puddles and small pools.

> The circular water body is extremely thin, taking up no vertical space, making it naturally suited for ground-level placement.

![](../../../images/9f5ed0fc1f1b9301.png)

**Typical Use Cases:**

Puddles on the streets after rain

Muddy puddles in muddy ground

Shallow water pool in a cave

Small wetland on grassland

## 3. Waterfall

The waterfall consists of 3 **independent components**, allowing Craftspeople to freely stack and combine them to create complete waterfall effects of varying heights and forms.

| Component | Description | Placement Suggestions |
| --- | --- | --- |
| **Top** | The source of the waterfall, featuring water overflowing from the edge | Place at the top of a cliff, platform, or mountain peak |
| **Side** | The vertical flow section of the waterfall; stackable to increase waterfall height | Stack vertically along the cliff face; no limit on quantity |
| **Bottom** | The transition or base impact section of the waterfall, representing the effect of water splashing into the surface below | Place at the waterfall's landing point to blend with the water body below |

![](../../../images/e601745af6d14309.png)

Total Creative Freedom: Craftspeople can manually combine the three component types based on the actual terrain in the scene to form a complete waterfall. Side components support multiple stacking, allowing them to adapt to cliff walls of any height.

![](../../../images/8082e8f51176de5a.png)

Waterfall colors can be modified through preset colors.
