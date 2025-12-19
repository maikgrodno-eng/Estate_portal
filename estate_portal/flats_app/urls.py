from django.urls import path
from flats_app.views import (flats_list, flat_detail, flat_create, flat_edit,
                             flat_delete, send_deal_request, owner_deal_request)


app_name = 'flats'

urlpatterns = [
    #http://localhost:8000/
    path('', flats_list, name='flats_list'),

    #http://localhost:8000/1/
    path('<int:flat_id>/', flat_detail, name='flat_detail'),

    path('add/', flat_create, name='flat_create'),

    path('<int:flat_id>/edit/', flat_edit, name='flat_edit'),

    path('<int:flat_id>/delete/', flat_delete, name='flat_delete'),

    path('<int:flat_id>/deal-request/', send_deal_request, name='send_deal_request'),

    path('my-deal-request/', owner_deal_request, name='owner_deal_request')
]