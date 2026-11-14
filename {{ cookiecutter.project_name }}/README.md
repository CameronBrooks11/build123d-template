# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Usage

```bash
just setup                                         # .venv with the project and its dev tools
uv run python -m {{ cookiecutter.package_name }}.part1    # build part1 into build/
just check                                         # format check, lint, type check
```
