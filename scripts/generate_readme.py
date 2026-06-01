from pathlib import Path

solutions = sorted(Path("solutions").glob("*"))

content = "# LeetCode Solutions\n\n"
content += f"Total Problems Solved: {len(solutions)}\n\n"

for file in solutions:
    content += f"- {file.name}\n"

Path("README.md").write_text(content)