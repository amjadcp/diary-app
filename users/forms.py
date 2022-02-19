from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *



class RegistrationForm(UserCreationForm):
    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'gender', 'birthday') 
    def __init__(self, *args, **kargs):
        super(RegistrationForm, self).__init__(*args, **kargs)
        self.fields['username'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'Username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'First Name',
            'name' : 'first_name',
            'id' : 'first_name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'Last Name',
            'name' : 'last_name',
            'id' : 'last_name',
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'Email',
            'name' : 'email',
            'id' : 'email',
        })

        self.fields['password1'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'Password',
            'name' : 'password1',
            'id' : 'password1',
        })

        self.fields['password2'].widget.attrs.update({
            'class' : 'input--style-4',
            'placeholder' : 'Confirm Password',
            'name' : 'password2',
            'id' : 'password2',
        })

        self.fields['gender'].widget.attrs.update({
            'class' : 'rs-select2 js-select-simple select--no-search',
            'type' : 'radio',
            'name' : 'gender',
            'id' : 'gender',
        })

        self.fields['birthday'].widget.attrs.update({
            'class' : 'form-control js-datepicker',
            'placeholder' : 'birthday',
            'name' : 'birthday',
            'id' : 'birthday',
            'type' : 'text',
        })
        