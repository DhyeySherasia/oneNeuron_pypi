import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

username = "DhyeySherasia"
project_name = "oneNeuron_pypi"

# Update the version every time we make a new commit
setuptools.setup(
    name=f"{project_name}-{username}",
    version="0.0.2",
    author=username,
    author_email="dhyeysherasia2002@gmail.com",
    description="An implementation of Perceptron in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{username}/{project_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{username}/{project_name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy"
    ]
)