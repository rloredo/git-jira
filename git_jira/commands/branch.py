import click

from git_jira.config import Config
from git_jira.git import GitBranch
from git_jira.jira import JiraIssue, JiraProject


def issue_fields_input(issue_types):
    fields = dict()
    click.echo("Fill in the required fields:")
    fields["summary"] = click.prompt("Summary", type=str)
    fields["description"] = click.prompt("Description", type=str)
    fields["issuetype"] = click.prompt("Issue type", type=click.Choice(issue_types))
    return fields

@click.command()
def branch():
    Config().load()
    issue_types = JiraProject().issue_types
    issue = JiraIssue(issue_fields_input(issue_types))
    GitBranch(issue.branch_name).create()
