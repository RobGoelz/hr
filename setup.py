from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
        readme = f.read()

setup(
        name='hr',
        version='0.1.0',
        description='Command-line user management utility',
        long_description=readme,
        author='Rob Goelz',
        author_email='RobGoelz@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[],
        entry_points={
            'console_scripts': 'hr=hr.cli:main',
        },
)
