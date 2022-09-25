from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,"home/home.html",context)

def about(request):
    context = {}
    return render(request,"home/about.html",context)

def feedback(request):
    context = {}
    return render(request,"home/feedback.html",context)

def menu(request):
    context = {}
    return render(request,"home/menu.html",context)