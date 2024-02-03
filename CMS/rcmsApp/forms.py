from django import forms
from .models import Customer, Complaint, Item, Model, Brand

class CustomerRegistrationForm(forms.ModelForm): #this is customer registration form
    class Meta:
        model = Customer  # Replace YourModel with the actual model class
        fields = ['name', 'phone_number', 'email_id', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name*'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number*'}),
            'email_id': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
            self.fields[field_name].help_text = ''


class PhoneSearchForm(forms.Form):
    phone_number = forms.CharField(label='Enter Phone Number', max_length=15)

class EngineerSearchForm(forms.Form):
    engineer_name = forms.CharField(label='Engineer Name', max_length=255)
    engineer_phone_number = forms.CharField(label='Engineer Phone Number', max_length=15)




class ComplaintForm(forms.Form):
    customer_name = forms.CharField(max_length=255, required=True)
    customer_phone_number = forms.CharField(max_length=15, required=True, help_text='Enter your phone number')
    complaint = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), required=True)
    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=False, empty_label="Select Item")
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False, empty_label="Select Brand")
    model = forms.ModelChoiceField(queryset=Model.objects.all(), required=False, empty_label="Select Model")

class NewComplaintForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number', max_length=15)

    class Meta:
        model = Complaint
        fields = ['phone_number', 'item', 'brand', 'model', 'complaint']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Add any validation or cleaning logic for the phone number if needed
        return phone_number

    def save(self, commit=True):
        instance = super().save(commit=False)
        customer, created = Customer.objects.get_or_create(phone_number=self.cleaned_data['phone_number'])
        instance.customer = customer
        if commit:
            instance.save()
        return instance