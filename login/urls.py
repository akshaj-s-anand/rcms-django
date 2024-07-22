from django.urls import path
from login.views import SuperuserLoginView, EngineerLoginView, DealerLoginView, CustomerLoginView, LogoutView

app_name= 'login'

urlpatterns = [
    path('superuser/', SuperuserLoginView.as_view(), name='superuser_login'),
    path('engineer/', EngineerLoginView.as_view(), name='engineer_login'),
    path('dealer/', DealerLoginView.as_view(), name='dealer_login'),
    path('customer/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]