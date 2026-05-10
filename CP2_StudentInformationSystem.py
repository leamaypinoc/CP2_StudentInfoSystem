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