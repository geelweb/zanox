# Zanox Client

Zanox API client implementation.

## Install

From source

    python setup.py build
    sudo python setup.py install


## Usage

    from zanox.client import Client
    import json

    cli = Client(connectid="your zanox connect id",
               secretkey="your zanox secret key"
               )
    response = cli.getProgramApplications(status="confirmed")
    programs = json.loads(response)

## Examples

To execute examples you have to define your connect id and secret key in a
config.py file

    cp examples/config.dist.py config.py
    vim config.py

    python examples/incentives_per_programs.py
