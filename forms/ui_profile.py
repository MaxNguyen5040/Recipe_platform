# ui_user_profile.py

class UIUserProfile:
    def __init__(self, user):
        self.user = user

    def display_user_profile(self):
        print(f"User: {self.user.name}, Skill Level: {self.user.skill_level}")

    def recommend_recipes_by_skill(self, recipes):
        recommended_recipes = [recipe for recipe in recipes if recipe.difficulty <= self.user.skill_level]
        return recommended_recipes

# main.py

user_profile = UIUserProfile(current_user)
user_profile.display_user_profile()

recommended_recipes = user_profile.recommend_recipes_by_skill(recipe_manager.get_all_recipes())
for recipe in recommended_recipes:
    ui_difficulty.display_difficulty(recipe)
