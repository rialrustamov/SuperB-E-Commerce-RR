from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages as message

from django.contrib.auth import get_user_model, login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.db import transaction

from user.models import *
from user.forms import *
from core.views import index

# Create your views here.

User = get_user_model()

def register_user(request):
    if request.method == 'POST' and 'register' in request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User(
                    username = form.cleaned_data.get('email'),
                    email=form.cleaned_data.get('email'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                )
                user.set_password(form.cleaned_data.get('password'))
                user.save()
            print("Done_Register")
        print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data.get('email')).first()
            login(request, user)
            return redirect(index)
            print("Done_Login")
        print(form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})




# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password_success')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')


def account_info(request):
    if request.method == "POST":
        print("salam")
        user_info = AccountInfo(request.POST)
        print(user_info,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        if user_info.is_valid():
            print("buda")
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.save()
    else:
        user_info = AccountInfo()
    
    return render(request, 'account_information.html', {'user_info': user_info})



def forgot_password(request):
    return render(request, 'forgot_password.html')



# Views

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "password_success.html")