import click

@click.command()
@click.argument('command')
@click.argument('args', nargs=-1)
def cli(command, args):
    click.echo('Hello world')
    pass

