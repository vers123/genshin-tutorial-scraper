---
title: Composite Node Graph Logs
path_id: mhtvlyi9zzoc
updated_at: 2025-10-21 20:20:23
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhtvlyi9zzoc
---

# I. Feature Overview

The Composite Node Graph Log function is used to debug Composite Nodes (view Composite Node input/output values; display runtime information within Composite Nodes)

# II. Debugging Process

## 1. Select Target Composite Node

In any [Node Graph Log](/ys/ugc/tutorial//detail/mhu951iz7wz8) debug mode, you can click to select Composite Nodes that have run in the logic tree

Composite Nodes cannot be selected independently. They can only be viewed within the Node Graph logs of the selected Node Graph that contains them. In other words, to inspect a Composite Node, you must monitor the Node Graph it belongs to.

![](../../images/7c1a93d07ddd8e87.png)

## 2. Composite Node Runtime Information

In Node Graph Debug Mode, hover a running Composite Node to view its input and output values.

![](../../images/569aa2f4dfc28757.png)

Double-click a Composite Node to open its debug mode (see below).

## 3. Composite Node Debug Mode

![](../../images/1e54c918c0b13287.png)

View input and output values: Hover a node to view its inputs and outputs.

![](../../images/c8fee1fe05691beb.png)

Tabs logic: In each active logic tree, every executed Composite Node opens as its own window.

![](../../images/b6c723ca7cac2116.png)
