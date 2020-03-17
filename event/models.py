from django.contrib.gis.db import models


class Voivodeship(models.Model):
    name = models.CharField(max_length=128)
    area = models.PolygonField(srid=4326, geography=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    voivodeship = models.ForeignKey(
        Voivodeship,
        related_name='voivodeship',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
