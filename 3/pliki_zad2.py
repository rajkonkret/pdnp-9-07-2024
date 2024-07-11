import chardet

# pip install chardet
# Chardet: The Universal Character Encoding Detector

with open('test.log', 'rb') as f:  # rb - odczyt binarny
    raw_data = f.read()

print(raw_data)
# b'Dodane\r\nDodane\r\nDodane\r\nDodane\r\nKolejne dodane\r\nKolejne dodane\r\nKolejne do\xc5\x9bdane\r\n'
result = chardet.detect(raw_data)
print(result)  # {'encoding': 'MacRoman', 'confidence': 0.6506521739130434, 'language': ''}
# po zwiększeniu próbki (większa ilość danych)
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# Dodane
# Dodane
# Dodane
# Dodane
# Kolejne dodane
# Kolejne dodane
# Kolejne dodane
# Kolejne doćąźśdane
