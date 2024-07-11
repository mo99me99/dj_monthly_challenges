from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
    'december': None,

}
# Create your views here.


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    return render(request,
                  'challenges/index.html',
                  context={'months': months}
                  )


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if ((month > len(months)) or (month < 1)):
        return HttpResponseNotFound('Invalid Month!')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    # '/challenges/'+redirect_month
    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,
                      'challenges/challenge.html',
                      context={
                          'challenge_text': challenge_text,
                          'month': month
                      }
                      )
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
