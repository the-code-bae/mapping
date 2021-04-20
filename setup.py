import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='mapping',  
     version='v0.0.1',
     # scripts=['dokr'] ,
     author="Maka I",
     author_email="nibe12@live.com",
     license="MIT",
     description="First package evs",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/the-code-bae/mapping",
     packages=setuptools.find_packages(),
     python_requires=">=3.5",
     install_requires=["requests", "geopy", "collections", "re", "requests", "pandas"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Development Status :: 3 — Alpha",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Topic :: Software Development :: Libraries",
         "Topic :: Software Development :: Libraries :: Python Modules",
         "Intended Audience :: Developers"
     ],
 )
