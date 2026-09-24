---
title: Key Behaviors
path_id: mhpb6pi79hjo
updated_at: 2026-04-03 15:02:32
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpb6pi79hjo
---

# I. Definition of Key Behaviours

*Key Behaviors* are purely client-side data. Craftspeople can actively define and record them through Node Graphs during skill casting. The system stores the recorded Key Behavior list and the client-side trigger time of each entry in the *Info Board*, and the recorded Key Behavior list can also be retrieved through Node Graphs

Key Behaviors can be treated as a simplified instruction sequence. Based on this, Craftspeople can implement time-sensitive skill chains or combo skills

# II. Basic Concepts of Key Behaviors

*Key Behavior ID*: The unique identifier for a Key Behavior. This ID is used when calling it through Node Graphs

*Client Time*: The time on the client when the Key Behavior is added

# III. Setting Key Behaviors via the Node Graph

Add Key Behavior

![](../../../images/c1bcafd4937e2dee.png)

Clear Key Behavior Log Panel

![](../../../images/7af4cabe44e0c269.png)

Get Current Key Behavior

![](../../../images/b21c394e4c647fc1.png)

Get Current Key Behavior (High Precision)

Client time is affected by floating-point precision. If higher precision is required, it is recommended to use the high-precision version of the node

![](../../../images/13e1ad3c20208de8.png)
