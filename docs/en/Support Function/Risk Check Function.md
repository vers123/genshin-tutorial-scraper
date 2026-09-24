---
title: Risk Check Function
path_id: mhgi4lrlrvj2
updated_at: 2026-09-11 10:55:58
category: Support Function
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhgi4lrlrvj2
---

# I. What Is the Risk Check Function

The *Risk Check function* can be used to check the Wonderland that the Craftsperson is currently working on. If the check reveals that the Wonderland has been set up with methods that are discouraged, or has violated certain hidden rules, warnings and explanations will be displayed.

The differences between the Risk Check function and *Playtest Verification* are as follows: Errors found in Playtest Verification will prevent the playtest from running normally. These are relatively serious errors that can cause features to stop working properly. In contrast, warnings from Risk Check generally relate to data errors and will not block the playtest or affect normal operations.

# II. How to Use the Risk Check Function

## 1. How to Enter

Click "Risk Check" in the System Menu to open the Risk Check interface.

![](../images/19d395da877ad08f.png)

## 2. Interface Guide

![](../images/fda7e26ea1f07894.png)

Click "Run Check" to check the current Wonderland.

![](../images/3ca0630a208c54d1.png)

The time on the left shows when that check was started.

The maximum number of check records that can be saved in the history is 5. If there are more than 5, the newest record will replace the oldest check record. Check records are saved only for the current edit session. Reloading a save will clear previous records.

The right side shows all risk items found in the current Wonderland.

# III. Special Notes

The message "Operation flow connections crosses logical sub-graphs" refers to the case shown in the red box below: operation flow data from the lower logic sub-graph is linked to the operation flow in the upper logic sub-graph, which will cause data transfer errors.

![](../images/1198dc304cd48df5.png)

![](../images/48bd828d5adb9219.png)
