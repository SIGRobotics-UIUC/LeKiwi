# Assembly
> **Estimated time:** 2 hours

*Exact component placements can be visualized in the [Fusion360 Online CAD](https://a360.co/4iD2gtf)*

*We assume you already have a [Koch Arm](https://github.com/jess-moss/koch-v1-1) built*
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

2. Add the servo driver and attach the wires to the 3 drive servos.

    <img src="media/assembly_imgs/IMG_2006.jpg" width="400" />
3. Wiring Electronics
   -    Use the wago lever connectors to connect the ground and power battery wire leads to the leads of the 12v->5v converter and the dc barrel plug adapter. Screw on the 12v to 5v converter to the bottom base plate with 2 m3x16 machine screws and 2 m3 nuts.

        <img src="media/assembly_imgs/IMG_1925.jpg" width="400" /> <img src="media/assembly_imgs/IMG_2007.jpg" width="400" />


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

    <img src="media/assembly_imgs/IMG_2007.jpg" width="400" />

### 5: Attach Cameras
*Note: The mounts we designed are specific to the cameras we chose. They may need to be modified for different camera modules.*
#### (Option 1) Mounting Arducam
For these [camera's](https://www.amazon.com/Arducam-Camera-Computer-Without-Microphone/dp/B0972KK7BC) you can print these parts 1x `3DPrintMeshes/base_camera_mount.stl` 
1. Screw the base camera mount onto the bottom base plate(attach the arducam 5MP wide angle camera to the mount with 2 m2.5x12 machine screws). The cable for the camera mount can also be fed through the cutout

    <img src="media/assembly_imgs/IMG_1935.jpg" width="300" />

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

<img src="media/assembly_imgs/IMG_2009.jpg" width="400" /> 
