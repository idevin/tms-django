from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"len is {len(name)}")

    return HttpResponse("NO POST RESPONSE")
