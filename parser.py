import numpy as np


def parse_file (file):
    taillard_file = open(file, "r")
    line = taillard_file.readline()
    nb = int(line.strip())
    weight = []
    distance = []
    print(nb)
    i = 0
    for line in taillard_file.readlines():
        print(line)
        tab = line.split()
        number_tab = [[int(x) for x in tab]]
        if len(number_tab[0]) != 0:
            i += 1
            if i <= nb:
                weight += number_tab
            else:
                distance += number_tab
            print(number_tab)
            print(distance)
    print(weight)
    print(distance)
    weight = np.array(weight)
    distance = np.array(distance)
    return weight, distance


a, b = parse_file("data/taillard12a.txt")
print(a)
print(b)