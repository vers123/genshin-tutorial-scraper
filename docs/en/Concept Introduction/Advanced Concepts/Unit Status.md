---
title: Unit Status
path_id: mh1lsn90mml6
updated_at: 2026-01-06 22:22:01
category: Concept Introduction/Advanced Concepts
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh1lsn90mml6
---

# I. Definition of Unit Status

*Unit Status* is a status management module for managing additional functions and attributes of Entities during Stage runtime.

During Stage runtime, Entities can be applied with Unit Statuses. Each Unit Status must have a defined *Applier Entity*.  
Entities can dynamically hold multiple Unit Statuses. Each status has a defined Runtime Duration that grants the Entity *Additional Effects* and *Additional Node Graph* functionality. Statuses must be predefined at the editing time to be enabled during runtime.  
Each active Unit Status has independent *Stack Layers*, and some functions can scale in real time with the number of stacks.  
A Unit Status ends when its *Runtime Duration* expires or when all *Stack Layers* are depleted.

## 1. Additional Effects

All *Additional Effects* come from the predefined *Effect Pool*, such as functional effects like "Mount Looping Effects" or numerical effects like "Motion Speed Change".

Each Additional Effect has certain runtime limits on both its Effective Target and Effect Intensity —  
*Effective Target*: Each effect can only apply to one or several among "Characters", "Creations", or "Objects". When a target entity tries to hold a Unit Status, if that status includes an effect that cannot apply to the entity’s type, the entity will fail to acquire the status. For example, the "Mount Screen Effect" is allowed only on "Characters", so any status using this effect can only be applied to character entities.  
*Effect Intensity*: An entity may receive multiple Additional Effects of the same type at the same time, but the final effect cannot stack without limit — it is restricted to a valid range. For example, with "Motion Speed Change", since the change cannot be less than -40% or greater than 40%, whether an entity has one effect of +50% speed change or five effects of +10% each, the final Motion Speed will never exceed 140%.

Additionally, some effects cannot coexist within the same Unit Status. For example, a Unit Status can provide only one type of Elemental Effect. If multiple *Mutually Exclusive* effects are configured, the last effect will take precedence.

## 2. Additional Node Graph

Each Unit Status can be related with a server Node Graph. When an Entity holds this status, the Node Graph is synchronously added to the corresponding Entity, and it is removed when the status ends.

The related Node Graph can only come from a *Status Node Graph*, where Composite Nodes can still be used.

![](../../images/c353d50ecd4270f0.png)

Unlike regular Node Graphs, if multiple Unit Statuses held by an Entity are related with the same Node Graph, it is considered related only once, and the Node Graph will lose relation only when the Entity has lost all related statuses.

# II. Editing Unit Statuses

After entering the Combat Preset page, select the Unit Status bar, create management Tabs as needed, and create the corresponding Unit Statuses within the Tabs.

![](../../images/059c39dd8ff1a2d6.png)

Click the New Status, then click Confirm Create in the pop-up to create a new Unit Status

![](../../images/724a17b4ffe84a19.png)

## 1. Naming and Identification

![](../../images/05b9795a6f8b5531.png)  
Each predefined Unit Status *Name* must be globally unique. A globally unique *Config ID* is automatically generated for it.  
You can use the Copy button to quickly duplicate this Config ID.  
![](../../images/f958e38f50787b45.png)  
You can also replace the *Icon* for each status.

## 2. Stacking Rules

![](../../images/723b848aff1fb533.png)  
When a status is stacked onto an existing one, detailed stacking rules must be defined.  
Each time stacking occurs, the new status's stack layers count is added to the existing status, but the total will not exceed the *Maximum Stack Layers*.  
The maximum count of the stacks may vary depending on the situation.  
When stacking may exceed the limit, you can choose whether to enable *Overlapping Data Update*.  
If updated, the overlapping data will sequentially replace the earliest existing stack data. Otherwise, the overlapping data will be discarded.  
If no change occurs to the stack data of the status, the stacking action is considered invalid, and the application of the status is also invalid.

