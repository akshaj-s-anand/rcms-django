from django.urls import path
from superuser.views import SuperUserDashboardView

app_name = 'superuser'

urlpatterns = [
    path('dashboard/', SuperUserDashboardView.as_view(), name = 'superuser_dashboard')
]
