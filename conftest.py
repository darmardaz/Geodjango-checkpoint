import pytest
from pytest_factoryboy import register

from event.factories import VoivodeshipFactory, EventFactory

register(VoivodeshipFactory)
register(EventFactory)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
