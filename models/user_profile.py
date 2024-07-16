class UserProfile:
    def __init__(self, user_id, username, bio, favorite_recipes):
        self.user_id = user_id
        self.username = username
        self.bio = bio
        self.favorite_recipes = favorite_recipes

    def add_favorite_recipe(self, recipe_id):
        self.favorite_recipes.append(recipe_id)

    def remove_favorite_recipe(self, recipe_id):
        self.favorite_recipes.remove(recipe_id)

    def update_bio(self, new_bio):
        self.bio = new_bio

user_profiles = {}

def create_user_profile(user_id, username, bio, favorite_recipes):
    user_profiles[user_id] = UserProfile(user_id, username, bio, favorite_recipes)

def get_user_profile(user_id):
    return user_profiles.get(user_id)

def add_favorite_recipe(user_id, recipe_id):
    if user_id in user_profiles:
        user_profiles[user_id].add_favorite_recipe(recipe_id)

def remove_favorite_recipe(user_id, recipe_id):
    if user_id in user_profiles:
        user_profiles[user_id].remove_favorite_recipe(recipe_id)

def update_user_bio(user_id, new_bio):
    if user_id in user_profiles:
        user_profiles[user_id].update_bio(new_bio)