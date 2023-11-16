class QuestionError(Exception):
	def __init__(self, error_message):
		super().__init__(error_message)
		self.text = error_message

	def __str__(self):
		return self.text


class IncorrectNumberOfParametersForQuestion(QuestionError):
	def __init__(self, error_message):
		super().__init__(error_message)

	def __str__(self):
		return super().__str__()


class WrongDifficulty(QuestionError):
	def __init__(self, error_message):
		super().__init__(error_message)

	def __str__(self):
		return super().__str__()


class ImpossibleAnswer(QuestionError):
	def __init__(self, error_message):
		super().__init__(error_message)

	def __str__(self):
		return super().__str__()


class QuizzError(Exception):
	def __init__(self, error_message):
		super().__init__()
		self.text = error_message

	def __str__(self):
		return self.text


class IncorrectNumberOfParametersForQuizz(QuizzError):
	def __init__(self, error_message):
		super().__init__(error_message)

	def __str__(self):
		return super().__str__()
