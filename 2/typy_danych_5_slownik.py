# słownik - para klucz - wartosc
# klucze nie mogą sie powtórzyć
#  {'user' :"radek"}
# json - słownik odpowiednik jsona

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary1 = {}
print(dictionary1)  # {}
print(type(dictionary1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 37
print(dictionary)  # {'imie': 'Radek', 'wiek': 37}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 37])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 37)])

# nadpisanie elementu
dictionary['imie'] = 'Tomek'
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37}

# wypisanie elementu ze słownika
print(dictionary['imie'])  # Tomek
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37}

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('Imie'))  # None
print(dictionary.get('Imie', 'default'))  # default

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', '3'), ('z', 2)])
print(dict_small)  # {'x': 2, 'y': '3', 'z': 2}

# input() - wprowadzanie danych np.: z klawiatury

# tekst = input("Wpisz tekst")
# print(tekst)

# napisać słownik pol-ang
# zbior danych - slownik
# wyswietlic słowka (klucze)
# pobrac słówko od użytkownika (input())
# wypisać tłuamczenie -> wartośc dla klucza
pol_ang = {'kot': 'cat', 'pies': 'dog', 'jabłko': 'apple'}
print("Słówka do przetłumaczenia", pol_ang.keys())
tekst = input("Podaj co chcesz przetłumaczyć")
# print(pol_ang[tekst.lower().replace(" ", "")])
print(pol_ang.get(tekst, "Nie ma takiego słówka"))
# strip() - usunięcie spacji  i białych znaków

# aplikacja kalkulator
# pobrać liczby od użytkownika
# wypisac wynik obliczenia (+)
a = input("Podaj pierwszą liczbę")  # zwraca str()
b = input("Podaj drugą liczbę")
print(a + b)  # to byląby konkatenacja
# print(pol_ang[tekst.lower().replace(" ", "")])
print(int(a) + float(b))  # 5.0
