from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

def index(request):
    myposts = Blogpost.objects.all()
    return render(request, "blog/index.html", {'myposts':myposts})

def blogpost(request, postid):
    post = Blogpost.objects.filter(post_id = postid)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})
