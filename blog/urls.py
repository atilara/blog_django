from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    # Criando o post new primeiro que o slug para que ele não pense que o new seja um slug
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    # Passando slug como paramêtro
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
]