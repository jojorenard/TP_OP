from tools import fitness, get_rand_voisin


class Aleatoire:

    def __init__(self, weight, distance, nb_pas, solution):
        self.weight = weight
        self.distance = distance
        self.nb_pas = nb_pas
        self.pas = 0
        self.pas_optimal = 0
        self.nb_fitness = 0
        self.solution = solution
        self.best_solution = self.solution
        self.best_fitness = fitness(self.weight, self.distance, self.solution)
        # self.marche()

    def marche(self):
        while self.pas < self.nb_pas:
            self.solution = get_rand_voisin(self.solution)
            solution_fitness = fitness(self.weight, self.distance, self.solution)
            self.nb_fitness += 1
            if solution_fitness < self.best_fitness:
                self.best_fitness = solution_fitness
                self.best_solution = self.solution
                self.pas_optimal = self.pas
            self.pas += 1
        # print(self.best_solution)
        # print(self.best_fitness)
        return self.best_solution, self.best_fitness, self.pas_optimal, self.nb_fitness
