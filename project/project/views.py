# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("hello world")
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html', {
        'content': "Hello Django ",
    })
