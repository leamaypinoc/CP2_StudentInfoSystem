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