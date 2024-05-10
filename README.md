# Birthday-Reminder
# Python Birthday Reminder System

## Introduction

Say goodbye to the stress of forgetting birthdays with our revolutionary Birthday Reminder app! Keep track of your loved ones' special days effortlessly. Not only can you save their birthdays, but you can also send them heartfelt messages two weeks before their big day and surprise them again on the actual date. Never miss a celebration again and make every birthday memorable with our app!

## Inspiration

What inspired this idea was the fact that I struggle to remember birthdays. It was frustrating to forget the birthdays of my friends and family, so I decided to create an app that reminds people of birthdays and allows them to send kind messages. My second inspiration was the My Heritage website, which sends automatic notifications about family events (including birthdays and anniversaries) at the beginning of the week. This functionality sparked the idea for my birthday reminder app, which is still under development.

## How to Use/Launch the Program

Initiate the program by executing the Python script within your preferred Python interpreter or integrated development environment (IDE). This will open the gateway to a realm of personalized functionalities and digital management.

## Utilizing the Program

Upon activation, users are empowered to engage in a series of structured operations. Begin by registering your presence, followed by a secure sign-in to access the system's features. Add significant dates such as birthdays, generate reminders as needed, preserve these reminders by saving them to a file, and avail yourself of the option to send notifications. It's imperative to note that any attempts at unauthorized access or actions are strictly prohibited, in accordance with the program's security protocols.

## Functional Overview and Code Analysis

1. **ReminderSystem Singleton**:
   - The ReminderSystem class ensures there is only one instance of the system, meeting the objective of having a single system managing reminders across users.

2. **User Management**:
   - The User class represents a user with attributes like username, email, password, and a BirthdayReminder instance. Users can perform various operations related to birthday reminders.

3. **Birthday Reminder**:
   - The BirthdayReminder class handles adding, removing, printing, saving, and sending notifications for birthdays.

4. **Notification Services**:
   - NotificationService, EmailNotification, and SMSNotification provide flexible notification options.

5. **Authorization**:
   - The Authorization class handles user authentication, login, logout, and permission checks.

## Usage Example

```python
# Snippets demonstrating usage
user1.add_birthday("Alice's Birthday", "04-27")
user2.add_birthday("Bob's Birthday", "05-01")

user1.print_reminders()
user2.print_reminders()

user1.save_reminders("reminders.txt")
user2.save_reminders("reminders.txt")

user1.send_notification("Your birthday is in two weeks")
user2.send_notification("Your birthday is in two weeks")

auth.login("alice@example.com", "password1")
if auth.is_logged_in():
    # Operations allowed for signed-in users
auth.logout()

Results
Results of this program.

Through developing this program, I have learned to:
Build a reminder system/notification system from scratch.
Choose and use design patterns effectively.
Develop a Flask application and utilize CSS and HTML.

Challenges:
I initially struggled with developing my Flask application due to my lack of prior experience. I learned from YouTube tutorials, which presented a bit of a challenge.
Initially, I struggled with importing my code to GitHub. However, I eventually figured out the process.

Conclusion
This coursework has successfully implemented a Birthday Reminder System in Python, offering efficient reminder management, authentication, and flexible notification options. My Future prospects include integrating more features like recurring reminders and enhancing scalability and user interface design.




NB: Please not if you go to my Clara22 repository you can see the flask app, I am still developing.
link https://github.com/aclara141/clara22

Work Done by Agina Ferrao


