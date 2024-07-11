# pliki csv
# plik tekstowy w którym wartości rodzielone są znakiem podziału (,;tab)
# Kowalski,Jan,Klodzko

import csv

filename = 'records.csv'
row = ['Radek', 'Coe', 2, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)
# {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

with open(filename, 'w', newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename_2 = 'records_2.csv'
with open(filename_2, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '19.1'},
    {'name': 'Tomek', 'branch': 'Cos', 'year': 3, 'cgpa': '9.11'},
    {'name': 'Zenek', 'branch': 'Cot', 'year': 5, 'cgpa': '9'},
    {'name': 'Marek', 'branch': 'Cog', 'year': 7, 'cgpa': '7.1'},
    {'name': 'Ania', 'branch': 'Coy', 'year': 1, 'cgpa': None},
]

filename_3 = 'records_3.csv'
with open(filename_3, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)

# newline='' - ominiecie problemu końća linii
# delimiter=";"  - wskazanie separatora
