from django.shortcuts import render

# Create your views here.

def index(request):
    index='this is index page'
    return render(request,'index.html')