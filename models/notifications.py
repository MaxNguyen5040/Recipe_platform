class Notification:
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message

    def send_email(self):
        print(f"Email sent to user {self.user_id}: {self.message}")

    def send_in_app(self):
        print(f"In-app notification for user {self.user_id}: {self.message}")

def notify_user(user_id, message):
    notification = Notification(user_id, message)
    notification.send_in_app()
    notification.send_email()
