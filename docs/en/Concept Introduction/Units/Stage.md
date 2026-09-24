---
title: Stage
path_id: mhhd9urqpbl2
updated_at: 2025-10-14 20:52:59
category: Concept Introduction/Units
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhhd9urqpbl2
---

*Stages* are special entities recommended for handling stage-specific logic.

# I. Creating a Stage Entity

When a new stage is created, a stage entity is automatically generated in the scene and represented by a unique icon.

![](../../images/bfb50e255171c9d7.png)

# II. Edit Stage Entities

![](../../images/8e264c48ee3b5865.png)

Switch to the Entity editing tab.

Editing stage entities is similar to other types of entities, but the configurable *basic information* and *components* will be different.

## 1. Basic Information

![](../../images/16d66039acddb415.png)

Basic Information tab, where you can configure all available attributes for the stage entity.

## 2. Common Components

![](../../images/1a351af49eedd687.png)

Common Components tab, where you can add common component settings to stage entities.

Overview of Available Components for Stage Entities:

[Custom Variables](/ys/ugc/tutorial//detail/mhso1b9wjica)

[Global Timer](/ys/ugc/tutorial//detail/mhawd6rl5kpy)

## 3. Node Graph

![](../../images/a93bb7c9ebfc03a6.png)

Node Graph Settings Tab, where you can add node graphs to stage entities or view existing node graphs.

# III. Stage Characteristics

Unlike other entity types, stage entities have the following unique characteristics:

## **1. Can Receive Special Events**

Some special events can only be received by stage entities, including:

![](../../images/011b3b1ee4314766.png)

![](../../images/48e72539c208cea0.png)

When *object* or *creation*-type entities are removed/destroyed, those entities cannot receive the corresponding events, which will instead be forwarded to the stage entity.

The subsequent logic will be processed by the stage entity as well.

## **2. Non-Physical Entity**

The stage entity is a purely logical entity.

## **3. Incomplete Placement Information**

Stage entities only have *position information*. They lack *rotation and scale information*.

## **4. Life Cycle**

Stage entities are created when the stage initializes and destroyed when the stage is removed.
