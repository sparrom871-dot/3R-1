import click

from rrr_1.rrr_1 import hello_world, calculate_mean


@click.command()
@click.option("--message", default=None, help="Print a message.")
@click.option("--values", multiple=True, type=float, help="Input numbers.")
def rrr_1_cli(message, values):
    """提供文字輸出及平均數計算功能。"""

    if values:
        # 計算平均數
        click.echo(f"Mean: {calculate_mean(values):.2f}")
    elif message is not None:
        # 保留原本的 Hello World 功能
        click.echo(hello_world(message))
    else:
        click.echo("Please provide --message or --values.")