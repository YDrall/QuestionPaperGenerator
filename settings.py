"""
App settings
"""
from repository.mem_store import InMemoryQuestionStore
from utils import random_paper_generator

QUESTION_STORE = InMemoryQuestionStore
PAPER_GENERATOR = random_paper_generator
