from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    # Passando pk como paramêtro
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail'),
]