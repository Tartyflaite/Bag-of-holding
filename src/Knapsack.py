class Knapsack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def get_value_and_weight(self, objects_dict : dict) :
        value = 0
        weight = 0
        for item in self.content :
            value += objects_dict[item][0]
            weight += objects_dict[item][1]
        return value, weight

    def print_content(self, objects_dict) -> None:
        poids = 0
        valeur = 0
        content = ""
        for obj in self.content:
            content += f"{obj} {objects_dict[obj][0]} {objects_dict[obj][1]}\n"
            poids += objects_dict[obj][1]
            valeur += objects_dict[obj][0]
        content += f"Le sac a {len(self.content)} objets, pour une valeur de {valeur} et un poids de {poids}/{self.capacity}"
        print(content)
      
    # Crée un nouveau Knapsack identique
    def duplicate(self) :
        knapsack = Knapsack(self.capacity)
        knapsack.content.extend(self.content)
        return knapsack

    # Vérifie si le sac peut ajouter l'objet à l'index indiqué et l'ajoute si possible. Return true si l'objet a été ajouté.
    def add_item(self, objects_dict : dict, objects_list : dict, index : int) -> bool :
        if (self.get_value_and_weight(objects_dict)[1] + objects_list[index][1][1] <= self.capacity) :
            self.content.append(objects_list[index][0])
            return True
        
        return False

# Solution greedy
def solve_knapsack_greedy(knapsack : Knapsack, objects_dict : dict) -> Knapsack:
    items_sorted = sort(objects_dict)

    for i in range (len(objects_dict)) :
        knapsack.add_item(objects_dict, items_sorted, i)

    return knapsack

def sort(objects_dict : dict) :
    return sorted(objects_dict.items(), key=lambda item: (item[1][0]/item[1][1]), reverse=True)

# Solution optimal
def solve_knapsack_optimal(knapsack : Knapsack, objects_dict : dict) -> Knapsack :
    objects_list = list(objects_dict.items())
    return find_optimal(knapsack, objects_dict, objects_list, 0)

# Création d'un arbre décisionnel. 
# Pour chaque item de la liste, deux branches sont créées : l'une où l'item est ajouté, l'autre sans ajout. 
# Lorsque la fin de la liste est atteinte, la valeur du knapsack à chaque branche est comparé à sa branche voisine et la meilleure est retournée.
def find_optimal(knapsack : Knapsack, objects_dict : dict, objects_list : list, index : int) -> Knapsack :
    if (index >= len(objects_dict) - 1) :
        return knapsack

    left = knapsack.duplicate()
    right = knapsack.duplicate()

    if right.add_item(objects_dict, objects_list, index) :
        right = find_optimal(right, objects_dict, objects_list, index + 1)

    left = find_optimal(left, objects_dict, objects_list, index + 1)

    if left.get_value_and_weight(objects_dict)[0] > right.get_value_and_weight(objects_dict)[0] :
        return left
    return right