import setuptools

setuptools.setup(
    name="drinfeld_modular_forms",
    version="0.0.1",
    author="David Ayotte",
    author_email="davidayotte94@outlook.com",
    description="SageMath implementation of Drinfeld modular forms",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DavidAyotte/drinfeld_modular_forms",
    packages=["drinfeld_modular_forms"],
    extras_require={"doc": "sphinx>=2"},
    classifiers=[
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ])
