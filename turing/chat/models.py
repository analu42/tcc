
# Create your models here.
from django.db import models
from django.utils.timezone import now

class Message(models.Model):
    sender = models.CharField(max_length=100)  # Pode ser 'bot' ou 'user' Armazena quem enviou a mensagem, podendo ser o usuário ou o bot.
    text = models.TextField()  # Conteúdo da mensagem
    timestamp = models.DateTimeField(default=now)  # Data e hora da mensagem

    def __str__(self):
        return f"{self.sender}: {self.text[:30]}..."
