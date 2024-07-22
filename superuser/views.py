from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class SuperUserDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard.html'
    
    # URL to redirect to for login
    login_url = 'login:superuser_login'
    
    # Define the test function
    def test_func(self):
        return self.request.user.is_superuser

    # Handle the case where the user fails the test
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            # Redirect to a different page for authenticated users who are not superusers
            return redirect('superuser:superuser_dashboard')
        else:
            # Redirect to the login page for unauthenticated users
            return redirect(self.login_url)