import csv

# Parent Class

class Person:
    def __init__(self, name,):
        self.name = name

# Child Class inheritance From Person

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def save_to_csv(self):
        with open('student.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.marks])
            print("Student Added Successfully")

# Class To Manage Student Records

class Student_Manager:
    def add_student(self):
        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")
        student = Student(name, marks)
        student.save_to_csv()

    def view_students(self):
        print("---Student Records---:")
        try:
            with open('student.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print('Name:', row[0], 'Marks:', row[1])
        except FileNotFoundError:
            print("No Records Found")

# Main Application Run

class App:
    def __init__(self):
        self.manager = Student_Manager()
    def run(self):
        while True:
            print("1. Add Student")
            print("2. View Students")
            print("3. Exit")
            choice = input("Enter Your Choice (1/2/3): ")
            if choice == '1':
                self.manager.add_student()
            elif choice == '2':
                self.manager.view_students()
            elif choice == '3':
                print("Exiting Application")
                break
            else:
                print("Invalid Choice. Please Try Again")

# Run The Application

if __name__ == "__main__":
    app = App()
    app.run()



