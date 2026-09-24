---
title: Custom Mini-Map Controls
path_id: mhkd8o0mhb2w
updated_at: 2026-05-15 17:59:46
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhkd8o0mhb2w
---

# 1. Features of Custom Mini-Map

The custom minimap allows Craftspeople to upload custom map images based on stage gameplay, and switch the mini-map displayed for each player via nodes

The map image can be customized to match the actual stage scene (size, orientation, and position)

The custom mini-map supports displaying all markers in the Mini-Map Marker Component

# II. Custom Mini-Map Management

![](../../../images/d4bcee8ce0c0e962.png)![](../../../images/f38d81fd6b7071c9.png)

You can open the mini-map editing panel via "Manage UI Control Groups" - "Inherent Content" - "Mini-Map"

*Initial Visibility*: Determines whether the mini-map is displayed for players applying the current UI layout*Show own field of view*: Determines whether the player applying the current UI layout displays the distance value above the minimap*Initial Map in Effect*: You can select the default active mini-map for the player applying the current UI layout. Note that switching a player's UI layout will not automatically switch the player's corresponding active minimap

# III. Custom Mini-Map Editing

## 1. Add Custom Mini-Map

![](../../../images/3b634152bb0a7857.png)

You can open the custom map editing panel through "Edit Map". Click the "+" button to create a new custom map

## 2. Upload Custom Image

![](../../../images/0890b82a54d58465.png)![](../../../images/53c74d1613197b78.png)

By clicking "Select Map Image", you can open the "Manage Map Image Resources" interface, allowing players to upload and select the images they wish to use

## 3. Mapping Custom Images to Stage Scenes

![](../../../images/f1c8e37129fccae7.png)

Origin Settings:

*Origin Point Coordinates*: The point that fully corresponds between the image and the scene, used to determine the fixed position of the image

Enter the coordinates of the origin point in the image to match the designated preset point in the scene

Orientation Point Settings:

*Orientation Point Coordinates*: The point used to determine the mapping direction between the image and the scene

Enter the coordinates of the orientation point in the image to match the designated preset point in the scene

Once the origin and orientation points are set, the anchoring and rotation mapping between the image and the scene will be established. This ignores the Y-axis, mapping only the scene's XZ-plane to the image's XY-plane

Note that the orientation point only defines the image's forward direction and is not used for scale calculations

*Scene Distance (m) Per 10 Pixels*：

The map scale determines the scaling ratio between the image and the scene. It can be calculated based on the scene size and your custom image dimensions

## 4. Map Display Settings

Mini-Map Zoom Ratio:

An existing setting parameter that determines the default zoom multiplier of the mini-map in the interface layout

![](../../../images/4c127d62e62b0f3f.png)

Main Map Zoom Settings:  
These settings determine the adjustable zoom scale for the map when viewed on the Main Map (M). Values are restricted to a minimum of 0.1 and a maximum of 2, with increments of 0.1

You can preview the results using the Zoom Preview controls below

## 5. Switching the Custom Mini-Map

![](../../../images/d1c24fe1362c30cd.png)

Server Node: Switch Custom Maps

Used to switch the mini-map displayed in the mini-map component of the target player's UI layout and apply its associated settings

Display Map: If Yes, the map will be displayed. if No, no map will be displayed (equivalent to having no map configured)
