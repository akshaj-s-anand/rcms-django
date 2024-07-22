from django.urls import path
from dealer.views import DealerDashboardView


app_name = 'dealers'

urlpatterns = [
    path('dashboard/', DealerDashboardView.as_view(), name='dealer_dashboard')
]