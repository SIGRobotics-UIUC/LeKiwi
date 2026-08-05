# LeKiwi URDF

The URDF uses the standard ROS mobile-base coordinate convention:

- `base_footprint` is the root frame at ground level, with +X forward, +Y left, and +Z up.
- `base_link` has the same orientation and is located at the original CAD origin, 32.937 mm above the ground plane.
- `base_plate_layer1-v5` and its descendants retain their generated CAD frames and names to preserve the existing kinematic tree.

Mesh paths are relative to `LeKiwi.urdf`, so load the model with the `URDF` directory as its base path.
