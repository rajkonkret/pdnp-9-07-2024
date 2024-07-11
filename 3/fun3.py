a = 10
b = 15


def dodaj():
    a = 7  # zmienne o zasiegu lokalnym
    b = 9
    print(a + b)


def dodaj2():
    print(a + b)  # wykona na zmiennych globalnych


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 9
    b = 8
    print(a + b)


print(f"Wartość a z góry (blobalna) wynosi  {a=}")  # Wartość a z góry wynosi  a=10
dodaj()  # 16
print(f"Wartość a z góry wynosi (globalna)   {a=}")  # Wartość a z góry wynosi  a=10
dodaj2()  # 25
print(f"Wartość a z góry wynosi (globalna)   {a=}")  # Wartość a z góry wynosi  a=10
dodaj3()  # 17
print(f"Wartość a z góry wynosi (globalna)   {a=}")  # Wartość a z góry wynosi (globalna)   a=9
dodaj2()  # 24
print(f"Wartość a z góry wynosi (globalna)   {a=}")  # Wartość a z góry wynosi (globalna)   a=9
