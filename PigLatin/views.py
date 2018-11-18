from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def translate(request):
    original = request.GET["Text"]
    translation = " ".join(f"{word}yay " if word[0].lower() in {"a", "o", "i", "e", "u"}
                      else f"{word[1:]}{word[0]}ay " for word in original.split())

    return render(request, "translate.html", {"original": original, "translation": translation})


def about(request):
    return render(request, 'about.html')
