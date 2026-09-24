---
title: Signal
path_id: mhkwzxrk3o2m
updated_at: 2025-10-21 16:38:25
category: Appendix/Node Graph Advanced Features
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhkwzxrk3o2m
---

# I. What is a Signal?

When building Node Graphs, you'll often encounter scenarios that require Global communication.

For example, when a mechanism is triggered, the following events may occur:

A certain gate opensSeveral torches light up with flamesA new Skill is added to the Character

If you implement the related logic directly on the mechanism, you'll need to construct it as shown in the graph below

![](../../images/835b2ad12eb8697d.png)

When iterating on this logic (e.g. if you need to add [Editing *Custom Variables* on Hilichurls] before igniting the flame), you would need to edit the mechanism's Node Graph each time, which is hardly an efficient implementation

![](../../images/302436062f54af82.png)

*Signals* are designed to address the issues described above

# **II. Signal Functions**

A Signal is a global custom structure. You can add multiple *Signal Parameters* of any type to itEach Signal is identified by a *Signal Name*.You can *send Signals* from any Entity's Server Node Graph. Sending Signals is a global actionYou can *receive Signals* from any Entity's Server Node Graph. Note that both sending and receiving are global actions. This means that when Entity 1 sends a Signal, any Entity within the Stage can monitor and receive it

With Signals, the logic from the above example can be implemented directly on each Entity

When the mechanism is triggered, send the Signal [Mechanism Trigger Signal]

![](../../images/ef6f25d48ff38a5b.png)

The gate receives the [Mechanism Trigger Signal] and updates its Preset Status (gate opens)

![](../../images/78104952be24a9c7.png)

The torch receives the [Mechanism Trigger Signal] and plays a flame effect

![](../../images/dbeaca6ee8695571.png)

The Character receives the [Mechanism Trigger Signal] and adds a Skill to itself

![](../../images/a9b6e6b3b02def0c.png)

At this point, if you need to add logics such as [Editing Custom Variables on Hilichurls], you can edit the Hilichurl's Node Graph directly:

![](../../images/a95f37d5aaa00ca2.png)

As you can see, even when adding or adjusting logics, you only need to edit the Node Graph of the relevant Entity, without changing the Node Graphs of other Entities.

In game logic development, this principle — **each Entity only handles logic for the Events it cares about, rather than directly manipulating other Entities** — is an important **decoupling** concept. It helps separate complex interaction logic between Entities

# III. Signal Configuration

In *Miliastra Sandbox*, you can configure Signals

![](../../images/276861c405d6b733.png)

Open the Signal Manager Interface to add and edit Signals

![](../../images/445396570a37d16f.png)

Each Signal is uniquely identified by its [Signal Name]. Signals with different names are treated as distinct, even if their parameters are identical

Each Signal can declare any number of Custom Parameters, which may be any valid Node Graph data type

As shown in the graph above, this Signal is named [Signal\_1] and contains three parameters

Parameter\_1: Type is Integer

Parameter\_2: Type is String

Parameter\_3: Type is Entity List

# IV. Using Signals

In a Node Graph, you can use [Send Signal] and [Receive Signal] Nodes to send or receive Signals

**Send Signal (Server Node Graph)**

![](../../images/58849a040040d7fa.png)

After placing a [Send Signal] Node in a Node Graph, you must first choose a [Signal Name]

![](../../images/1a9e3cc0c6f26e85.png)

Once a [Signal Name] is chosen, the Node's Input Parameters expand to include all parameters defined for that Signal. You can then pass values into the Signal here, which will then be received on the Signal listener side

![](../../images/ff837827a1700179.png)

**Send Signal to Server Node Graph (Client Node Graph)**

In skill node graphs, you can also use predefined signals to send to the server node graph. All server node graphs can listen for this signal.

![](../../images/fe751d9778f570fa.png)

**Monitor Signal**

![](../../images/78a3cb7a06f043a6.png)

Signals can be received on any Entity, but you must first select a [Signal Name]

![](../../images/4c48c2b2ae7a9864.png)

After selecting a [Signal Name], the Node's Output Parameters will include all parameters defined for that Signal, letting you retrieve the values passed from the [Send Signal] Node

![](../../images/db2c8cdcb422963d.png)
