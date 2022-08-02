from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
# class EditUserForm(UserChangeForm):
#     class Meta:
#         pass

class UpdateUserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email',]

class wallet_address_form(forms.ModelForm):
    class Meta:
        model = wallet_details
        fields = ['wallet_address',]

# class product_buy(forms.ModelForm):
#     class Meta:
#         model = orders
