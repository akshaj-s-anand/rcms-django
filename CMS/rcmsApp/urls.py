from django.urls import path
from . import views
from .views import search_complaints, engineer_search, complaint_list, new_complaint, register_complaint

urlpatterns = [
    path("", views.index, name="index"),
    path("complaint-form/", views.complaint_form, name="complaint_form"),
    path('search-complaints/', search_complaints, name='search_complaints'),
    path('engineer-search/', engineer_search, name='engineer_search'),
    path('complaint_list/', complaint_list, name='complaint_list'),
    path('new_complaint/', new_complaint, name='new_complaint'),
    path('register_complaint/', register_complaint, name='register_complaint'),
]
