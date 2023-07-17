# pre-commit-hooks
A common set of pre-commit hooks for various programming languages. It stores a centralized configuration that can be reused by multiple projects.

# Usage
Add any hooks listed in the `.pre-commit-hooks.yaml` to your `pre-commit-config.yaml`, e.g.:
```yaml
repos:
  - repo: https://github.com/TCLResearchEurope/ctw-pre-commit-hooks
    rev: v1.0.0
    hooks:
      - id: ctw-general-hooks
      - id: ctw-python-hooks
      - id: ctw-typescript-hooks
```

Currently available hooks are:
- `ctw-general-hooks` - Language agnostic hooks. Suitable for any repository.
- `ctw-python-hooks` - Python-related hooks. Suitable for repositories with Python code.
- `ctw-typescript-hooks` - Typescript-related hooks. Suitable for repositories with TypeScript code.

> Some of the hooks copy configuration files to the root directory of your repository, e.g. flake8. It allows you to install these tools in your workspace and have them check the code directly in IDE rather than waiting for pre-commit to do it.

# Development

If you want to quickly test the changes without pushing to the remote, you can use the `pre-commit try-repo` command for interactive development. Alternatively, you can modify the config so that `repo` points to the local version of this repository and set `rev` to your branch or commit SHA, e.g.:

```yaml
repos:
  - repo: /your/workspace/ctw-pre-commit-hooks/
    rev: your-branch
    hooks:
      - id: ctw-general-hooks
      - id: ctw-python-hooks
      - id: ctw-typescript-hooks
```

# Release
Follow the steps below to release a new version of CTW pre-commit hooks:
1. Modify the source-code.
2. Describe the changes and bump the version in `CHANGELOG.md` according to [SemVer](https://semver.org/).
3. Go through the merge request cycle.
4. Tag the new release after merging to main.

# Maintainers
CTW (Cloud Team Warsaw) - Cloud engineers from TCL Research Europe
