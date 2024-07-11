from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no suger for the entire month!'
    elif month == 'february':
        challenge_text = 'Walk for at least 20 minutes every day!'
    elif month == 'march':
        challenge_text = 'Learn Django for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(challenge_text)
