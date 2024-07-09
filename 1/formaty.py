user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # zmiennoprzecinkowy -> float
print(type(wersja))  # <class 'float'>
liczba = 1234567890  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 39 lat.
# %s sprawdza typ
# print("Witaj %d masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczba

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
print("Wiatj {}, masz teraz {} lat".format(user, wiek))  # Wiatj Tomek, masz teraz 39 lat
# f - f-string - sformatowany tekst

# przy wyswietlaniu zaokrągla
print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X się nie zmmieniło", x)  # X się nie zmmieniło 3.14

# zaokrąglenie
y = round(x)
print("y=", y)  # y= 3

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90)
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f'{user:>10}')  # "     Tomek"  wyrównał do prawej do dlugosci 10
print(f'{user:<20}')  # "Tomek               "
print(f'{user:^20}')  # "       Tomek        "

print(liczba)
print(f'NAsza duża liczba {liczba:,}')  # NAsza duża liczba 1,234,567,890
print(f'NAsza duża liczba {liczba:_}')  # NAsza duża liczba 1_234_567_890
print(f'NAsza duża liczba {liczba:,}'.replace(",", " "))  # NAsza duża liczba 1_234_567_890
print(f'NAsza duża liczba {liczba:,}'.replace(",", "."))  # NAsza duża liczba 1_234_567_890
# NAsza duża liczba 1 234 567 890
# NAsza duża liczba 1.234.567.890

liczba2 = 123_456_789_123
print(liczba2)  # 123456789123
print(type(liczba2))  # <class 'int'>
