def powitanie():
    print("Cześć")


def info():
    print("Jestem pakietem")


print(__name__)  # __main__ jak uruchamiam plik bezpośrednio
# przy uruchmianiu podczas importu: pakiet.fun
if __name__ == '__main__':
    print("Uruchomione przy imporcie")
