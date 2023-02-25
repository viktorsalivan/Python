from django.shortcuts import render
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts} )


def detail(request,id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/detail.html',  {'post': post} )


def about(request):
    return render(request, 'blog/about.html')
