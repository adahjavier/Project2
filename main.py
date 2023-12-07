from student import Student
from PyQt6.QtWidgets import QApplication
from gradebook import GradeBook
from gui import StudentAppGUI

def main():
    """
    Main function to start the student grading system.
    """
    grade_book = GradeBook()

    # Adding sample student data
    grade_book.add_student(Student("Alice", 85))
    grade_book.add_student(Student("Bob", 70))
    grade_book.add_student(Student("Charlie", 95))

    # File handling operations
    grade_book.write_student_data("student_data.txt")  # Writing student data to a file
    grade_book.read_student_data("student_data.txt")   # Reading student data from a file

    app = QApplication([])
    window = StudentAppGUI(grade_book)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
