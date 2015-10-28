from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {
		'helloMsg' : "Welcome to our website :)",
		'header' : "Renos",
	}
	return render(request, 'rango/index.html', context_dict)
