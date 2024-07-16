class RecipeAnalytics:
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        self.views = 0
        self.comments = 0
        self.shares = 0

    def increment_views(self):
        self.views += 1

    def increment_comments(self):
        self.comments += 1

    def increment_shares(self):
        self.shares += 1

analytics = {}

def get_recipe_analytics(recipe_id):
    if recipe_id not in analytics:
        analytics[recipe_id] = RecipeAnalytics(recipe_id)
    return analytics[recipe_id]

def increment_view_count(recipe_id):
    get_recipe_analytics(recipe_id).increment_views()

def increment_comment_count(recipe_id):
    get_recipe_analytics(recipe_id).increment_comments()

def increment_share_count(recipe_id):
    get_recipe_analytics(recipe_id).increment_shares()