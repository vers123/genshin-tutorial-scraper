---
title: Light Source
path_id: mh2ygorj0pna
updated_at: 2025-10-21 15:16:03
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2ygorj0pna
---

# I. Light Source Component Functions

The Light Source component allows Creators (Craftspeople) to mount lights on Entities

Light sources provide basic illumination and can also be used to alter the environment's lighting and atmosphere

Multiple light sources can be active within a single Light Source Component at the same time

# II. Editing the Light Source Component

## **1. Adding Light Source** Component

![](../../../images/259f7c141d906709.png)

(1) In the Entity/Prefab Editing interface, open the Component Editing Tab

(2) Click "Add Common Component" below, select "Light Source," then click to add

(3) Click "Advanced Editing" to expand the editing tab

## **2. Light Source** Component Settings

The following parameters can be configured for each light source:

![](../../../images/98ca01f648ce8b10.png)

*Initially Effective*: When enabled, the light source becomes effective when the entity is created

*Light Source ID*: Distinguishes this light source from others on the entity; cannot be edited

*Light Source Name*: Customizable; used for notes

*Light Source Type*: Currently supports Point Light and Spotlight.

*Color*: Sets the color shown on illuminated models

*Radius*: Illumination radius

*Intensity*: Degree of color or brightness change on the illuminated model

*Effective Range*: The light source is loaded only when a character enters this range. Used for performance optimization.

*Effect Range Preview*: When enabled, displays the active range of this light source in the Editing interface

*Attachment Point*: Specifies the Attachment Point the light source follows; defaults to the root node

*Location, Rotation*: Controls its Location and Rotation relative to the Attachment Point

Click [Add Light Source] to add a new light source

![](../../../images/50b21dca9e1eccfd.png)

# III. Node Graph Related

Toggle Entity Light Source

![](../../../images/fd1ba949e3bcb189.png)
