# git-jira

[![PyPI](https://img.shields.io/pypi/v/git-jira.svg)](https://pypi.python.org/pypi/git-jira)

A git addon to manage Jira from git.

## Prerequisites

Create a Jira API token: https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/

## Installation

The easiest (and best) way to install git-jira is through pip:

```bash
pip install git-jira
```

To make it work, you need a `config.yml` with your authentication credentials and default project.  
Run `git jira configure` to generate this file.  

The **Jira server url** should have the format `https://yourservername.atlassian.net`. For now, the authentication only supports API tokens.  
The **project id** should have the format `XX` and is the one that you can find at the beginning of the issues (e.g. `TP-123`).

## Usage

### Branch

Use `git jira branch` to create an issue in Jira and checkout to a branch with the format `TP-1234-summary-of-issue`.  
The creation will ask the required fields interactively.  
For now, the supported field types are:

- Short text, paragraph
- Number
- Dropdown (single choice)
- Checkbox (multiple choice)

## Caveats

`git jira --help` won't work. To see the global help, run `git jira` or `git-jira --help`

## Development

```bash
virtualenv env 
source env/bin/activate
pip install -e ".[dev]"
```
