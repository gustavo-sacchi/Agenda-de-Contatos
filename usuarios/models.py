from django.db import models
from contatos.models import Contato
from django import forms
from django.contrib.auth.models import AbstractUser


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()


class UserPersonalizado(AbstractUser):
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(blank=True, upload_to='fotos_perfil', verbose_name='Foto de Perfil')

