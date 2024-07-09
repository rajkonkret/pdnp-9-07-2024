tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
print(type(tekst))  # <class 'str'>

# chcemy zamienić tekst na duże litery
# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())
tekst_upper = tekst.upper()  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE

tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie
print(type(tekst_lower))  # <class 'str'>

print(tekst.count("i"))  # 3
print(tekst.count("j", 0, 4))  # 0, te szare to tyko podpowiedzi PyCharm
# z praweej strony zbiór otwarty
# (0,4) w tym przypadku analizuje tylko litery z indeksow 0123
#  numerowanie indeksów od 0
# witaj świecie
# 0123456789

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "

print(tekst[4])  # j, podajemy nr indeksu

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie' zapisany jako bajty
# b - dane w postaci binarnej
# \x jako dane szesnastkowe
# \xc5 - 197
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
tekst_format = f"Mam na imię {imie} i lubię pythona."
# f - fstring, tekst sformatowany
print(tekst_format)  # Mam na imię Radek i lubię pythona.
tekst_format_2 = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format_2)
# "	Mam na imię Radek
# i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace
print(f"\tMam na imię {imie.upper()}\n i lubię pythona.\b")
# 	Mam na imię RADEK
#  i lubię pythona

starszy = "Witaj %s!"
print(starszy % imie)  # pod %s podstawiamy wartość zmiennej imie, Witaj Radek!
# %s - string

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Teskt 
wielolinijkowy
    tabulator""")
# "Teskt
# wielolinijkowy
#     tabulator"

"""
Komentarz
wielolinijkowy
"""
print("Imie:", imie)  # Imie: Radek
