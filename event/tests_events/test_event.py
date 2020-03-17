import pytest
from django.urls import reverse
from event.models import Event, Voivodeship


pytestmark = pytest.mark.django_db


def test_event(event_factory):
    event_factory()
    assert Event.objects.count() == 1


def test_api_get_event(event, api_client):
    url = reverse(f'event_detail', kwargs={'pk': event.id})
    response = api_client.get(url)
    assert_data = {
        "name": event.name,
        "description": event.description,
        "voivodeship": event.voivodeship.name
    }
    assert response.status_code == 200
    assert response.data == assert_data


def test_api_get_event_not_found(api_client):
    url = reverse(f'event_detail', kwargs={'pk': 1})
    response = api_client.get(url)
    assert_data = "None event"
    assert response.status_code == 404
    assert response.data == assert_data


def test_api_read_event_list(event_factory, api_client):
    url = reverse(f'event_list')
    event_factory.create_batch(1)
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data.get('results')) == 1


def test_api_create_event(voivodeship_factory, api_client):
    voivodeship = voivodeship_factory()
    url = reverse(f'create_event')
    event = {
        "name": "text",
        "description": "test",
        "lat": 10,
        "lng": 20
    }
    response = api_client.post(url, format='json', data=event)
    assert Voivodeship.objects.count() == 1
    assert response.status_code == 201
    assert Event.objects.count() == 1
    assert Event.objects.first().voivodeship == voivodeship
