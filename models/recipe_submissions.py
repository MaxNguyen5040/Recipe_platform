class RecipeSubmission:
    def __init__(self, submission_id, recipe_data, user_id):
        self.submission_id = submission_id
        self.recipe_data = recipe_data
        self.user_id = user_id
        self.status = 'Pending'

    def approve(self):
        self.status = 'Approved'
        save_recipe_to_db(self.recipe_data)

    def reject(self):
        self.status = 'Rejected'

submissions = {}

def submit_recipe(submission_id, recipe_data, user_id):
    submissions[submission_id] = RecipeSubmission(submission_id, recipe_data, user_id)

def review_submission(submission_id, approve=True):
    if submission_id in submissions:
        if approve:
            submissions[submission_id].approve()
        else:
            submissions[submission_id].reject()