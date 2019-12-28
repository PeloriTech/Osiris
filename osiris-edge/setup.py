import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('Osiris/version.py').read())

setuptools.setup(
    name="Osiris",
    version=__version__,
    author="Pelori",
    author_email="samcrane8@gmail.com",
    description="A tool for managing AI systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/peloritech/osiris",
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
        'python-nmap'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        osiris=cli:cli
    ''',
)