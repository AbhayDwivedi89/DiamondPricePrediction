from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->List[str]:
  requirement = []
  with open(file_path) as file_obj:
    requirement = file_obj.readlines()
    requirement = [req.replace('\n','') for req in requirement]
    return requirement
  




setup(
    name = "DiamondPricePrediction" ,
    version='0.0.1' , 
    author='Abhay Dwivedi',
    author_email= 'abhaydwivedi956@gmail.com',
    install_requires = get_requirements('requirement.txt'),
    packages= find_packages() 



)

