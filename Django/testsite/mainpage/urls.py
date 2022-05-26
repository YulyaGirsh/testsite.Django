from django.urls import path
from .views import index, get_category, views_places

from .views import *
app_name = 'mainpage'
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='location'),
    path('category/<int:places_id>/', views_places, get_category, name='views_places'),

]
