---
title: Craftsperson Subscription
path_id: mh8xs59s1r7u
updated_at: 2026-07-10 14:57:09
category: Concept Introduction/Advanced Concepts/Peripheral System
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh8xs59s1r7u
---

# I. Definition of Craftsperson Subscription

The Craftsperson Subscription feature helps creators (Craftspeople) build a private audience base and attract fans to play their stages, allowing them to push published or updated content to their subscribed fans and players in real time

# II. Publishing Subscription Notifications

When creators (Craftspeople) release or update a Stage, there will be a prompt asking whether to publish Stage Updates. If this option is checked, a notification will be sent to their subscribed fans

![](../../../images/477da2b48639ca85.png)

Each creator (Craftsperson) can publish up to 3 notifications per week. After the limit is reached, no more notifications can be published that week. The limit resets at 4:00 AM every Monday.  
Note: Removing a published notification or Stage will not restore your available notification count.

You can manage all published notifications via "Popular Miliastra Wonderland" → "Subscription Notifications" → "My Notifications"

# III. In-Game Subscription Functions

## 1. In-Game Subscription Button ![](../../../images/5f1f1c116c05aee7.png)

Added a "Subscribe to Craftsperson" button under UI Control Group Management → Add UI Control → Prefab Template. Craftspeople can add this button to the in-game interface to attract fans. The button can also be added to Floating Interaction Pages, and it remains active during playtests

## 2. Server Node - Check Whether Player Has Subscribed

![](../../../images/843bc195bb270f16.png)

Adds a new query node that supports real-time checking of whether a player is a subscriber of a Wonderland Creator. It can be used to configure fan benefits and similar functions

When querying the creator themselves, the node outputs "True" by default

# IV. Additional Rules for Craftsperson Subscription

![](../../../images/8073cf704e7a5c61.png)

As a Craftsperson's subscriber count and engagement metrics grow, the subscribe button will change correspondingly as a status symbol of a popular Craftsperson
