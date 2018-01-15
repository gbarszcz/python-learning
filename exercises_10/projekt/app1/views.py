from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import render_to_string

def index(request):
    return HttpResponse("Hello world")


def par(request, p, p2):
    return HttpResponse(p + ", " + p2)

def template(request, p, p2):
    d = {
        'zmienna': p,
        'zmienna2': p2
    }
    template = render_to_string('template.html', d)
    return HttpResponse(template)
