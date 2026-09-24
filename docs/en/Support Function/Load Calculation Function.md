---
title: Load Calculation Function
path_id: mh2dk89mo6iq
updated_at: 2025-10-21 21:13:36
category: Support Function
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2dk89mo6iq
---

# I. What is Load Calculation Function?

During Stage editing, this function performs real-time evaluation of the environment. It calculates the complexity of Scene Layout and the number and density of Entities, then provides risk warnings by area.

After a Stage runs, the system generates a Load report. It records the Stage's Static Units Layout and Node Graph activity, then compiles the data into a summary report with risk warnings for Creators (Craftspeople).

# II. Stage Load Level

The Stage Load setting feature provides Creators (Craftspeople) with auxiliary detection for monitoring Stage Load.

![](../images/96c234031084c616.png)

Open the *Stage Settings* in the system menu. Under **Basic Configuration — Load Settings**, you can adjust the minimum Load requirement needed for the Stage to run properly.

![](../images/3f34b68caafb466f.png)

The higher the Load requirement level, the higher the Load metric limit. During Stage editing, the warning threshold for Load detection also increases accordingly.

Based on the configured Stage Load requirements and the actual editing state, the final Load requirement will be displayed in the Details Interface after deployment. Players will also receive Load-related prompts before gameplay.

# III. Load Calculation Function Overview

Provides both Static and Dynamic Load calculation methods.

*Static Load Calculation*

Provides recommended Load limits during Static editing and estimates the current Load of the Stage being edited.

If the limit is exceeded, a warning is issued, as this may result in stutters, frame drops, or even crashes during Stage runtime.

If performance is within the limit, the current editing status is good and the playtest is expected to go smoothly. However, this method cannot evaluate Load costs from dynamic runtime logics like node graphs, so runtime issues, such as stutters, cannot be fully prevented

*Dynamic Load Calculation*

Creators (Craftspeople) can manually startLoad recording, which will capture Load data during Stage runtime in a playtest.

During Stage runtime, each Player's Load is monitored. When a Player's Stage Load reaches its peak, a screenshot is taken. After the playtest ends, a report is compiled and provided to the Creator (Craftsperson).

*Client Server-related Load Metrics*

Related to the devices used by Players when running a Stage, the current client server upper limit is based on standard PC hardware specifications

Please check **Stage Settings — Player Count Configuration**

Local memory — Others mainly include memory consumption required for the **max number** of players

*Server-related Metrics Load*

Please check **Stage Settings — Player Count Configuration**

The Server deploys Load based on the configured minimum player count. For example, if the server Load N is deployed for 1 Player, then the Stage's deployed Load will be the minimum player count x N

![](../images/ed6b8680c8d306cc.png)

# IV. Static Load Calculation

The menu bar provides a Static Load option. Click to view the current Global Load calculation.

To help Creators (Craftspeople) locate places where Load exceeds limits, the Stage is divided into Areas. Each Area provides its own Load calculation to support targeted adjustments.

## 1. Static Load Calculation — Global

Summarizes Load calculations across all Areas in the current Stage being edited. All Static Load metrics are consolidated here

![](../images/4cffd8c41671d9d4.png)

|  |  |
| --- | --- |
| Parameter | Description |
| *\*Icon* | ![](../images/9189fdc26f97467a.png)If any metric exceeds the recommended value, a warning will be issued |
| *\*Global Resource Ratio* | The highest Load calculation result across all areas in the current Stage, compared to the total available Load.  Displays the percentage of total Assets used |
| *\*Static Calculation Load* | A notification will appear if theLoad calculation exceeds the limit in any Area of the current Stage |
| *\*Static Memory Load* | A notification will appear if theLoad calculation exceeds the limit in any Area of the current Stage |
| *\*Save File Size* | Estimates the storage space required when uploading the current Stage after saving.  If it exceeds the limit, **Creators (Craftspeople) will be prevented from uploading** |

## 2. Static Load Calculation — Area

Click **View Load Status** to expand the details interface

### (1) Regional Load Overview

