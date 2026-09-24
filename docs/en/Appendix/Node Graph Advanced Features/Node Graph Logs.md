---
title: Node Graph Logs
path_id: mhbsu00psmvs
updated_at: 2025-10-22 03:21:59
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhbsu00psmvs
---

# I. What is a Node Graph Log

When developing gameplay logic, you may encounter many cases where issues are difficult to pinpoint.

The Node Graph Log displays the execution flow of a Node Graph at different points in time and shows the input and output parameter values of each Node, which will help Creators (Craftspeople) to debug more effectively

The graph below shows a Node Graph in Log Viewing mode![](../../images/5929836463f1b842.png)

# II. Debugging Through Node Graph Logs

## 1. Enable Node Graph Logs

From Window — Log, open the Node Graph Logs window

![](../../images/a8b635d60368ca71.png)

Node Graph Log Tab

![](../../images/b182feefe80af087.png)

## 2. Debug through Node Graph Logs

**Filter Node Graphs**

Before debugging with logs, select which Node Graphs to include in the Node Graph Filter Tab, as shown in the graph below

![](../../images/3b67a8a0a1909573.png)

After filtering, when the Stage runs, the selected Node Graph will return log information during execution

Log information includes the following:

Node Graph Events: Shows the currently active Node Graphs and the time points at which they became active

Print Information: Information printed through the [*Print String*] node

![](../../images/4cffcbd84d304fa3.png)

Double-click an active Node Graph to enter the Node Graph Debug mode

![](../../images/295dc437167ea9d9.png)

**Node Graph Debug Mode**

In the Debug Tools at the top-left, you can view the active *Logic Subgraphs* (there may be multiple) at the current log timestamp. Each Logic Subgraph is a Node Graph Execution Flow triggered by an Event Node

When you select the currently active Logic Subgraph, its section will be highlighted (as shown in the graph below)

![](../../images/d38fd3c5e8abc9a4.png)

Hover over a Node to view its current input and output parameter values

![](../../images/b00f0c5ad6cf19f8.png)
