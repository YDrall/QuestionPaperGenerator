from entity.question import Question


def random_paper_generator(difficulty, marks=0):
    return Question(
        "text",
        "subject",
        "topic",
        difficulty,
        marks
    )
