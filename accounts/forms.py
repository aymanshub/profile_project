from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'first_name',
            'last_name',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'email',
            'birth_date',
            'bio',
            'avatar',
            'city',
            'state',
            'country_of_residence',
            'favorite_animal',
            'hobby',
        ]
