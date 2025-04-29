from tabnanny import verbose
from django.db import models

class Cor(models.Model):
    descricao = models.CharField(max_length=40)

    class Meta: 
        verbose_name ='cor'
        verbose_name_plural = 'cores'
    
    def __str__(self):
        return self.descricao