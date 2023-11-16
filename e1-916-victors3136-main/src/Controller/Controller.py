from src.Repository.MasterList import MasterList
from src.Domain.Question import Question

DIFFICULTY_TO_POINTS_MAP = {'easy': 1, 'medium': 2, 'hard': 3}


class Controller:
	def __init__(self):
		self.__master_list = MasterList()
		self.__master_list.load_data()

	def add_question(self, question_string):
		self.__master_list.add_question(question_string)

	def create_quizz(self, quizz_string):
		self.__master_list.create_quizz(quizz_string)

	@staticmethod
	def play_quizz(file_name: str):
		questions_answers_points = []
		with open(file_name, "r") as quizz_file:
			quizz = quizz_file.read().split("\n")
		quizz_file.close()
		for question in quizz:
			if len(question) == 0:
				quizz.remove(question)
		for index in range(len(quizz)):
			question = Question(quizz[index])
			question_statement = question.text + "\n" + question.choice_a + "\n" + question.choice_b + "\n" + question.choice_c + "\n"
			question_answer = question.correct_choice
			question_points = DIFFICULTY_TO_POINTS_MAP[question.difficulty]
			questions_answers_points.append([question_statement, question_answer, question_points])
		return questions_answers_points
