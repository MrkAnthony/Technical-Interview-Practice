class Car:
    def __init__(self, name, categories, next_generation=None):
        self.name = name
        self.categories = categories
        self.is_purchased = False
        self.next_generation = next_generation


def get_model_lineage(starter_model):
    res = []

    current_model = starter_model

    while current_model:
        res.append(current_model.name)
        current_model = current_model.next_generation

    return res


mustang_2024 = Car("Mustang 2024", ["sports", "coupe"])
mustang_2022 = Car("Mustang 2022", ["sports", "coupe"], mustang_2024)
mustang_2020 = Car("Mustang 2020", ["sports", "coupe"], mustang_2022)

mustang_2020_lineage = get_model_lineage(mustang_2020)
print(mustang_2020_lineage)

mustang_2022_lineage = get_model_lineage(mustang_2022)
print(mustang_2022_lineage)

mustang_2024_lineage = get_model_lineage(mustang_2024)
print(mustang_2024_lineage)

