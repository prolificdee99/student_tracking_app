from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.activities = []
        self.homework_done = {}
        self.studied_today = {}

    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"Activity '{activity}' added.")

    def display_activities(self):
        if self.activities:
            print(f"\n{self.name}'s activities:")
            for idx, activity in enumerate(self.activities, 1):
                print(f"{idx}. {activity}")
        else:
            print(f"\nNo activities recorded for {self.name}.")

    def check_homework(self):
        today = str(date.today())
        if self.homework_done.get(today):
            print("Homework already done today.")
            return

        answer = input(f"{self.name}, have you done your assignment today? (yes/no): ").strip().lower()
        if answer == 'yes':
            print("Great job! Keep up the good work!")
            self.homework_done[today] = True
        else:
            print("You should go and do your assignment. Remember, every effort counts!")

    def check_studied(self):
        today = str(date.today())
        if self.studied_today.get(today):
            print("Studying already done today.")
            
