import factory
from factory import fuzzy
from django.contrib.gis.geos import Polygon
from .models import Event, Voivodeship


class VoivodeshipFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=25)
    area = Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))

    class Meta:
        model = Voivodeship


class EventFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=25)
    description = fuzzy.FuzzyText(length=25)
    voivodeship = factory.SubFactory(VoivodeshipFactory)

    class Meta:
        model = Event
