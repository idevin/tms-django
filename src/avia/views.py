from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, "avia/index.html")


def create(request):
    if request.method == "POST":
        return render(request, "avia/results.html")
    else:
        return redirect(index)
