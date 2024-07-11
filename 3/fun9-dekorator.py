# dekorator - wykorzystuje mechanizm funkcji wewnętrznej
# dekorator przyjmuje funkcje i dodaje noą funkcjonalność

# funkcja dekorująca
def dekor(func):
    def wew():
        print("Dekorujemy")
        return func()

    return wew  # adres funkcji wew


@dekor  # uzywamy dekoratora dekor na tej funkcji
def hej():
    print("Hej")


hej()  # Hej
# Po dodaniu dekoratora
# Dekorujemy
# Hej
