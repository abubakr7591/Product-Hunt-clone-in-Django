from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('create/', views.product_create, name='product_create'),
	path('products/<int:product_id>', views.detail, name='detail'),
	path('products/<int:product_id>/upvote', views.upvote, name='upvote'),
]