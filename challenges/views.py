from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


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


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    list_items = ''
    for month in months:
        capatalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'\n <li><a href="{month_path}">{capatalized_month}</a></li>'

    response_data = f'<ul> {list_items} </ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if ((month > len(months)) or (month < 1)):
        return HttpResponseNotFound('Invalid Month!')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    # '/challenges/'+redirect_month
    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
