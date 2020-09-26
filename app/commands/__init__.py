from flask.cli import AppGroup

cli_command = AppGroup('cli', help='Command Line Interface')

from . import SampleCommand
