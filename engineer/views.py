from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class EngineerDashboardView(TemplateView):
    template_name = 'engineer_dashboard.html'