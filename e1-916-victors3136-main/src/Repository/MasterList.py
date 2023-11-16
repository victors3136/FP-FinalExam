import random

from src.Domain.Exceptions import IncorrectNumberOfParametersForQuizz, QuizzError
from src.Domain.Question import Question

INITIAL_QUESTION_NUMBER = 100
LOW_BOUND = 0
HIGH_BOUND = 1001
CURRENT_YEAR = 2023
FIRST_INDEX = 0


class MasterList:
	def __init__(self):
		self.__question_list = []

	def set_up(self):
		MasterList.generate_questions()
		self.load_data()

	@staticmethod
	def generate_questions():
		master_file = open("MasterList.txt", "w")
		for index in range(INITIAL_QUESTION_NUMBER):
			question_text = random.choice(["What is the biggest number?", "What is the smallest number?", "What year is the closest to the current year?",
			                               "Which of the following is the closest to a multiple of 123?"])
			choice_a = choice_b = choice_c = correct_answer = difficulty = None
			while choice_a == choice_b or choice_b == choice_c or choice_c == choice_a:
				choice_a = random.randint(LOW_BOUND, HIGH_BOUND)
				choice_b = random.randint(LOW_BOUND, HIGH_BOUND)
				choice_c = random.randint(LOW_BOUND, HIGH_BOUND)
			if question_text == "What is the biggest number?":
				correct_answer = max(choice_a, choice_b, choice_c)
				difficulty = "easy"
			if question_text == "What is the smallest number?":
				correct_answer = min(choice_a, choice_b, choice_c)
				difficulty = "easy"
			if question_text == "What year is the closest to the current year?":
				correct_answer = sorted([choice_a, choice_b, choice_c], key = lambda x: abs(x - CURRENT_YEAR))[FIRST_INDEX]
				difficulty = "medium"
			if question_text == "Which of the following is the closest to a multiple of 123?":
				correct_answer = sorted([choice_a, choice_b, choice_c], key = lambda x: x % 123)[FIRST_INDEX]
				difficulty = "hard"
			question_id = index
			question_string = str(question_id) + ";" + question_text + ";" + str(choice_a) + ";" + str(choice_b) + ";" + str(choice_c) + ";" + str(
				correct_answer) + ";" + difficulty
			question = Question(question_string)
			master_file.write(str(question) + "\n")
		master_file.close()

	def load_data(self):
		question_list = []
		with open("MasterList.txt", "r") as master_file:
			text = master_file.read().split("\n")
			for line in text:
				if len(line):
					question = Question(line)
					question_list.append(question)
		master_file.close()
		self.__question_list = question_list[:]

	def save_data(self):
		with open("MasterList.txt", "w") as master_file:
			for question in self.__question_list:
				master_file.write(str(question) + "\n")
		master_file.close()

	def add_question(self, question_string):
		question = Question(question_string)
		self.__question_list.append(question)
		self.save_data()

	def get_questions_of_difficulty(self, difficulty):
		"""
		Function that makes a sublist of all questions of required difficulty in the master list
		:param difficulty: specifies the difficulty of the questions chosen
		:return: list of Question objects
		"""
		list = []
		for question in self.__question_list:
			if question.difficulty == difficulty.lower():
				list.append(question)
		return list

	def create_quizz(self, quizz_string):
		"""
		Function creates a quizz file from a string
		:param quizz_string: contains 3 parameters separated by spaces
		:return: None
		may raise IncorrectNumberOfParametersForQuizz if upon splitting the quizz_string into parameters, there are not exactly 3 parameters
		may raise QuizzError if there are nt enough questions to make a correct quizz
		"""
		parameters = quizz_string.split()
		if len(parameters) != 3:
			raise IncorrectNumberOfParametersForQuizz("You did not specify the correct number of parameters for the quizz!")
		questions_number = int(parameters[1])
		difficulty = parameters[0]
		if "\n" in difficulty:
			difficulty.remove("\n")
		base_difficulty_questions = self.get_questions_of_difficulty(parameters[0])
		if len(base_difficulty_questions) * 2 < questions_number:
			raise QuizzError("Not enough questions of specified difficulty!")
		question_queue = []
		while len(question_queue) < questions_number:
			while len(base_difficulty_questions):
				if len(question_queue) == questions_number:
					break
				question = random.choice(base_difficulty_questions)
				question_queue.append(question)
				base_difficulty_questions.remove(question)
			if len(question_queue) == questions_number:
				break
			while len(question_queue) < questions_number:
				question = random.choice(self.__question_list)
				if question not in question_queue:
					question_queue.append(question)
		filename = parameters[2]
		with open(filename, "w") as quizz_file:
			for question in question_queue:
				quizz_file.write(str(question) + "\n")
		quizz_file.close()
