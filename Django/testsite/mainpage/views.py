from django.shortcuts import render
from django.http import HttpResponse
from .models import Places, Categories


def index(request):
    places = Places.objects.all()
    context = {
        'places': places,
        'title': 'Мои любимые места',
    }
    return render(request, 'mainpage/index.html', context)


def get_category(request, category_id):
    places = Places.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    return render(request, 'mainpage/category.html',
                  {'places': places, 'maincategory': category})


def views_places(request, places_id):
    places_item = Places.objects.get(pk=places_id)
    return render(request, 'mainpage/view_places.html', {'places_item': places_item})


def test(request):
    return HttpResponse('<h2>Тестовая страница</h2>')
