from openpyxl import load_workbook

from Methodes.aleatoire import Aleatoire
from Methodes.Tabou import Tabou
from Methodes.Recuit import Recuit
import tools
import random
import numpy as np
import RunTest
import Convert2Excel as convert


'''
# Pour lancer la fonction Aleatoire
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# nombre de pas max
def lancer_aleatoire(iteration, weights, distances, nb_pas=100):
    best_value = float('inf')
    best_schema = []
    solution = list(range(len(weights)))
    for i in range(iteration):
        print(i)
        schema_pro, value_pro, pas_optimal, nb_fitness = Aleatoire(weights, distances, nb_pas, solution).marche()
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
        random.shuffle(solution)
    print("Résultat du lancement de l'algo Aleatoire: ")
    print("Fitness obtenue: ", best_value)
    print("Placement pour chaque équipement obtenu: ", best_schema)


# Pour lancer la fonction Recuit
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# nombre de fois qu'on baisse la proba
# nombre qu'on cherche de voisin par proba
# 1-proba_baisse = taux de baisse de la proba à chaque tour nb_proba_change
def lancer_recuit(iteration, weights, distances, temp, nb_proba_change, nb_voisin_change, proba_baisse):
    best_value = float('inf')
    best_schema = []
    placement_array = np.arange(0, len(weights), 1)
    for i in range(iteration):
        print(i)
        # faire un random
        schema_pro, value_pro, pas_optimal, nb_fitness = Recuit(weights, distances, temp, nb_proba_change,
                                                                nb_voisin_change, proba_baisse).marche()
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
        random.shuffle(placement_array)
    print("Résultat du lancement de l'algo Recuit: ")
    print("Fitness obtenue: ", best_value)
    print("Placement pour chaque équipement obtenu: ", best_schema)


# Pour lancer la fonction Tabou
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# taille de la liste tabou
# nombre de pas max
# limit de voisinage
def lancer_tabou(iteration, weights, distances, tabou_size=20, nb_pas=100, limit=0):
    best_value = float('inf')
    best_schema = []
    placement_array = np.arange(0, len(weights), 1)
    for i in range(iteration):
        print(i)
        # faire un random
        schema_pro, value_pro, pas_optimal, nb_fitness = Tabou(weights, distances, tabou_size, nb_pas, placement_array,
                                                               limit).execute()
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
        random.shuffle(placement_array)
    print("Résultat du lancement de l'algo Tabou: ")
    print("Fitness obtenue: ", best_value)
    print("Placement pour chaque équipement obtenu: ", best_schema)


# a, b = tools.parse_file("data/taillard100a.txt")
# lancer_aleatoire(10, a, b, 10000)
# lancer_recuit(10, a, b, 60000, 1000, 100, 0.99)
# lancer_tabou(10, a, b, 20, 10, 20)

# RunTest.run_aleatoire("12")
# RunTest.run_tabou("12")
# RunTest.run_recuit("12")'''



# Pour executer les aléatoires
# RunTest.run_aleatoire("12")
# RunTest.run_aleatoire("15")
# RunTest.run_aleatoire("17")
# RunTest.run_aleatoire("20")
# RunTest.run_aleatoire("25")
# RunTest.run_aleatoire("30")
# RunTest.run_aleatoire("35")
# RunTest.run_aleatoire("40")

# RunTest.run_aleatoire("50")
# RunTest.run_aleatoire("60")
# RunTest.run_aleatoire("80")
# RunTest.run_aleatoire("100")

# Pour executer les recuits
'''RunTest.run_recuit("12")
RunTest.run_recuit("15")
RunTest.run_recuit("17")
RunTest.run_recuit("20")
RunTest.run_recuit("25")
RunTest.run_recuit("30")
RunTest.run_recuit("35")
RunTest.run_recuit("40")
RunTest.run_recuit("50")
RunTest.run_recuit("60")
RunTest.run_recuit("80")
RunTest.run_recuit("100")'''

# Pour executer les tabous
# RunTest.run_tabou("12")
# RunTest.run_tabou("15")
# RunTest.run_tabou("17")
# RunTest.run_tabou("20")
# RunTest.run_tabou("25")
# RunTest.run_tabou("30")
# RunTest.run_tabou("35")

# RunTest.run_tabou("40")
# RunTest.run_tabou("50")
# RunTest.run_tabou("60")

# RunTest.run_tabou("80")
# RunTest.run_tabou("100")

'''convert.convert_aleatoire("12")
convert.convert_aleatoire("15")
convert.convert_aleatoire("17")
convert.convert_aleatoire("20")
convert.convert_aleatoire("25")
convert.convert_aleatoire("30")
convert.convert_aleatoire("35")
convert.convert_aleatoire("40")
convert.convert_aleatoire("50")
convert.convert_aleatoire("60")
convert.convert_aleatoire("80")
convert.convert_aleatoire("100")'''

'''convert.convert_recuit("12")
convert.convert_recuit("15")
convert.convert_recuit("17")
convert.convert_recuit("20")
convert.convert_recuit("25")
convert.convert_recuit("30")
convert.convert_recuit("35")
convert.convert_recuit("40")
convert.convert_recuit("50")
convert.convert_recuit("60")
convert.convert_recuit("80")
convert.convert_recuit("100")'''

'''convert.convert_tabou("12")
convert.convert_tabou("15")
convert.convert_tabou("17")
convert.convert_tabou("20")
convert.convert_tabou("25")
convert.convert_tabou("30")
convert.convert_tabou("35")
convert.convert_tabou("40")
convert.convert_tabou("50")
convert.convert_tabou("60")
convert.convert_tabou("80")
convert.convert_tabou("100")'''
