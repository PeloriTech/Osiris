import os, json
import click
import Osiris
from Osiris.utils.Scanner import Scanner


@click.group()
def cli():
    pass


'''
Create a new Osiris project.
'''
@cli.command()
def init():
    # Create a new Osiris Build
    cwd = os.getcwd()
    if os.path.isfile(cwd + '/osiris.json'):
        click.echo('Build file already exists in directory.')
        return

    cameras = []

    resp = input("Would you like to automatically scan for and add videostreams to this project?\n")

    if resp.lower() == 'y' or resp.lower() == 'yes':
        click.echo('Beginning Scan (this may take a moment)')
        scanner = Scanner()
        streams: list = scanner.scan()
        for stream in streams:
            cameras += [{
                "type": "onvif",
                "ip": stream.ip,
                "status": stream.status,
                "interface": stream.interface,
                "endpoint": "/stream0",
                "user": "admin",
                "password": "password"
            }]
        click.echo('System scan is complete.')
    else:
        click.echo('Not scanning for cameras.')
    build = {
        "name": "osiris",
        "version": Osiris.__version__,
        "cameras": cameras
    }

    with open('osiris.json', 'w') as f:
        json.dump(build, f, indent=4, separators=(',', ': '))


'''
List currently detected cameras.
'''
@cli.command()
def list():
    pass


'''
Scan for cameras locally / on the network.
'''
@cli.command()
def scan():
    click.echo('Running Osiris Scan')
    scanner = Scanner()
    streams: list = scanner.scan()
    for stream in streams:
        print('{}   {}      {}'.format(stream.ip, stream.status, stream.interface))