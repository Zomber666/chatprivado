from django.contrib import admin
from .models import Room, Message



# Register your models here.

admin.site.register(Room)
admin.site.register(Message)







# Inicia sesión con tu superusuario, y deberías ver:
# Sala Privada
# Mensaje
# Desde ahí puedes crear salas
# ver los mensajes y hasta subir archivos manualmente para hacer pruebas.