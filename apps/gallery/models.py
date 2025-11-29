from django.contrib.auth.models import User
from django.db import models

from shared.models import BaseModel


class Folder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_name = models.CharField('Nome da pasta', max_length=255)
    description = models.TextField('Descrição da pasta', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Pasta'
        verbose_name_plural = 'Pastas'
    
    def __str__(self):
        return self.folder_name


class Image(BaseModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    image = models.ImageField('Imagem')

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return f'Pasta'
