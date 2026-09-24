---
title: Shared Creation Mode
path_id: mh541ircljeu
updated_at: 2026-09-20 16:40:29
category: Support Function
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh541ircljeu
---

# I. Function Overview

Shared Creation Mode is a comprehensive real-time multiplayer system that enables multiple Craftspeople to edit different areas of the same Stage simultaneously

# II. Core Mechanics

- A Stage is divided into 64 independently editable Shared Creation Sections, plus one Core Section containing indivisible and core Stage data  
- Each Section has its own ID range (bits 16-21)  
- The current Editing Section can be switched dynamically  
- Supports importing and exporting shared creation files to facilitate task delegation and workflow merging among multiple Craftspeople

# III. Create a Shared Creation Mode Save

## 1. Create Directly with a New Save

![](../images/f4bc908e3a3df98b.png)  
New Save - Select "Save as Shared Creation File" - Confirm Creation

## 2. Create a Shared Creation Save from a Standard Save

![](../images/a05c8eb75a8c559d.png)

![](../images/73ef6b532df8c703.png)  
Stage Settings - Shared Creation Mode - New Shared Creation Mode File - Confirm

This will create a new Shared Creation Mode Save rather than directly converting the current standard save.

# IV. Managing Shared Creation Sections

![](../images/1f8dda62bd307934.png)

## 1. View Shared Creation Sections

![](../images/89cde9536554e72d.png)

Stage Settings - Shared Creation Mode - Left-click a Shared Creation Section

- Category

- Included Assets: number of Entities, Prefabs, and other assets

- Shared Creation Section Name: displayed locally only

- Open File Directory

## 2. Switch the Editing Section

Following the steps above, click the button in the lower-right corner to set the section as the current Editing Section

![](../images/5e4ce82cd24c94f1.png)

Right-click a Shared Creation Section - Switch to Edit

![](../images/20e983c6baa8a721.png)

# V. Change Status

## 1. Status List

### 1. Usage Status

|  |  |  |
| --- | --- | --- |
| Status | Icon | Meaning |
| Used | ![](../images/ef3466563fd5688d.png) | The Shared Creation Section contains file data |
| Unused | ![](../images/17df1564f0289acd.png) | The Shared Creation Section is empty |
| Current Editing Section | ![](../images/f19750ebbe8b1b0e.png) | All newly created content is added to the section currently being edited |

### 2. Ownership Status (Local Only)

|  |  |  |
| --- | --- | --- |
| Status | Icon | Meaning |
| Default | ![](../images/a5d93f8c053b5c3e.png) | Unmarked section content |
| My Section | ![](../images/a741cb9dd212f1bb.png) | Section content edited by you |
| Other Members' Section | ![](../images/ed3ced94166b0976.png) | Section content outside your editing scope |

## 2. Modification Methods

### **1. Single Edit**

Right-click a Shared Creation Section - Change Category to

![](../images/53d687bd886709fd.png)

### **2. Batch Edit**

Click [Multi-Select Mode]

![](../images/8c37eb70ee74230d.png)

Left-click the sections you want to edit (selected sections will be highlighted with a green border). Left-click again to deselect

![](../images/0123b12d0fe80883.png)

Once all desired sections are selected, right-click - Change Category to

![](../images/728818e1a457508e.png)

## 3. Filter Shared Creation Sections

Most content (e.g., Prefabs, UI Control Group Management, and Skill Resource Management) can be filtered to display only specific Shared Creation Sections

![](../images/07e4577bc387422d.png)

![](../images/3dbd8f8aa4b8b4b2.png)

# VI. Import and Export

## 1. Switch Between Standard Mode and Shared Creation Mode

ESC Menu - Manage Asset Import/Export - Upper-right corner - Switch to Shared Creation Mode

The button in the upper-right corner indicates the target mode to switch to, rather than the current active mode. As shown below, if the button displays "Shared Creation Mode," the system is currently in "Standard Mode." Refer to the indicator in the upper-left corner to confirm the current mode.

![](../images/bd5acbfbe1ef75ad.png)

## 2. Export Shared Creation Sections

Stage Settings - Shared Creation Mode - Open File Directory

![](../images/9a8662f7fbb8d004.png)

Click to open the local file explorer where the Stage's Shared Creation Section files are stored. The file structure consists of 1 core file (.gilh) and 64 stage slice files (.gis).

![](../images/8831011388c5d7fa.png)

Select and copy the desired Shared Creation Section file(s) (.gis) to be loaded later

![](../images/d08a9672c167baf6.png)

## 3. Import Shared Creation Sections

ESC Menu - Manage Asset Import/Export - Switch to Shared Creation Mode - Load Shared Creation File

![](../images/a09a6c8bdfebb9c2.png)

Open the local directory designated for loadable Shared Creation Section files, and place the desired section file(s) (.gis) into this folder

![](../images/a1e803081b919eb3.png)

Once loaded, the contents of the Shared Creation Section will become visible (The system will only display sections originating from the same shared creation stage save. Cross-Stage importing between different stage saves is not supported)

![](../images/2d82d2eccb0333d6.png)

Overwrite Save File: Directly replaces all content in the corresponding Shared Creation Section (e.g., if you import Shared Creation Section 7, all existing content in Section 7 will be cleared and replaced with the imported data)

![](../images/5a418bacdecaf468.png)

## 4. Newly Supported Content for Import/Export

**Perimeter Settings (New)**  
Includes  
- Leaderboard  
- Rank System  
- Achievement System  
**Background Music (New)**  
Includes  
- All Background Music Assets  
- Music configuration parameters

# VII. Data Rules

Modifications to Shared Creation Section data take effect only upon saving

Under certain circumstances, due to the dynamic loading of base data, a pop-up notice may indicate that too many content segments were allocated to a Shared Creation Section and have been reassigned to other sections. These underlying data adjustments will have no impact on the save file itself

![](../images/d1270acee9dfaa93.png)
