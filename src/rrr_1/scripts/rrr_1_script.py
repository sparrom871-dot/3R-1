"""CLI script for the rrr_1 package. This will be called on the command line"""

import click

from rrr_1.rrr_1 import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def rrr_1_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
