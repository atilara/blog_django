from django.db import models
# Importanto timezone para trabalhar com datas
from django.utils import timezone
# Importando user que está logado
from django.contrib.auth.models import User

# Criação de uma classe para postagens
class Post(models.Model):
	title = models.CharField(max_length=250)
	# Título como caracter
	slug = models.SlugField(max_length=250)
	# On delete é obrigatório, deleta todas as postagens relacionadas a um usuário
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
# Create your models here.
