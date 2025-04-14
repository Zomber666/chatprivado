from django.contrib import admin
from .models import SalaPrivada, Mensaje



# Register your models here.

admin.site.register(SalaPrivada)
admin.site.register(Mensaje)







# Inicia sesión con tu superusuario, y deberías ver:
#Sala Privada
#Mensaje
#Desde ahí puedes crear salas
#ver los mensajes y hasta subir archivos manualmente para hacer pruebas.