from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def page(request):
    my_variable = 'Hello World!'
    years_old = 15
    a_diary = 10
    array_city_capitale = [ "Paris", "London", "Washington" ]

    return render(request, 'en/public/index.html', {'my_var': my_variable,
    'years': years_old, 'array_city': array_city_capitale, 'nb_diaries': a_diary})

# View for connection page.
def connection(request):
    return render(request, 'en/public/connection.html')
