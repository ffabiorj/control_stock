from django import forms
from .models import Stock


class StockEntryForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'