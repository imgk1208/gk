from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "vHome" : "active",
        "vAbout" : "",
        "vBlogs" : "",
        "vDoubts" : "",
    }
    return  render(request, 'index.html', context)

def about(request):
    context = {
        "vHome" : "",
        "vAbout" : "active",
        "vBlogs" : "",
        "vDoubts" : "",
    }
    return render(request, 'about.html', context)

def blog(request):
    context = {
        "vHome" : "",
        "vAbout" : "",
        "vBlogs" : "active",
        "vDoubts" : "",
    }
    return render(request, 'blog.html', context)

def doubts(request):
    context = {
        "vHome" : "",
        "vAbout" : "",
        "vBlogs" : "",
        "vDoubts" : "active",
    }
    return render(request, 'doubts.html', context)

