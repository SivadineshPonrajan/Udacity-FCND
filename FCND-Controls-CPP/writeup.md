## Project: Controller

---
### Writeup   

The current writeup.md file that you are reading is my writeup for how i overcame each tasks. 


### Implementing the controller

#### scenario 1: Intro Scenario

![Code 1](./animations/scenario1.gif)

Since the thrusts is dependent on mass of the body and it is simply being set to 0.4 . Changing the mass to 0.5 gave the expected pass solution.

---

#### scenario 2: Attitude Control

![Code 1](./animations/scenario2.gif)

The roll pitch controller function is implemented in cpp. Basically it is a P controller. In the rotation matrix the values at the positions R13 and R23 is to be corrected to control the roll and pitch. Thus the kpPQR and kpBank values are altered to get the desired output.

---

#### scenario 3: Position Control

![Code 1](./animations/scenario3.gif)

The altitude control function is implemented in cpp. Basically it is a PID controller. Basically position error is calculated and integrated to find the I term. The velocity is also calculated. Then the corected Z is determined. Then it is used to calculate the thrust and the orientation of the vehicle. Thus the kpPosXY, kpPosZ, KiPosZ, kpVelXY and kpVelZ values are changed. kpPQR and kpBank values are also altered without affecting the other scenario to get the desired output.

---

#### scenario 4: Nonidealities

![Code 1](./animations/scenario4.gif)

The LateralPositionControl function is implemented in cpp. Basically it is a PD controller. The X and Y coordinates are calculated. The position and velocity errors are calculated and optimized below the minimum level. The kpPosXY and the kpVelXY values are altered without affecting the other scenario to get the desired output.

---

#### scenario 5: Trajectory follow

![Code 1](./animations/scenario5.gif)

The yawControl function is implemented in cpp. Basically position error of the quad is optimized. Generally yaw handles the Z movement of the quad. Thus the error is optimized and updated. The kpYaw value is altered without affecting the other scenario to get the desired output.
