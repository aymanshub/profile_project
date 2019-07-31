from PIL import Image
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
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
        widget=FengyuanChenDatePickerInput()
    )
    avatar = forms.ImageField(widget=forms.FileInput, required=False)

    # Avatar parameters will be hidden,
    # need them for FE to BE calculations
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    rotate = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    scaleX = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    scaleY = forms.IntegerField(widget=forms.HiddenInput(), required=False)

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

    def save(self):
        profile = super().save()

        # save avatar picture if only a new one has been selected
        if len(self.files):
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            w = self.cleaned_data.get('width')
            h = self.cleaned_data.get('height')
            rotate = self.cleaned_data.get('rotate')
            scaleX = self.cleaned_data.get('scaleX')
            scaleY = self.cleaned_data.get('scaleY')

            image = Image.open(profile.avatar)

            if scaleX == -1:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if scaleY == -1:
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            if rotate:
                image = image.rotate(rotate*-1, expand=True)

            if x or y or w or h:
                image = image.crop((x, y, w + x, h + y))

            image.save(profile.avatar.path)

        return profile