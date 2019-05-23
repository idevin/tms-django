from django.shortcuts import render, redirect
from avia.forms import AviaForm


# Create your views here.

def index(request):
    form = AviaForm()
    return render(request, "avia/index.html", {"form": form})


def create(request):
    if request.method == "POST":
        return render(request, "avia/results.html")
    else:
        return redirect(index)