## 3. Timing Rules

![](../../images/a5d4eab93d58d1b7.png)

Each active Unit Status may have a defined Life Cycle. When the Life Cycle is exceeded, the status is automatically removed.  
Enabling *Infinite Duration* prevents the status from being removed when its Life Cycle expires, and any updates to the status will no longer affect its Initial Runtime Duration.  
If the Initial Runtime Duration of a status is finite, when an Entity gains a new status, that status's Life Cycle is set to its *Initial Runtime Duration*.  
If the Initial Runtime Duration is finite, you can enable*Stack Shared Duration*.  
When disabled, each stack calculates its Runtime Duration independently. Once a stack exceeds its Runtime Duration, it is automatically removed, reducing the corresponding Stack Layers of the status

Stack Layers Count.  
 In this case, the Maximum Stack Layers count is 10.  
 When enabled, all stacks are removed together once the status exceeds its duration. However, each time a new stack is applied, the status's *Time Remaining* may be extended based on specific rules.  
 Each time a new stack is applied, the current Time Remaining of the status may be increased by an *Extended Duration*.  
When *Maximum Extended Duration Limit* is enabled, the extended Time Remaining cannot exceed the *Maximum Duration*, even if the original Time Remaining was greater.  
 In this case, the Maximum Stack Layers count is 1000.

## 4. Related Node Graph

![](../../images/a72300ba6c336037.png)  
The *Status Node Graph* related with an Entity while it holds a status.

## 5. Status Coexistence

![](../../images/e5b5081cd6871e59.png)  
When the same Unit Status is repeatedly applied to an Entity, different handling can be configured based on the Applier Entity, and the most recent update time is recorded.  
The same Applier cannot apply two instances of the same‑name Unit Status to a Target Entity; instead, it is added to the already applied status.  
When different Appliers apply the same Unit Status to a Target Entity, you must decide whether these statuses can *stack from different Applier sources*:  
If stackable, then after the stacking action is successfully completed, you can enable *Record Latest Applier*.  
If stacking is not allowed, set a *Coexistence Limit* for this status from different Appliers.  
When the Coexistence Limit is reached, define a *Same Name Status Update Strategy* to determine how new applications are handled:   
*Cannot Update* — the status application fails and the action is terminated.  
*Minimum Time Remaining* — remove the status with the shortest Time Remaining, then apply the new one.  
*Earliest Update Time* — removes the status with the earliest last update time, then applies the new status. If the status has not been re-applied, its first application time is used.  
*Earliest Application Time* — remove the status applied earliest, even if its Time Remaining is not the shortest, then apply the new one.

## 6. Yielding and Replacement

![](../../images/21695e0ee946af50.png)  
When applying a status, the *Yielding Status List* may affect the outcome of the application, and the *Replacement Status List* may affect the statuses held by the target Entity.  
If the target already holds any Unit Status from the Yielding Status List, the application is immediately terminated and fails.  
If the target already holds any Unit Status from the Replacement Status List, all corresponding statuses are removed before the new status is applied.

# III. Unit Status Execution

## 1. Apply via Component

![](../../images/8e381eab7f19e2df.png)

If a preset Unit Status is configured in the target Entity's *Unit Status Component*, the corresponding status is applied by the Stage Entity when the Entity is created.  
The Stack Layers Count for the status can be configured in the component, and statuses are applied in the top-to-bottom order of the configuration.  
The same status can only be applied once within the component.

