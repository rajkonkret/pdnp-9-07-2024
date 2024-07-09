import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>

print(5 * wiek)  # 235
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)  # 0.023221343873517788, float
print(rok // wiek)  # 2024 // 47 = 43 bo 43 * 47 = 2021 reszty 3, czesc całkowita z dzielenia
print(rok % wiek)  # reszta z dzielenia, modulo 3
print(5 % 2)  # reszta 1
print(wiek ** rok)  # potęgowanie
# len() - długość kolekcji
print(len(str(wiek ** rok)))  # długość 3385 znaków
# print(len(str(wiek ** rok ** 2)))  # ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# 1.3 x 10 ^ 3
print(0.1 + 0.2)  # 0.30000000000000004
# liczby typu float posiadają błąd zaokrąglenia
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")

print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda fałsz
# True, False
czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>, typ logiczny
# 1 - prawda, 0 - fałsz
print(int(False))  # 0
print(int(czy_znasz_python))  # 1

x = 1
print(bool(x))  # True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = "radek"
print(bool(x))  # True
x = ''
print(bool(x))  # False
x = 0
print(bool(x))  # False
x = None  # nic, nie wiem, null
print(bool(x))  # False

# działąnia logiczne
# and - i
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

x = 0
print(not x == 1)  # == porównanie, True 0 nie jest równwe 1 dlatego wynik True

a = 8
b = 6

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a < b = }")  # Porównanie a < b = False
print(f"Porównanie {a <= b = }")  # Porównanie a <= b = False
print(f"Porównanie {a >= b = }")  # Porównanie a >= b = True
print(f"Porównanie {a == b = }")  # Porównanie a == b = False   # == porównanie
print(f"Porównanie {a != b = }")  # Porównanie a True        # != - różne
