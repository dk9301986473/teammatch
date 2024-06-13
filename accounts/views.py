from django.shortcuts import render,redirect


# Create your views here.



def register(request):
    return render(request,'index.html')