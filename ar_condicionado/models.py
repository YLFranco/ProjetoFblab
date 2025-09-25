from django.db import models

class ArCondicionado(models.Model):
    nome = models.CharField(max_length=100)
    temperatura = models.FloatField()
    
    def __str__(self):
        return self.nome