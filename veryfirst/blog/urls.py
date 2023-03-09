from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreateView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='list'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
