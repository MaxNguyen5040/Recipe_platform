from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    ratings = db.relationship('Rating', backref='recipe', lazy=True)

    @property
    def avg_rating(self):
        if self.ratings:
            return sum(r.rating for r in self.ratings) / len(self.ratings)
        return 0
    
    def set_difficulty(self, difficulty):
        if difficulty in difficulties:
            self.difficulty = difficulties[difficulty]
        else:
            print("Invalid difficulty level")

# Association table for many-to-many relationship
recipe_tags = db.Table('recipe_tags',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class RecipeDifficulty:
    def __init__(self, level, description, skill_required):
        self.level = level
        self.description = description
        self.skill_required = skill_required

difficulties = {
    'Easy': RecipeDifficulty('Easy', 'Suitable for beginners.', 1),
    'Medium': RecipeDifficulty('Medium', 'Requires some cooking experience.', 2),
    'Hard': RecipeDifficulty('Hard', 'Challenging recipes for experienced cooks.', 3),
    'Expert': RecipeDifficulty('Expert', 'Complex recipes for experts.', 4)
}