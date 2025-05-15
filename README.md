# build123d-cad-template

A Cookiecutter template for build123d CAD projects.

## Quickstart

### Create Project from Cookie Cutter Template

```bash
pip install cookiecutter
cookiecutter https://github.com/CameronBrooks11/build123d-cad-template.git
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
