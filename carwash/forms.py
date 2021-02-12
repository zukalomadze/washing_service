from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.forms import EmailField, CharField, Textarea, ModelChoiceField, TextInput

from carwash.models import Order, Car, WashType, CarType


class CarForm(forms.ModelForm):
    licence_plate = CharField(widget=forms.TextInput(attrs={'class': 'car-input-fields'}))
    car_type = ModelChoiceField(empty_label='Choice Car Type',
                                widget=forms.Select(attrs={'class': 'form-control car-input-fields'}), queryset=CarType.objects.all())

    class Meta:
        model = Car
        fields = ('licence_plate', 'car_type')
