from constants import DIFFICULTY_LEVELS
from exceptions import InvalidAttributeError


class Question:

    def __init__(self, text, subject, topic, difficulty, marks):
        if difficulty not in DIFFICULTY_LEVELS:
            raise InvalidAttributeError("Unknown difficulty level.")
        self.text = text
        self.subject = subject
        self.topic = topic
        self.difficulty = difficulty
        self.marks = marks

    def to_dict(self):
        return {
            "text": self.text,
            "subject": self.subject,
            "topic": self.topic,
            "difficulty": self.difficulty,
            "marks": self.marks
        }

    def __str__(self):
        return str(self.to_dict())