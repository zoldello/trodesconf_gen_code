from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent

with open(HERE / "README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    # add requirements here
]

EXTRAS_REQUIRE = {
    "docs": [
        "sphinx>3.1",
        "sphinx-autodoc-typehints",
        "sphinx-rtd-theme",
        "m2r2",  # mdinclude directive
    ],
    "tests": [
        "coverage>=5",  # pyproject.toml support
        "pytest>=6",  # pyproject.toml support
    ],
    "tools": [
        "black",
        "isort",
        "mypy",
        "pylint>=2.5",  # pyproject.toml support
        "tox>=3.4",  # pyproject.toml support
    ],
}

EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["docs"] + EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["tools"]

setup(
    name="trode_config_generator",
    version="0.1.0",
    description="Trodes config generator",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/zoldello/trode_config_generator",
    author="Phil Adenekan",
    author_email="zoldello@live.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        # add keywords here
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    project_urls={
        "Bug Reports": "https://github.com/zoldello/trode_config_generator/issues",
        "Source": "https://github.com/zoldello/trode_config_generator",
    },
)
