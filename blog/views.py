from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
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

class BlogDeleteView(DeleteView):
	model = Post
	template_name = "blog/post_delete.html"
	success_url = reverse_lazy('home')
