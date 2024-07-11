from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render


monthly_challenges = {
    'january': 'january : Eat no suger for the entire month!',
    'february': 'february : Walk for at least 20 minutes every day!',
    'march': 'march !',
    'april': 'april !',
    'may': 'may !',
    'june': 'june !',
    'july': 'july !',
    'august': 'august challenge!',
    'september': 'september challenge!',
    'october': 'october challenge!',
    'november': 'november challenge!',
    'december': 'december challenge!',

}
# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if ((month > len(months)) or (month < 1)):
        return HttpResponseNotFound('Invalid Month!')

    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_to='/challenges/'+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
