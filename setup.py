from setuptools import find_packages,setup # find all packages in ml project
from typing import List

HTPEN_E_DOT ='-e .'

def get_requirments(file_path:str)->List[str]:
    '''
    this fuct will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HTPEN_E_DOT in requirments:
            requirments.remove(HTPEN_E_DOT)
    
    return requirments


setup(
    name='mlproject',
    version='0.0.1',
    author='shashank',
    author_email='shashankkurakula.417@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)