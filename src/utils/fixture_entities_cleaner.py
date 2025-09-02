from typing import TypeVar

from src.api.basic_client import BasicClient

FixtureClient = TypeVar('FixtureClient', bound=BasicClient)


def fixture_entities_cleanup(client: FixtureClient, entity_id: str | int):
    try:
        client.delete(entity_id)
    except Exception as e:
        print(e)
