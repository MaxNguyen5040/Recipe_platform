class RecipeSearch:
    def __init__(self, recipes):
        self.recipes = recipes

    def search_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]

    def filter_by_cuisine(self, cuisine):
        return [recipe for recipe in self.recipes if recipe.cuisine == cuisine]

# main.py

recipe_search = RecipeSearch(recipe_manager.get_all_recipes())
recipes_with_tomato = recipe_search.search_by_ingredient("Tomato")
italian_recipes = recipe_search.filter_by_cuisine("Italian")
