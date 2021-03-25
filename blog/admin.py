from django.contrib import admin
# Importando o model
from .models import Post
# Register your models here.
admin.site.register(Post)