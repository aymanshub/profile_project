from django import forms
from django.core import validators
from . import models
from ckeditor.widgets import CKEditorWidget
from .widgets import FengyuanChenDatePickerInput


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'first_name',
            'last_name',
        ]


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget(),
                          validators=[validators.MinLengthValidator(10)]
                          )
    birth_date = forms.DateField(
        # input_formats=['%d/%m/%Y %H:%M'],
        input_formats=['%d/%m/%Y'],
        widget=FengyuanChenDatePickerInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        verify_email = cleaned_data.get('verify_email')

        if email != verify_email:
            raise forms.ValidationError(
                    "You need to enter the same email in both fields"
                )

    class Meta:
        model = models.Profile
        fields = [
            'email',
            'verify_email',
            'birth_date',
            'bio',
            'avatar',
            'city',
            'state',
            'country_of_residence',
            'favorite_animal',
            'hobby',
        ]
