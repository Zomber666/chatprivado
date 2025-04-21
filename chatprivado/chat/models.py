from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Room(models.Model):
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"sala {self.id}"
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='mensajes/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.sender.username} en Sala {self.room.id}"
    
# Este modelo te permite tener:
# Salas privadas con múltiples usuarios
# Mensajes con texto y/o archivos adjuntos
# Despues de crear modelos registrarlos en admin.py del proyecto 