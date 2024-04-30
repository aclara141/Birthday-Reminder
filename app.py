from abc import ABC, abstractmethod
from datetime import date, timedelta


class ReminderSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = {}  # Dictionary to store users
        return cls._instance


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.reminder = BirthdayReminder()

    def add_birthday(self, name, date):
        self.reminder.add_birthday(name, date)

    def remove_birthday(self, name):
        self.reminder.remove_birthday(name)

    def print_reminders(self):
        self.reminder.print_birthdays()

    def save_reminders(self, filename):
        self.reminder.save_to_file(filename)

    def send_notification(self, message):
        self.reminder.send_notifications(message)


class BirthdayReminder:
    def __init__(self):
        self.birthdays = {}

    def add_birthday(self, name, date):
        self.birthdays[name] = date

    def remove_birthday(self, name):
        if name in self.birthdays:
            del self.birthdays[name]

    def print_birthdays(self):
        for name, date in self.birthdays.items():
            print(f"{name}: {date}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for name, date in self.birthdays.items():
                file.write(f"{name}: {date}\n")

    def send_notifications(self, message):
        today = date.today()
        two_weeks_prior = today + timedelta(days=14)
        for name, b_date in self.birthdays.items():
            b_month, b_day = map(int, b_date.split('-'))
            if b_month == two_weeks_prior.month and b_day == two_weeks_prior.day:
                print(f"Sending two weeks reminder to {name}: {message}")
            elif b_month == today.month and b_day == today.day:
                print(f"Sending birthday notification to {name}: {message}")


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):
    def send_notification(self, message):
        # Code to send email notification
        print(f"Email notification sent: {message}")


class SMSNotification(NotificationService):
    def send_notification(self, message):
        # Code to send SMS notification
        print(f"SMS notification sent: {message}")


class Authorization:
    def __init__(self):
        self.logged_in_user = None

    def login(self, email, password):
        # Example: Check email and password against a database or predefined values
        for user in ReminderSystem()._instance.users.values():
            if user.email == email and user.password == password:
                self.logged_in_user = user
                print(f"Logged in as {user.username}")
                return
        print("Invalid email or password")

    def logout(self):
        self.logged_in_user = None
        print("Logged out")

    def is_logged_in(self):
        return self.logged_in_user is not None

    def check_permission(self, required_role):
        if self.is_logged_in() and self.logged_in_user.role == required_role:
            return True
        return False


# Usage example
if __name__ == "__main__":
    system = ReminderSystem()
    auth = Authorization()

    # Registration
    user1 = User("Alice", "alice@example.com", "password1")
    system.users[user1.email] = user1
    user2 = User("Bob", "bob@example.com", "password2")
    system.users[user2.email] = user2

    # Sign-in
    auth.login("alice@example.com", "password1")

    if auth.is_logged_in():
        # Adding birthdays (allowed for signed-in users)
        user1.add_birthday("Alice's Birthday", "04-27")
        user2.add_birthday("Bob's Birthday", "05-01")

        # Printing reminders
        user1.print_reminders()
        user2.print_reminders()

        # Saving reminders (allowed for signed-in users)
        user1.save_reminders("reminders.txt")
        user2.save_reminders("reminders.txt")

        # Sending notifications (allowed for signed-in users)
        email_service = EmailNotification()
        user1.send_notification("Your birthday is in two weeks")
        user2.send_notification("Your birthday is in two weeks")

        # Logout
        auth.logout()

        # Trying unauthorized operation after logout
        user1.add_birthday("Unauthorized Birthday", "01-01")  # Won't be executed
    else:
        print("Please sign-in to perform operations.")
