from django.urls import path
from home.views import Home,CheckPhoneNumber, SuryaGharView, AboutView, ServiceView, ProductView, ContactView, ComplaintView

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('check_phone_number/', CheckPhoneNumber.as_view(), name='check_phone_number'),
    path('suryaghar/', SuryaGharView.as_view(), name = 'surya_ghar'),
    path('about/', AboutView.as_view(), name= "about"),
    path('service/', ServiceView.as_view(), name= "services"),
    path('products/', ProductView.as_view(), name = 'products'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('complaints/', ComplaintView.as_view(), name='complaint'),
]
