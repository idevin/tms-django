from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = "DENIED"
    if request.method == "POST":
        age = int(request.POST.get("age"))
        if age >= 18:
            text = "Welcome"
    return HttpResponse(text)
