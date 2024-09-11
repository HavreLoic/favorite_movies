from django.shortcuts import render, HttpResponse

# Create your views here.
def index(response):
    context = {
        'movies': ['Wolf King', 'Bad Blood', 'Red notice']
        }
    return render(response, 'movies_app/index.html', context)

def about(response):
    return render(response, 'movies_app/about.html')