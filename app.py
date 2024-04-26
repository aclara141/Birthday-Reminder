import datetime
import os

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class BirthdayReminder:
    def __init__(self):
        self.users = {}  # Store users with email as key and User object as value
        self.birthdays = {}  # Store birthdays with name as key and (birthdate, email) as value

    def register_user(self, email, password):
        if email in self.users:
            print("User already exists. Please log in.")
            # my comment <- remove this comment
        else:
            self.users[email] = User(email, password)
            print("User registered successfully.")

    def login(self, email, password):
        if email in self.users and self.users[email].password == password:
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False

    def add_birthday(self, email, name, birthdate):
        if email in self.users:
            self.birthdays[name] = (birthdate, email)
            print(f"Birthday added successfully for {name}.")
        else:
            print("User not found. Please log in.")

    def remove_birthday(self, email, name):
        if name in self.birthdays and self.birthdays[name][1] == email:
            del self.birthdays[name]
            print(f"Birthday removed successfully for {name}.")
        else:
            print("Birthday not found or unauthorized.")

    def print_reminders(self):
        today = datetime.date.today()
        for name, (birthdate, email) in self.birthdays.items():
            if birthdate.month == today.month and birthdate.day == today.day:
                print(f"Today is {name}'s birthday!")
                self.send_notification(email, f"Happy Birthday, {name}!")

            elif birthdate.month == today.month and birthdate.day - today.day == 14:
                print(f"Reminder: {name}'s birthday is in two weeks.")
                self.send_notification(email, f"Your birthday is in two weeks, {name}!")

    def send_notification(self, email, message):
        print(f"Notification sent to {email}: {message}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for name, (birthdate, email) in self.birthdays.items():
                file.write(f"{name},{birthdate},{email}\n")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    name, birthdate_str, email = line.strip().split(',')
                    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
                    self.birthdays[name] = (birthdate, email)

# Example usage
reminder = BirthdayReminder()

# Register users
reminder.register_user("alice@example.com", "password123")
reminder.register_user("bob@example.com", "securepassword")

# Log in
reminder.login("alice@example.com", "password123")

# Add birthdays
reminder.add_birthday("alice@example.com", "Alice", datetime.date(1990, 5, 15))
reminder.add_birthday("bob@example.com", "Bob", datetime.date(1985, 9, 10))

# Print reminders and send notifications
reminder.print_reminders()

# Save birthdays to file
reminder.save_to_file("birthdays.txt")
