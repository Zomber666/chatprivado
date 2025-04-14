from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class SalaPrivada(models.Model):
    participantes = models.ManyToManyField(User)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"sala {self.id}"
    

class Mensaje(models.Model):
    sala = models.ForeignKey(SalaPrivada, on_delete=models.CASCADE)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(blank=True)
    archivo = models.FileField(upload_to='mensajes/', blank=True, null=True)
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente.username} en Sala {self.sala.id}"
    
# Este modelo te permite tener:
# Salas privadas con múltiples usuarios
# Mensajes con texto y/o archivos adjuntos
# Despues de crear modelos registrarlos en admin.py del proyecto 