import os

FILE_NAME = "students.txt"


student_ids = []
student_names = []
student_grades = []


def load_students():
    """Load student records from the file when the program starts."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 3:
                    student_ids.append(data[0])
                    student_names.append(data[1])
                    student_grades.append(float(data[2]))
                    

def save_students():
    """Save all student records to the file."""
    with open(FILE_NAME, "w") as file:
        for i in range(len(student_ids)):
            file.write(
                f"{student_ids[i]}|"
                f"{student_names[i]}|"
                f"{student_grades[i]}\n"
            )

def add_student():
    print("\n-- Add Student --")
    sid = input("Enter Student ID: ").strip()

    if sid in student_ids:
        print("ID already exists!")
        return

    name = input("Enter Name: ").strip()

    while True:
        try:
            grade = float(input("Enter Grade (1-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    student_ids.append(sid)
    student_names.append(name)
    student_grades.append(grade)

    save_students() 
    print(f"Student '{name}' added successfully!")

    
def view_students():
    print("\n-- All Students --")

    if not student_ids:
        print("No students found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Grade'}")
    print("-" * 35)

    for i in range(len(student_ids)):
        print(
            f"{student_ids[i]:<10} "
            f"{student_names[i]:<20} "
            f"{student_grades[i]}"
        )

def search_student():
    print("\n-- Search Student --")
    sid = input("Enter Student ID: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)
        print(f"ID: {student_ids[i]}")
        print(f"Name: {student_names[i]}")
        print(f"Grade: {student_grades[i]}")
    else:
        print("Student not found.")


def delete_student():
    print("\n-- Delete Student --")
    sid = input("Enter Student ID to delete: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        print(f"Deleted: {student_names[i]}")

        student_ids.pop(i)
        student_names.pop(i)
        student_grades.pop(i)

        save_students()  
    else:
        print("Student not found.")


def update_student():
    print("\n-- Update Student --")
    sid = input("Enter Student ID to update: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        print(f"Current Name : {student_names[i]}")
        print(f"Current Grade: {student_grades[i]}")

        
        new_name = input("Enter New Name: ").strip()

       
        while True:
            try:
                new_grade = float(input("Enter New Grade (1-100): "))
                if 0 <= new_grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

        
        student_names[i] = new_name
        student_grades[i] = new_grade

        
        save_students()

        print("Student updated successfully!")
    else:
        print("Student not found.")

 def show_menu():
    print("\n================================")
    print("   STUDENT INFORMATION SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("0. Exit")
    print("================================")


while True:
    show_menu()
    choice = input("Enter a number: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 0-5.") 