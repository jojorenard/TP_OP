from Methodes.aleatoire import Aleatoire
from Methodes.Tabou import Tabou
from Methodes.Recuit import Recuit
import tools
import random
import numpy as np

a, b = tools.parse_file("data/taillard12a.txt")

def lancer_tabou(iteration, a, b):
    best_value = float('inf')
    best_schema = []
    placement_array = np.arange(0, len(a), 1)
    for i in range(iteration):
        # print(i)
        # faire un random
        schema_pro, value_pro = Tabou(a, b, 20, 100, placement_array).execute()
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
        random.shuffle(placement_array)
    print(best_schema)
    print(best_value)

# Aleatoire(a, b, 100)


lancer_tabou(100, a, b)

# Recuit(a, b, 60000, 1000, 1000, 0.99)
