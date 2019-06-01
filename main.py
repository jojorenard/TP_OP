from Methodes.aleatoire import Aleatoire
from Methodes.Tabou import Tabou
import tools
import numpy as np

def lancer_tabou(iteration):
    a, b = tools.parse_file("data/taillard12a.txt")
    best_value = float('inf')
    best_schema = []
    for i in range(iteration):
        # faire un random
        schema_pro, value_pro = Tabou(a, b, 200, 100).execute()
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
    print(best_schema)
    print(best_value)

# Aleatoire(a, b, 100)


lancer_tabou(1)
