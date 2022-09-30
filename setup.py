import pathlib

from setuptools import setup, find_packages

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name='git-jira',
    description='A git addon to manage Jira from git.',
    version='0.0.0',
    packages=find_packages(),
    python_requires='>=3.6.2',
    entry_points='''
        [console_scripts]
        git-jira=git_jira.cli:cli
    ''',
    author="rloredo",
    keyword="git, jira",
    long_description=README,
    install_requires=[
        'click>=8.0',
        'jira>=3.4.1'
    ],
    long_description_content_type="text/markdown",
    license='',
    url='https://github.com/rloredo/git-jira',
    author_email='loredo.rod@gmail.com',
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
