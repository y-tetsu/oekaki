from setuptools import setup


setup(
    name='oekaki',
    version='0.0.1',
    license='MIT License',
    install_requires=[
    ],
    description='A simple canvas application using tkinter',
    author='y-tetsu',
    url='',
    packages=[
        'oekaki',
    ],
    package_data={
        "": ["*.py"]
    },
    entry_points={
        "console_scripts": [
            "start_oekaki=oekaki.oekaki:start_oekaki",
        ]
    },
)
