from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../accounts/login')
    return render(request, 'registration/registration.html', {'form':form})
