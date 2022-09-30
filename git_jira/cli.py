from typing import List, Optional

import click
# import yaml

# def get_yaml_content(file_path: str) -> dict:
#     with open(file_path) as f:
#         return yaml.safe_load(f)

# CONFIG = get_yaml_content("config.yaml")

@click.group()
def cli():
    pass


@click.command()
def branch():
    click.echo("Branch command not implemented yet")


@click.command()
def status():
    click.echo("Status command not implemented yet")


cli.add_command(branch)
cli.add_command(status)
