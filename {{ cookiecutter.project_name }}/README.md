# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Usage

```bash
just setup                                              # .venv with the project and its dev tools
uv run python -m {{ cookiecutter.package_name }}.part1  # build part1 into build/
just parts                                              # build every part
just check                                              # format check, lint, type check
```

Run the OCP CAD Viewer in VS Code to see each part as it builds.

Pushing a tag such as `v0.1.0` builds the parts and publishes them as a release.
