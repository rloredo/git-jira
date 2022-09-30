import click
import yaml
from git_jira.config import CONFIG_FILE_PATH, write_config_file, config_file_exists

@click.group()
def cli():
    pass

@click.command()
def config():
    click.echo("Welcome to git-jira. Let's generate your config file...")
    config_dict = dict({'jira': dict()})
    config_dict['jira']['jserver_url'] = click.prompt("Insert your Jira server url", type=str)
    config_dict['jira']['username'] = click.prompt("Insert your Jira username", type=str)
    config_dict['jira']['api_token'] = click.prompt("Create an API token here https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ \nand insert your Jira API token", type=str)
    config_dict['jira']['default_project_key'] = click.prompt("Select default project to use. \nLeave empty if you want to specify it as flags. Insert the short code (like TP, PJ, etc)", type=str) 
    click.echo(f"A config.yaml file with the following params will be created at {CONFIG_FILE_PATH}\n\n{yaml.dump(config_dict)}")
    if click.confirm('Do you want to continue?'):
        write_config_file(config_dict)
        click.echo(f"Config file successfully created. Run git jira debug to test the connection.")
    else:
        click.echo(f"Configuration aborted.")

@click.command()
def debug():
    if config_file_exists():
        click.echo(f"Config file found at {CONFIG_FILE_PATH}")
    else:
        click.echo("Config file not found. Run git jira config to generate.")


@click.command()
def branch():
    click.echo("Branch command not implemented yet")

@click.command()
def status():
    click.echo("Status command not implemented yet")

cli.add_command(config)
cli.add_command(debug)
cli.add_command(branch)
cli.add_command(status)
