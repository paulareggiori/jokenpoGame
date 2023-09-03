"""
This module contains Actions class contains all game
actions and messages.
"""


class Actions:
	def __int__(self):
		self.play = True

	def welcome(self, lang):
		if lang == "EN":
			print("Hello and welcome to  Rock, Paper, Scissors game!")
		elif lang == "PT":
			print("Olá e bem vindo ao Jokenpô!")

	def language(self):
		print("Select the language you want.\n")
		print("Selecione o idioma desejado.\n")
		print("EN - For English\n")
		print("PT - Para Português\n")
		lang = input("").upper()
		if lang == "EN":
			pass
		elif lang == "PT":
			pass
		else:
			print("Not a valid language! We will just go ahead in English.")
			lang = "EN"
		return lang

	def start_quiz(self, lang):
		if lang == "EN":
			answer = input("Do you want to start the game? ")
			if answer.lower() == "yes":
				self.play = True
				return self.play
			elif answer.lower() == "y":
				self.play = True
				return self.play
			else:
				self.play = False
				return self.play
		elif lang == "PT":
			answer = input("Você quer começar a jogar? ")
			if answer.lower() == "sim":
				return True
			elif answer.lower() == "s":
				return True
			else:
				return False

	def user_answer(self, lang):
		if lang == "EN":
			user_play = input("What's your play? ")
		elif lang == "PT":
			user_play = input("Qual é a sua jogada? ")
		return user_play

	def play_again(self, lang):
		if lang == "EN":
			answer = input("Do you want to play again? ")
			if answer.lower() == "yes":
				self.play = True
				return self.play
			elif answer.lower() == "y":
				self.play = True
				return self.play
			else:
				self.play = False
				return self.play
		elif lang == "PT":
			answer = input("Você quer jogar novamente? ")
			if answer.lower() == "sim":
				self.play = True
				return self.play
			elif answer.lower() == "s":
				self.play = True
				return self.play
			else:
				self.play = False
				return self.play

	def final_score(self, score, games, lang):
		if lang == "EN":
			print("Your final score is {} out of {} games.".format(score, games))
		elif lang == "PT":
			print("Sua pontuação final é {} de {} jogos.".format(score, games))

	def goodbye(self, lang):
		if lang == "EN":
			print("Thank you and goodbye!")
		elif lang == "PT":
			print("Obrigada e adeus!")
