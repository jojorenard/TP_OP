import tools


class Tabou:

    def __init__(self, weight_array, dim_array, tabu_size, iteration_number, placement_array, limite=0):
        self.weight_array = weight_array
        self.dim_array = dim_array
        self.tabu_size = tabu_size
        self.iteration_number = iteration_number
        self.pas_optimal = 0
        self.nb_fitness = 0
        self.limite = limite
        # chaque index représente la machine et la valeur serait l'emplacement de la machine
        # Etant en python, les listes commencent par l'index 0. Donc la machine 1 sera l'index 0; idem emplacement
        self.best_placement_array = placement_array
        self.tabu_list = []

    def execute(self):
        # best_placement_array = np.arange(0, len(self.dim_array), 1)
        # best_placement_array = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10]
        best_voisin = self.best_placement_array.copy()
        best_fitness = tools.fitness(self.weight_array, self.dim_array, self.best_placement_array)

        for i in range(self.iteration_number):
            fitness_voisin_min = float('inf')
            n_permutation = 0
            # print(i)
            voisins = self.calcul_voisinage(best_voisin, self.limite)
            for index, voisin in enumerate(voisins):
                fitness_voisin_pro = tools.fitness(self.weight_array, self.dim_array, voisin)
                self.nb_fitness += 1
                if fitness_voisin_pro < fitness_voisin_min:
                    fitness_voisin_min = fitness_voisin_pro
                    best_voisin = voisin
                    n_permutation = index

            if fitness_voisin_min > best_fitness:
                if len(self.tabu_list) >= self.tabu_size:
                    if not tools.tab_contains(self.tabu_list, n_permutation):
                        self.tabu_list.pop(0)
                        self.tabu_list += [n_permutation]
                else:
                    self.tabu_list += [n_permutation]
            else:
                self.best_placement_array = best_voisin.copy()
                best_fitness = fitness_voisin_min
                self.pas_optimal = i
        # print(self.best_placement_array)
        # print(best_fitness)
        return self.best_placement_array, best_fitness, self.pas_optimal, self.nb_fitness

    def calcul_voisinage(self, placement_array, limite):
        voisins = []
        n_permutation = 0
        for index_a, placement_a in enumerate(placement_array):
            for index_b, placement_b in enumerate(placement_array[index_a+1:]):
                if n_permutation not in self.tabu_list and (limite == 0 or index_b < limite):
                    voisin = placement_array.copy()
                    voisin[index_a] = placement_b
                    voisin[index_b + index_a + 1] = placement_a
                    voisins += [voisin]
                n_permutation += 1
        return voisins
