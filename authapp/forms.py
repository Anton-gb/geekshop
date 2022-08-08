from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser
import random, hashlib



class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, **kwargs):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user

    def clean_age(self):
        current_age = self.cleaned_data['age']
        if current_age < 18:
            raise forms.ValidationError('Вы слишком молоды для этого')

        return current_age

    def clean_email(self):
        user_email = self.cleaned_data['email']
        if ShopUser.objects.filter(email=user_email).exists():
            raise forms.ValidationError('Эта почта уже зарегистрирована')

        return user_email


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        current_age = self.cleaned_data['age']
        if current_age < 18:
            raise forms.ValidationError('Вы слишком молоды для этого')

        return current_age

    def clean_email(self):
        user_name = self.cleaned_data['username']
        user_email = ShopUser.objects.get(username=user_name).email
        user_email_in_form = self.cleaned_data['email']
        user_email_new = ShopUser.objects.filter(email=user_email_in_form).exists()
        if user_email != user_email_in_form and user_email_new:
            raise forms.ValidationError('Эта почта уже зарегистрирована')

        return user_email
