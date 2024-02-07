from django.shortcuts import render, redirect
from .models import Complaint, Customer, Engineer, Model, Item, Brand
from .forms import CustomerRegistrationForm, PhoneSearchForm, EngineerSearchForm, ComplaintForm, NewComplaintForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title
    }
    return render(request, 'home/index.html', context)
    
def complaint_form(request): 
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the Customer model
            customer = form.save()
            # Redirect to a success page or another page
            return redirect('register_complaint')
            
    else:
        form = CustomerRegistrationForm()

    complaints = Complaint.objects.all()
    title = "leading power backup solution company -Kerala"
    context = {
        'complaints': complaints,
        'form': form,
        'title':title,
    }
    return render(request, 'support/complaint_form.html', context)

def search_complaints(request):
    if request.method == 'POST':
        form = PhoneSearchForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            customer = Customer.objects.filter(phone_number=phone_number).first()
            if customer:
                complaints = customer.related_complaints().order_by('-pub_date')
                return render(request, 'support/complaint_list.html', {'complaints': complaints})
            else:
                error_message = "No customer found with the specified phone number."
                return render(request, 'support/search_complaints.html', {'form': form, 'error_message': error_message})
    else:
        form = PhoneSearchForm()
    title = "leading power backup solution company -Kerala"
    context = {
        'form': form,
        'title':title,
    }

    return render(request, 'support/search_complaints.html', context)

def engineer_search(request):
    if request.method == 'POST':
        form = EngineerSearchForm(request.POST)
        if form.is_valid():
            engineer_name = form.cleaned_data['engineer_name']
            engineer_phone_number = form.cleaned_data['engineer_phone_number']
            
            # Retrieve the engineer based on name and phone number
            engineer = Engineer.objects.filter(name=engineer_name, phone_number=engineer_phone_number).first()
            
            if engineer:
                # Retrieve complaints related to the engineer
                complaints = Complaint.objects.filter(assigned_engineer=engineer).order_by('-pub_date')
                return render(request, 'support/complaints_for_engineer.html', {'complaints': complaints})
            else:
                error_message = "No engineer found with the specified name and phone number."
                return render(request, 'support/engineer_search.html', {'form': form, 'error_message': error_message})
    else:
        form = EngineerSearchForm()

    title = "leading power backup solution company -Kerala"
    context = {
        'form': form,
        'title':title,
    }
    return render(request, 'support/engineer_search.html', context)



def complaint_list(request):
    title = "leading power backup solution company -Kerala"

    context = {
        'title':title,
    }
    return render(request, 'support/complaint_list.html', context)


def register_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            # Extract form data
            customer_name = form.cleaned_data['customer_name']
            customer_phone_number = form.cleaned_data['customer_phone_number']
            complaint_text = form.cleaned_data['complaint']

            # Find the customer
            customer = Customer.objects.filter(name=customer_name, phone_number=customer_phone_number).first()

            # Ensure the customer is found before proceeding
            if customer:
                # Create a new complaint
                Complaint.objects.create(
                    customer=customer,
                    item=form.cleaned_data['item'],
                    brand=form.cleaned_data['brand'],
                    model=form.cleaned_data['model'],
                    complaint=complaint_text,
                    status='Open'  # Set the default status or customize as needed
                )

                # Redirect to the complaint list or any other page
                return redirect('support/complaint_list')

            # Handle the case when the customer is not found
            error_message = "Customer not found with the specified name and phone number."
            return render(request, 'support/complaint_list.html', {'form': form, 'error_message': error_message})

    else:
        form = ComplaintForm()
        form.fields['item'].queryset = Item.objects.all()
        form.fields['brand'].queryset = Brand.objects.all()
        form.fields['model'].queryset = Model.objects.all()
    title = "leading power backup solution company -Kerala"
    context = {
        'form': form,
        'title':title,
    }

    return render(request, 'support/complaint_list.html', context)


def new_complaint(request):
    if request.method == 'POST':
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support/register_complaint')  # Redirect to the success page
    else:
        form = NewComplaintForm()
    title = "leading power backup solution company -Kerala"
    context = {
        'form': form,
        'title':title,
    }

    return render(request, 'support/new_complaint.html', context)



def register_complaint(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }


    return render(request, 'support/register_complaint.html', context)

def complaint_home(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'support/complaint_home.html', context)

def about(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/about.html', context)

def services(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/services.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Construct email message
            email_message = f'Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage:\n{message}'

            # Send email
            send_mail(
                'New Contact Form Submission',
                email_message,
                email,
                ['webnovaitpark@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'support/register_complaint.html')  # Redirect to success page after form submission
    else:
        form = ContactForm()
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
        'form':form,
    }
    return render(request, 'home/contact.html', context)

def battery(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/battery.html', context)

def solar_products(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/solar_products.html', context)

def solar_water_heater(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/solar_water_heater.html', context)

def ups(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/ups.html', context)

def brand_orion(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/brand_orion.html', context)

def brand_livguard(request):
    title = "leading power backup solution company -Kerala"
    context = {
        'title':title,
    }
    return render(request, 'home/brand_livguard.html', context)