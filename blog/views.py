from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    return render(request, 'blog/blog.html')

def category(request):
    return render(request, 'blog/categories.html')