class UIAchievements:
    def __init__(self, user):
        self.user = user

    def display_achievements(self):
        for achievement in self.user.achievements:
            print(f"Achievement: {achievement.name}, Description: {achievement.description}")

    def notify_new_achievement(self, achievement):
        print(f"Congratulations! You've earned a new achievement: {achievement.name}")

# main.py

achievements_ui = UIAchievements(current_user)
achievements_ui.display_achievements()

new_achievement = Achievement("Master Chef", "Complete 50 recipes")
current_user.add_achievement(new_achievement)
achievements_ui.notify_new_achievement(new_achievement)
