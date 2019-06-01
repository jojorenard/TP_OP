import numpy as np
from tools import fitness, get_rand_voisin


class Aleatoire:

    def __init__(self, weight, distance, nb_pas):
        self.weight = weight
        self.distance = distance
        self.nb_pas = nb_pas
        self.pas = 0
        self.solution = list(range(len(weight)))
        self.best_solution = self.solution
        self.best_fitness = fitness(self.weight, self.distance, self.solution)
        self.marche()


    def marche(self):
        while self.pas<self.nb_pas:
            self.solution = get_rand_voisin(self.solution)
            solution_fitness = fitness(self.weight, self.distance, self.solution)
            if solution_fitness < self.best_fitness:
                self.best_fitness = solution_fitness
                self.best_solution = self.solution
            self.pas += 1
        print(self.best_solution)
        print(self.best_fitness)


