---
title: Image Controls
path_id: mhg1gur8jqrq
updated_at: 2026-09-16 15:16:06
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhg1gur8jqrq
---

# I. Image Features

*Images* can be configured in the UI Layout to display the corresponding images in the UI Layout. They are a type of UI control used to beautify the interface and enrich its visual presentation

During stage runtime, Image Controls can be triggered through Node Graphs

# **II. Editing Images**

![](../../../images/257c0d5f92fdb868.png)

## **1. Add an Image**

In the *UI Control Group Editor window*, add the UI Control Template - Image

![](../../../images/12564c2db7a30806.png)

## 2. Image Settings

![](../../../images/f911a2f7e6a97760.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Image Source* | Enumerate: Supports Static Reference, Dynamic Reference, Item, State, Skill, and Unit Status  The selected option affects the subsequent configuration parameters |

### **(1) When the Image Source is set to Static Reference**

![](../../../images/41de40d4ac1f5c40.png)

*Reference Asset Resource:* Select a preset asset. Some assets support color configuration.

![](../../../images/f74daefe04de2589.png)

*Fill Color:* Image assets are divided into monochrome and full-color types. Colors can be adjusted using the color selector. Monochrome assets generally produce better results when recolored.

*Image Type:* Supports Basic and Stretch types. Some image assets support stretching and can be found through the filter options in the Image Asset Library.

![](../../../images/387df93d734bcd4b.png)

|  |  |  |
| --- | --- | --- |
| Image Attribute | Property | Common Uses |
| *Normal* | When the image is stretched, all four corners deform along with it | Suitable for combining specific shapes or basic patterns |
| *3-panel layout* | When stretched in either the horizontal or vertical direction, the four corners retain their original shape | Surface images for custom-styled buttons, tabs, and similar UI controls |
| *3 × 3 Grid* | When stretched in the horizontal or vertical direction, the four corners retain their original shape | Surfaces for list items in single-choice windows, or for the background images of controls such as tabs and single-choice windows |

### **(2) When the Image Source is set to other types**

![](../../../images/2358647d28cac720.png)

Supports Craftspeople in configuring custom variables for use as identifiers for the corresponding images

### (3) Image Control Color Configuration

All image source types support color configuration.

Note: If it is an Asset Group, the Fill Color option will not be available.

![](../../../images/0460ade104d56ccf.png)

# III. Images in Client Controls

Client Image controls can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `ImageControl` in the API documentation to view the related APIs

## 1. Masking

![](../../../images/80c523f16e6de2d5.png)

### (1) Masking

Client Image controls support flexible mask settings. For example:

Select any image asset and enable masking to define the image shape to retainAdd another image beneath it and drag it below the first image in the hierarchyThe child image will be clipped to the shape of the parent Image control

![](../../../images/9f01adcdab5e3340.png)

### (2) Soft Edge

When enabled, the edges of the image are softened based on the specified parameters

*Soft Mode:* Softens the edges of the image

|  |  |
| --- | --- |
| Option | Function |
| *Pixels* | Softens the image edges based on the X- and Y-axis values  ![](../../../images/f376a141d06c4fea.png) |
| *Percentage* | Softens the image edges based on the percentage of the horizontal and vertical dimensions  ![](../../../images/1c38ae646b6cb815.png) |

### (3) Fill by Progress

Allows an image to be displayed based on a progress value, with the corresponding area of the image shown according to the current progress

*Shape:* Sets the shape of the progress fill*Direction:* Determines the fill direction. The effect varies depending on the selected shape*Start Position:* Determines where the fill begins. The effect varies depending on the selected shape

|  |  |
| --- | --- |
| Option | Function |
| *Horizontal* | *Fill Effect Preview:*  ![](../../../images/87e5724db687ce3e.gif) |
| *Vertical* | *Fill Effect Preview:*  ![](../../../images/28c65e42029938f1.gif) |
| *Radial90* | *Fill Effect Preview:*  ![](../../../images/217552e7b73e53b8.gif) |
| *Radial180* | *Fill Effect Preview:*  ![](../../../images/78db2e043ac12927.gif) |
| *Radial360* | *Fill Effect Preview:*  ![](../../../images/6ad0f2897378000a.gif) |

### (4) Invert Mask Area

When enabled, areas that were originally masked become visible, while areas that were originally visible become masked and hidden

## 2. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation.

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/f0500f7cca9f459c.png)
