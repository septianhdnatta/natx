from setuptools import setup, find_packages
from Cython.Build import cythonize
import glob

setup(
    name="natx",
    version="0.2.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=cythonize(
        glob.glob("src/natx/*.py"),
        compiler_directives={
            "language_level": "3"
        }
    ),
    zip_safe=False,
)
