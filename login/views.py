# views.py
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import logout
from django.urls import reverse_lazy

class SuperuserLoginView(LoginView):
    template_name = 'login_superuser.html'

    def get_success_url(self):
        return reverse_lazy('superuser:superuser_dashboard')

class EngineerLoginView(LoginView):
    template_name = 'login_engineer.html'

    def get_success_url(self):
        return reverse_lazy('engineer:engineer_dashboard')

class DealerLoginView(LoginView):
    template_name = 'login_dealer.html'

    def get_success_url(self):
        return reverse_lazy('dealers:dealer_dashboard')

class CustomerLoginView(LoginView):
    template_name = 'login_customer.html'

    def get_success_url(self):
        return reverse_lazy('customers:customer_dashboard')

class LogoutView(RedirectView):
    url = reverse_lazy('home:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

