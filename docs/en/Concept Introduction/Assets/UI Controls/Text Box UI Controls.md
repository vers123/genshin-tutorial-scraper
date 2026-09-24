---
title: Text Box UI Controls
path_id: mha9au0hpj0o
updated_at: 2026-09-16 16:26:54
category: Concept Introduction/Assets/UI Controls
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mha9au0hpj0o
---

# I. Text Box Functions

![](../../../images/5f46d0137a752566.png)

During stage runtime, display pre-edited *text content.*

If the text content contains custom variable, it will update the display in real-time.

# **II. Editing the Text Box**

![](../../../images/bbc59b4d5f2e86c9.png)

*Background Color*

![](../../../images/8982aab9ea2d44de.png)

Choose a transparent or semi-transparent black background

*Font Size*

Font Size Configuration

*Text Content*

Edit the text box's content; supports characters, text, numbers, and custom variables.

![](../../../images/d79b5a6dd8de5e70.png)

![](../../../images/c95a8d0580b896d3.png)

By inserting variables, you can select *custom variables* predefined on stage entities and player entities

When an inserted custom variable changes, the displayed text updates at runtime.

Insert the referenced custom variable in rich text format, with the following format:

**{Type:Prefix.VariableName}**

Type:

1 when referencing a custom variable

Prefix: See the table below

|  |  |
| --- | --- |
| **Custom Variable Target** | **Prefix** |
| Players 1 – 8 | p1~8 |
| Stage Entity | lv |
| Player's Own Entity | ps |

For example, if you need to insert a reference to a custom variable named "Test2" on Player 4, the rich text should be written as: {1:p4.Test2}

*Align*

Choose an appropriate alignment based on the position and content of the text

![](../../../images/640a0cf12fa2baf0.png)

|  |  |  |
| --- | --- | --- |
| Alignment Method | Description | Diagram |
| ![](../../../images/9eb94f0be969a869.png) | Left Align | ![](../../../images/d52b55654728d9da.png) |
| ![](../../../images/5a9fadc0c4a6e0a6.png) | Horizontal Center | ![](../../../images/20114b68ac0e74c2.png) |
| ![](../../../images/cc4bf495308fb6c1.png) | Right Align | ![](../../../images/1b37d1ffafa0f23f.png) |
| ![](../../../images/7b17de497027e0f4.png) | Top Align | ![](../../../images/fbc67bfa6c4fe059.png) |
| ![](../../../images/84e0b62f07e78029.png) | Vertical Center | ![](../../../images/1cc8b5a15d013d21.png) |
| ![](../../../images/bac3505a88c24bd6.png) | Bottom Align | ![](../../../images/9e7a2248cc63dbe3.png) |

# III. Adjusting Text Box Layout in the UI

Resize the text box by dragging its borders in the edit window when the cursor changes to a resize arrow.

Its position and size update automatically after adjustment.

![](../../../images/80ee0bfc5754b7f7.png)

# IV. Text Boxes in Client Controls

Client Text Box controls can have *Client Scripts* attached and can be called through *Client Scripts*

API Reference: Search for `TextBoxControl` in the API documentation to view the related APIs

![](../../../images/a6fe8e4ff2ab2781.png)

## 1. Controller Navigation

*Selectable via Controller Joystick Navigation:* Determines whether this control can be selected via controller navigation

When enabled, you can configure which other controls are selected when navigating in each of the four directions with the controller

![](../../../images/66013e10ae7f8c98.png)
