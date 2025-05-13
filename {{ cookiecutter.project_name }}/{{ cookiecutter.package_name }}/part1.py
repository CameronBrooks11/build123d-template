# === Standard Libraries ===
from dataclasses import (
    dataclass,
)  # define structured data containers to define parametric part specifications
from pathlib import (
    Path,
)  # For managing file paths and export locations

# === Core Libraries ===
import build123d as bd  # Main b123d CAD kernel and modeling API
from build123d_ease import (
    show,
)  # b123d helper function to show the CAD model in the CAD viewer.
from loguru import (
    logger,
)  # Rich logging for CLI and debugging
from utils.export import (
    export_part,
)  # Reusable STL/STEP export utility

# === Project Utilities (local modules) ===
from {{ cookiecutter.package_name }}.utils.viewer import (
    debug_show_locals,
    setup_viewer,
    viewer_running,
)

# === CAD spec ===


@dataclass
class Part1Spec:
    """Specification for part1."""

    part1_radius: float = 20

    def __post_init__(self) -> None:  # Validation of parameters
        assert self.part1_radius > 0, "part1_radius must be positive"


def make_part1(spec: Part1Spec) -> bd.Part | bd.Compound:
    """Create a CAD model of part1."""
    p = bd.Part(None)
    p += bd.Cylinder(radius=spec.part1_radius, height=20)
    return p


# === Script Entrypoint ===

if __name__ == "__main__":
    logger.info("Generating part geometry...")

    # Setup optional viewer
    try:
        classes = setup_viewer()
    except Exception as e:
        logger.warning(f"Viewer setup failed: {e}")
        classes = ()

    part1 = make_part1(Part1Spec())

    if viewer_running():
        try:
            show(part1)
        except Exception as e:
            logger.error(f"Failed to show part in viewer: {e}")
    else:
        logger.info("Viewer not running — skipping live show.")

    export_folder = Path(__file__).parent.parent / "build"
    export_folder.mkdir(exist_ok=True)

    export_part(part1, "part1", export_folder)

    try:
        debug_show_locals(classes)
    except Exception as e:
        logger.warning(f"debug_show_locals failed: {e}")
