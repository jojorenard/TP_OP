from Methodes.aleatoire import Aleatoire
import tools
import numpy as np

a, b = tools.parse_file("data/taillard12a.txt")
print(a)
print(b)
Aleatoire(a, b, 100)
