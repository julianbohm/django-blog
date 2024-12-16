from django.shortcuts import render
from .models import About

# Create your views here.

def about_view(request):
    about_content = About.objects.first()  
    return render(request, 'about/about.html', {'about': about_content})




