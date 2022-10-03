from django.db import models

# Create your models here.

class Crypto(models.Model):
    crypto_ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.crypto_ticker
        

class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


