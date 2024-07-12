import requests

# pip instal requests
url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
# http get

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx - ok
# 3xx przekierowania
# 4xx 404 - brak zasobu, 400 Bad Request
# 5xx 500 internal Server Error bład serwera
print(response.text)  # odczytujemy jsona (str)
# {"table":"A","currency":"euro","code":"EUR",
# "rates":[{"no":"135/A/NBP/2024","effectiveDate":"2024-07-12","mid":4.2567}]}
response_data = response.json()  # zamiana jsona na słownik
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '135/A/NBP/2024', 'effectiveDate': '2024-07-12', 'mid': 4.2567}]}
print(response_data)

print(type(response_data))  # <class 'dict'>
print(response_data['currency'])  # euro
print(response_data['code'])  # EUR
print(response_data['rates'])
# [{'no': '135/A/NBP/2024', 'effectiveDate': '2024-07-12', 'mid': 4.2567}]
print(response_data['rates'][0])  # {'no': '135/A/NBP/2024', 'effectiveDate': '2024-07-12', 'mid': 4.2567}
print(response_data['rates'][0]['mid'])  # 4.2567
