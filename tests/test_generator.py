
import sys
import tempfile
import unittest
from pathlib import Path

# Allow the tests to import main.py from the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import main


class TestDockerfileGenerator(unittest.TestCase):

    def test_detect_python_project(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir)
            (project / "requirements.txt").write_text(
                "Flask\n", encoding="utf-8"
            )

            self.assertEqual(
                main.detect_project_type(project), "Python"
            )

    def test_detect_node_project(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir)
            (project / "package.json").write_text(
                '{"name": "test-app"}', encoding="utf-8"
            )

            self.assertEqual(
                main.detect_project_type(project), "Node.js"
            )

    def test_missing_directory(self):
        missing_path = (
            Path(tempfile.gettempdir())
            / "docker-generator-path-that-does-not-exist-12345"
        )

        self.assertEqual(
            main.detect_project_type(missing_path),
            "Error: Directory does not exist",
        )

    def test_file_path_instead_of_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "app.js"
            file_path.write_text("", encoding="utf-8")

            self.assertEqual(
                main.detect_project_type(file_path),
                "Error: Path is not a directory",
            )

    def test_unknown_project(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.assertEqual(
                main.detect_project_type(temp_dir), "Unknown"
            )

    def test_both_project_types(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir)
            (project / "requirements.txt").write_text(
                "Flask\n", encoding="utf-8"
            )
            (project / "package.json").write_text(
                '{"name": "test-app"}', encoding="utf-8"
            )

            self.assertEqual(
                main.detect_project_type(project),
                "Error: Both Python and Node.js project files found",
            )

    def test_generate_node_dockerfile(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = main.generate_dockerfile(temp_dir, "Node.js")
            dockerfile = Path(temp_dir) / "Dockerfile"

            self.assertTrue(dockerfile.is_file())
            self.assertIn("FROM node:22-alpine", dockerfile.read_text())
            self.assertIn("CMD [\"npm\", \"start\"]", dockerfile.read_text())
            self.assertIn("Dockerfile created at:", result)

    def test_generate_dockerignore(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = main.generate_dockerignore(temp_dir)
            dockerignore = Path(temp_dir) / ".dockerignore"

            self.assertTrue(dockerignore.is_file())
            self.assertIn(".env", dockerignore.read_text())
            self.assertIn("node_modules", dockerignore.read_text())
            self.assertIn(".git", dockerignore.read_text())
            self.assertIn(".dockerignore created at:", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
