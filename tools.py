import numpy as np
from Methodes.Tabou import Tabou

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


"""a, b = parse_file("data/taillard12a.txt")
print(a)
print(b)"""


def fitness(weight_array, dist_array, placement_array):
    sum = 0
    for index_a, placement_a in enumerate(placement_array):
        for index_b, placement_b in enumerate(placement_array[index_a+1:]):
            sum += weight_array[placement_a][placement_b]*dist_array[index_a][index_b + index_a + 1]
    return sum*2


def tab_contains(tab, element):
    for tab_element in tab:
        if tab_element == element:
            return True
    return False
