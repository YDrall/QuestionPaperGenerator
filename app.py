import settings
from service.question_generator import QuestionPapersGenerator

QUESTION_STORE = settings.QUESTION_STORE


def load_data():
    sample_data = [
        {
            "marks": 100,
            "difficulty_map": {
                "Easy": 20,
                "Medium": 50,
                "Hard": 30
            }
        },
        {
            "marks": 40,
            "difficulty_map": {
                "Easy": 10,
                "Medium": 50,
                "Hard": 40
            }
        }
    ]
    return sample_data


if __name__ == "__main__":
    data = load_data()
    question_count = 10  # Assuming that every question paper have only 10 questions
    store = QUESTION_STORE()
    for d in data:
        print("Generating questions: \n")
        questions = QuestionPapersGenerator(
            question_count, d.get('marks'), d.get('difficulty_map')).generate()
        store.add(questions)

        # print questions to console
        for question in questions:
            print(question)
        print("\n")
