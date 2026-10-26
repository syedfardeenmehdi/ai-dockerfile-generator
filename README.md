# AI Dockerfile Generator

![CI](https://github.com/syedfardeenmehdi/ai-dockerfile-generator/actions/workflows/ci.yml/badge.svg)

A Python-based developer tool that detects Python and Node.js projects and automatically generates a suitable `Dockerfile` and `.dockerignore` file.

This project demonstrates practical skills in Python automation, Docker, automated testing, Git, GitHub, and CI/CD using GitHub Actions.

> **Note:** The current implementation uses predefined templates and rule-based project detection. AI-powered generation is planned as a potential future enhancement.

## Features

- Detects Python projects using `requirements.txt` or `pyproject.toml`.
- Detects Node.js projects using `package.json`.
- Generates Dockerfiles using predefined templates.
- Generates `.dockerignore` files to exclude unnecessary files.
- Handles missing directories, invalid paths, unknown projects, and conflicting project types.
- Includes automated unit tests using Python's `unittest` framework.
- Automatically runs tests through GitHub Actions on pushes and pull requests.

## Tech Stack

- **Language:** Python 3.13
- **Containerization:** Docker
- **Testing:** Python `unittest`
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions

## Project Structure

```text
ai-dockerfile-generator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── sample-node-app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.js
│   └── package.json
├── sample-python-app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── tests/
│   └── test_generator.py
├── .gitignore
├── main.py
└── README.md
```

## Prerequisites

- Python 3.13 or a compatible Python 3 version.
- Docker Desktop, if you want to build and run the generated containers.
- Git, if you want to clone the repository.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/syedfardeenmehdi/ai-dockerfile-generator.git
cd ai-dockerfile-generator
```

### 2. Run the Generator

```bash
python main.py
```

When prompted, enter the path to your application directory.

For the Python sample:

```text
sample-python-app
```

The generator detects the project type and creates a `Dockerfile` and `.dockerignore` in the selected application directory.

For the Node.js sample, run the generator again and enter:

```text
sample-node-app
```

> **Note:** Running the generator on a sample directory overwrites its existing generated `Dockerfile` and `.dockerignore` files.

## Run the Tests

From the project root, run:

```bash
python -m unittest discover -s tests -v
```

The test suite checks project detection, invalid paths, conflicting project types, Dockerfile generation, and `.dockerignore` generation.

## Build and Run the Sample Applications

### Python Sample

Build the Docker image:

```bash
docker build -t ai-dockerfile-demo:latest ./sample-python-app
```

Run the container:

```bash
docker run --rm -p 5000:5000 ai-dockerfile-demo:latest
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Node.js Sample

Build the Docker image:

```bash
docker build -t ai-dockerfile-node-demo:latest ./sample-node-app
```

Run the container:

```bash
docker run --rm -p 3001:3000 ai-dockerfile-node-demo:latest
```

Open [http://localhost:3001](http://localhost:3001) in your browser.

If a host port is already in use, choose another available host port and update the port mapping and browser URL accordingly.

## Continuous Integration

GitHub Actions automatically runs the unit tests when code is pushed or a pull request is opened.

**Workflow file:** `.github/workflows/ci.yml`

The CI badge at the top of this README displays the workflow status. It will reflect the actual result once the workflow runs successfully or fails.

## What I Learned

- Automating repetitive Docker configuration tasks using Python.
- Detecting project types from application files.
- Generating Dockerfiles and Docker ignore rules.
- Writing and running automated unit tests.
- Using Git and GitHub for version control and collaboration.
- Configuring CI workflows using GitHub Actions.

## Future Improvements

- Add AI-assisted Dockerfile recommendations through an AI API.
- Validate generated Dockerfiles and project dependencies.
- Support additional programming languages and frameworks.
- Add more test cases and security checks.
- Develop a web interface for generating Dockerfiles.

## Author

**Fardeen Mehdi**

- GitHub: [syedfardeenmehdi](https://github.com/syedfardeenmehdi)
- Project Repository: [AI Dockerfile Generator](https://github.com/syedfardeenmehdi/ai-dockerfile-generator)

---

*Built as a hands-on project to practise Python automation, Docker, testing, and DevOps CI/CD workflows.*
