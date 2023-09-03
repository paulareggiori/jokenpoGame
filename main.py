"""
This is a rock, paper, scissors game that takes in user input
and checks against the computer randomize choice.
Game keeps a counter of wins-losses until user exit the game.
"""
from actions import Actions
from computer import Computer
from validation import Validation

# Stater objects
computer_answer = Computer()
game_actions = Actions()
validation = Validation()

# Welcome user
lang = game_actions.language()
game_actions.welcome(lang)

# Ask if they want to start playing
play = game_actions.start_quiz(lang)
while play:
    user = game_actions.user_answer(lang)
    computer = computer_answer.get_computer_answer(lang)

    # Validate answer and add to score
    validation.check_answer(computer, user, lang)

    # Ask if user wants to play again
    play = game_actions.play_again(lang)

# When questions are done, show finished score
total_score = validation.get_score()
total_games = validation.total_games()
game_actions.final_score(total_score, total_games, lang)

# Goodbye message
game_actions.goodbye(lang)
