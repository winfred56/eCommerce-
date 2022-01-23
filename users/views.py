from email import message
from http.client import ImproperConnectionState
from django.shortcuts import render, redirect
from .models import Profile
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data.get('email')
            send_mail = ("Welcome To Winfred Ecommerce !", "We very delighted to have you.", "We very delighted to have you.", settings.EMAIL_HOST_USER, recipient)
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form':form})

