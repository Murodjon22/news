from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import Http404
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "base.html"
    context_object_name = 'blog'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by('-time')


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

def test_404(request):
    raise Http404("Bu test uchun 404 sahifa.")