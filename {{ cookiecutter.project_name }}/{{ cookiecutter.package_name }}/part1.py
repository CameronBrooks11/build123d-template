"""part1: a cylinder, the starting point for a part.

Run it with `python -m {{ cookiecutter.package_name }}.part1`. It writes part1.stl
and part1.step to build/, and shows the part in the OCP CAD Viewer when the
viewer is running.
"""

from dataclasses import dataclass
from pathlib import Path

import build123d as bd
from build123d_ease import show
from loguru import logger

from {{ cookiecutter.package_name }}.utils.export import export_part
from {{ cookiecutter.package_name }}.utils.viewer import (
    debug_show_locals,
    setup_viewer,
    viewer_running,
)


@dataclass
class Part1Spec:
    """The dimensions of part1, in millimetres."""

    radius: float = 20
    height: float = 20

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError(f"radius must be positive, got {self.radius}")
        if self.height <= 0:
            raise ValueError(f"height must be positive, got {self.height}")


def make_part1(spec: Part1Spec) -> bd.Part:
    """Build part1 from its spec."""
    return bd.Cylinder(radius=spec.radius, height=spec.height)


if __name__ == "__main__":
    part1 = make_part1(Part1Spec())

    if viewer_running():
        classes = setup_viewer()
        show(part1)
        debug_show_locals(classes)
    else:
        logger.info("OCP CAD Viewer not running; skipping the preview")

    export_folder = Path(__file__).parent.parent / "build"
    export_folder.mkdir(exist_ok=True)
    export_part(part1, "part1", export_folder)
