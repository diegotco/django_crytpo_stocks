#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol=sfasfsfasdfs'
parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '9496fbdd-0baa-4f97-8cfc-40f8d3231c1b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
  dic = data["data"]
  print(dic)
  print(type(dic))
  for v in dic.values():
    if v:
      print("Lleno", dic)
    else:
      print("vacio")

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)