When considering player gameplay, with the player's location as the center, the surrounding environment and entities within a certain range will occupy a certainLoad.Therefore, inLoad calculation, Load is calculated and displayed by Area, making results easier to understand.

*\*Show Only Overloaded Areas*: Checked by default. When enabled, only Areas with high Load usage are displayed; otherwise, all Areas are shown.

Areas are displayed in ascending order by Area ID.

![](../images/607b24c76788b7b1.png)

*\*Indicator on the Right Side of the Area*: Represents the current Area's Load usage status

|  |  |
| --- | --- |
| Parameter | Description |
| ![](../images/294b693e0f399b2a.png) | The current Area's Static Load has exceeded the limit. Adjustment recommended |
| ![](../images/68494085eaafc811.png) | The current Area's Static Load is approaching its upper limit. |

### (2) Area Load Details

The content of each Stage is calculated independently within each included Area, without interference between them.

The total Load calculation for each Area consists of *Static Memory Load* and *Static Calculation Load*.

**Specified area's** *Static Memory Load*

Clicking a specific Area expands its Load calculation details. In Scene editing, overlaps between the calculation Area and the Scene are displayed

Scenes and Entities within an Area consume that Area's memory Load

![](../images/5eca3c3d13875c55.png)

Stage Load calculation Areas are evenly distributed across the entire Scene. This ensures that calculations exist for different height ranges.

![](../images/b75123c3251135e1.png)

**Orientation-specific** *Static**Calculation Load*

When Players are in different Areas but face the same Location, they can see or interact with the same Stage content. This means multiple Areas may include the same Stage content in Load calculations. The orientation data refines the Load calculation range, helping Creators (Craftspeople) optimize adjustments

As shown in the example below, you might wonder why the empty white area also has a highLoadcalculation

This happens because the actual calculation distance is greater than the illustrated range. Load calculations begin from the center Location and extend in the specified direction to the visible detection range. The graph only shows the starting point and Orientation range

Therefore, the high Load calculation shown in the graph is due to too many enemies placed along the negative Z-axis

![](../images/501896973081f982.png)

![](../images/396c938c29ae1c64.png)

As shown in the graph, two Areas with different Orientations both recorded Load for the same Stage content, demonstrating that each Area's Load calculation is independent

![](../images/51ed183cdb7a5418.png)

By selecting a specific Orientation, you can view Load calculation details for that Orientation. All included Entities and their respective Load values are listed

|  |  |  |
| --- | --- | --- |
| Parameter | Description | |
| *\*Location* | The central Location used for Load calculation within each Area | |
| *\*Orientation* | Starting from the central Location, the Load calculation values are displayed within an 80m range detected in the specified Orientation.  In Scene editing, the corresponding Orientation range is also displayed. | |
| FOV Cone — Red  Represents Static Calculation Load exceeding the recommended value | ![](../images/4c2d2818a89b8fff.png) |
| FOV Cone — Yellow  Represents Static Calculation Load, approaching the recommended value | ![](../images/6ab2475a5106c876.png) |
| FOV Cone — White  Represents Static Calculation Load, below the recommended value | ![](../images/f21391a0a33c46e2.png) |
| *\*Static Calculation Load* | The current orientation-specific **Static Calculation Load**/Recommended Upper Limit  First, the Area calculates the Load of Entities within the visible range, starting from the central location in the specified orientation.  Second, based on the distance between each Entity and the center point, a distance coefficient is applied. The total load of all Entities is then calculated as the Static Calculation Load.  As shown below, eight identical slimes produce different load results depending on their distances from the center. The farther away, the lower the Load.  ![](../images/3c8bec18cc1efb2a.png)  In the second graph, the red Area contains 16 slimes, while the blue Area has only 8. Even with distance coefficients reducing values at greater ranges, the red Area still bears higher Calculation Load due to having more Entities  ![](../images/6d0a87eaec8f177d.png) | |
| *\*Static Memory Load* | Current Area's **Static Memory Load** | |

# V. Dynamic Load Calculation

During Stage runtime, Entities and Special Effects generated by Node Graphs affect the Load. These impacts cannot be estimated by Static calculations. Therefore, Dynamic Load Calculation is provided, allowing Creators (Craftspeople) to obtain Stage runtime Load data for adjustments.

