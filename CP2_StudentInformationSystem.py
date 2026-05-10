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
                    student_grades.append(float(data[2]))s