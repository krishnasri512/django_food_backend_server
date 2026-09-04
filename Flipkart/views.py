from django.shortcuts import render

# Create your views here.

def flipcart(req):
    return render(req,"index.html")


def myntra(request):
    return render(request,"index.html")