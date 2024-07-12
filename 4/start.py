# import kl4
import pakiet  # import pakietu
from pakiet.fun import info  # bezposredni import metody ze wskazanego pliku
from pakiet import fun  # importuje plik z pakietu
import pakiet.fun as pf  # plik jako alias

# kur = kl4.Kura("Kura")
# kur.dziobanie()
print(pakiet)  # <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\pdnp-9-07-2024\\pakiet\\__init__.py'>
# po doodaniu w __init__ metody powitanie
# jest ona dostępn apo imporcie pakietu
pakiet.powitanie()
# Cześć
pakiet.fun.info()
# Jestem pakietem
fun.info()
fun.powitanie()
info()  # Jestem pakietem
pf.powitanie()
pf.info()
# Cześć
# Jestem pakietem