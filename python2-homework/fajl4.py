with open('adat.txt', 'r') as f1:
    my_list = f1.readlines()

with open('fajl4-hez masik.py', 'w') as f2:
    for i in my_list:
        f2.write(i)
