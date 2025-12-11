from collections import defaultdict
import enum
import re

all_ingredients = []
all_allergens = []
allergens_unique = set()
ingredient_unique = set()

def read_input(filename):

    rows = open(filename).read().split("\n")
    for row in rows:
        idx = row.index("(contains")
        all_ingredients.append(set(row[:idx].split()))
        ingredient_unique.update(set(row[:idx].split()))
        
        all_allergens.append(set(row[idx+10:-1].split(", ")))
        allergens_unique.update(set(row[idx+10:-1].split(", ")))


def ingredient_by_allergen(allergen):
    possible_ings = []
    for i, ingredients in enumerate(all_ingredients):
        if allergen in all_allergens[i]:
            possible_ings.append(ingredients)
    return set.intersection(*possible_ings)


def count_ingredients(ingredient):
    count = 0

    for i in all_ingredients:
        count += ingredient in i

    return count

def sort_allergens(ingredients):
    sorted_allergens = sorted(ingredients)
    danger_list = ""
    for allergen in sorted_allergens:
        danger_list += ingredients[allergen] + ","
    return danger_list[:-1]
    

def solve(filename):
    read_input(filename)
    ingredients = {}
    reserved_ingredients = set()
    while len(ingredients) != len(allergens_unique):
        for allergen in allergens_unique:
            try_ingredient = ingredient_by_allergen(allergen).difference(reserved_ingredients)
            if len(try_ingredient) == 1:
                ingredient = try_ingredient.pop()
                ingredients[allergen] = ingredient
                reserved_ingredients.add(ingredient)


    free = ingredient_unique.difference(reserved_ingredients)
    count = 0
    for f in free:
        count += count_ingredients(f)
    
    
    print(f'A: {count}')
    print(f'B: {sort_allergens(ingredients)}')

if __name__ == "__main__":
    solve("input")