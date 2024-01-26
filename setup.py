import setuptools

# Open README.md for more detailed information
with open("README.md", "r", encoding="utf-8") as f:
    detail_description = f.read()

# Personal details description
__VERSION__ = "0.0.0"
SRC_REPO = ""
AUTHOR_USER_NAME = "rajarajeshwarir2021"
AUTHOR_EMAIL = "rajarajeshwarir2021@gmail.com"
REPO_NAME = "MLOPS-Water-Potability-prediction"


setuptools.setup(
    name=SRC_REPO,
    __version__=__VERSION__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for water potability prediction application",
    long_description=detail_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)