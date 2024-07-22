from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class DealerDashboardView(TemplateView):
    template_name = 'dealer_dashboard.html'