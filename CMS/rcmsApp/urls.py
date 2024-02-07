from django.urls import path
from . import views
from .views import search_complaints, engineer_search, complaint_list, new_complaint, register_complaint, complaint_home, about, contact, services, battery, ups, solar_water_heater, solar_products, brand_orion, brand_livguard

urlpatterns = [
    path("", views.index, name="index"),
    path("complaint-form/", views.complaint_form, name="complaint_form"),
    path('search-complaints/', search_complaints, name='search_complaints'),
    path('engineer-search/', engineer_search, name='engineer_search'),
    path('complaint_list/', complaint_list, name='complaint_list'),
    path('new_complaint/', new_complaint, name='new_complaint'),
    path('register_complaint/', register_complaint, name='register_complaint'),
    path('complaint_home/', complaint_home, name= 'complaint_home'),
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('services/', services, name= 'services'),
    path('battery/', battery, name= 'battery'),
    path('solar_products/', solar_products, name= 'solar_products'),
    path('solar_water_heater/', solar_water_heater, name= 'solar_water_heater'),
    path('ups/', ups, name= 'ups'),
    path('brand_orion/', brand_orion, name= 'brand_orion'),
    path('brand_livguard/', brand_livguard, name= 'brand_livguard'),



]
