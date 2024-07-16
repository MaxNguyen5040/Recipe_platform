from notifications import notify_user
from import_export import import_recipe, export_recipe_to_pdf
from collaborative_cooking import create_session, join_session, leave_session, get_session_participants
from user_profiles import create_user_profile, get_user_profile, add_favorite_recipe, remove_favorite_recipe, update_user_bio


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

def handle_create_session(session_id, recipe_id, participants):
    create_session(session_id, recipe_id, participants)

def handle_join_session(session_id, user_id):
    join_session(session_id, user_id)

def handle_leave_session(session_id, user_id):
    leave_session(session_id, user_id)

def handle_get_session_participants(session_id):
    return get_session_participants(session_id)

def handle_create_user_profile(user_id, username, bio, favorite_recipes):
    create_user_profile(user_id, username, bio, favorite_recipes)

def handle_get_user_profile(user_id):
    return get_user_profile(user_id)

def handle_add_favorite_recipe(user_id, recipe_id):
    add_favorite_recipe(user_id, recipe_id)

def handle_remove_favorite_recipe(user_id, recipe_id):
    remove_favorite_recipe(user_id, recipe_id)

def handle_update_user_bio(user_id, new_bio):
    update_user_bio(user_id, new_bio)
