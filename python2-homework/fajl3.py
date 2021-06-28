with open('adat.txt', 'r') as f1:
    my_list = f1.readlines()

with open('fajl3-hoz masik.py', 'w') as f2:
    f2.write(str(my_list))

