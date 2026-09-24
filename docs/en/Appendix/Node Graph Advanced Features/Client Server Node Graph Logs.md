---
title: Client Server Node Graph Logs
path_id: mh2u7z9zwba2
updated_at: 2025-10-22 03:21:00
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2u7z9zwba2
---

# I. Feature Overview

This feature is used for debugging client node graphs (displays the execution flow of node graphs and shows the input/output values of nodes within the graph).

# II. Limitations and Feature Planning

## 1. Limitations

Unlike the original node graph log system, due to the client node graphs' operating logic, this feature currently only displays logs from the Local using the logging function; it cannot view node graph logs from other players' client node graphs logs.

## 2. Feature Planning

Future versions will provide functionality to display client node graphs logs from other players participating in playtests.

# III. Function Entry Point

From Miliastra Sandbox > Window > Logs, click to open [Log System]

![](../../images/9a4bd7cc4656ae8e.png)

# IV. Debugging Process

## 1. Select Target Node Graph

Before starting a playtest, in the Filter panel, select all client node graphs from which you want to capture log information.

The highlighted section in the graph is used to select target logs for client node graphs. Selection limit for client node graphs: 99 (Server Node Graph limit remains 10)

Note: Only the selected target Node Graphs will return log information.

![](../../images/3e0a05df6927785f.png)

New feature: Select all node graphs of this type.

![](../../images/8f24a76536e3683e.png)

## 2. Node Graph Log View

During gameplay, when a selected client node graph is triggered, log information is generated

The log information includes the following:

Node graph name, effective time, and mounted objects;

![](../../images/1900b77d56b8c8cb.png)

Double-click the active client node graph to open its debug mode (see below);

## 3. Node Graph Debug Mode

When in Client Node Graph Debug Mode, all active nodes and their execution flows are highlighted. Hover over a node to view its current input and output parameter values.

![](../../images/1d8f192447f1e204.png)
