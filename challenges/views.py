from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

#def january(request):
#    return HttpResponse("Study Django 1 hour a day!")

#def february(response):
#    return HttpResponse("Study Python 1 hour a day!")

def monthly_challenge(request, month): #using month bcuz thats our argument name in urls.py
    challenge_text= None
    if month == 'january':
        challenge_text = "Study Django 1 hour a day!"
    elif month == 'february':
        challenge_text = "Study Python 1 hour a day!"
    else:
        return HttpResponseNotFound("This month is not valid!")

    return HttpResponse(challenge_text)

