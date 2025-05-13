def export_part(part, name, folder):
    from pathlib import Path

    from build123d import Compound, Part, Solid, export_step, export_stl
    from loguru import logger

    assert isinstance(part, (Part, Solid, Compound)), (
        f"{name} is not an expected type ({type(part)})"
    )
    if not part.is_manifold:
        logger.warning(f"Part '{name}' is not manifold")

    folder = Path(folder)
    export_stl(part, str(folder / f"{name}.stl"))
    export_step(part, str(folder / f"{name}.step"))
    logger.success(f"Exported {name}.stl and {name}.step")
