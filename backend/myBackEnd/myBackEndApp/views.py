from django.shortcuts import render


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")
