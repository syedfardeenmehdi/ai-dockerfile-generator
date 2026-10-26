
from pathlib import Path


def detect_project_type(project_path):
    project = Path(project_path)

    if not project.exists():
        return "Error: Directory does not exist"

    if not project.is_dir():
        return "Error: Path is not a directory"

    has_python = (
        (project / "requirements.txt").is_file()
        or (project / "pyproject.toml").is_file()
    )

    has_node = (project / "package.json").is_file()

    if has_python and has_node:
        return "Error: Both Python and Node.js project files found"

    if has_python:
        return "Python"

    if has_node:
        return "Node.js"

    return "Unknown"


def generate_dockerfile(project_path, project_type):
    project = Path(project_path)

    if project_type == "Python":
        dockerfile = """FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
"""

    elif project_type == "Node.js":
        dockerfile = """FROM node:22-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
"""

    else:
        return "Error: Unsupported project type"

    dockerfile_path = project / "Dockerfile"
    dockerfile_path.write_text(dockerfile, encoding="utf-8")

    return f"Dockerfile created at: {dockerfile_path}"


def generate_dockerignore(project_path):
    project = Path(project_path)

    dockerignore = """\
.git
.venv
venv
__pycache__
*.pyc
node_modules
.env
.vscode
.idea
"""

    dockerignore_path = project / ".dockerignore"
    dockerignore_path.write_text(dockerignore, encoding="utf-8")

    return f".dockerignore created at: {dockerignore_path}"


if __name__ == "__main__":
    print("AI Dockerfile Generator")

    project_path = input(
        "Enter the path to your application folder: "
    ).strip()

    project_type = detect_project_type(project_path)

    if project_type.startswith("Error:"):
        print(project_type)

    elif project_type == "Unknown":
        print("Could not identify the project type.")

    else:
        print(f"Detected project type: {project_type}")

        dockerfile_result = generate_dockerfile(
            project_path, project_type
        )
        print(dockerfile_result)

        dockerignore_result = generate_dockerignore(project_path)
        print(dockerignore_result)
