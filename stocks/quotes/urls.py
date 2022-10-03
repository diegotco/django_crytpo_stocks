from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name="home"),

    # Stocks
    path('stocks.html', views.stocks, name="stocks"),
    path('delete/<stock_id>', views.delete, name="delete" ),
    path('delete_stock.html', views.delete_stock, name="delete_stock" ),

    #Crypto
    path('crypto.html', views.crypto, name="crypto"),
    path('delete/<crypto_id>', views.delete_c, name="delete_c" ),
    path('delete_crypto.html', views.delete_crypto, name="delete_crypto" ),

    
    

]