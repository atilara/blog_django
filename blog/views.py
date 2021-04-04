from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView

from . models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"

class BlogCreateView(CreateView):
	model = Post
	template_name = "blog/post_new.html"
	# Puxa todos os campos do backend para o form no frontend
	fields = ('author', 'title', 'content')

class BlogUpdateView(UpdateView):
	model = Post
	template_name = "blog/post_edit.html"
	# Puxa todos os campos do backend para o form no frontend
	fields = ('title', 'content')
