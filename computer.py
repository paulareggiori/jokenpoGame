"""
This module contains computer answer class used
to find a randomize choice.
"""
import random


class Computer:
	def __init__(self):
		self.plays_en = {0: "rock", 1: "paper", 2: "scissors"}
		self.plays_pt = {0: "pedra", 1: "papel", 2: "tesoura"}
		self.computer = 0

	def computer_answer(self, lang):
		number = random.randint(0, 2)
		if lang == "EN":
			self.computer = self.plays_en.get(number)
		elif lang == "PT":
			self.computer = self.plays_pt.get(number)

	def get_computer_answer(self, lang):
		self.computer_answer(lang)
		return self.computer
