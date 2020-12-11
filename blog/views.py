from django.shortcuts import render, get_object_or_404
from .models import Blog

blogs = Blog.objects.order_by('-date')[:5]

def all_blogs(request):
    if request.GET.get('identity')=='admin' and request.GET.get('password')=='admin@1234':
        boxdisable = 'nav-link enabled'
    else:
        boxdisable = 'nav-link disabled'
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'box_disable':boxdisable})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.GET.get('identity')=='admin' and request.GET.get('password')=='admin@1234':
        boxdisable = 'nav-link enabled'
    else:
        boxdisable = 'nav-link disabled'
    return render(request, 'blog/detail.html', {'blog':blog, 'box_disable':boxdisable})
