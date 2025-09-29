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
        print(f"Activity '{activity}' added for {self.name}.")

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
            print(f"Homework already done today for {self.name}.")
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
            print(f"Studying already done today for {self.name}.")
            return

        answer = input(f"{self.name}, have you studied today? (yes/no): ").strip().lower()
        if answer == 'yes':
            print("Good work! Keep challenging yourself!")
            self.studied_today[today] = True
        else:
            print("You should go and study. Remember, learning is the key to success!")

    def summary(self):
        print(f"\n--- Summary for {self.name} ---")
        print(f"Age: {self.age}")
        print(f"Activities: {', '.join(self.activities) if self.activities else 'No activities recorded'}")
        print(f"Homework done today: {'Yes' if self.homework_done.get(str(date.today())) else 'No'}")
        print(f"Studied today: {'Yes' if self.studied_today.get(str(date.today())) else 'No'}")
        print("-------------------------------\n")


def get_student_info():
    full_name = input("Enter student's full name (first name and surname): ")
    student_name = ' '.join([name.capitalize() for name in full_name.split() if name.strip()])

    while True:
        try:
            student_age = int(input("Enter student's age: "))
            if student_age <= 0:
                print("Please enter a valid age greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")

    return Student(student_name, student_age)


def student_menu(student):
    while True:
        print(f"\n--- Menu for {student.name} ---")
        print("1. Add Activity")
        print("2. Display Activities")
        print("3. Check Homework")
        print("4. Check Studying")
        print("5. Show Summary")
        print("6. Go Back to Main Menu")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            activity = input("Enter activity name: ").strip()
            if activity:
                student.add_activity(activity)
            else:
                print("Activity cannot be empty.")
        elif choice == '2':
            student.display_activities()
        elif choice == '3':
            student.check_homework()
        elif choice == '4':
            student.check_studied()
        elif choice == '5':
            student.summary()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


def main():
    print("Welcome to the Multi-Student Tracking App!")

    students = []

    while True:
        print("\n--- Main Menu ---")
        print("1. Add New Student")
        print("2. Select Student")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            student = get_student_info()
            # Optional default activities
            for act in ["Assignment", "Personal Studies"]:
                student.add_activity(act)
            students.append(student)
            print(f"{student.name} has been added successfully!")
        elif choice == '2':
            if not students:
                print("No students available. Please add a student first.")
                continue

            print("\nAvailable Students:")
            for idx, s in enumerate(students, 1):
                print(f"{idx}. {s.name}")

            try:
                selected = int(input("Select a student by number: ")) - 1
                if 0 <= selected < len(students):
                    student_menu(students[selected])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 3.")


if __name__ == "__main__":
    main()
