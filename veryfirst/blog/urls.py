from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new')
]
