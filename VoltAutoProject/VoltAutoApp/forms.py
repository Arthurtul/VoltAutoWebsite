from django import forms
from .models import Car, Comment, CarModel


class CarForm(forms.ModelForm):
    year = forms.ChoiceField(choices=[(r, r) for r in range(1990, 2025)])

    class Meta:
        model = Car
        fields = ['title', 'automaker', 'car_model', 'description', 'price', 'image', 'year', 'mileage', 'battery_capacity', 'range_per_charge']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
