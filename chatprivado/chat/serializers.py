# Queremos que nuestro sistema permita enviar y recibir mensajes dentro de salas privadas, a través de una API REST.
# Esto te permitirá luego conectar un frontend (web, móvil, etc.) fácilmente.


from rest_framework import serializers
from .models import Room, Message
from django.contrib.auth.models import User

# Este serializer define qué campos del modelo,
# User vamos a mostrar cuando se use, en este caso el id y el username.
class Userserializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['id', 'username',]


class Messageserializer(serializers.ModelSerializer):
    remitente = Userserializer(read_only=True)

class Meta:
    models = Message
    fields = ['id', 'sala', 'remitente', 'texto', 'archivo', 'enviado_en',]

class Roomserializer(serializers.ModelSerializer):
    participantes = Userserializer(many=True, read_only=True)

    class Meta:
        models = Room
        fields = ['id', 'participantes', 'creada_en',]