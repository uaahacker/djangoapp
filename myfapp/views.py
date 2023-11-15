from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")


def solar(request):
    return render(request, "solar.html")