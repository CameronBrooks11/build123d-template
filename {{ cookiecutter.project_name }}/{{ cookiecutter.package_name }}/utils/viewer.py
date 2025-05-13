from build123d import BuildLine, BuildPart, BuildSketch
from ocp_vscode import (
    Camera,
    ColorMap,
    set_colormap,
    set_defaults,
    set_port,
    show_all,
    show_clear,
)

from {{ cookiecutter.package_name }}.utils.config import VIEWER_DEFAULTS, VIEWER_PORT


def setup_viewer():
    set_port(VIEWER_PORT)
    show_clear()

    set_defaults(
        reset_camera=Camera.KEEP
        if VIEWER_DEFAULTS["reset_camera"] == "keep"
        else Camera.RESET,
        ortho=VIEWER_DEFAULTS["ortho"],
        black_edges=VIEWER_DEFAULTS["black_edges"],
    )

    set_colormap(ColorMap.seeded(**VIEWER_DEFAULTS["colormap"]))

    return (BuildPart, BuildSketch, BuildLine)


def viewer_running(port=VIEWER_PORT):
    import socket

    try:
        sock = socket.create_connection(("localhost", port), timeout=1)
        sock.close()
        return True
    except Exception:
        return False


def debug_show_locals(classes, slocal=False):
    import inspect

    frame = inspect.currentframe()
    if frame is None or frame.f_back is None:
        return

    caller_locals = frame.f_back.f_locals
    variables = list(caller_locals.items())

    s_o, s_n = [], []
    for name, obj in variables:
        if isinstance(obj, classes) and not name.startswith(("_", "cf")):
            if getattr(obj, "_obj_name", "") == "sketch" or slocal:
                s_o.append(obj)
                s_n.append(f"{name} ({obj._obj_name})")
            elif hasattr(obj, "sketch"):
                s_o.append(obj.sketch)
                s_n.append(f"{name} ({obj._obj_name})")
    if s_o:
        show_all(*s_o, names=s_n, reset_camera=Camera.KEEP)
