# GitHub Actions CI

The workflow at `.github/workflows/github-actions.yml` runs on every push. It
builds the repository's existing Docker image, installs the Python
requirements inside the container, and runs the unit tests with pytest.

This workflow does not use AWS or deploy the application. The existing Jenkins
files and pipeline are unchanged.
