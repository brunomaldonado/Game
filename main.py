
from shutil import get_terminal_size
import random
import colorama
from colorama import Fore, Style, Back
colorama.init()

rock_u = '''
         _______     
     ---'   _;__)   
           (_____) 
           (_____) 
           (____)   
     ---.__(___)   
'''
rock_c = '''
                              _______
                             (__:_   '___
                            (_____) 
                            (_____)
                             (____)
                              (___)__.---
'''
paper_u = '''
         _______
     ---'   ____)____
               ______)
               _______)
              _______)
     ---.__________)
'''
paper_c = '''
                              _______         
                         ____(____   '___
                        (______
                       (_______ 
                        (________
                          (__________.---
'''

scissors_u = '''
         _______
     ---'   ____)____
               ______)
            __________)
           (____)
     ---.__(___)
'''

scissors_c = '''
                             _______
                        ____(____   '___
                       (______
                      (__________
                            (____)
                             (___)__.---
'''


user_images = ["", rock_u, paper_u, scissors_u]
comp_images = ["", rock_c, paper_c, scissors_c]


def check_rules(user_choice, computer_choice, user_bookmark, comp_bookmark):

    if user_choice == 1:
        user_choice_name = "ROCK..."
    elif user_choice == 2:
        user_choice_name = "PAPER.."
    else:
        user_choice_name = "SCISSORS"

    if computer_choice == 1:
        comp_choice_name = "ROCK..."
    elif computer_choice == 2:
        comp_choice_name = "PAPER.."
    else:
        comp_choice_name = "SCISSORS"

    if user_choice == computer_choice:
        print()
        print(f"{Fore.MAGENTA}                    Tie!!!...   \n{Fore.WHITE}")
        print("    user choice               comp choice")
        print("                     V/S                  ")
        print(
            f"       {Fore.GREEN}{user_choice_name}                   {Fore.CYAN}{comp_choice_name}")
        print(
            f"          {Fore.GREEN}{user_bookmark}                         {Fore.CYAN}{comp_bookmark}")
        print(
            f"{Fore.GREEN}{user_images[user_choice]}                    {Fore.WHITE}     {Fore.CYAN}{comp_images[computer_choice]}")
        print()

    elif user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 3 or user_choice == 3 and computer_choice == 1:
        comp_bookmark += 1
        print()
        print(f"{Fore.WHITE}           %r wins %r " %
              (comp_choice_name, user_choice_name))
        print(f"{Fore.CYAN}                Computer Wins \n")
        print(f"{Fore.WHITE}    user choice               comp choice")
        print("                     V/S                  ")
        print(
            f"      {Fore.GREEN}{user_choice_name}                   {Fore.CYAN}{comp_choice_name}")
        print(
            f"         {Fore.GREEN}{user_bookmark}                         {Fore.CYAN}{comp_bookmark}")
        print(
            f"{Fore.GREEN}{user_images[user_choice]}                    {Fore.WHITE}       {Fore.CYAN}{comp_images[computer_choice]}")
        check_winners(user_choice, computer_choice,
                      user_bookmark, comp_bookmark)
        print()

    elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1 or user_choice == 3 and computer_choice == 2:
        user_bookmark += 1
        print()
        print(f"{Fore.WHITE}           %r wins %r" %
              (user_choice_name, comp_choice_name))
        print(f"{Fore.GREEN}                 User Wins\n")
        print(f"{Fore.WHITE}    user choice               comp choice")
        print("                     V/S                  ")
        print(
            f"      {Fore.GREEN}{user_choice_name}                   {Fore.CYAN}{comp_choice_name}")
        print(
            f"         {Fore.GREEN}{user_bookmark}                         {Fore.CYAN}{comp_bookmark}")
        print(
            f"{Fore.GREEN}{user_images[user_choice]}                    {Fore.WHITE}     {Fore.CYAN}{comp_images[computer_choice]}")
        check_winners(user_choice, computer_choice,
                      user_bookmark, comp_bookmark)
        print()

    return user_bookmark, comp_bookmark


def check_winners(user_choice, computer_choice, user_bookmark, comp_bookmark):
    if user_bookmark == 3:
        print(f"{Fore.GREEN}{'*' * 46}")
        print(f"{Fore.GREEN}             THE USER WON THE GAME")
        print(f"{'*' * 46}{Fore.WHITE}")
        print()

        print(f"{Fore.YELLOW}Do you want to play again? (y/n): ")
        ans = input().lower()
        if ans == 'n':
            exit()
        run_game()

    if comp_bookmark == 3:
        print(f"{Fore.CYAN}{'*' * 46}")
        print(f"{Fore.CYAN}            THE COMPUTER WON THE GAME")
        print(f"{'*' * 46}{Fore.WHITE}")
        print()

        print(f"{Fore.YELLOW}Do you want to play again? (y/n) ")
        ans = input().lower()
        if ans == 'n':
            exit()
        run_game()


def run_game():
    choice_options = ["", "rock", "paper", "scissors"]
    choice_options[0] = 0
    choice_options[1] = 1
    choice_options[2] = 2
    choice_options[3] = 3
    user_bookmark = 0
    comp_bookmark = 0
    rounds = 1

    while True:
        computer_choice = random.randint(1, 3)
        try:
            print(f"{Fore.WHITE}{'*' * 19} ROUND", rounds, '*' * 18)
            user_choice = int(
                input(f"\n{Fore.WHITE}Type 1. rock, 2. paper 0r 3. scissors: "))
            user_bookmark, comp_bookmark = check_rules(
                user_choice, computer_choice, user_bookmark, comp_bookmark)
        except ValueError:
            print(f"{Fore.RED}{'*' * 12}¡¡¡ wrong option !!!. {'*' * 12}{Fore.WHITE}")
            print()
            continue
        while user_choice >= 4 or user_choice < 1:
            print(f"{Fore.RED}{'*' * 12}¡¡¡ wrong option !!!. {'*' * 12}{Fore.WHITE}")
            print()
            try:
                print(f"{Fore.WHITE}{'*' * 19} ROUND", rounds, '*' * 18)
                user_choice = int(
                    input(f"\n{Fore.WHITE}Type 1. rock, 2. paper 0r 3. scissors: "))
                user_bookmark, comp_bookmark = check_rules(
                    user_choice, computer_choice, user_bookmark, comp_bookmark)
            except ValueError:
                continue
        rounds += 1


if __name__ == '__main__':
    run_game()

# 25844962
