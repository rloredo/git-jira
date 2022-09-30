# git-jira

A git addon to manage Jira from git.

# Installation

The easiest (and best) way to install git-jira is through pip:

```bash
pip install git-jira
```

To make it work, you need a `config.yml` with your authentication credentials and default project.  
Run `git jira config` to generate this file.

## Development

```bash
virtualenv env 
source env/bin/activate
pip install -e ".[dev]"
```
