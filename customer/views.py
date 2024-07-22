from django.shortcuts import render 
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib import messages
from customer.forms import CustomerCreationWithGroupForm
from django.urls import reverse_lazy
from django.http import JsonResponse
# Create your views here.

class CustomerDashboardView(TemplateView):
    template_name = 'customer_dashboard.html'
    
class CustomerListView(ListView):
    template_name = 'superuser/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        customer_group = Group.objects.get(name='Customer')
        return User.objects.filter(groups=customer_group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerCreationWithGroupForm()
        return context

class CustomerCreateView(CreateView):
    form_class = CustomerCreationWithGroupForm
    template_name = 'superuser/add_customer.html'
    success_url = reverse_lazy('customers:customer_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(group)
        
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"message": "Customer created successfully."}, status=200)
        
        messages.success(self.request, 'User created successfully and added to Customer group.')
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
        
        messages.error(self.request, 'Error creating user.')
        return super().form_invalid(form)
    
class CustomerBulkDeleteView(View):
    def post(self, request, *args, **kwargs):
        selected_customers = request.POST.getlist('selected_customers')
        if selected_customers:
            User.objects.filter(id__in=selected_customers).delete()
            messages.success(request, "Selected customers have been deleted.")
        else:
            messages.error(request, "No customers selected.")
        return redirect('customers:customer_list')