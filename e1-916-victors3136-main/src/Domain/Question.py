from src.Domain.Exceptions import ImpossibleAnswer, IncorrectNumberOfParametersForQuestion, WrongDifficulty


class Question:
	def __init__(self, parameter_string):
		parameters = parameter_string.split(";")
		if len(parameters) != 7:
			raise IncorrectNumberOfParametersForQuestion("The question does not have enough paramters. Qid: " + str(parameters))
		if parameters[6].lower() not in ["easy", "medium", "hard", "easy\n", "medium\n", "hard\n"]:
			raise WrongDifficulty("Difficulty level must be easy, medium or hard")
		if parameters[5] not in [parameters[2], parameters[3], parameters[4]]:
			raise ImpossibleAnswer("Correct answer must be one of the 3 options")
		self.__id = parameters[0]
		self.__text = parameters[1]
		self.__choice_a = parameters[2]
		self.__choice_b = parameters[3]
		self.__choice_c = parameters[4]
		self.__correct_choice = parameters[5].lower()
		self.__difficulty = parameters[6].lower()

	def __eq__(self, other):
		if isinstance(other, Question) is False:
			return False
		return self.id == other.id and self.choice_a == other.choice_a and self.choice_b == other.choice_b and self.choice_c == other.choice_c and \
			self.correct_choice == other.correct_choice and self.difficulty == other.difficulty

	@property
	def id(self):
		return self.__id

	@property
	def text(self):
		return self.__text

	@property
	def choice_a(self):
		return self.__choice_a

	@property
	def choice_b(self):
		return self.__choice_b

	@property
	def choice_c(self):
		return self.__choice_c

	@property
	def correct_choice(self):
		return self.__correct_choice

	@property
	def difficulty(self):
		return self.__difficulty

	def __str__(self):
		return self.id + ";" + self.text + ";" + self.choice_a + ";" + self.choice_b + ";" + self.choice_c+ ";" + self.correct_choice + ";" + self.difficulty
