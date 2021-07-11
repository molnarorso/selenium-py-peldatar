import csv

with open('fajlcsvszureshez.csv', 'w', newline='', encoding='utf-8') as f0:
    with open('table_in.csv', 'r', newline='', encoding='utf-8') as f1:
        reader = csv.reader(f1)
        for i in reader:
            f0.write(i[1])
            f0.write(',')
            f0.write(i[0])
            f0.write('\n')