"""CLI script for the 3R-1 package. This will be called on the command line"""

import click

from 3R-1.3R-1 import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def 3R-1_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
