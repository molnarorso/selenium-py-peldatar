with open('adat.txt', 'r') as f1:
    with open('fajl5-hoz masik.py', 'w') as f2:
        for i in f1.readlines():
            f2.write(i)
