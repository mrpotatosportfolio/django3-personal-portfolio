from django.shortcuts import render
from .models import Project
def home(request):
    projects = Project.objects.all()
    if request.GET.get('identity')=='admin' and request.GET.get('password')=='admin@1234':
        boxdisable = 'nav-link enabled'
    else:
        boxdisable = 'nav-link disabled'
    return render(request, 'portfolio/home.html', {'projects':projects, 'box_disable':boxdisable})
