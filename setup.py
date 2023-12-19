import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="Chicken_Disease_Classification"
Author_User_Name="Ricky2054"
SRC_REPO="cnnClassifier"
Author_email="deyricky36@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_email,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_User_Name}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)