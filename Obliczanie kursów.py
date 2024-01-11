import requests
from datetime import datetime, timedelta

def pobierz_kursy_waluty(waluta):
    url = f'https://api.nbp.pl/api/exchangerates/rates/A/{waluta}/last/7/?format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        kursy = [entry['mid'] for entry in data['rates']]
        return kursy
    else:
        print(f"Błąd podczas pobierania danych dla {waluta}")
        return None

def czy_wartosc_wzrosla_spadla(kursy):
    if kursy is not None and len(kursy) >= 2:
        poprzedni_kurs, ostatni_kurs = kursy[-2], kursy[-1]

        if ostatni_kurs > poprzedni_kurs:
            return "Wzrost"
        elif ostatni_kurs < poprzedni_kurs:
            return "Spadek"
        else:
            return "Bez zmian"
    else:
        return "Brak danych do analizy"

def main():
    waluta = input("Podaj kod waluty (CHF, EUR, PLN, USD, GBP): ").upper()

    if waluta not in ["CHF", "EUR", "PLN", "USD", "GBP"]:
        print("Nieprawidłowy kod waluty. Program zakończył działanie.")
        return

    kursy_waluty = pobierz_kursy_waluty(waluta)
    analiza = czy_wartosc_wzrosla_spadla(kursy_waluty)

    print(f"Analiza wahania kursu {waluta}: {analiza}")

if __name__ == "__main__":
    main()
