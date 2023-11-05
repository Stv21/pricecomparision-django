# forms.py
from django import forms

class PriceAlertForm(forms.Form):
    url = forms.URLField(label='Flipkart URL', required=True)
    desired_price = forms.DecimalField(label='Desired Price', required=True)
