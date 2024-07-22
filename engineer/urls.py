from django.urls import path
from engineer.views import EngineerDashboardView


app_name = 'engineer'

urlpatterns = [
    path('dashboard/', EngineerDashboardView.as_view(), name = 'engineer_dashboard') 
]