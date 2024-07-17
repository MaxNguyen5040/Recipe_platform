class Achievement:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class UserAchievements:
    def __init__(self, user_id):
        self.user_id = user_id
        self.achievements = []

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

achievement_badges = {
    'Easy': Achievement('Easy Chef', 'Completed 10 easy recipes.'),
    'Medium': Achievement('Medium Chef', 'Completed 10 medium recipes.'),
    'Hard': Achievement('Hard Chef', 'Completed 10 hard recipes.'),
    'Expert': Achievement('Expert Chef', 'Completed 10 expert recipes.')
}

user_achievements = {}

def create_user_achievements(user_id):
    user_achievements[user_id] = UserAchievements(user_id)

def award_achievement(user_id, difficulty):
    if user_id in user_achievements and difficulty in achievement_badges:
        user_achievements[user_id].add_achievement(achievement_badges[difficulty])

# Example usage
create_user_achievements('user123')
award_achievement('user123', 'Easy')