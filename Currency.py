import urllib.request
import json

url_eur = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json'
url_usd = 'https://api.nbp.pl/api/exchangerates/rates/A/USD/?format=json'
url_chf = 'https://api.nbp.pl/api/exchangerates/rates/A/CHF/?format=json'

with urllib.request.urlopen(url_eur) as response_eur:
    kwota_eur = json.load(response_eur)

with urllib.request.urlopen(url_usd) as response_usd:
    kwota_usd = json.load(response_usd)

with urllib.request.urlopen(url_chf) as response_chf:
    kwota_chf = json.load(response_chf)
import pprint


kwota = float(input('Enter Amount:'))
waluta = input('Enter Currency:')
kurs_USD =(kwota_usd["rates"][0]["mid"])
kurs_EUR=(kwota_eur["rates"][0]["mid"])
kurs_CHF =(kwota_chf["rates"][0]["mid"])

if waluta == "USD":
    kwota_pln = kwota * kurs_USD
elif waluta == "EUR":
    kwota_pln = kwota * kurs_EUR
elif waluta == "CHF":
    kwota_pln = kwota * kurs_CHF
else:
    print(f"Unknown currency {waluta}")
    exit(1)

print(f'Amount {kwota} {waluta} is {kwota_pln} PLN')