# Calculator DevOps Project

A simple Python calculator project with a Docker-based CI environment, a Jenkins
pipeline, and a GitHub Actions workflow. The calculator supports addition,
subtraction, and multiplication of two positive integers.

## Calculator API

The AWS SAM template defines a Lambda function with three POST routes:

| Route | Request body | Successful response |
| --- | --- | --- |
| `/add` | `{"a": 10, "b": 5}` | `{"result": 15}` |
| `/subtract` | `{"a": 10, "b": 5}` | `{"result": 5}` |
| `/multiply` | `{"a": 10, "b": 5}` | `{"result": 50}` |

Both inputs must be positive integers. The Lambda handler returns HTTP 400 for
invalid inputs and HTTP 404 for an unknown route.

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── github-actions.yml  # GitHub Actions CI
├── github-actions/
│   └── README.md              # GitHub Actions notes
├── src/
│   ├── app.py                 # Lambda handler
│   └── calculator.py          # Calculator operations
├── tests/
│   └── test_calculator.py     # Unit tests
├── Dockerfile                 # Python/SAM build image used for CI
├── Jenkinsfile                # Jenkins pipeline
├── requirements.txt           # Python test dependencies
└── template.yaml              # AWS SAM application definition
```

## Run tests locally

Install the Python dependency and run the unit tests:

```bash
python -m pip install -r requirements.txt
python -m pytest
```

## CI pipelines

### Jenkins

The existing `Jenkinsfile` builds the Docker image, installs requirements,
runs pytest, and runs AWS SAM validation and build commands. It does not deploy
the application.

### GitHub Actions

The workflow at `.github/workflows/github-actions.yml` runs on every push. It
builds the Docker image and runs pytest inside a container. It does not run SAM
commands, use AWS credentials, or deploy the application. GitHub requires
workflow files to be stored under `.github/workflows/`.

## Docker

Build the CI image from the repository root:

```bash
docker build --tag calculator-ci .
```

Run dependency installation and the unit tests inside the image:

```bash
docker run --rm calculator-ci bash -lc "pip install -r requirements.txt && python -m pytest"
```

Docker Desktop or another Docker Engine must be running to build and run the
container.

## AWS/SAM scope

`template.yaml` describes an AWS SAM Lambda/API application. The current
GitHub Actions workflow does not interact with AWS or deploy that template.
The Jenkins pipeline validates and builds the SAM application but also does
not deploy it.
