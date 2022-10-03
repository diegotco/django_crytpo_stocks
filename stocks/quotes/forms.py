#from socket import fromshare
from django import forms
from .models import Crypto, Stock

class CryptoForm(forms.ModelForm):
    class Meta:
        model = Crypto
        fields = ["crypto_ticker"]

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
