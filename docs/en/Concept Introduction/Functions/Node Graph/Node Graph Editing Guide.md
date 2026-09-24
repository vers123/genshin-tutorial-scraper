---
title: Node Graph Editing Guide
path_id: mh0zkz9izs8q
updated_at: 2025-10-21 23:46:59
category: Concept Introduction/Functions/Node Graph
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh0zkz9izs8q
---

# I. Entry Point for Node Graph Editing

Node graph editing must be done in the *Miliastra Sandbox*. Please locate the Miliastra Sandbox entry point as shown in the graph below

![](../../../images/b980854cd2960f11.png)

The main window of the Miliastra Sandbox is shown in the graph below

![](../../../images/3b9aa439c1f0bcb5.png)

Server Node Graph (Graph A)Created Node Graph (Graph B)

# II. Creating a New Node Graph

## 1. Server Node Graphs

![](../../../images/ab439ca792fb3edb.png)

In the Node Graph Management interface on the left (A), choose the type you want to create: Entity Node Graph, Status Node Graph, Class Node Graph, or Item Node GraphIn the menu on the right, Select [Create Node Graph]

Double-click the newly created node graph to open the Editing Tab

![](../../../images/01690d8ae7c22473.png)

You can also right-click a node graph to rename it and perform other common file operations

![](../../../images/bddfa1bd28aee427.png)

## 2. Client Serve Node Graphs

The Client Node Graph Resource Explorer is closed by default. To open it, choose Window > Client Node Graph Resource Explorer (top-left)

![](../../../images/34c41fcd346d7a88.png)

The Client Node Graph Resource Explorer works like the Server Node Graph Resource Explorer. In the Asset Management panel on the left, select the node graph type you need, then right-click in the right panel to create a new node graph

![](../../../images/c85dfcacab82adb6.png)

# III. Node Graph Actions

After entering the node graph editing tab (as shown below):

![](../../../images/c041193cac48580c.png)

## 1. Create Nodes

**Create via menu**

The most common way to create a node is to right-click in the editing area to open the node menu

You can find specific nodes by searching through node categories

![](../../../images/9079f3854e283e3e.png)

Shown below is the [When Custom Variable Changes] node. You can find this node under [Event Node] >[Custom Variable]

![](../../../images/70c250476ff67be7.png)

Click to create a new node in the editing area

![](../../../images/c3340f98a974e335.png)

**Quick Creation by Connecting**

Another common way to create nodes is through quick connections

To do this, drag a connection from a pin outward and release without connecting to any other node. This will bring up the node creation menu.

This menu will automatically filter all nodes that match the pin **type** (i. e., those that can be directly connected)

![](../../../images/dd069bc91b641c2a.png)

## 2. Node Connections

Hold and drag outward from a pin to create a connection line

Connect it to a valid pin on another node to complete the connection

![](../../../images/ba8013537c7db732.png)

## 3. Other Node Graph Operations

**Connection Details**

Hover over a pin or connection to highlight the connection and its endpoints. This is especially useful in complex graphs

![](../../../images/6ec711421ca3764d.png)

**Right-Click Menu Actions (Nodes)**

Delete: Delete nodes

Cut: Cut the node, then you can paste with (Ctrl + V)

Copy: Copy the node, then you can paste with (Ctrl + V)

Disconnect Node Connection: Remove all connections to this node

Notes: Add a comment on this node

Generate Composite Node: See [Composite Nodes](/ys/ugc/tutorial//detail/mhty17iqeht0)

![](../../../images/99bcef71300ae3fe.png)

**Right-Click Menu Actions (Pins)**

Jump to Next Node: Jump to the next node connected to this pin

Disconnect Link: Remove the pin's connection

![](../../../images/c967520fda969ec3.png)

**Node Graph Shortcut Menu Actions**

![](../../../images/a64909a1983d95ee.png)

Collapse Menu: Collapse the shortcut menu

Enter Comment: Add a comment to the node. Click to add a new comment when clicking on a node

![](../../../images/9125d3e836a60066.png)

Search Nodes: Click to open the node search tab

![](../../../images/2e744175cfead6c2.png)

Node Graph Variables: Click to open the node graph variables tab

![](../../../images/1ca7af9a069ff5e0.png)

Signal Management: Click to open the Server Signal Explorer

![](../../../images/79dfa273453845bf.png)

Editing Area Zoom: Zoom in/out of the edit area. You can also use the mouse wheel to zoom

![](../../../images/3ea59ab1998ecc96.png)

Operation Log: View the operations in the current node graph

![](../../../images/6de27c2f39a2b0f6.png)

Undo: Undo a single step of an operation

Restore: After undoing an operation, you can redo the undo to restore the previous state

Save: Save current node graph

Save As: Save the current node graph as a new node graph file
