from setuptools import find_packages, setup

setup(
    name="phmsa_da",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.16.0",
        "pandas>=1.0.0",
        "matplotlib>=3.1.0",
        "seaborn>=0.9.0",
        "scikit-learn>=0.24.0",
        "jupyter>=1.0.0",
        "notebook>=6.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.8.0",
        ],
    },
    python_requires=">=3.6",
) 