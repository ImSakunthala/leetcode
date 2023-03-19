"""Rock paper scissors is a hand game, usually played between two people, in which each player simultaneously forms
one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".

Here to get familiar with Python Class/Error handling, We choose to write a code for Rock, Paper, Scissors game with
random module in it. Steps to take this explained below:

Step 1 -> Get User Input -> Whether Rock/ Paper/ Scissors -> if user input is invalid, then ask user for a valid input.
         [Error handling -> For valid input, TypeError (I/P type -> string)]
Step 2 -> Get Computer Input -> Using Random module -> print the Computer Choice
Step 3 -> Get Score using User Input and Computer Choice, store the score
Step 4 -> Declare win if either of them have 10 points.
 """
import random
from enum import Enum
from typing import List


class Result(Enum):
    TIE = 0
    USER_WON = 1
    COMPUTER_WON = -1


class RockPaperScissorsGame:
    available_choices = ['Rock', 'Paper', 'Scissors']
    wining_rule = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Rock'}

    def __init__(self, number_of_attempts: int = 10):
        self.NUMBER_OF_ATTEMPTS = number_of_attempts
        self.results: List[Result] = []

    def get_user_choice(self) -> str:
        player_choice = ''

        while player_choice == '':
            try:
                user_input = input('Enter your choice[Rock/Paper/Scissors]:').title()
                if user_input in self.available_choices:
                    player_choice = user_input
                else:
                    raise ValueError(f'{user_input} is not a valid input')
            except ValueError as ex:
                print(ex)
                print(f'Enter your choice from {self.available_choices}:')

        return player_choice

    def get_computer_choice(self) -> str:
        computer_choice = random.choice(self.available_choices)
        print(f'System choice: {computer_choice}')
        return computer_choice

    def get_result(self, user_choice: str, computer_choice: str) -> Result:
        if user_choice == computer_choice:
            return Result.TIE
        elif self.wining_rule[user_choice] == computer_choice:
            return Result.USER_WON
        else:
            return Result.COMPUTER_WON

    def display_result(self, result: Result):
        match result:
            case Result.TIE:
                print(f'Its a Tie')
            case Result.USER_WON:
                print('User Won')
            case Result.COMPUTER_WON:
                print('Computer Won')
            case _:
                print(f'Result[{result}] is unknown')

    def run(self, attempt: int):
        print(f'\nAttempt: {attempt}:')
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        result = self.get_result(user_choice, computer_choice)
        self.results.append(result)
        self.display_result(result)

    def final_result(self):
        user_won = self.results.count(Result.USER_WON)
        computer_won = self.results.count(Result.COMPUTER_WON)

        if user_won > computer_won:
            print(f'User won with {user_won} and computer lost with {computer_won}')
        elif computer_won > user_won:
            print(f'computer won with {computer_won} and user lost with {user_won}')
        else:
            print(f"Game tie with user {user_won} and computer with {computer_won}")

    def start(self):
        attempt = 1
        while attempt <= self.NUMBER_OF_ATTEMPTS:
            self.run(attempt)
            attempt += 1
        self.final_result()

game = RockPaperScissorsGame(3)
game.start()
