from setuptools import find_packages, setup

HYEN_DOT="-e ."

def get_requirements(file_path: str) -> list[str]:
    '''this function will return thelist of requirements '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements if req.strip()]

        if HYEN_DOT in requirements:
            requirements.remove(HYEN_DOT) 
    return requirements


setup(
    name="MLProject",
    version="0.1.0",
    author="LAKAVATH SANDEEP",
    author_email="lakavathsandeep31@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)