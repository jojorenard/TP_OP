import numpy as np
import math

from tools import fitness, get_rand_voisin


class Recuit:

    def __init__(self, weight, distance, temp, n1, n2, val):
        self.n1 = n1
        self.n2 = n2
        self.val = val
        self.temp = temp
        self.weight = weight
        self.distance = distance
        self.pas = 0
        self.pas_optimal = 0
        self.nb_fitness = 0
        self.solution = list(range(len(weight)))
        self.fitness = fitness(self.weight, self.distance, self.solution)
        self.best_solution = self.solution
        self.best_fitness = self.fitness
        # self.marche()

    def marche(self):
            for k in range(self.n1):
                for i in range(self.n2):
                    voisin = get_rand_voisin(self.solution)
                    voisin_fitness = fitness(self.weight, self.distance, voisin)
                    self.nb_fitness += 1
                    self.pas += 1
                    diff = self.fitness - voisin_fitness
                    if diff < 0:
                        self.solution = voisin
                        self.fitness = voisin_fitness
                        if self.fitness < self.best_fitness:
                            self.best_fitness = self.fitness
                            self.best_solution = self.solution
                            self.pas_optimal = self.pas
                    else:
                        p = np.random.random()
                        if p < math.e**(-diff/self.temp):
                            self.solution = voisin
                            self.fitness = voisin_fitness
                self.temp = self.val * self.temp

            # print(self.best_solution)
            # print(self.best_fitness)
            return self.best_solution, self.best_fitness, self.pas_optimal, self.nb_fitness
