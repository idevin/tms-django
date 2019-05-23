from django.shortcuts import render, redirect
from avia.forms import AviaForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    form = AviaForm()
    return render(request, "avia/index.html", {"form": form})


def create(request):
    if request.method == "POST":
        form = AviaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, "avia/results.html", context=data)
        else:
            errors = form.errors
            return HttpResponse(f"{errors}")
    else:
        return redirect(index)
