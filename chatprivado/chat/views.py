from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Room, Message
from .serializers import Roomserializer, Messageserializer





# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = Roomserializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Messageserializer
    permission_classes = [permissions.IsAuthenticated]