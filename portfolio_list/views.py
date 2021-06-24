from django.shortcuts import render
from .models import Project

def home(request):
	projects = Project.objects.all() #grabs all the objects from the database contained in the Project table
	return render(request, 'home.html', {'projects': projects})
