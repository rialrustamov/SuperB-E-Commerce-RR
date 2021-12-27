from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()


class UserRegisterForm(forms.Form):
    email = forms.EmailField(max_length=50, help_text='Max 50 character', required=True, widget=forms.EmailInput(attrs={ 
        'type' : "text",
        'id' : "email", 
        'name' : "", 
        'title' : "",
        'class' : "input-text"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'id' : "pass", 
        'name' : "", 
        'title' : "",
        'class' : "input-text"}))
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'id' : "pass2", 
        'name' : "", 
        'title' : "",
        'class' : "input-text"}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "name", 
        'name' : "",
        'class' : "input-text"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "surname", 
        'name' : "",
        'class' : "input-text"}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)
    photo = forms.ImageField(label='Photo', required=False)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already in use.')
        return email

    def clean(self):
        data = super(UserRegisterForm, self).clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation does not match.')
        return data


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={ 
        'type' : "text",
        'id' : "email", 
        'name' : "", 
        'title' : "",
        'class' : "input-text"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'id' : "pass", 
        'name' : "", 
        'title' : "",
        'class' : "input-text"}))

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data['email']).first()
        if not user:
            raise forms.ValidationError('User does not exist.')
        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError('Password is incorrect.')
        return self.cleaned_data


class PasswordChangingForm(PasswordChangeForm):
#     first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
#         'type' :"text", 
#         'id' : "firstname", 
#         'name' : "",
#         'value' : "Rial",
#         'maxlength' : "255",
#         'class' : "input-text required-entry"}))
#     last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
#         'type' :"text", 
#         'id' : "lastname",
#         'name' : "",
#         'value' : "Rustamov",
#         'maxlength' : "255",
#         'class' : "input-text required-entry"}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={ 
#         'type' : "text",
#         'name' : "", 
#         'id' : "email",
#         'value' : "example@example.com",
#         'title' : "Email Address",
#         'class' : "input-text required-entry validate-email"}))
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'title' : "Current Password",
        'id' : "current_password", 
        'class' : "input-text"}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'id' : "password", 
        'name' : "", 
        'title' : "New Password",
        'class' : "input-text validate-password"}))
    new_password2 = forms.CharField(label='New Password Confirmation', widget=forms.PasswordInput(attrs={ 
        'type' : "password",
        'id' : "confirmation", 
        'name' : "", 
        'title' : "Confirm New Password",
        'class' : "input-text validate-cpassword"}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class AccountInfo(forms.Form):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "name", 
        'name' : "",
        'class' : "input-text"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "surname", 
        'name' : "",
        'class' : "input-text"}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)
    photo = forms.ImageField(label='Photo', required=False)

     
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already in use.')
        return email