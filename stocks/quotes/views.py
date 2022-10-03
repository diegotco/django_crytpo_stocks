#from email import message
from termios import TIOCPKT_FLUSHREAD
from django.shortcuts import render, redirect
from .models import Crypto, Stock
from .forms import CryptoForm, StockForm
from django.contrib import messages
from django.template.defaulttags import register

# Create your views here.

def home(request):
    import requests
    import json

    return render(request, 'home.html')


def crypto(request):
    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json

    if request.method == 'POST':
       
        form = CryptoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your crypto has been added!"))
            return redirect('crypto')
        else:
            messages.error(request, ("That crypto symbol doesn't exist! Try again."))
            return redirect('crypto')
    
    else:

        crypto_ticker = Crypto.objects.all()
        crypto_output = []

        for crypto_item in crypto_ticker:
            url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol="+ str(crypto_item)
            parameters = {
            #   'start':'1',
            #   'limit':'5000',
            #   'convert':'USD'
            }
            headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'XXXX',
            }

            session = Session()
            session.headers.update(headers)

            try:
                response = session.get(url, params=parameters)
                result = json.loads(response.text)
                crypto_output.append(result)    

            except (ConnectionError, Timeout, TooManyRedirects, ValueError) as e:
                print(e)
        crypto_str_list = []
        for i in crypto_ticker:
            text = str(i)
            upper_text = text.upper()
            crypto_str_list.append(upper_text)
        return render(request, 'crypto.html', {'crypto_ticker': crypto_ticker, 'crypto_output': crypto_output, 'range': range(0,len(crypto_ticker)), 'crypto_str_list': crypto_str_list})

def stocks(request):
    import requests
    import json
   
    if request.method == 'POST':

        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your stock has been added!"))
            return redirect('stocks')
        else:
            messages.error(request, ("That stock ticker doesn't exist! Try again."))
            return redirect('stocks')

    else:

        ticker = Stock.objects.all()
        output = []

        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token=XXXX")
            try:
                api = json.loads(api_request.content)
                output.append(api)

            except Exception as e:
                api = "Error..."
                
        str_list = []
        for i in ticker:
            ticker_text = str(i)
            upper_ticker_text = ticker_text.upper()
            str_list.append(str(upper_ticker_text))
        return render(request, 'stocks.html', {'ticker': ticker, 'output': output, 'range': range(0,len(ticker)), 'str_list': str_list})



def delete_c(request, crypto_id):  
    crypto_item = Crypto.objects.get(pk=crypto_id)
    crypto_item.delete()
    messages.success(request, ("Crypto has been deleted!"))
    return redirect(crypto)

def delete_crypto(request): 
    crypto_ticker = Crypto.objects.all()
    return render(request, 'delete_crypto.html', {'crypto_ ticker': crypto_ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted!"))
    return redirect(stocks)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})


@register.filter
def index(indexable, i):
    return indexable[i]

