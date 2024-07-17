class Notification:
    def __init__(self, message, read=False):
        self.message = message
        self.read = read

class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        self.notifications.append(Notification(message))

    def get_unread_notifications(self):
        return [notification for notification in self.notifications if not notification.read]

    def mark_all_as_read(self):
        for notification in self.notifications:
            notification.read = True

notifications = NotificationSystem()
notifications.add_notification("New recipe added: Spaghetti Carbonara")
unread_notifications = notifications.get_unread_notifications()
for notification in unread_notifications:
    print(f"Notification: {notification.message}")
