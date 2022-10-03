import click
from pick import pick

from git_jira.jira import JiraIssue, JiraMetaIssue
from git_jira.git import GitBranch

def prompt_field(field):
    if field["type"] == "string":
        return click.prompt(field["name"], type=str)
    elif field["type"] == "option":
        option, _ = pick([opt["value"] for opt in field["options"]], field["name"])
        click.echo(f"{field['name']}: {option}")
        return {'value' : option}
    elif field["type"] == "array":
        response = pick([opt['value'] for opt in field['options']], field['name'], multiselect=True, min_selection_count=1)
        click.echo(f"{field['name']}: {', '.join([option[0] for option in response])}")
        return [{'value' : option[0]} for option in response]

def issue_fields_input():
    meta_issue = JiraMetaIssue()
    fields = dict()
    click.echo("Fill in the required fields")
    fields["project"] = {"key": meta_issue.project_code}
    option, _ = pick(meta_issue.issue_type_names, "Issue type")
    fields["issuetype"] = {"name": option}
    click.echo(f"Issue type {option}")
    fields["summary"] = click.prompt("Summary", type=str)
    fields["description"] = click.prompt("Description", type=str)
    #Iterate if there is any other required
    for field in meta_issue.required_fields(fields["issuetype"]["name"]):
        if field['key'] not in ["project", "issuetype", "summary", "description", "reporter"]:
            fields[field['key']] = prompt_field(field)
    return fields

@click.command()
def branch():
    issue = JiraIssue(issue_fields_input())
    GitBranch(issue.branch_name).create()
    click.echo(f"{issue.type} created at {issue.url}")
