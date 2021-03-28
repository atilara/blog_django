from django.db import models
# Importanto timezone para trabalhar com datas
from django.utils import timezone
# Importando user que está logado
from django.contrib.auth.models import User

# Criando manager customizado herdando de manager
class PublishedManager(models.Manager):
	# Fazendo uma query que retorna os artigos publicados
	def get_queryset(self):
		return super(PublishedManager.self).get_queryset().filter(status='publicado')

# Criação de uma classe para postagens
class Post(models.Model):
	# Status de aprovação, o post precisa ser revisado antes de publicado
	STATUS = (
		('rascunho', 'Rascunho'),
		('publicado', 'Publicado'),
	)
	title = models.CharField(max_length=250)
	# Título como caracter
	slug = models.SlugField(max_length=250)
	# On delete é obrigatório, deleta todas as postagens relacionadas a um usuário
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	published = models.DateTimeField(default=timezone.now)
	# Para que a data e hora não seja modificada dps da criação é usado o auto_now_add
	created = models.DateTimeField(auto_now_add=True)
	# auto_now modificado sempre que acontecer uma alteração
	modified = models.DateTimeField(auto_now=True)
	# O campo status no banco possui o status como possíveis escolhas
	status = models.CharField(max_length=10, choices=STATUS, default='rascunho')

	# Para utilizar manager customizado
	# objects = models.Manager()
	# published = PublishedManager()

	# Classe meta configura algumas coisas existentes nesse model, no momento está ordenando
	# os posts do mais recente para o mais antigo
	class Meta:
		ordering = ('-published',)


	# Para que o painel administrativo do django traga o nome da postagem corretamente:
	# Função retorna o título do post
	def __str__(self):
		return self.title
	
	
# Create your models here.
