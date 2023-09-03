"""
This module contains Validate class used to check
if the answers of the user are write and keep track
of their score.
"""


class Validation:
	def __init__(self):
		self.score = 0
		self.ties = 0
		self.total = 0

	def check_answer(self, computer, user, lang):
		self.add_total()
		if lang == "EN":
			if computer.lower() == "rock":
				if user.lower() == "rock":
					print("It's a tie!")
					self.add_tie()
				elif user.lower() == "paper":
					print("You win! :)")
					self.add_score()
				elif user.lower() == "scissors":
					print("You loose! :(")
				else:
					print("Probably a typo so loose!")
			if computer.lower() == "paper":
				if user.lower() == "paper":
					print("It's a tie!")
					self.add_tie()
				elif user.lower() == "scissors":
					print("You win! :)")
					self.add_score()
				elif user.lower() == "rock":
					print("You loose! :(")
				else:
					print("Probably a typo so loose!")
			if computer.lower() == "scissors":
				if user.lower() == "scissors":
					print("It's a tie!")
					self.add_tie()
				elif user.lower() == "rock":
					print("You win! :)")
					self.add_score()
				elif user.lower() == "paper":
					print("You loose! :(")
				else:
					print("Probably a typo so loose!")
		if lang == "PT":
			if computer.lower() == "pedra":
				if user.lower() == "pedra":
					print("Empatou!")
					self.add_tie()
				elif user.lower() == "papel":
					print("Você ganhou! :)")
					self.add_score()
				elif user.lower() == "tesoura":
					print("Você perdeu! :(")
				else:
					print("Resposta inválida, você perdeu!")
			elif computer.lower() == "papel":
				if user.lower() == "papel":
					print("Empatou!")
					self.add_tie()
				elif user.lower() == "tesoura":
					print("Você ganhou! :)")
					self.add_score()
				elif user.lower() == "pedra":
					print("Você perdeu! :(")
				else:
					print("Resposta inválida, você perdeu!")
			elif computer.lower() == "tesoura":
				if user.lower() == "tesoura":
					print("Empatou!")
					self.add_tie()
				elif user.lower() == "pedra":
					print("Você ganhou! :)")
					self.add_score()
				elif user.lower() == "papel":
					print("Você perdeu! :(")
				else:
					print("Resposta inválida, você perdeu!")

	def add_score(self):
		self.score += 1

	def add_tie(self):
		self.ties += 1

	def add_total(self):
		self.total += 1

	def total_games(self):
		return self.total

	def get_score(self):
		return self.score

