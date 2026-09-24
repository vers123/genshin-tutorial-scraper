---
title: Projectile Motion Device
path_id: mhr97di71wpg
updated_at: 2025-10-16 21:27:03
category: Concept Introduction/Functions/Common Components
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhr97di71wpg
---

# I. Functions of Projectile Motion Device Component

The Projectile Motion Device component enables entities to perform complex movements

Only one projectile motion device can be active on a component at a time

The position of the *projectile motion device* may vary at each end, therefore it is recommended for use with *projectiles* or motion-based effects

If a disconnection or reconnection occurs, the projectile motion device's position may reset

# II. Add Projectile Motion Devices

![](../../../images/ae10a8c361a55f69.png)

(1) In the entity/prefab editing interface, open the Editing Components tab

(2) Click "Add Common Components" below, select and click "Projectile Motion Device" to add it

(3) Click "Advanced Editing" to expand the editing tab

# III. Projectile Motion Device Types

The Projectile Motion Device currently supports four types

## 1. Linear Projectile

![](../../../images/e652ad141b2f5f59.png)

*Initial Speed*: The velocity direction when the component gets initialized

*Speed*: Speed value

*Acceleration*: The increase in velocity per second

*Acceleration Duration*: The duration for which the acceleration rate takes effect

*Ground Hugging Movement*: Whether the movement is attached to the ground

## 2. Parabolic Projectile

![](../../../images/2e3a402b025c52e8.png)

*Initial Speed*: The velocity direction when the component gets initialized

*Speed*: Speed value

*Gravitational Acceleration*: Vertical downward direction, speed increase value per second

## 3. Tracking Projectile

![](../../../images/9b45fa0b267d5551.png)

*Tracking Object:* The target to track.

*Track Target Attachment Point:* Tracks attachment point on the target.

*Initial Speed*: The velocity direction when the component gets initialized

*Speed*: Speed value

*Acceleration*: The increase in velocity per second

*Acceleration Duration*: The duration for which the acceleration rate takes effect

*Tracking Angular Velocity:* The projectile will turn towards the tracking target at the specified tracking angular velocity from its initial direction. If this value is small, the projectile may not be able to hit the target directly due to the slow turning speed.  
*Tracking Final Phase:* This can be set to one of three types:

*None*: No final stage settings. After reaching the tracking target, the projectile will continue to attempt to track the target, which may cause it to oscillate around the target.

*Cancel Tracking*: When the projectile is within a certain range of the tracking target (configured by *Stop Tracking Range*), it will stop the tracking function and continue in a straight line with the direction it had at that moment. This means the tracking projectile will not hit the target directly. It can be used to create projectiles that players can dodge by moving.

*Stop Tracking Range*: Configures the distance from the tracking target at which the tracking will stop.

*Adsorption Tracking*: When the projectile is within a certain range of the tracking target (configured by *Adsorption Range*), it will try to attach to the target over a fixed period (*Adsorption Time*). After this period, it will move stably with the target. Common tracking projectiles can use this configuration.

*Adsorption Range*: The distance from the tracking target at which the projectile will start to attract.

*Adsorption Time*: The fixed time it takes for the projectile to attach to the tracking target and then move stably with it.

## 4. Radial Fire

![](../../../images/e3077c0923676148.png)

*Around Object*: The object to orbit around.

*Track Target Attachment Point*: Which attachment point on the circular motion target.

*Rotate Clockwise*: When enabled, the object rotates clockwise; when disabled, it rotates counterclockwise.

*Circumradius*: The radius of the circular motion.

*Angular Velocity*: The angular velocity of the circular motion.

# IV. Node Graph Related

Create Projectile

![](../../../images/cc49665e5684f301.png)
