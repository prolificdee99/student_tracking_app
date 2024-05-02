class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.activities = []
        self.homework_done = False
        self.studied_today = False

    def add_activity(self, activity):
        self.activities.append(activity)

    def display_activities(self):
        if self.activities:
            print(f"{self.name}'s activities:")
            for activity in self.activities:
                print(activity)
        else:
            print(f"No activities recorded for {self.name}.")

    def check_homework(self):
        if not self.homework_done:
            print(f"{self.name}, have you done your assignment?")
            answer = input("Enter 'yes' if done, 'no' otherwise: ").lower()
            if answer == 'no':
                print("You should go and do your assignment. Remember, every effort counts!")
            else:
                print("Great job! Keep up the good work!")
                self.homework_done = True
        else:
            print("Homework already done.")

    def check_studied(self):
        if not self.studied_today:
            print(f"{self.name}, have you studied today?")
            answer = input("Enter 'yes' if studied, 'no' otherwise: ").lower()
            if answer == 'no':
                print("You should go and study. Remember, learning is the key to success!")
            else:
                print("Good work! Keep challenging yourself!")
                self.studied_today = True
        else:
            print("Studying already done today.")

# Welcome message
print("Welcome to the Student Tracking App!")

# Enter student's full name
full_name = input("Enter student's full name (first name and surname): ")
student_name = ' '.join([name.capitalize() for name in full_name.split()])
student_age = int(input("Enter student's age: "))
student = Student(student_name, student_age)

# Example activities (you can modify as needed)
activities = ["Assignment", "Personal Studies"]

for activity in activities:
    student.add_activity(activity)

student.display_activities()
student.check_homework()
student.check_studied()
