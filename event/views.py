from rest_framework import serializers, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services
from .models import Event


class CheckVoivodeshipApi(APIView):
    class InputSerializer(serializers.Serializer):
        lat = serializers.IntegerField(min_value=0, max_value=90)
        lng = serializers.IntegerField(min_value=0, max_value=90)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lng, lat = serializer.validated_data.get("lng"), serializer.validated_data.get(
            "lat"
        )
        voivodeship = services.get_voivodeship_from_coordinates(lat=lat, lng=lng)
        if voivodeship is None:
            return Response("Point outside of Poland", status.HTTP_400_BAD_REQUEST)
        return Response({"Voivodeship": voivodeship.name})


class CreateEventApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        description = serializers.CharField()
        lat = serializers.IntegerField(min_value=0, max_value=90)
        lng = serializers.IntegerField(min_value=0, max_value=90)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = services.create_event(serializer.validated_data)
        if event is None:
            return Response("Event outside of Poland", status.HTTP_400_BAD_REQUEST)
        return Response(
            {"name": event.name, "voivodeship": event.voivodeship.name},
            status.HTTP_201_CREATED,
        )


class EventDetailApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        voivodeship = serializers.StringRelatedField(many=False)

        class Meta:
            model = Event
            fields = ("name", "description", "voivodeship")

    def get(self, request, pk: int):
        event = services.get_event_by_id(pk)
        if event is None:
            return Response("None event", status.HTTP_404_NOT_FOUND)
        serializer = self.OutputSerializer(event, many=False)
        return Response(serializer.data)


class EventListApi(generics.ListAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        voivodeship = serializers.StringRelatedField(many=False)

        class Meta:
            model = Event
            fields = ("name", "description", "voivodeship")

    queryset = Event.objects.all()
    serializer_class = OutputSerializer
