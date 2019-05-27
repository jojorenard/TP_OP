import numpy as np
from tools import fitness


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



    def get_voisins(self):
        voisins = []
        for index, x in enumerate(self.solution):
            for index2, y in enumerate(self.solution[index + 1:]):
                voisin = self.solution.copy()
                voisin[index] = y
                voisin[index2 + index + 1] = x
                voisins += [voisin]
        return voisins

    def marche(self):
        while self.pas<self.nb_pas:
            voisins = self.get_voisins()
            self.solution = voisins[np.random.randint(len(voisins))]
            solution_fitness = fitness(self.weight, self.distance, self.solution)
            if solution_fitness < self.best_fitness:
                self.best_fitness = solution_fitness
                self.best_solution = self.solution
            self.pas += 1
        print(self.best_solution)
        print(self.best_fitness)


