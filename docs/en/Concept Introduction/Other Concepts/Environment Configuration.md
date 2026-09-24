---
title: Environment Configuration
path_id: mh09s594an7u
updated_at: 2026-03-31 15:36:54
category: Concept Introduction/Other Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh09s594an7u
---

# I. Definition of Environment Configuration

Environment Configuration includes a series of environment-related parameters that enrich how elements in the Scene are presented

Environment Configurations must be predefined and applied to each player's client

# II. Editing Environment Configuration

Switch to the Terrain Editing tab to select Environment Configurations on the left.

![](../../images/ffa5a92e93430f93.png)

Click [New Environment] and [Confirm Create] to create a new Environment Configuration

![](../../images/585af49969df5c96.png)

## 1. Environment Configuration

### (1) Effective Target

![](../../images/b5640c7d8ac8a051.png)

You can select which players this environment configuration will apply to

### (2) Background Preset

![](../../images/ad585a1308b502c9.png)

Select a background preset to determine the general visual style of the scene

*Auto switch with time*: When enabled, all elements related to the background will transition dynamically over time. When disabled, these elements remain static at their current fixed values

*Set Time Point*: Defines the specific timepoint where current background settings are saved. Different settings can be saved at different timepoints, allowing for dynamic transitions as the in-game clock advances

*Dynamic Preview*: When "Auto switch with time" is enabled, you can toggle the dynamic preview to observe environmental transitions

![](../../images/735bce58694862f0.png)

*Reference Timepoint List*: Select any saved time point to view its specific background settings

*Weather Configuration*: Select a pre-configured weather configuration to associate with the current timepoint

*Time Elapsed Per Second (min)*: Defines how much in-game time passes for every one second of real-world time during a preview. A value of 24 matches Teyvat time. The configurable range is [0, 60]

*Current Preview Timepoint*: Displays the current timepoint during a preview

*Preview*: Click [Preview] to start the environment clock at the defined [Time Elapsed Per Second]. This allows you to observe dynamic environment transitions over a 24-hour cycle

### (3) Background Settings

![](../../images/b1a67944b628df21.png)

*Background Rotation*: Adjusts the rotation of the background

*Direct Angle*: The incident angle of the primary ambient light source  
*Intensity*: The brightness of the primary ambient light source. The higher the value, the brighter the light becomes

*Blur*: The diffusion of the primary ambient light source. The higher the value, the more blurred the light becomes

*Light Color*: The color of the light received by the environment

*Filter Style*: Adds a filter effect at the camera layer

*Halo Color*: Sets the halo color of the environment

*Halo Intensity*: Sets the halo intensity of the environment. The higher the intensity, the more visible the halo becomes

*Horizon Intensity*: Adjusts the visibility of the horizon. The higher the intensity, the more defined the horizon's silhouette

*Sky Background Color*: Adjusts the sky colors for both upper / lower sunny side sky background color

*Environment Color*: Adjusts the colors for the top / side / ground surfaces of the environment

![](../../images/9784a6d1a4be9792.png)

Supports configurable color parameters. You can use color selector to adjust the color and transparency

![](../../images/ae60f9f1f7f1f91b.png)

![](../../images/f7b42449224308d7.png)

When [Auto Switch with Time] is enabled, you can inspect the specific parameter values associated with the current timepoint

### (4) Environmental Elements

![](../../images/8068fb5cb5612cc4.png)

*Sun*: Enabled by default. Configurable parameters include color, brightness, angle, orbit tile angle, and size

*Moon*:Enabled by default. Configurable parameters include color, brightness, angle, orbit tile angle, size and fullness

*Stars*: When enabled, you can adjust their density and intensity

*Galaxy*: When enabled, you can adjust its intensity and light color

*Clouds*: When enabled, you can set the type of the clouds, including high clouds, mid clouds, low clouds and faint clouds, along with their respective intensity and light color

## 2. Light Source List

![](../../images/09c37b029bf794b9.png)

The light sources bound to this Environment Configuration are activated together with the Configuration.

### (1) Light Source Configuration Entry Point

![](../../images/d620fd54d4d4572f.png)

Click "Add Light Source" > "Open Light Source Manager" to access the Light Source Management Tool

![](../../images/27e1d59f03d00fdd.png)

Click the system menu in the top left corner, then click Manage Light Source] to open the Light Source Management Tool

### (2) Light Source Configuration

![](../../images/bfb865f6a1873982.png)

Light Source Parameter Settings:

*Source File*: Indicates which Environment Configurations reference this light source

*Location, Rotation*: Controls its Location and Rotation in the Scene.

*Light Source Type*: Currently supports Point Light and Spotlight.

*Color*: Sets the color shown on illuminated models

*Radius*: Illumination radius

*Intensity*: Degree of color or brightness change on the illuminated model

*Effective Range*: The light source is loaded only when a character enters this range. Used for performance optimization.

![](../../images/e49fd4e7695f6625.png)

## 3. Weather

![](../../images/1c097b52f7ac2c45.png)

Multiple Weather configurations can be set within a single Environment Configuration and enabled together with it

![](../../images/5f27dd33e2b42e95.png)

*Initially Effective*: Defines whether this configuration is active upon startup

*Weather Type*: Currently only supports fog

*Auto Switch with Time*: When enabled, the weather will change over time. When disabled, the weather will remain locked to the current configuration's fixed values

*Distance Fog Settings*: Based on Camera Location, creates a fog effect that occludes distant models and the skybox.

*High Fog Settings*: Based on Scene height, creates a fog effect that occludes distant models and the skybox.

# III. Environment Time

Stage settings allow you to define the initial timepoint and the time passage speed, both of which can be adjusted via nodes

Environment time is a globally unique runtime value; the server continuously advances this clock regardless of individual player configurations. Visual transitions driven by time will only be visible when the "*Auto Switch with Time*" option is enabled in the environment configuration

Note: The time passage configuration in stage settings dictates the actual time passage speed during gameplay. In contrast, the same configuration in environment configuration is strictly for editor previews and does not affect the passage speed during gameplay

![](../../images/21fad64776a862cd.png)

# IV. Manage Environment Configuration via Node Graphs

![](../../images/90698a837e647ef0.png)

![](../../images/1be13bb0b116883a.png)

![](../../images/c59ac8bd41d3d9fb.png)

![](../../images/e08135337feec6ab.png)
