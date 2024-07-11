import csv

fields = []
rows = []

filename = 'records_2.csv'
# filename = 'records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "
    f.seek(0)  # zerujemy odczyt pliku na początek
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(f, delimiter=";")
    print(csvreader)  # <_csv.reader object at 0x000001B8092A1180>
    fields = next(csvreader)  # odczyt pojedynczego elemntu z iteratora, ustawia wskaźnik na następny

    for row in csvreader:  # po odczytaniu przez next pierwszego elementu ta pętla wystartuje od drugiego elemntu
        # print(row)
        rows.append(row)


print(rows)
print(fields)
# [['Radek', 'Coe', '2', '9.1']]
# ['name', 'branch', 'year', 'cgpa']
# ,
# "
# <_csv.reader object at 0x000001FB921B1180>
# [['Radek', 'Coe', '2', '9.1']]
# ['name', 'branch', 'year', 'cgpa']
#
# Process finished with exit code 0

