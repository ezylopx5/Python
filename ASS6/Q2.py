# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.
# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.
# import random
# num = random.choice(["Rock","Paper","Scissors"])

# class Rockpaperscissors:
#     def __init__(self):
#         return
#     def totround(self,numround):
#         for i in range(numround):
#             in_put = str(input("Your turn "))
#             if in_put == num:
#                 return print("You win ")
#             else:
#                 sum += i 
#     def check_win(self,):

#         if sum < numround - sum:

#             print("You've won") 
#         else:
#             print("You've lost")
             

        

#         return
#     def com_choice(self):
#         return
    

import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(["Rock", "Paper", "Scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            self.user_wins += 1
            return "User wins this round!"
        else:
            self.computer_wins += 1
            return "Computer wins this round!"

    def play_game(self):
        while self.current_round < self.total_rounds:
            print(f"\nRound {self.current_round + 1}/{self.total_rounds}")
            user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()

            if user_choice not in ["Rock", "Paper", "Scissors"]:
                print("Invalid input! Try again.")
                continue

            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            self.current_round += 1

        self.check_game_winner()

    def check_game_winner(self):
        print("\nGame Over!")

        if self.user_wins > self.computer_wins:
            print("You won the game!")
        elif self.user_wins < self.computer_wins:
            print("Computer wins the game!.")
        else:
            print("It's a draw!")


rounds = int(input("Enter number of rounds: "))
game = RockPaperScissors(rounds)
game.play_game()