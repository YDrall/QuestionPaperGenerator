import settings
from exceptions import InvalidArgumentError


PAPER_GENERATOR = settings.random_paper_generator


class QuestionPapersGenerator:
    def __init__(self, question_count, total_marks, difficulty_map):
        """
        Construct paper generator service layer
        :param question_count: total number of questions to be generated
        :param total_marks: Paper total marks
        :param difficulty_map: key value pair of difficulty and weight percent in paper
        """
        self.question_count = question_count
        self.total_marks = total_marks
        self.difficulty_map = difficulty_map

    def generate(self):
        questions = []
        question_weight = self.total_marks / self.question_count
        self._validate_difficulty_weight()
        for q_type, perc in self.difficulty_map.items():
            # Assuming that types with float values will be ignored.
            questions_to_generate = int((perc/100) * self.question_count)
            for _ in range(questions_to_generate):
                questions.append(PAPER_GENERATOR(q_type, marks=question_weight))
        return questions

    def _validate_difficulty_weight(self):
        weight_sum = 0
        for key, value in self.difficulty_map.items():
            weight_sum += value
        if weight_sum != 100:
            raise InvalidArgumentError("Total weight not adds up to 100%")
