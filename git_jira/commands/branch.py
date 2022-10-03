import click

from git_jira.jira import JiraIssue, JiraMetaIssue
from git_jira.git import GitBranch

def array_input(field):
    options_valid = False
    options = [opt['value'] for opt in field['options']]
    while options_valid == False:
        input = click.prompt(f"{field['name']}. Multiple choice: {', '.join(options)}", type=str)
        input = input.replace(' ', ',').replace(',,', ',').split(',')
        for option in input:
            if option in options:
                options_valid = True
            else:
                options_valid = False
                click.echo("Invalid option(s) selected. Please try again...")
                break
    return input

def prompt_field(field):
    if field["type"] == "string":
        return click.prompt(field["name"], type=str)
    elif field["type"] == "option":
        return {'value' : click.prompt(field["name"], type=click.Choice([opt["value"] for opt in field["options"]]))}
    elif field["type"] == "array":
        return [{'value' : option} for option in array_input(field)]

def issue_fields_input():
    meta_issue = JiraMetaIssue()
    fields = dict()
    click.echo("Fill in the required fields")
    fields["project"] = {"key": meta_issue.project_code}
    fields["issuetype"] = {"name": click.prompt("Issue type", type=click.Choice(meta_issue.issue_type_names))}
    fields["summary"] = click.prompt("Summary", type=str)
    fields["description"] = click.prompt("Description", type=str)
    #Iterate if there any other required
    for field in meta_issue.required_fields(fields["issuetype"]["name"]):
        if field['key'] not in ["project", "issuetype", "summary", "description", "reporter"]:
            fields[field['key']] = prompt_field(field)
    return fields

@click.command()
def branch():
    issue = JiraIssue(issue_fields_input())
    GitBranch(issue.branch_name).create()
    click.echo(f"{issue.type} created at {issue.url}")
