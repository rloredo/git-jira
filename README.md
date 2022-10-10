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

You can also create a branch from an existing issue, using the issue code (TP-XX). For this, use `git jira branch -k <issue_key>`

### List

Use `git jira list` to list issues and their branches. By default, it list all issues in planned. You can use the flag `-s` or `--status` to change this behaviour.

### Status

Use `git jira status` to check the status of an issue specified in a branch. If you're in a branch `TP-10-issue-summary` this command will show you the info related to the Jira issue `TP-10`. 
In the future you will be able to update the status and add comments using this command.

## Caveats

`git jira --help` won't work. To see the global help, run `git jira` or `git-jira --help`

## Development

```bash
virtualenv env 
source env/bin/activate
pip install -e ".[dev]"
```
