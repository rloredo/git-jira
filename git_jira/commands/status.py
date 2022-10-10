import click
from pick import pick
from git_jira.git import GitBranch
from git_jira.jira import Jira, JiraIssue
from git_jira.utils import INDICATOR

def update_issue(issue):
    new_value, _ = pick(issue.available_statuses, "Update to:", indicator=INDICATOR)
    Jira().jira.transition_issue(issue.issue, new_value)
    return new_value

@click.command()
@click.option('-u', '--update', is_flag = True, show_default=True, default=False, help="Update the issue status")
@click.option('-c', '--comment', default=None, help="Add a comment to the issue")
def status(update, comment):
    branch = GitBranch()
    if branch.issue_key:
        issue = JiraIssue(issue_key = branch.issue_key)
        if update:
            new_value = update_issue(issue)
            click.echo(f"Status of issue {issue.key} updated to {new_value}")
        elif comment:
            c = Jira().jira.add_comment(issue=issue.issue, body=comment)
            click.echo(f"Comment added. See it here: {issue.url}?focusedCommentId={c.id}")
        else:
            click.echo(f"Issue type: {issue.type}")
            click.echo(f"Summary: {issue.summary}")
            click.echo(f"Assigned to: {issue.assignee}")
            click.echo(f"Status: {issue.status}")
            click.echo(f"See more at {issue.url}")
    else:
        click.echo("No issue found for this branch.")
