from home.models import Enquiry, ProductDetails, Contact
from django import forms
from django.core.validators import RegexValidator

class EnquiryForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex='^\d{1,10}$',
                message='Phone number must be between 1 and 10 digits',
                code='invalid_phone_number'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Max 10 numbers',
            'class': 'form-control',
            'maxlength': '10'
        })
    )

    class Meta:
        model = Enquiry
        fields = ['phone_number', 'name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter your Name',
            'class': 'form-control'
        })

class ProductFilterForm(forms.Form):
    name = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'})
    )
    brand = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'})
    )
    category = forms.ChoiceField(
        choices=ProductDetails.PRODUCT_LIST, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    recommended_uses_for_product = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recommended Uses'})
    )
    power_source = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power Source'})
    )

    class Meta:
        model = ProductDetails
        fields = ['name', 'brand', 'category', 'recommended_uses_for_product', 'power_source']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }