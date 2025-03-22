# problem link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/


# solution:
class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        recipe_graph = defaultdict(list)  # Graph representing ingredient dependencies
        ingredient_count = defaultdict(int)  # Tracks remaining ingredients needed for each recipe
        
        # Build the graph and in-degree count
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                recipe_graph[ingredient].append(recipe)  # Ingredient leads to recipe
            ingredient_count[recipe] = len(ingredient_list)  # Number of required ingredients

        queue = supplies[:]  # Initialize queue with available supplies
        possible_recipes = []  # List to store recipes that can be made

        # Process ingredients in topological order
        for ingredient in queue:
            for dependent_recipe in recipe_graph[ingredient]:  # Recipes that need this ingredient
                ingredient_count[dependent_recipe] -= 1  # Reduce required ingredients
                if ingredient_count[dependent_recipe] == 0:  # If all ingredients are available
                    possible_recipes.append(dependent_recipe)
                    queue.append(dependent_recipe)  # Add it to available supplies

        return possible_recipes
