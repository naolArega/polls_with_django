from django.shortcuts import render

def index(request):
	context = {
		'data' : 'hello world'
	}
	return render(request, 'home/index.html', context)