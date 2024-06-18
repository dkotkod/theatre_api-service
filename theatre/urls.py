from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PlayViewSet,
    PerformanceViewSet,
    TheatreHallViewSet,
    ActorViewSet,
    GenreViewSet,
    ReservationViewSet,
    TicketViewSet
)

app_name = 'theatre'

router = DefaultRouter()
router.register(r'plays', PlayViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'theatre-halls', TheatreHallViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
