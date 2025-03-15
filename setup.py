from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path, "r") as file_obj:  # Corrected: use 'file_obj' instead of 'file'
        requirements = file_obj.readlines()  # Corrected: 'file_obj.readlines()'
        requirements = [req.strip() for req in requirements]  # Remove newline characters

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Shubham",
    author_email="sharmashubham1509@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # Use corrected function
)
