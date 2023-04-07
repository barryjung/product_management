from django import forms
from .models import Product, Inbound, Outbound

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']


class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['code', 'quantity', 'ammount']


class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['code', 'quantity', 'ammount']
