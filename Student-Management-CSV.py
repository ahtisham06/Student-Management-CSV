import csv

def add_student():
  name = input("Enter student name: ")
  marks = input("Enter marks: ")
  with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, marks])
  print("Student added successfully!")
 
def view_students():
  print("\n--- Student Records ---\n")
  try:
    with open("students.csv", "r") as f:
      reader = csv.reader(f)
      for row in reader:
        print("Name:", row[0], "| Marks:", row[1])
  except FileNotFoundError:
      print("No records found.")

def main():
  while True:
    print("\n--- Student Management System ---\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
      add_student()
    elif choice == "2":
      view_students()
    elif choice == "3":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

main()
    












