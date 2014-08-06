# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Postagem(models.Model):
	titulo			 = models.CharField(max_length=100,verbose_name="Título")
	texto			 = models.CharField(max_length=20000,verbose_name="Texto")
	data_de_postagem = models.DateField(verbose_name="Data de Postagem")
