from setuptools import setup

setup(
    name = 'space_race',
    version = '0.1.0',
    packages = ['space_race'],
    entry_points = {
        'console_scripts': [
            'space_race = space_race.__main__:main'
        ]
    }
)