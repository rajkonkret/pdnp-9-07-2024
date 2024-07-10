dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wyświetli klucze
for i in dictionary:
    print(i)

# imie
# nazwisko
for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyświetla wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

dictionary_2 = {'name': 'imie', 'company': "Orange"}
d = {}
for k, v in dictionary_2.items():
    d[v] = k
print(d)  # {'imie': 'name', 'Orange': 'company'}

# Dla key, value ze słownika dictionary_2
# zbuduj słownik gdzie value będzie kluczem, key wartością {value:key}
print({value: key for key, value in dictionary_2.items()})  # {'imie': 'name', 'Orange': 'company'}
# items to jest para: 'name': 'imie' -> key : value
# {value:key}
