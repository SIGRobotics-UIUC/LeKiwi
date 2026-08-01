# /// script
# dependencies = [
#   "manifold3d==3.5.2",
#   "numpy==2.5.1",
# ]
# ///

"""Generate the lower-plate adapter for the Yahboom Pi 5 power board.

The 65 x 56 mm board uses the Raspberry Pi 58 x 49 mm mounting pattern. The
adapter's 40 x 40 mm pattern fits the LeKiwi base plate's 20 mm hole grid.

Run with:
    uv run generate_pi5_power_board_adapter.py
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path

import numpy as np
from manifold3d import Manifold

PLATE_WIDTH = 72.0
PLATE_DEPTH = 63.0
PLATE_HEIGHT = 3.0
CORNER_RADIUS = 4.0

BASE_HOLE_SPACING = (40.0, 40.0)
BASE_HOLE_DIAMETER = 3.5
BOARD_HOLE_SPACING = (58.0, 49.0)
BOARD_HOLE_DIAMETER = 2.8
CIRCULAR_SEGMENTS = 64


def rounded_plate() -> Manifold:
    width, depth, height = PLATE_WIDTH, PLATE_DEPTH, PLATE_HEIGHT
    radius = CORNER_RADIUS
    solid = Manifold.cube((width - 2 * radius, depth, height), center=True)
    solid += Manifold.cube((width, depth - 2 * radius, height), center=True)
    for x in (-width / 2 + radius, width / 2 - radius):
        for y in (-depth / 2 + radius, depth / 2 - radius):
            solid += Manifold.cylinder(
                height, radius, circular_segments=CIRCULAR_SEGMENTS, center=True
            ).translate((x, y, 0))
    return solid


def hole_pattern(spacing: tuple[float, float], diameter: float) -> Manifold:
    holes = Manifold()
    for x in (-spacing[0] / 2, spacing[0] / 2):
        for y in (-spacing[1] / 2, spacing[1] / 2):
            hole = Manifold.cylinder(
                PLATE_HEIGHT + 2,
                diameter / 2,
                circular_segments=CIRCULAR_SEGMENTS,
                center=True,
            ).translate((x, y, 0))
            holes += hole
    return holes


def build_adapter() -> Manifold:
    adapter = rounded_plate()
    adapter -= hole_pattern(BASE_HOLE_SPACING, BASE_HOLE_DIAMETER)
    adapter -= hole_pattern(BOARD_HOLE_SPACING, BOARD_HOLE_DIAMETER)
    return adapter


def write_binary_stl(solid: Manifold, output: Path) -> None:
    mesh = solid.to_mesh()
    vertices = np.asarray(mesh.vert_properties, dtype=np.float32)[:, :3]
    triangles = np.asarray(mesh.tri_verts, dtype=np.uint32)

    with output.open("wb") as stl:
        stl.write(b"LeKiwi Pi 5 power board adapter".ljust(80, b"\0"))
        stl.write(struct.pack("<I", len(triangles)))
        for triangle in triangles:
            points = vertices[triangle]
            normal = np.cross(points[1] - points[0], points[2] - points[0])
            length = np.linalg.norm(normal)
            if length:
                normal /= length
            stl.write(struct.pack("<12fH", *normal, *points.flat, 0))


def main() -> None:
    default_output = (
        Path(__file__).resolve().parent.parent / "pi5_power_board_adapter.stl"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()

    adapter = build_adapter()
    if adapter.is_empty():
        raise RuntimeError("adapter generation produced an empty solid")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_binary_stl(adapter, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
