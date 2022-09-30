from jira import JIRA, Issue
from sh import git

PROJECT_KEY = 'TP'
URL = 'https://gitjira.atlassian.net'
EMAIL = 'loredo.rod@gmail.com'
TOKEN = 'eYfFxOKdYLR840nT6Bi286F2'

# TODO: username/token tuple Only valid for Jira Cloud
# We need to support self hosted Jira, where auth is done with
# token auth, with the PAT token: token_auth="API token"
jira = JIRA(URL, basic_auth=(EMAIL, TOKEN))


def get_issue_types():
    project_id = jira.project(PROJECT_KEY).id
    issue_types = jira.issue_types()
    return [it.name for it in issue_types if issue_type_in_project(it, project_id)]


def issue_type_in_project(issue_type, project_id):
    return hasattr(issue_type, 'scope') and issue_type.scope.project.id == project_id

ISSUE_TYPES=get_issue_types()


def create_branch(issue_key: str, summary: str):
    branch_name = f"{issue_key}-{summary.replace(' ', '-').lower()}"
    git.checkout('-b', branch_name)


def create_issue(input_fields) -> Issue:
    input_fields['issuetype'] = { 'name': input_fields['issuetype'] }
    fields = {
        'project': PROJECT_KEY,
        **input_fields
    }
    return jira.create_issue(fields=fields)

# Creates a jira ticket
# Creates a branch with the ticket code
def run(input_fields):
    issue = create_issue(input_fields)
    create_branch(issue.key, input_fields['summary'])
