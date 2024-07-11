# json = {"name" : "Radek"}
# obiekt typu pata klucz - wartość
# odpowiednikiem jsona w pythonie jest słownik
import json

person_dict = {'name': "Radek", 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

# upiększenie
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowane klucze
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)
print(type(data))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
print(data['name'])  # Radek

json_text = json.dumps(data)
print(json_text)
print(type(json_text))
# {"age": 40, "czy_pali": null, "name": "Radek"}
# <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
