---
title: Client Controls and Client Scripts
path_id: mhvzvl0iai80
updated_at: 2026-09-16 18:08:25
category: Concept Introduction/Advanced Concepts/UI Control Groups Management
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhvzvl0iai80
---

# I. Definitions of Client Controls and Client Scripts

*Server Controls:* Before the Version 7.1 update, all UI Controls were Server Controls and were controlled by Server Node Graphs

*Client Controls:* Client Controls are controlled by Client Scripts rather than Server Node Graphs and must be used together with Client Scripts

*Client Scripts:* Client Scripts provide logic control for Client Controls and must be used together with Client Controls. For details on the APIs available to scripts, see [Local UI Control API Documentation](/ys/ugc/tutorial//detail/mhtakr07vej4)

# II. Accessing Client Controls

## 1. Edit from a Client Control Template

Manage UI Control Groups - UI Control Group Library - Client Control Templates. Click "Add Client Control" to add the required Client Controls and save them as a template

![](../../../images/383e344f6229f23a.png)

## 2. Edit from a Client Control Container

Manage UI Control Groups - Interface Layout - Add UI Control → add and select Client Control Container - Canvas Settings - Go to Edit. You can then add and edit Client Controls on the Container Details page

![](../../../images/5d155a68e5c243e7.png)

# III. Using Client Controls

For Client Controls to display properly on the main screen, they must be placed within a *Client Control Container*, which is itself a Server Control. All *Client Controls* must be created within a *Client Control Container*

At runtime, Client Controls and Client Scripts function properly only when their Client Control Container is active and visible

The following example shows how to create a Client Control that functions properly

## 1. Add a Client Control Container

In Manage UI Control Groups - Interface Layout, click Add UI Control - Client Control Container

![](../../../images/17d17e59d533da93.png)

## 2. Edit the Client Control Container Canvas

Select the Client Control Container and use Canvas Settings to edit the Client Controls it contains

![](../../../images/e621fa2eca9cffd9.png)

Click Go to Edit to open the Client Control Container Details page, where you can edit the Client Controls within the container

![](../../../images/437b61824719a60d.png)

## 3. Create Client Controls

On the Client Control Container Details page, click *Add Control* to add the required Client Controls.

Note that the Client Container Control that a Client Control depends on must be enabled for the Client Control to display properly on the main screen at runtime. If the container is hidden or disabled, the Client Controls within it will not be displayed properly.

![](../../../images/15a2b589329d7ed8.png)

# IV. Related UI Control Assets

## 1. Server Control Assets

![](../../../images/93a00b577ba2e8b9.png)

The *Client Control Container* allows *Client Controls* to display properly while a Wonderland stage is running, but the container itself is a Server Control

For details, see [Local UI Control Vessel](/ys/ugc/tutorial//detail/mhlz2lrly3dq)

## 2. Client Control Assets

Client Controls can only be added through the Canvas Settings of a *Client Control Container* or in a *Client Control Template*

For more information about the APIs referenced below, see [Local UI Control API Documentation](/ys/ugc/tutorial//detail/mhtakr07vej4)

![](../../../images/a624f78f91fad5f5.png)

Container Node

![](../../../images/201f779b3cb1eb96.png)

Primarily serves as an attachment point for other Client Controls

For details, see [Vessel Node UI Control](/ys/ugc/tutorial//detail/mh3qqq9xc102)

API Reference: Search for `ContainerControl` in the API documentation to view the related Script APIs

**Text Box**

![](../../../images/c29a3e9f2fe9cc35.png)

Provides the same basic functionality as the Server Text Box Control, with additional support for Controller Navigation

For details, see [Text Box UI Controls](/ys/ugc/tutorial//detail/mhnltrr3g966)

API Reference: Search for `TextBoxControl` in the API documentation to view the related Script APIs

**Text Window**

![](../../../images/f18404fb3cda9e40.png)

Provides the same functionality as the Text Box Control, with additional support for scrolling

For details, see [Text Window UI Control](/ys/ugc/tutorial//detail/mhv38jig94kk)

API Reference: Search for `TextWindowControl` in the API documentation to view the related Script APIs

**Image**

![](../../../images/cce22b3e30ee9937.png)

Provides the same basic functionality as the Server Image Control, with additional support for masking and Controller Navigation

For details, see [Image UI Controls](/ys/ugc/tutorial//detail/mh2oih9jou22)

API Reference: Search for `ImageControl` in the API documentation to view the related Script APIs

**UI Animation**

![](../../../images/6558c36e7ff1a2cf.png)

Provides the same basic functionality as the Server UI Animation Control, with additional support for Controller Navigation

For details, see [Interface Animation UI Control](/ys/ugc/tutorial//detail/mh2iyk9fa4gy)

API Reference: Search for `UIAnimationControl` in the API documentation to view the related Script APIs

**Fullscreen UI Animation**

![](../../../images/e7eee18aee0e2a9c.png)

Provides the same basic functionality as the Server Fullscreen UI Animation Control, with additional support for Controller Navigation

For details, see [Fullscreen Interface Animation UI Control](/ys/ugc/tutorial//detail/mhbn4i09l5ns)

API Reference: Search for `FullscreenUIAnimationControl` in the API documentation to view the related Script APIs

**Preset Button**

![](../../../images/ca63abc6195070a7.png)

A special Client Interactive Button that supports configurable icons and display text for four statuses

For details, see [Preset Button UI Control](/ys/ugc/tutorial//detail/mhdbkf04v6y8)

API Reference: Search for `PresetButton` in the API documentation to view the related Script APIs

**Key Hint**

![](../../../images/fad1f43d92c53da7.png)

A preconfigured hint control that supports displaying shortcut key prompts for PC, keyboard and mouse, and controller input

For details, see [Key Hint](/ys/ugc/tutorial//detail/mh265urgupye)

API Reference: Search for `UIKeyHintControl` in the API documentation to view the related Script APIs

**Cursor Event Area**

![](../../../images/4a4382487a5577d5.png)

Can be used to detect cursor events

For details, see [Cursor Detection Area UI Control](/ys/ugc/tutorial//detail/mhd4fxr5v6la)

API Reference: Search for `CursorEventArea` in the API documentation to view the related Script APIs

**Grid Scroller**

![](../../../images/7672bf2ecc04b393.png)

Can be used as a scrolling list for Item Inventories, product lists, and similar interfaces

For details, see [Grid View](/ys/ugc/tutorial//detail/mhfkrr0i7gds)

API Reference: Search for `GridScrollerControl` in the API documentation to view the related Script APIs

**Reference Control**

![](../../../images/03e3d0de0ca34654.png)

Can reference other templates and supports previewing them

For details, see [Template Reference UI Control](/ys/ugc/tutorial//detail/mhucb6reudwm)

API Reference: Search for `ReferenceControl` in the API documentation to view the related Script APIs

# V. Related Client Control Functions

## 1. Client-Server Communication Rules

*Sending Signals from Client Scripts to the Server:* Client Scripts send signals to the Server using `ServerSignal:SendSignal()`. Different parameters can be added to the signal using the relevant `ServerSignal` methods*Sending Signals from the Server to Client Scripts via Node Graphs:* Use the Server Node "Send Client Scripted ServerSignal" to send signals to Client Scripts. Client Scripts can listen for Server signals using `script:RegisterServerSignalHandler(signalName: string, callback: fun(signalName: string, signalParams: any[]))`*Signal Latency:* In Co-Op Mode, the minimum latency for signals sent from the Server is 100 ms

## 2. Client Control and Client Container Control Interaction Rules

*Client Control Display:* When the Client Container Control containing a Client Control is visible, the Client Control and its scripts function normally*When Client Controls Are Destroyed:* Client Controls are destroyed when their Client Container Control is hidden or destroyed

## 3. Handling Client Controls After Reconnection

When a player teleports or reconnects after being disconnected, all Client Controls are destroyed and reset to their initial state. To retain the UI displayed before teleporting, Craftspeople must implement the UI restoration logic themselves

## 4. Client Key Event Response Rules

Client key events are passed according to the rendering order of controls. Controls earlier in the hierarchy and sort order have higher response priorityUse `AddKeyEventListener` to handle key event response rules

## 5. Controller Navigation

Controller Navigation events can only be triggered when a control on the current interface has focus (that is, when the Controller Navigation frame is positioned on the corresponding control)If no control on the current interface has focus, Controller Navigation events cannot be triggered or handled properly

### (1) Configuring Controller Navigation for a Container Node

When "IsolateNavigation" is enabled, navigation based on the nearest control cannot cross the Container Node boundary in either direction

![](../../../images/3be1f91a98d30b1d.png)

### (2) Script Configuration

Controls alone cannot provide a complete Controller Navigation configuration. The relevant adaptation logic must also be handled in scriptsThe default focused control for the interface must be specified in a script using `SetControllerFocus` and `GetControllerFocus`

![](../../../images/dac4f1eb655aee88.png)

## 6. Localization

Script-related multilingual configurations can be managed under "Manage Multi-language Text" - Script Text VariablesConfigured TextMap IDs can be retrieved in scripts using `GetText`. See the API documentation for details on this method

![](../../../images/386db64e35e8d641.png)

## 7. Audio

Search for `PlayAudio2D` in the API documentation to view the related audio APIs

## 8. Logs

Logs can be used to view information and errors generated while Client Scripts are running

### (1) Usage

*Start Debugging:* In Logs, select Client Scripts, then confirm your selection*Viewing Debug Information:* If a script error occurs at runtime, double-click the corresponding entry to view the error details

![](../../../images/18b2029321075995.png)

### (2) Local Logs

Issues such as *recursive script calls* at runtime may cause longer stage loading times or freezes and may not be reported in the standard logs. In such cases, check the local log for detailed informationLocal logs are stored in the same location as Client Scripts and use the filename "ErrorLog.txt." (A local log is created only when an error cannot be reported in the standard logs)

# VI. Accessing Client Scripts

Miliastra Sandbox - Client Script Resource Explorer - Client Script Mapping folder

![](../../../images/e4ff101687608588.png)

![](../../../images/e20b599e07a998e2.png)

# VII. Using Client Scripts

Client Scripts can be used to implement most 2D gameplay mechanics and dynamic UI effects

The following example shows how to create a Client Script that runs properly:

## 1. Create Using a Script Mapping

Edit the file path to link a Client Script to a local file. After saving, the Lua script in the linked file can run during playtesting

### (1) Create a Script Mapping

Right-click any Client Script folder - New Script Mapping

![](../../../images/17e308bda01081a1.png)

### (2) Edit the Script Mapping Path

A Script Mapping must be linked to a local file for the script in that file to run properly during playtesting

![](../../../images/840cf2d13f74b38e.png)

### (3) Select a Local File to Link to the Script Mapping

In the folder that opens, select the local file to link to the Script MappingA successfully linked file appears as shown below

![](../../../images/ca59c8df433e22f2.png)

## 2. Create Using a Client Script

The New Client Script option creates a local script file and a Script Mapping at the same time and automatically links them

### (1) Create a Client Script

Right-click any Client Script folder - New Client Script

![](../../../images/62a516b4ca5731b0.png)

### (2) Create a Client Script and Local File

In the folder that opens, enter a name for the local file and save it. A Script Mapping created this way uses the same name as the local fileA successfully created script and linked local file appear as shown below

![](../../../images/2f966e5432230db4.png)

## 3. Link a Script to a Client Control

A script must be linked to a Client Control to function properly

On the Script tab of any Client Control, click Add Script to attach a Client Script to the control*Script Upload Rules:* Only Lua files with mappings created in Miliastra Sandbox are packaged and uploaded. Scripts that exist only as local files without a mapping cannot be uploaded properly at runtime

![](../../../images/bf5bc0d9a515067c.png)

# VIII. Client Script Rules

Client Scripts can access only the Template Indexes of Client Controls. By using a Client Control's Template Index, a Client Script can dynamically create Client Controls at runtime or modify the content of the corresponding controls

All controls other than Client Controls on a Client Container Control canvas and controls in Client Control Templates are Server Controls. The Template Indexes of Server Controls cannot be accessed by Client Scripts

## 1. Accessing Client Controls in Scripts

To access a Client Control, its Control Template Index is required. The following section explains Control Template Indexes and how to use them in scripts

### (1) Access a Client Control Template Index

While editing, click a Client Control to view its Control Template Index IDSearch for `ControlPrefabIndex` in the API documentation to view the APIs related to Control Template Index IDs and use them in scripts*At Runtime:* Client Controls generate runtime IDs that can be used by scripts. Search for `controlId` in the API documentation to view the APIs related to runtime IDs*Note:* For Client Controls saved as templates, only the *parent node* can be dynamically created through the `ClientUIBaseControl` API*Note:* Client Controls placed on the main screen and *child nodes* of Client Controls saved as templates cannot be dynamically created through script APIs

![](../../../images/4adee3988a339e28.png)

### (2) Access a Script Mapping ID

Scripts can use Script Mapping IDs to access other scriptsSearch for `scriptMappingId` in the API documentation to view the APIs related to Script Mapping IDs

![](../../../images/34fbd4ccb304a0b3.png)

## 2. Client Script Variables

In Client Script Resource Explorer, right-click any Client Script and select Edit Script Variables to configure its variables

*Client Control ID:* While editing, enter the Template Index of the corresponding Client Control. At runtime, the script can use this variable to obtain the runtime ID corresponding to that Template Index

![](../../../images/0645d6928967f4f2.png)

#
