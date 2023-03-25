# Problem Link: https://www.codewars.com/kata/525c65e51bf619685c000059


# My Solution:

def cakes(recipe, available):
    num_cakes = float("inf")
    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0
        num_cakes = min(num_cakes, available[ingredient] // amount)
    return num_cakes
