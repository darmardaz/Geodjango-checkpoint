from django.contrib.gis.geos import GEOSGeometry

from .models import Voivodeship, Event


def get_voivodeship_from_coordinates(lat: int, lng: int):
    point = GEOSGeometry(f"Point({lat} {lng})", srid=4326)
    return Voivodeship.objects.get(area__intersects=point)


def create_event(data):
    voivodeship = get_voivodeship_from_coordinates(data.get('lat'), data.get('lng'))
    if voivodeship is None:
        return
    event = Event.objects.create(
        voivodeship=voivodeship,
        name=data.get('name'),
        description=data.get('description')
    )
    return event


def get_event_by_id(event_id: int):
    event = Event.objects.filter(id=event_id).first()
    return event
