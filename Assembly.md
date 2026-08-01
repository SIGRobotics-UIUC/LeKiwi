# Assembly
> **Estimated time:** 2 hours

*Exact component placements can be visualized in the [Fusion360 Online CAD](https://a360.co/4k1P8yO)*

*We assume you already have a [SO-100/SO-101 Arm](https://github.com/TheRobotStudio/SO-ARM100) built*
### 1. Assemble Wheel Modules (3 per robot)

1. Attach the drive motor to the motor mount using 4 m2x5 tap screws.

    <img src="media/assembly_imgs/DSC00001.jpg" width="300" />

2. Screw the drive motor mount onto the bottom base plate using 4 m3x12 machine screws.

    <img src="media/assembly_imgs/DSC00002.jpg" width="300" />

3. Attach the wheel hub to the omniwheel using 2 m4x12 machine screws.

    <img src="media/assembly_imgs/DSC00004.jpg" width="300" />

4. Attach the servo horn to the wheel hub using 2 m3x16 machine screws.

    <img src="media/assembly_imgs/DSC00005.jpg" width="300" />
    <img src="media/assembly_imgs/DSC00006.jpg" width="300" />

5. Attach the servo horn to the drive motor using 1 m3x6 machine screw.

    <img src="media/assembly_imgs/DSC00003.jpg" width="300" />

With all 3 modules attached to the bottom base plate:

<img src="media/assembly_imgs/DSC00007.jpg" width="350" /> <img src="media/assembly_imgs/DSC00008.jpg" width="350" />

### 2. Bottom Plate Assembly
1. Insert m3 nuts into the mounts for the servo controller and battery mounts. Screw both onto the bottom base plate with 4 m3x12 machine screws.

    <img src="media/assembly_imgs/IMG_1922.jpg" width="400" /> <img src="media/assembly_imgs/IMG_1926.jpg" width="400" />
2. Add the servo driver and attach the wires to the 3 drive servos.

    <img src="media/assembly_imgs/IMG_1927.jpg" width="400" />
3. Wiring Electronics
   - For the **12V version**:
   Disconnect the battery before working on the power wiring. Print the [Pi 5 power board adapter](3DPrintMeshes/pi5_power_board_adapter.stl), and mount it in the lower-right electronics bay using four M3x16 screws and four M3 nuts. The adapter uses the base-plate grid holes at `(40,-60)`, `(40,-20)`, `(80,-60)`, and `(80,-20)` mm in the STL coordinate system. Attach the power board to the adapter's 58x49mm hole pattern using its included M2.5 hardware. Keep the screw terminal and USB-C output facing toward the center of the robot.

   Use the Wago lever connectors to split the battery positive and ground leads between the servo power circuit, DC barrel plug adapter, and Pi 5 power board. Connect the power-board branch to the `+` and `-` screw-terminal inputs, checking polarity before reconnecting the battery. Connect the board's USB-C output to the Raspberry Pi 5 with the 0.5m, e-marked 5A USB-C cable. Do not use a USB-A cable for this connection.

   The board requires at least 7V input for its full 5V/5A output, so it must connect to the 12V battery branch rather than a regulated 5V rail. After booting the Pi, check that the negotiated current is 5000mA and that no undervoltage event is reported:

   ```bash
   od -An -tu4 --endian=big /proc/device-tree/chosen/power/max_current
   vcgencmd get_throttled
   ```

   The expected outputs are `5000` and `throttled=0x0`. Do not force `usb_max_current_enable=1` to hide a cable or power-board problem.

   ```mermaid
   flowchart LR
       battery[12V battery] --> split[Wago split]
       split --> servos[12V servo circuit]
       split --> barrel[DC barrel adapter]
       split --> board[Pi 5 power board]
       board -->|5V/5A e-marked USB-C cable| pi[Raspberry Pi 5]
   ```

    - For the **5V version**: you can use the powerbamk holder to keep the powerbank in place `3DPrintMeshes/5v_specific/5v_power_bank_holder.stl`. The powerbank can be mounted in the back on the lower plate.

        <img src="media/assembly_imgs/IMG_7.jpg" width="400" />
        
      The cables can be connected  according to following diagram:
      
        <img src="media/assembly_imgs/Slide1.jpeg" width="400" />

### 3. Top plate Assembly
1. Place the raspberry pi 5 into the pi case bottom and snap on the top part of the case. 
2. Attach the Pi to the top base plate using 2 m3x12 machine screws and mount the SO-101 arm with 4 m3x20 machine screws. Using our modified SO-101 base or the original will work as there are holes for both in the plate.

    <img src="media/assembly_imgs/IMG_1929.jpg" width="400" />

- For the **Wired version**: you can print these two parts: `3DPrintMeshes/wired_specific/cable_holder v0.stl` and `3DPrintMeshes/wired_specific/usb_connector_case v1.stl` and assemble them like the images below. It is **very important** to plug the usb-c cable in the way like the images. Thus the `UGreen` logo on the same side as `20GBS, 240W` logo side. And the `20GBS, 240W` side on top into your laptop. If the usb-c extenstion cable can't find your camera's or motor controller board, the cable orientation is probably wrong and should be flipped 180 degrees!

    Add cable holder and usb hub holder like this:

    <img src="media/assembly_imgs/WIRED4.jpeg" width="400" />

    Attach cables for 2 camera's motor control board and usb-c extender like this (important!):

    <div style="display: flex; align-items: flex-start;">
     <img src="media/assembly_imgs/WIRED1.jpeg" width="30%" alt="Wired Step 1" />
     <img src="media/assembly_imgs/WIRED2.jpeg" width="30%" alt="Wired Step 2" />
     <img src="media/assembly_imgs/WIRED3.jpeg" width="30%" alt="Wired Step 3" />
    </div>


### 4. Final Assembly
1. Feed the servo controller usb-c to usb-a, 5v usb-c power, and SO0-101 servo wires through the hole in the top base plate. 

    <img src="media/assembly_imgs/IMG_1930.jpg" width="300" />

2. Mount the top base plate onto the motor mounts using 4 m3x12 machine screws.

    <img src="media/assembly_imgs/IMG_1933.jpg" width="400" />

### 5: Attach Cameras
*Note: The mounts we designed are specific to the cameras we chose. They may need to be modified for different camera modules.*
#### (Option 1) Mounting Arducam
For these [camera's](https://www.amazon.com/Arducam-Camera-Computer-Without-Microphone/dp/B0972KK7BC) you can print these parts 1x `3DPrintMeshes/base_camera_mount.stl` and 1x `3DPrintMeshes/wrist_camera_mount.stl`.
1. Screw the base camera mount onto the bottom base plate(attach the arducam 5MP wide angle camera to the mount with 2 m2.5x12 machine screws). The cable for the camera mount can also be fed through the cutout

    <img src="media/assembly_imgs/IMG_1935.jpg" width="300" />
2. Screw the wrist camera mount to the static gripper using 4 m2x5 tap screws(attach the arducam 5MP wide angle camera to the mount with 2 m2.5x12 machine screws)

    <img src="media/assembly_imgs/IMG_1934.jpg" width="300" />

#### (Option 2) Mounting Webcam
For these [camera's](https://www.amazon.fr/Vinmooog-equipement-Microphone-Enregistrement-conférences/dp/B0BG1YJWFN/) you can print these parts 1x `3DPrintMeshes/webcam_mount/webcam_mount.stl`, 1x `3DPrintMeshes/webcam_mount/so100_gripper_cam_mount_insert.stl` and 1x `3DPrintMeshes/webcam_mount/webcam_mount_wrist.stl`. These can be used to attach a wrist and base camera to LeKiwi.

1. Print the new gripper with insert for the M3 nut, and insert the nut. Then insert the motor and attach gripper. 

    <img src="media/assembly_imgs/IMG_1.jpg" width="300" />
2. Now take the camera mount `3DPrintMeshes/webcam_mount/webcam_mount_wrist.stl`, and add a M3x12mm bolt and screw it firmly until it locks with the M3 nut in the gripper. Then insert your camera in the mount and add 2x M3x35mm bolts in the back holes to lock the camera in place, use 2 nuts that you insert in the slots to lock the bolts.

    <img src="media/assembly_imgs/IMG_3.jpg" width="200" />

3. Do the same for the base camera `3DPrintMeshes/webcam_mount/webcam_mount.stl` and attach it to the front of LeKiwi.

    <img src="media/assembly_imgs/IMG_2.jpg" width="300" />


### Plug everything in and its ready!
Power the electronics by plugging in the DC barrel plug adapter to the servo motor controller and the 5v usb-c connector to the raspberry pi 5. The usb cables from the servo controller and the cameras can directly be plugged in to the raspberry pi.

<img src="media/assembly_imgs/IMG_1940.jpg" width="400" /> <img src="media/assembly_imgs/IMG_1938.jpg" width="400" />
