
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='openseespyvis',  
    version='0.1',
    scripts=['openseespyvis'] ,
    author="Anurag Upadhyay",
    author_email="anurag.upadhyay@utah.edu",
    description="A development branch of openseespy visualization commands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/u-anurag/openseespyvis",
    packages=setuptools.find_packages(),
    license='LICENSE.md',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )