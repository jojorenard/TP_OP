import numpy as np
import datetime
import random
import time

import tools
from Methodes.Recuit import Recuit
from Methodes.Tabou import Tabou
from Methodes.aleatoire import Aleatoire


# Pour écrire dans les fichiers de résultat
def write_fixe(path_and_file, start_time, solution, nb_pas: str, value, pas_optimal, nb_fitness, schema):
    file_result = open("result/"+path_and_file, "a")
    file_result.write("Temps d'exécution :" + str(datetime.timedelta(seconds=time.time() - start_time)) + "\n")
    file_result.write("Les paramètres: \n")
    file_result.write("La plaquette: " + str(solution) + ", Nombre de pas: " + nb_pas + "\n")
    file_result.write("Résultat du lancement de l'algo: \n")
    file_result.write("Fitness obtenue: " + str(value) + " après " + str(pas_optimal) + " pas\n")
    file_result.write("Nombre de fitness calculé en tout: " + str(nb_fitness) + "\n")
    file_result.write("Placement pour chaque équipement obtenu: " + str(schema) + "\n")
    file_result.write("----------------------------------------------------------------------------------\n")
    file_result.close()


def write_random(path_and_file, start_time, iteration, nb_pas: str, best_value, pas_optimal, nb_fitness_total, best_schema):
    file_result = open("result/"+path_and_file, "a")
    file_result.write("Temps d'exécution :" + str(datetime.timedelta(seconds=time.time() - start_time)) + "\n")
    file_result.write("Les paramètres: \n")
    file_result.write("Itération: " + str(iteration) + ", Nombre de pas: " + nb_pas + "\n")
    file_result.write("Résultat du lancement de l'algo: \n")
    file_result.write("Fitness obtenue: " + str(best_value) + " après " + str(pas_optimal) + " pas\n")
    file_result.write("Nombre de fitness calculé en tout: " + str(nb_fitness_total) + "\n")
    file_result.write("Placement pour chaque équipement obtenu: " + str(best_schema) + "\n")
    file_result.write("----------------------------------------------------------------------------------\n")
    file_result.close()


####################################################################################################
# Random
def run_aleatoire(file_number: str):
    file_config = open("test_config/aleatoire/aleatoire"+file_number+".txt", "r")
    file_name = file_config.readline().strip("\n")
    nb_test = file_config.readline().strip("\n")
    index_test = 1
    weights, distances = tools.parse_file("data/"+file_name)
    # Partie avec plaquette fixe
    config = file_config.readline().strip("\n")
    while config != "random":
        lancer_aleatoire_fixe(weights, distances, int(config), file_number)
        config = file_config.readline().strip("\n")
        print(index_test, "/", nb_test)
        index_test += 1
    for config in file_config.readlines():
        config.strip("\n")
        config_infos = config.split(";")
        lancer_aleatoire_random(int(config_infos[0]), weights, distances, int(config_infos[1]), file_number)
        print(index_test, "/", nb_test)
        index_test += 1
    file_config.close()
    print("aleatoire", file_number, "finished")


def lancer_aleatoire_fixe(weights, distances, nb_pas, file_number: str):
    start_time = time.time()
    solution = list(range(len(weights)))
    schema, value, pas_optimal, nb_fitness = Aleatoire(weights, distances, nb_pas, solution).marche()
    write_fixe("aleatoire/aleatoire"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal,
               nb_fitness, schema)

    start_time = time.time()
    solution = list(range(len(weights)-1, -1, -1))
    schema, value, pas_optimal, nb_fitness = Aleatoire(weights, distances, nb_pas, solution).marche()
    write_fixe("aleatoire/aleatoire"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal,
               nb_fitness, schema)

    start_time = time.time()
    solution = list(range(0, len(weights), 2)) + list(range(1, len(weights), 2))
    schema, value, pas_optimal, nb_fitness = Aleatoire(weights, distances, nb_pas, solution).marche()
    write_fixe("aleatoire/aleatoire"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal,
               nb_fitness, schema)


# Pour lancer la fonction Aleatoire
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# nombre de pas max
# le fichier (numéro) concerné
def lancer_aleatoire_random(iteration: int, weights, distances, nb_pas, file_number: str):
    best_value = float('inf')
    best_schema = []
    pas_optimal = 0
    start_time = time.time()
    solution = list(range(len(weights)))
    nb_fitness_total = 0
    for i in range(iteration):
        schema_pro, value_pro, pas_optimal_pro, nb_fitness = Aleatoire(weights, distances, nb_pas, solution).marche()
        nb_fitness_total += nb_fitness
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
            pas_optimal = pas_optimal_pro
        random.shuffle(solution)
    write_random("aleatoire/aleatoire"+file_number+".txt", start_time, iteration, str(nb_pas), best_value, pas_optimal,
                 nb_fitness_total, best_schema)


####################################################################################################
# Recuit
def run_recuit(file_number: str):
    file_config = open("test_config/recuit/recuit"+file_number+".txt", "r")
    file_name = file_config.readline().strip("\n")
    nb_test = file_config.readline().strip("\n")
    index_test = 1
    weights, distances = tools.parse_file("data/"+file_name)
    # Partie avec plaquette fixe
    config = file_config.readline().strip("\n")
    while config != "random":
        config_infos = config.split(";")
        lancer_recuit_fixe(weights, distances, int(config_infos[0]), int(config_infos[1]), int(config_infos[2]),
                           float(config_infos[3]), file_number)
        config = file_config.readline().strip("\n")
        print(index_test, "/", nb_test)
        index_test += 1
    for config in file_config.readlines():
        config.strip("\n")
        config_infos = config.split(";")
        lancer_recuit_random(int(config_infos[0]), weights, distances, int(config_infos[1]), int(config_infos[2]),
                             int(config_infos[3]), float(config_infos[4]), file_number)
        print(index_test, "/", nb_test)
        index_test += 1
    file_config.close()
    print("recuit", file_number, "finished")


def lancer_recuit_fixe(weights, distances, temp, nb_proba_change, nb_voisin_change, proba_baisse, file_number: str):
    nb_page = str(nb_proba_change)+"*"+str(nb_voisin_change)+"="+str(nb_proba_change*nb_voisin_change)
    start_time = time.time()
    solution = list(range(len(weights)))
    schema, value, pas_optimal, nb_fitness = Recuit(weights, distances, temp, nb_proba_change, nb_voisin_change,
                                                    proba_baisse).marche()
    write_fixe("recuit/recuit"+file_number+".txt", start_time, solution, nb_page, value, pas_optimal, nb_fitness,
               schema)

    start_time = time.time()
    solution = list(range(len(weights)-1, -1, -1))
    schema, value, pas_optimal, nb_fitness = Recuit(weights, distances, temp, nb_proba_change, nb_voisin_change,
                                                    proba_baisse).marche()
    write_fixe("recuit/recuit"+file_number+".txt", start_time, solution, nb_page, value, pas_optimal, nb_fitness,
               schema)

    start_time = time.time()
    solution = list(range(0, len(weights), 2)) + list(range(1, len(weights), 2))
    schema, value, pas_optimal, nb_fitness = Recuit(weights, distances, temp, nb_proba_change, nb_voisin_change,
                                                    proba_baisse).marche()
    write_fixe("recuit/recuit"+file_number+".txt", start_time, solution, nb_page, value, pas_optimal, nb_fitness,
               schema)


# Pour lancer la fonction Recuit
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# nombre de fois qu'on baisse la proba
# nombre qu'on cherche de voisin par proba
# 1-proba_baisse = taux de baisse de la proba à chaque tour nb_proba_change
def lancer_recuit_random(iteration, weights, distances, temp, nb_proba_change, nb_voisin_change, proba_baisse,
                         file_number: str):
    best_value = float('inf')
    best_schema = []
    start_time = time.time()
    placement_array = np.arange(0, len(weights), 1)
    pas_optimal = 0
    nb_fitness_total = 0
    for i in range(iteration):
        # faire un random
        schema_pro, value_pro, pas_optimal_pro, nb_fitness = Recuit(weights, distances, temp, nb_proba_change,
                                                                    nb_voisin_change, proba_baisse).marche()
        nb_fitness_total += nb_fitness
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
            pas_optimal = pas_optimal_pro
        random.shuffle(placement_array)
    nb_page = str(nb_proba_change) + "*" + str(nb_voisin_change) + "=" + str(nb_proba_change * nb_voisin_change)
    write_random("recuit/recuit"+file_number+".txt", start_time, iteration, nb_page, best_value, pas_optimal,
                 nb_fitness_total, best_schema)


####################################################################################################
# Tabou
def run_tabou(file_number: str):
    file_config = open("test_config/tabou/tabou"+file_number+".txt", "r")
    file_name = file_config.readline().strip("\n")
    nb_test = file_config.readline().strip("\n")
    index_test = 1
    weights, distances = tools.parse_file("data/"+file_name)
    # Partie avec plaquette fixe
    config = file_config.readline().strip("\n")
    while config != "random":
        config_infos = config.split(";")
        lancer_tabou_fixe(weights, distances, int(config_infos[0]), int(config_infos[1]), int(config_infos[2]),
                          file_number)
        config = file_config.readline().strip("\n")
        print(index_test, "/", nb_test)
        index_test += 1
    for config in file_config.readlines():
        config.strip("\n")
        config_infos = config.split(";")
        lancer_tabou_random(int(config_infos[0]), weights, distances, int(config_infos[1]), int(config_infos[2]),
                            int(config_infos[3]), file_number)
        print(index_test, "/", nb_test)
        index_test += 1
    file_config.close()
    print("tabou", file_number, "finished")


def lancer_tabou_fixe(weights, distances, tabu_size, nb_pas, limit, file_number: str):
    start_time = time.time()
    solution = list(range(len(weights)))
    schema, value, pas_optimal, nb_fitness = Tabou(weights, distances, tabu_size, nb_pas, solution, limit).execute()
    write_fixe("tabou/tabou"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal, nb_fitness,
               schema)

    start_time = time.time()
    solution = list(range(len(weights)-1, -1, -1))
    schema, value, pas_optimal, nb_fitness = Tabou(weights, distances, tabu_size, nb_pas, solution, limit).execute()
    write_fixe("tabou/tabou"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal, nb_fitness,
               schema)

    start_time = time.time()
    solution = list(range(0, len(weights), 2)) + list(range(1, len(weights), 2))
    schema, value, pas_optimal, nb_fitness = Tabou(weights, distances, tabu_size, nb_pas, solution, limit).execute()
    write_fixe("tabou/tabou"+file_number+".txt", start_time, solution, str(nb_pas), value, pas_optimal, nb_fitness,
               schema)


# Pour lancer la fonction Tabou
# nombre de fois qu'on lance l'algo fois
# matrice des poids weights
# matrice des distance distances
# taille de la liste tabou
# nombre de pas max
# limit de voisinage
# le fichier (numéro) concerné
def lancer_tabou_random(iteration, weights, distances, tabou_size, nb_pas, limit, file_number: str):
    best_value = float('inf')
    best_schema = []
    start_time = time.time()
    placement_array = np.arange(0, len(weights), 1)
    pas_optimal = 0
    nb_fitness_total = 0
    for i in range(iteration):
        # faire un random
        schema_pro, value_pro, pas_optimal_pro, nb_fitness = Tabou(weights, distances, tabou_size, nb_pas,
                                                                   placement_array, limit).execute()
        nb_fitness_total += nb_fitness
        if value_pro < best_value:
            best_value = value_pro
            best_schema = schema_pro
            pas_optimal = pas_optimal_pro
        random.shuffle(placement_array)
    write_random("tabou/tabou"+file_number+".txt", start_time, iteration, str(nb_pas), best_value, pas_optimal,
                 nb_fitness_total, best_schema)
