def solve_knapsack_greedy ( knapsack , objects_dict ) -> Knapsack:


def solve_knapsack_best ( knapsack , objects_dict ) -> Knapsack:


def solve_knapsack_optimal ( knapsack , objects_dict ) -> Knapsack:



class Knapsack:

    def _init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def get_value_and_weight(self, objects_dict) -> (int, int):
        poids = 0
        valeur = 0
        for obj in self.content:
            poids += objects_dict[obj][1]
            valeur += objects_dict[obj][0]
        return valeur, poids

    def print_content(self, objects_dict) -> None:
        poids = 0
        valeur = 0
        content = ""
        for obj in self.content:
            content += obj + " " + objects_dict[obj] + "\n"
            poids += objects_dict[obj][1]
            valeur += objects_dict[obj][0]
        content += "Le sac a" + len(self.content) + "objets, pour une valeur de " + valeur + " et un poids de " + poids + "/" + self.capacity + "\n"
