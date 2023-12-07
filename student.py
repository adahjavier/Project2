class Student:
    """
    Class representing a student with a name and a score.
    """

    def __init__(self, name: str, score: int):
        """
        Initialize a student with a name and a score.

        Args:
        - name (str): The name of the student.
        - score (int): The score of the student.
        """
        self._name = name
        self._score = score

    def get_grade(self, best_score: int) -> str:
        """
        Calculate and return the grade of the student based on the best score.

        Args:
        - best_score (int): The best score among the students.

        Returns:
        - str: The grade of the student.
        """
        if self._score >= best_score - 10:
            return 'A'
        elif self._score >= best_score - 20:
            return 'B'
        elif self._score >= best_score - 30:
            return 'C'
        elif self._score >= best_score - 40:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        """
        Return a string representation of the student.
        """
        return f"Student {self._name} has score {self._score}"
