import click

# How you doin'?
# This is a sample command.
from . import cli_command


@cli_command.command('sample:command')
@click.argument('name')
def create_user(name):
    print(name)
