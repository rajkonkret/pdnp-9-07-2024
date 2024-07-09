import sys

print()  # wypisz/wydrukuj
print("Nazywam się Radek")
print('Nazywam się Radek')
# print("Nazywam się Radek')
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-9-07-2024\1\pierwszy.py", line 4
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 4)
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
# ctrl d - powielanie zaznaczonych elementów
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, tekst
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'>, liczba całkowita
print(sys.int_info)
# zakres inta określony liczbą znaków
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
print(39 + 39)  # 78
print("39" + "39")  # konkatenacja, łączenie tekstów 3939
# silne typowanie - nie ma niejawnej konwersji typów podczas operacji (zamiany)
# my musimy jawnie rzzutować na typ, który potrzebujemy
print(int("39") + 39)  # int() - rzutowanie (zamiana) na int
print("Radek" + str(39))  # Radek39, zamiana na tekst str()

print(160 * "50")  # 160 raz wypisany napis 50, 505050505050505050505050505050505050505050505...
print(160 * 50)  # 8000
print(5 * "4")  # 44444

# zmienna - szufladka, pudełko, przechowuje jeden element
# snake_case -> PEP8
# nazwa powinna sugerować co zmienna zawiera
# typowanie dynamiczne - w kazdej chwili mozemy dowolny typ danych wrzucic do dowolnej zmiennej

name = "Radek"  # wpisanie wartości do zmiennej
print(name)  # wypisanie zawartości zmiennej, nazwa bez cudzysłowia, Radek
print(type(name))  # <class 'str'>

name = 56
print(name)  # 56
print(type(name))  # <class 'int'>

# podpowiedzi
name: str = 90  # to tylko podpowiedź!!!
print(name)  # 90
print(type(name))  # <class 'int'>
# pip install mypy skrypt do sprawdzania czy podpowiedzi sa zgodne z typem danych w zmiennej
# (venv) PS C:\Users\CSComarch\PycharmProjects\pdnp-9-07-2024> mypy .\1\pierwszy.py
# 1\pierwszy.py:52: error:
# Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# 1\pierwszy.py:57: error: Name "name" already defined on line 48  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)

# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(name) + "Kowalski")  # 90Kowalski
print(str("Radek") + "Kowalski")  # RadekKowalski

age = 48
print(age)
print(type(age))
# 48
# <class 'int'>
