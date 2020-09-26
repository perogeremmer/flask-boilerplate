import click

from app.commands import command_cli

# How you doin'?
# This is a sample command.
@command_cli.command('sample:command')
@click.argument('name')
def create_user(name):
    print(name)

