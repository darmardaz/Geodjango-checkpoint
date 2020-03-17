from django.contrib import admin
from django.urls import path

from event import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/check-voiv/', views.CheckVoivodeshipApi.as_view(), name="voivodeship_check"),
    path('api/events/', views.EventListApi.as_view(), name="event_list"),
    path('api/event/', views.CreateEventApi.as_view(), name="create_event"),
    path('api/event/<int:pk>/', views.EventDetailApi.as_view(), name="event_detail"),
]
