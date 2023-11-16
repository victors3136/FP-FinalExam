import unittest
from src.Domain.Exceptions import IncorrectNumberOfParametersForQuizz, QuizzError
from src.Domain.Question import Question
from src.Repository.MasterList import MasterList


class Tests(unittest.TestCase):
	def test_create_quizz_errors(self):
		master_list = MasterList()
		with self.assertRaises(QuizzError):
			master_list.create_quizz("easy 2 new.txt")
		with self.assertRaises(IncorrectNumberOfParametersForQuizz):
			master_list.create_quizz("easy 2")

	def test_get_questions_of_difficulty(self):
		master_list = MasterList()
		master_list.add_question("1;Question?;Answer;Nope;NotThis One;Answer;easy")
		question = Question("1;Question?;Answer;Nope;NotThis One;Answer;easy")
		for element in master_list.get_questions_of_difficulty("easy"):
			self.assertEqual(element, question)
		self.assertEqual(len(master_list.get_questions_of_difficulty("hard")), 0)
