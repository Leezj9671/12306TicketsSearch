from setuptools import setup

setup(
    name = 'tickets',
    version  = '1.0',
    py_modules = ['show', 'stations'],
    install_requires = ['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points = {
        # tickets 命令就是引用了show中的cli()
        'console_scripts': ['tickets = show:cli']
    }
)