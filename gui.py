from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from gradebook import GradeBook


class StudentAppGUI(QMainWindow):
    """
    Graphical User Interface for the student grading system.
    """

    def __init__(self, grade_book: GradeBook):
        """
        Initialize the GUI with a reference to the GradeBook.

        Args:
        - grade_book (GradeBook): The GradeBook object containing student data.
        """
        super().__init__()

        self.grade_book = grade_book

        self.setWindowTitle("Student Grading System")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.score_label = QLabel("Enter score:")
        self.score_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.calculate_grade)

        self.result_label = QLabel("")

        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.score_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def calculate_grade(self):
        """
        Calculate the grade based on the entered score and display it.
        """
        score_text = self.score_input.text()
        try:
            score = int(score_text)
            best_score = self.grade_book.get_best_score()
            grade = self.calculate_student_grade(score, best_score)
            self.result_label.setText(f"Grade: {grade}")
        except ValueError:
            self.result_label.setText("Please enter a valid score.")

    def calculate_student_grade(self, score: int, best_score: int) -> str:
        """
        Calculate the grade based on the entered score and the best score.

        Args:
        - score (int): The entered score.
        - best_score (int): The best score among the students.

        Returns:
                Returns:
        - str: The calculated grade.
        """
        if score >= best_score - 10:
            return 'A'
        elif score >= best_score - 20:
            return 'B'
        elif score >= best_score - 30:
            return 'C'
        elif score >= best_score - 40:
            return 'D'
        else:
            return 'F'

