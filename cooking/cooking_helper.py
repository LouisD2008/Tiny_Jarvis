import csv
import random


def get_recipe():
    list = []
    rand_int = random.randint(1, 33)
    with open("recipes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=("Title", "Ingredients", "Recipe", "Prep & Cooking Time"))
        for row in reader:
            list.append(row)  # each JSON object = un plat. So it's a list with all the plat JSON objects, easily accessible
    return list[rand_int]