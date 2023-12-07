from typing import List
from student import Student

class GradeBook:
    """
    Class representing a collection of students.
    """

    def __init__(self):
        """
        Initialize an empty list to store students.
        """
        self._students: List[Student] = []

    def add_student(self, student: Student):
        """
        Add a student to the collection.

        Args:
        - student (Student): The student object to be added.
        """
        self._students.append(student)

    def get_best_score(self) -> int:
        """
        Calculate and return the best score among the students.

        Returns:
        - int: The best score among the students.
        """
        if not self._students:
            return 0
        return max(student._score for student in self._students)

    def assign_grades(self, best_score: int):
        """
        Assign grades to all students in the collection based on the best score.

        Args:
        - best_score (int): The best score among the students.
        """
        for student in self._students:
            student_grade = student.get_grade(best_score)
            print(f"{student} has grade {student_grade}")

    def read_student_data(self, file_name: str):
        """
        Read student data from a file.

        Args:
        - file_name (str): The name of the file to read student data from.
        """
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    name, score = line.strip().split(',')
                    self._students.append(Student(name, int(score)))
        except FileNotFoundError:
            print("File not found.")

    def write_student_data(self, file_name: str):
        """
        Write student data to a file.

        Args:
        - file_name (str): The name of the file to write student data to.
        """
        try:
            with open(file_name, 'w') as file:
                for student in self._students:
                    file.write(f"{student._name},{student._score}\n")
        except IOError:
            print("Error writing to file.")
