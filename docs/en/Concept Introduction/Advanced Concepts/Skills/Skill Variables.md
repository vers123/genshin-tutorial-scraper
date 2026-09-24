---
title: Skill Variables
path_id: mh7dyo0rguc8
updated_at: 2026-08-06 15:05:14
category: Concept Introduction/Advanced Concepts/Skills
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7dyo0rguc8
---

# I. What Are Skill Variables?

*Skill variables* are values that can be persistently stored on the player. They are similar to Custom Variables, but differ in the following ways:

1. Skill Variables are client-side values. They can be modified directly by Client Nodes, and changes take effect immediately, so they are more responsive than Custom Variables

2. Skill Variables are Floating Point Numbers by default. Other data types are not currently supported

3. Skill variable values will be set to 0 after the character is defeated

Skill Variables can be used to record information in real time, enabling asynchronous queries within the same skill or information transfer across skills

# II. Editing Skill Variables

Click [Skill Variable Management] in the System Menu to open the Skill Variable Management interface

![](../../../images/1f51dd3b3c9d3197.png)

Globally available Skill Variables can be edited in this interface

![](../../../images/9a54eb78587740fc.png)

Click [Add New Variables] to add a new Skill Variable

*Variable Name*: The name of the Skill Variable

*Configuration ID*: The unique identifier for the Skill Variable. This ID is used when referencing it in Node Graphs

# III. Modifying Skill Variables via the Node Graph

Set Skill Variable

![](../../../images/795ab950bae6e629.png)

Increase Skill Variable Value

![](../../../images/9e593b94afb0f065.png)

Query Skill Variable Value

![](../../../images/c8fd1e3481523c28.png)
