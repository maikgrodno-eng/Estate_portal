from django.urls import path
from flats_app.views import flats_list


app_name = 'flats'

urlpatterns = [
    path('', flats_list, name='flats_list'),
]