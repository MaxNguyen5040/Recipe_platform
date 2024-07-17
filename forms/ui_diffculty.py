class UIDifficulty:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def display_difficulty(self, recipe):
        print(f"Recipe: {recipe.name}, Difficulty: {recipe.difficulty}")

    def filter_by_difficulty(self, difficulty):
        filtered_recipes = [recipe for recipe in self.recipes if recipe.difficulty == difficulty]
        return filtered_recipes

# main.py

ui_difficulty = UIDifficulty(recipe_manager.get_all_recipes())
for recipe in recipe_manager.get_all_recipes():
    ui_difficulty.display_difficulty(recipe)

filtered_recipes = ui_difficulty.filter_by_difficulty("Medium")
for recipe in filtered_recipes:
    ui_difficulty.display_difficulty(recipe)