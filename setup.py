from setuptools import find_packages, setup 
## function is used to scan all the folders with __init__.py and it will be considered as a package.
from typing import List

def get_requirements()->List[str]:
    ## This function will return the list of requirements.
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e. 
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements file not found")
    
    return requirement_list

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author = "Bikash",
    author_email="bikashojha101@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)