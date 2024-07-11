# działania z plikami
# with - context manager
# usprawnia prace z pliki
# open() - operacja na plikach
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jescze jedno\n")

# w - nadpisuje istniejący blik - dane zostają skasowane
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")

# a - dopisuje na końcu pliku
with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Kolejne dodane\n")
    file.write("Kolejne dodane\n")
    file.write("Kolejne dośdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
