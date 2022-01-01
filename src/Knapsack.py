class Knapsack:

    def __init__(self, capacity):
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
            content += f"{obj} {objects_dict[obj][0]} {objects_dict[obj][1]}\n"
            poids += objects_dict[obj][1]
            valeur += objects_dict[obj][0]
        content += f"Le sac a {len(self.content)} objets, pour une valeur de {valeur} et un poids de {poids}/{self.capacity}"
        print(content)

    def duplicate(self):
        knapsack = Knapsack(self.capacity)
        knapsack.content.extend(self.content)
        return knapsack

    def append_item(self, objects_dict, index):
        if self.get_value_and_weight()



def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    items_sorted = sort_value_efficiency(objects_dict)
    for item in items_sorted:
        if knapsack.get_value_and_weight(objects_dict)[1]+item[1][1] <= knapsack.capacity :
            knapsack.content.append(item[0])
    return knapsack


def sort_value_efficiency(objects_dic: dict):
    return sorted(objects_dic.items(), key=lambda item: (item[1][0] / item[1][1]), reverse=True)


def solve_knapsack_best(knapsack, objects_dict) -> Knapsack:
    return knapsack


def solve_knapsack_optimal(knapsack, objects_dict) -> Knapsack:
    return find_optimal(knapsack, objects_dict, 0)


def find_optimal(knapsack: Knapsack, objects_dict: dict, index: int) -> Knapsack:
    if (index >= len(objects_dict) - 1):
        return knapsack

    left = knapsack.duplicate()
    right = knapsack.duplicate()

    if right.append_item(objects_dict, index):
        right = find_optimal(right, objects_dict, index + 1)

    left = find_optimal(left, objects_dict, index + 1)

    if left.get_value_and_weight(objects_dict)[0] > right.get_value_and_weight(objects_dict)[0]:
        return left
    return right

