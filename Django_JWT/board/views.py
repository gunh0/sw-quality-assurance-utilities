from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects
    #posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'board/posts.html', {'posts':posts})