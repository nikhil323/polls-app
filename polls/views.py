from django.http import HttpResponse


def index(request, **kwargs):
    print("========>", request, kwargs)
    return HttpResponse("Hello, world. You're at the polls index.")