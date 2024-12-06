from django.shortcuts import render, HttpResponse

 
def home(request):
    return render(request , "home.html")

def dashboard(request):
    return render(request , "dashboard.html")

def robux(request):
    return render(request , "robux.html")

    