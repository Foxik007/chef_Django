from pyexpat import model

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get('slug'))

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request,'base.html',)