from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction


from .models import (
    Play,
    Performance,
    TheatreHall,
    Actor,
    Genre,
    Reservation,
    Ticket
)

from .serializers import (
    PlayListSerializer, PlayDetailSerializer,
    PerformanceListSerializer, PerformanceDetailSerializer,
    TheatreHallListSerializer, TheatreHallDetailSerializer,
    ActorSerializer, GenreSerializer,
    ReservationSerializer, TicketSerializer
)


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PlayListSerializer
        return PlayDetailSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PerformanceListSerializer
        return PerformanceDetailSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TheatreHallListSerializer
        return TheatreHallDetailSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TicketSerializer
        return TicketSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        reservation = serializer.validated_data.pop("reservation", None)
        user = self.request.user
        if not reservation:
            reservation = Reservation.objects.create(user=user)
        serializer.save(reservation=reservation)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save()

    @transaction.atomic
    def perform_destroy(self, instance):
        instance.delete()
