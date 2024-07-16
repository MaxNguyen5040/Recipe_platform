from notifications import notify_user
from import_export import import_recipe, export_recipe_to_pdf

def add_comment(recipe_id, user_id, comment_text):
    recipe_owner_id = get_recipe_owner(recipe_id)
    notify_user(recipe_owner_id, "Your recipe has a new comment!")

def rate_recipe(recipe_id, user_id, rating):
    recipe_owner_id = get_recipe_owner(recipe_id)
    notify_user(recipe_owner_id, "Your recipe has a new rating!")

def share_recipe(recipe_id, user_id):
    recipe_owner_id = get_recipe_owner(recipe_id)
    notify_user(recipe_owner_id, "Your recipe has been shared!")

def get_recipe_owner(recipe_id):
    return 1

def handle_import_request(file_path):
    import_recipe(file_path)

def handle_export_request(recipe_id):
    export_recipe_to_pdf(recipe_id)