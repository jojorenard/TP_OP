from Methodes.aleatoire import Aleatoire
from Methodes.Recuit import Recuit
import tools
import numpy as np

a, b = tools.parse_file("data/taillard12a.txt")
print(a)
print(b)
Aleatoire(a, b, 100)

Recuit(a,b, 60000, 1000, 1000, 0.99)