from django.contrib import admin
# Importando o model
from .models import Post

# Register your models here.
@admin.register(Post)

# Classe que vai gerenciar as modificações no admin
class PostAdmin(admin.ModelAdmin):
	# Modifica os campos que aparecerão na listagem do painel
	list_display = ('title', 'author', 'published', 'status')
	# Adiciona opções de filtro
	list_filter = ('status', 'created', 'published', 'author')
	# Adiciona campo de pesquisa
	search_fields = ('title', 'content')
	# Filtro robusto para datas
	date_hierarchy = 'published'
	# Adiciona slug automaticamente utilizando dicionário no py
	prepopulated_fields = {'slug': ('title',)}
	# Manipulação robusta por ID
	raw_id_fields = ('author',)