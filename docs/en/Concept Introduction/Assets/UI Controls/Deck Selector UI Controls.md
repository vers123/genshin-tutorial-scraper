---
title: Deck Selector UI Controls
path_id: mh1g8q9w7x02
updated_at: 2026-03-27 16:26:19
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh1g8q9w7x02
---

The Deck Selector provides a simple interface for editing decision interactions

Supports editing of decision-making content, including decision time, presentation of decision options, interaction methods for decisions, etc.

# **I. Deck Selector** Functions

![](../../../images/a0db749914993240.png)

During stage runtime, the *Deck* *Selector* can be invoked through default configurations or the node graph.  
Supports player interaction, and send a *Decision Pop-up Completion Event* to the node graph upon timeout or after interaction.

# **II. Editing Deck Selector**

![](../../../images/f6db4edc52f39945.png)

## **1. Add Deck Selectors**

In the *UI Control Group Editor Window*, add the UI control template - Deck SelectorThe Deck Selector is a default UI controls group

![](../../../images/2f5e4cfa7eabfd4f.png)

## **2. Interface** Configuration - Deck Selector

This section configures the Deck Selector's overall appearance and usage rules, allowing players to customize its display style

### (1) Visibility

![](../../../images/532a72a1995430da.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Index* | Parameters used to invoke the Deck Selector node |
| *Initially Visible* | If unchecked, the UI control will not be visible when activated.  This parameter can be adjusted through the Node Graph - *Modify UI Control Group Status*. |

### (2) Transform

![](../../../images/807025b676ed9874.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Location* | Supports manually entering the UI Control's location  You can also adjust it by dragging the UI Control in the editing tab |
| *\*Size* | Configuration not supported |
| *Layer* | The higher the number, the higher the display layer |

## **3. Interface Configuration** - Decision Panel

### (1) Page Settings

![](../../../images/ba5fb9d31bdc4705.png)

#### a. Visibility

![](../../../images/cdfdc25b5792202e.png)

#### b. Deck Selector

![](../../../images/049ed59a4c5d63a5.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | | Description |
| *Show Title* | | When checked, the current Deck Selector will have an editable title at the top |
| *Title Text* | | Supports editing the display title |
| *Interface Layout* | Provides two style options to choose from | |
| List | ![](../../../images/3e0f13eadff6ff0d.png) |
| Grid | ![](../../../images/278056847c0e2155.png) |

#### **c. Show selected quantity**

![](../../../images/c2bae6331ccdc022.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Show Selected Quantity* | Determines whether to show the current number of selected items in the Deck Selector interface |

#### **d. Show reset count limit**

![](../../../images/2aebf269b6e36335.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Show Reset Count Limit* | Determines whether to show the minimum and maximum number of resettable options in the Deck Selector interface |

#### **e. Show Remaining Time(s)**

![](../../../images/47dc0c32d23082c9.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Show Remaining Time (s)* | If checked, the Deck Selector will automatically close when the countdown timer ends without requiring manual input  If the player completes the interaction before the countdown ends, whether the interface remains visible depends on *Decision Completion Style* and *Decision Completion Style Duration* settings |
| *Pre-End Warning Time (s)* | When the countdown reaches the configured time, the time display interface will show a flashing red warning effect |

#### **f. Other Settings**

![](../../../images/23933834e963ad83.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Pause Game on Page Open in Single-Player Mode* | If checked, the game will pause during the selection process when the stage is a single-player stage. |
| *Controls can collapse* | If checked, the deck selector can be manually collapsed.  You can choose to postpone handling, process it later, or wait until it times out.  ![](../../../images/aa0e21021aacebc3.png) |
| *Selection can be canceled* | If checked, the Deck Selector can be manually closed. The Deck Selector will add a UI control for closing, and it will support interactions.  If closed, it triggers the node graph's Decision Completion - Closed manually event |

### (2) Option Configuration

![](../../../images/c454b3508842b705.png)

#### **a. Known Deck Settings**

![](../../../images/89c4751fb664e100.png)

|  |  |
| --- | --- |
| Configuration Parameters | Description |
| *Display Deck Icon* | Whether the displayed card includes an icon. If it does, the icon can be configured in the settings |
| *Display Deck Title* | Whether the displayed card includes a title. If it does, the icon can be configured in the settings |
| *Display Deck Description* | Whether the displayed card includes a description. If it does, the icon can be configured in the settings |

#### **b. Unknown Deck Settings**

![](../../../images/423643c27c33e7ab.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Reveal result after Selection* | After the decision is made, determine whether to play an animation and switch the display to the option's actual return value | |
| *Result Page Closing Method* | Closes after the countdown ends | Additional configuration of **countdown duration (s)** |
| Closed Manually | Requires manually closing the pop-up to end it |
| *Countdown(s)* | After the decision is complete, the deck selector will automatically close after the configured time | |

#### **c. Deck Settings**

![](../../../images/1ecb23a703d3a93d.png)

Use Edit Details to configure deck display

![](../../../images/bd6ac60bc4cf10b5.png)

|  |  |  |
| --- | --- | --- |
| Configuration Parameters | Description | |
| *Deck ID* | Used for displaying the cards when invoking the Deck Selector in the node graph.  Increments sequentially starting from 1, cannot be modified | |
| *Deck Types* | Known Deck | Provides a clearly configurable icon |
| Unknown Deck | Provides only a question mark icon. Recommended to use together with **Reveal Result After Selection** and **Closes after the countdown ends** |
| *Deck Icon* | This configuration will only be available when icon configuration is enabled in general settings | |
| *Deck Title* | Text Configuration | |
| *Deck Description* | Text Configuration | |
| *Tag Color* | Text Color | |
| *Tag Description* | Text Configuration | |

# **III. Managing Deck Selector Through Node Graphs**

**Invoke Deck Selector**

![](../../../images/45432881f3cfe0b1.png)

**Close Deck Selector**

![](../../../images/cf6474ba47432943.png)

**When Deck Selector Is Complete**

![](../../../images/3ed3f78c5bdd3efd.png)

**Random Deck Selector Selection List**

![](../../../images/c2a5756575cbfa85.png)
