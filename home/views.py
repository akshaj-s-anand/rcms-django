from django.views.generic import CreateView, View, TemplateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from home.models import Enquiry, ProductDetails, Contact
from home.forms import EnquiryForm, ProductFilterForm, ContactForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
class CheckPhoneNumber(View):
    def get(self, request):
        phone_number = request.GET.get('phone_number', None)
        response = {
            'exists': False,
            'name': ''
        }
        if phone_number:
            try:
                enquiry = Enquiry.objects.get(phone_number=phone_number)
                response['exists'] = True
                response['name'] = enquiry.name
            except Enquiry.DoesNotExist:
                pass
        return JsonResponse(response)

@method_decorator(csrf_exempt, name='dispatch')
class Home(CreateView, SuccessMessageMixin):
    template_name = 'home.html'
    model = Enquiry
    form_class = EnquiryForm
    # success_url = reverse_lazy('home:home')
    success_message = "Your enquiry has been submitted successfully!"
    
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        # Override get_success_url to return None or an empty string to prevent redirection
        return None

class SuryaGharView(TemplateView):
    template_name = 'surya_ghar.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class ServiceView(TemplateView):
    template_name = 'services.html'
    
class ProductView(ListView):
    template_name = 'products.html'
    model = ProductDetails
    context_object_name = 'products' 
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        recommended_uses = self.request.GET.get('recommended_uses_for_product')
        power_source = self.request.GET.get('power_source')
        
        if category:
            queryset = queryset.filter(category=category)
        if brand:
            queryset = queryset.filter(brand=brand)
        if recommended_uses:
            queryset = queryset.filter(recommended_uses_for_product=recommended_uses)
        if power_source:
            queryset = queryset.filter(power_source=power_source)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductFilterForm(self.request.GET)
        return context
    
class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = 'home:home'
    
class ComplaintView(TemplateView):
    template_name = 'complaints.html'