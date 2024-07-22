from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class CustomerCreationWithGroupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        # Bypass default validation
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("Please confirm your password")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group, created = Group.objects.get_or_create(name='Customer')
            user.groups.add(group)
        return user
