class InMemoryQuestionStore:
    def __init__(self, questions=None):
        self.questions = questions or []

    def add(self, question):
        self.questions.extend(question)

    def _filter(self, filters):
        # TODO: implement this.
        return NotImplemented

    def list(self, filters):
        if not filters:
            return self.questions
        return self._filter(filters)

    def get(self, key):
        return NotImplemented
