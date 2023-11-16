from src.Controller.Controller import Controller
from src.Domain.Exceptions import QuestionError, QuizzError

COMMAND_NAME_INDEX = 0
COMMAND_PARAMETERS_INDEX = 1


class UI:
	def __init__(self):
		self.__user_command = None
		self.__game = Controller()

	def get_command(self):
		self.__user_command = input("> ")

	def run(self):
		while True:
			self.get_command()
			if self.__user_command.lower() == "exit":
				break
			self.interpret_command()

	def interpret_command(self):
		command = self.__user_command.split(" ", maxsplit = 1)
		match command[COMMAND_NAME_INDEX]:
			case "add":
				try:
					self.__game.add_question(command[COMMAND_PARAMETERS_INDEX])
				except QuestionError as qe:
					print(qe)
				finally:
					return

			case "create":
				try:
					self.__game.create_quizz(command[COMMAND_PARAMETERS_INDEX])
				except QuizzError as qe:
					print(qe)
				finally:
					return

			case "start":
				try:
					print("Welcome to the quizz!")
					maxpoints = 0
					userpoints = 0
					file_name = command[COMMAND_PARAMETERS_INDEX]
					all_questions = Controller.play_quizz(file_name)
					for sublist in all_questions:
						question = sublist[0]
						answer = sublist[1]
						points = sublist[2]
						print(question)
						user_answer = input("Your answer:\n> ")
						if user_answer.strip().lower() == answer:
							userpoints += points
							print("Correct! Congratulations!")
						else:
							print("That is wrong :(")
						maxpoints += points
					print("Game over. Your score: " + str(userpoints) + "/" + str(maxpoints))
				except IOError as ioe:
					print(ioe)
				finally:
					return
		print("Invalid command")
		return
