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
            avia_passengers = form.cleaned_data['avia_passengers']

            price = 100 if avia_passengers == 1 else 100 * 2 * avia_passengers

            return render(request, "avia/results.html", {"price": price, "form": form})
        else:
            return HttpResponse(f"{form.errors}")
    else:
        return redirect(index)
