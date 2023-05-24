from uuid import uuid4

import anvil.server
from anvil.tables import app_tables


@anvil.server.callable
def search_ballot(*args, **kwargs):
    return app_tables.ballot.search(*args, **kwargs)


@anvil.server.callable
def add_ballot(attrs):
    defaults = {
        "uuid": uuid4(),
        "dkg_ritual_id": 0,
        "storage_location": "",
        "protocol_version": 1,
    }
    return app_tables.ballot.add_row(**defaults, **attrs)


@anvil.server.callable
def get_ballot(attrs):
    return app_tables.ballot.get(uuid=attrs["uuid"])
