from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT = '-e .'
def get_requirments(file_path:str )-> List[str]:
    requirments = []
    with open (file_path) as fileObject:
        requirments = fileObject.readlines()
        requirments = [req.replace('\n' , '') for req in requirments]

    if HYPE_E_DOT in requirments:
        requirments.remove(HYPE_E_DOT)
        
    return requirments


setup(
    name = 'mlproject',
    author = 'Aniket Vishwakarma',
    packages = find_packages(),
    install_req =get_requirments('requirment.txt')
)