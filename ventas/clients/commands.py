import click


@click.group()
def clients():
    """Manages the client livecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, postion):
    """Create a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """"List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """"Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """"Deletes a client"""
    pass


all = clients