For details, please refer to [Unit Statuses](/ys/ugc/tutorial//detail/mhd7nxrfa8im)

## 2. Manage with Server Nodes

![](../../images/26d71076666e5cf5.png)![](../../images/24fca2444d67dc36.png)  
When both the Applier Entity and the Target Entity are present, the system attempts to apply the corresponding Unit Status to the target and returns one of the following results:  
*Failed: Unexpected error* — failure due to special cases, such as the Applier or Target not being present in the scene  
*Failed: Operation paused for another process* — the target already holds one or more statuses from the Yielding Status List; the application does not proceed  
*Failed: Maximum coexistence limit reached* — the target has already reached the coexistence limit for statuses from other Appliers, and replacement is not allowed  
*Failed: Unable to add additional stack* — when attaching to the target's existing status, all stacks are full and updates are not accepted  
*Success: New status applied* — a new status is applied to the target  
*Success: Slot stacking* — an existing status on the target is updated

**Usage of Unit Status Parameter Dictionary**

Some unit statuses can be pre-defined with override tags. In the actual use of the [Add Unit Status] node, a parameter dictionary can be dynamically passed in. If the dictionary contains a key that matches the override tag, the unit status configuration value will take effect according to the value associated with that key. Note: Dynamic property modifications cannot coexist with the original version; only one can be set.

**Example**: The initial configuration value for attack power correction is 10, and an override tag `delta` is defined. If the configuration value is modified using a parameter dictionary in the node graph, the ATK correction value will become 20 after the node logic takes effect.

![](../../images/b0c2778782ea42c7.png)

![](../../images/de3b7586c5c93698.png)![](../../images/16b7ac14900820d8.png)![](../../images/a555a8a82c4547e6.png)  
When the Remover Entity is present, the system attempts to remove the corresponding status from the Target Entity.  
When the removal target holds one or more coexisting statuses, you can choose:  
*All Coexisting Statuses With the Same Name* — regardless of whether the Applier is self, all statuses with the same name held by the target are removed  
*Status With Fastest Stack Loss* — if stacks are timed independently, remove the status whose first stack has the shortest Time Remaining; if stacks are not timed independently, remove the status with the shortest Time Remaining  
(Not available) statuses applied by self — if the target holds a status whose Applier matches self, remove it

![](../../images/288cd279d841a4c1.png)  
When the target entity gains a new unit status or an existing unit status is updated, this event will be triggered.

![](../../images/3702ae8070d44968.png)![](../../images/bacb2cd0c091612a.png)  
When the Target Entity loses an existing Unit Status, this Event is dispatched.  
If multiple coexisting statuses on the target are removed, the same number of Events is received.  
Removal reasons include:  
 *Replaced by other Unit Status* — a new status was applied, replacing this status  
 *Duration exceeded* — the status exceeded its Initial Runtime Duration, or all stacks exceeded their Initial Runtime Duration and ended naturally  
 *Dispelled* — the status was forcibly terminated by a Skill, an Ability Unit, or a fully reacted Element  
 *Status expired* — the status removed itself because some of its effects ended  
 *Class changed* — the Player switched Class, removing statuses attached to the previous Class

![](../../images/3bb71d0ab4d41bf4.png)  
You can search whether the Target Entity present in the scene already holds a given Unit Status

## 3. Manage with Ability Units

![](../../images/e0fa923e2b102edb.png)

![](../../images/df9f673343c41ba9.png)

Add or remove specified Unit Statuses in the Local Projectile's Ability Unit.

![](../../images/12be747dfbe82b50.png)  
When the Local Projectile hits the Target, use the Ability Unit to add or remove Unit Statuses on the Target

For details, see [Ability Units](/ys/ugc/tutorial//detail/mh0ucw9e76f6)

## 4. Manage with Skill Node Graphs

![](../../images/359bf87cccd99f02.png)  
When both the Applier Entity and the Target Entity are present, attempt to apply the corresponding Unit Status to the Target, but the final result cannot be determined.

![](../../images/5e1e71f5e098709c.png)

Regardless of whether the Remover Entity is present, attempt to remove the corresponding Unit Status from the Target. If the Remover Entity is not present, the removal is treated as source-less.  
Regardless of the Applier, all statuses with the same Config ID are removed.