## 1. Dynamic Load Calculation Window

Open Miliastra Sandbox and, from the **Window** of the Menu Bar, open the **Load Detection** window.

![](../images/9581aa2f0a3f4eb3.png)

![](../images/d708567f7f36ed0f.png)

## 2. Enable Dynamic Load Calculation

![](../images/4c4f3dcfb3506efe.png)

Turn on the **Enable Load Testing** switch in the top-left corner.Do a **playtest** of the Stage**.**

When the Stage starts running, dynamic Load detection begins, taking screenshots whenever the Load exceeds recommended values during runtime.

***Important Notes:*** Enabling Dynamic Load Test will itself impact the Load.

![](../images/ef1f7d175695b270.png)

![](../images/e278e32667b5f52c.png)

After the playtest ends, the Dynamic Load log for the Stage will be automatically imported.

***Important Notes:*** Do not turn off the Load test switch during the playtest or while viewing reports.

## 3. View Dynamics Load Calculation Report

![](../images/7e786c47c63122f6.png)

**Submenu**

![](../images/626afdf39176a926.png)

|  |  |
| --- | --- |
| Parameter | Description |
| *\*Calculation Load Spike (Local)* | When Dynamic Calculation Load approaches or exceeds the limit, detailed data will be provided along with adjustment recommendations |
| *\*Memory Load Spike (Local)* | When Dynamic Memory Load approaches or exceeds the limit, detailed data will be provided along with adjustment recommendations |
| *\*Processor Spike (Server)* | When the server processor approaches or exceeds its limit, detailed data will be provided along with adjustment recommendations |
| *\*Memory Load Spike (Server)* | When server memory approaches or exceeds its limit, detailed data will be provided along with adjustment recommendations |

### **(1) Local Calculation Load Spike**

**Load Detection Tool Hint**

![](../images/b108f1f51f736747.png)

**Load Detection Tool Details**

![](../images/9ee17ed5ffab794e.png)

*\***List of Anomaly Moments*

During the playtest, data is collected every second.

If the Dynamic Calculation Load exceeds the recommended value, screenshots will be taken and listed here in chronological order

Select to view details

*\***Anomaly Moments* *Comparison Chart*

With the selected anomaly as the center of the chart, the actual runtime screenshots will be displayed on the right side. This supports comparing detailed Load data up to 5 seconds before and after (if available)

Select an anomaly from the graph/filter bar, and the Load details will display a comparison between the selected moment and the anomaly moment

![](../images/7e786c47c63122f6.png)

*\*Load Details*

The selected anomaly moment will have data screenshots listed here, including runtime entities and environmental information.

Expand an entity to also view details such as its mounted special effects

### **(2) Local Memory Load Anomaly**

The interface data display section for Dynamic Memory Load has the same significance as Local Calculation Load anomalies.

![](../images/9f35ad1c5cbc937e.png)

### **(3) Server Processor Anomalies**

**Stage Runtime Hint**

![](../images/17c97ab59e57a8a1.png)

**Load Detection Tool Hint**

![](../images/d92888c8b556e244.png)

**Load Detection Tool Details**

![](../images/9d4c662976398305.png)

|  |  |  |
| --- | --- | --- |
| Parameter | Description | |
| *Anomaly Log* | The cause of the anomaly is labeled | |
| *System Content* | Explanation of processor Load consumed by essential system functions | |
| *Anomaly Node Graph* | Explanation of processor Load consumed by the Anomaly Node Graph | |
| *Details* | *ID* | Node graph ID |
|  | *Load* | The Load value of the specified function |
|  | *Load Percentage* | The percentage of total Load taken by the specified function |
|  | *Affiliated Entity* | If the target is a Node Graph, the associated Entity will be provided |
|  | *Operation* | Locate the Node Graph and open it directly for editing |

### **(4) Server Memory Load Anomalies**

**Load Detection Tool Details**

![](../images/806c0508a9e10047.png)

Displays server memory usage anomalies and total memory consumption

Different suggestions will be provided depending on the cause of the memory anomalies
