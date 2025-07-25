# build123d-template

A Cookiecutter template for build123d CAD projects.

## Quickstart

### Create Project from Cookie Cutter Template

```bash
pip install cookiecutter
cookiecutter https://github.com/CameronBrooks11/build123d-template.git
```

You will be prompted for six values—here’s how to fill them:

- **project_name**  
  The name of your project directory and GitHub repo. Use hyphens, not spaces (e.g. `my-cad-project`).

- **package_name**  
  The Python import name. Must be a valid identifier (lowercase, underscores only), matching `project_name` with hyphens replaced by underscores (e.g. `my_cad_project`).

- **author_name**  
  Your full name for metadata (e.g. `Jack Daniel`).

- **email**  
  Your contact email (e.g. `jdrocks@email.com`).

- **version**  
  Typically this should be the initial version using [SemVer](https://semver.org/) (e.g. `0.1.0`).

- **project_description**  
  A short, descriptive tagline for your project (e.g. `A build123d CAD project for robotics prototypes`).

Next navigate into your newly created project using the `project_name` you entered:

```bash
cd project_name
```

### Initialize Git and make your first commit

Start by initializing a new git repository and commit the initial contents of your newly created project template:

```bash
git init
git add .
git commit -m "Initial cookiecutter scaffold"
```

### Method 1: Using GitHub CLI (API auth)

If you have the GitHub CLI installed and authenticated via `gh auth login`, run:

```bash
gh repo create OWNER/project_name --public --source . --remote origin --push
```

### Method 2: Using HTTPS & Personal Access Token

If you prefer standard Git commands, do:

```bash
git branch -M main
git remote add origin https://github.com/OWNER/project_name.git
git push -u origin main
```

> You will be prompted for your GitHub username and a personal access token (PAT) when pushing over HTTPS.

## Usage

Once your project is scaffolded and you’ve initialized git, you’ll want to run and develop your CAD scripts using the build123d workflow.

### 1. Install the Project in Editable Mode

Editable installs ensure that your local code changes are immediately available when you run the package. From the project root, run:

pip install -e .

This makes your package (e.g. flowcell_manifold) importable system-wide, which fixes ModuleNotFoundError issues when running scripts.

### 2. Run a Script

- You can now run your CAD generation scripts using:

  - `python -m flowcell_manifold.part1`

- This approach ensures that Python treats flowcell_manifold as a proper package and sets up the import paths correctly.

### 3. Exporting CAD Files

By default, the script (e.g. part1.py) will:

- Generate the part geometry.

- Attempt to show it in the build123d viewer (if available).

- Export the part as part1.stl and part1.step into the build folder located at:

  - `<project_root>/build/`

### 4. Adding New Parts

To create a new part:

- Add a new Python file (e.g. part2.py) in the flowcell_manifold directory.

- Follow the structure of part1.py with a Spec dataclass and make_part() function.

- Run it with:

  - `python -m flowcell_manifold.part2`
