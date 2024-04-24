from django.shortcuts import render

def home(request):
    context = { "title": "Home" }
    return render(request, "homepage/home.html", context=context)
