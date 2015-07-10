from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    return JsonResponse({
        'firstName': 'Luis',
        'lastName': "Orozco",
        'Example': {
            "Data1": True,
            "Data2": (1, 2, 3, 4),
            "Data3": [5, 6, 7, 8]
        }
    })


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)