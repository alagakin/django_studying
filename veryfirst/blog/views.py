from django.views.generic import ListView

from blog.models import Post


class BlogView(ListView):
    model = Post
    template_name = 'blog/home.html'
