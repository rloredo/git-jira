from functools import cached_property

from jira import JIRA, Issue

from git_jira.config import Config
from git_jira.utils import singleton


# TODO: username/token tuple Only valid for Jira Cloud
# We need to support self hosted Jira, where auth is done with
# token auth, with the PAT token: token_auth="API token"
@singleton
class Jira:
    def __init__(self):
        self.config = Config().jira

    @cached_property
    def jira(self):
        return JIRA(
            self.config["server_url"],
            basic_auth=(self.config["username"], self.config["api_token"]),
        )


class JiraProject:
    def __init__(self, project_code=None):
        self.project_code = (
            self.project_code if project_code else Jira().config["default_project_key"]
        )

    @cached_property
    def project(self):
        return Jira().jira.project(self.project_code)

    @cached_property
    def issue_types(self):
        issue_types = Jira().jira.issue_types()
        return [it.name for it in issue_types if self.issue_type_in_project(it)]

    def issue_type_in_project(self, issue_type):
        return (
            hasattr(issue_type, "scope")
            and issue_type.scope.project.id == self.project.id
        )


class JiraIssue:
    def __init__(self, fields):
        self.summary = fields["summary"]
        self.issue = Jira().jira.create_issue(self.fields)

    @cached_property
    def project(self):
        return Jira().config["default_project_key"]

    @cached_property
    def fields(self, fields):
        fields["issuetype"] = {"name": fields["issuetype"]}
        fields["project"] = self.project

    @cached_property
    def branch_name(self):
        return f"{self.issue.key}-{self.issue.summary.replace(' ', '-').lower()}"
