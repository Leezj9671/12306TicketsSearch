from setuptools import setup

setup(
    name='tickets',
    py_modules=['show', 'stations'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['show=show:cli']
    }
)