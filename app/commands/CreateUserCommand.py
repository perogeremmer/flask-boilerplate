from uuid import uuid4

import click

# How you doin'?
# This is a sample command.
from werkzeug.security import generate_password_hash

from . import cli_command


@cli_command.command('user:create')
@click.argument('name')
@click.argument('email')
@click.argument('password')
def create_user(name, email, password):
    from app.models.user import Users
    user = Users()
    user.id = str(uuid4())
    user.name = name
    user.email = email
    user.password = generate_password_hash(password)

    from app import db
    db.session.add(user)

    print(user)
