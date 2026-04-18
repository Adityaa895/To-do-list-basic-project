from setuptools import setup, find_packages

setup(
    name="aditya-todo-list",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "todo-gui=todo_list.main:main",
        ],
    },
    author="Aditya Singh",
    description="A simple To-Do List GUI app built during my Python learning journey, focusing on clean code, structure, and practical use.",
    python_requires=">=3.7",
)