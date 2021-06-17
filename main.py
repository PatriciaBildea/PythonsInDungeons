import os
import winsound
import Player
import Enemies
import Utils
import random

sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)

Utils.Messages.intro_message()
play = True  # used wile player does not exit
while play:
    user_answer = input('''Would you like to start the adventure?
Yes or No -> ''')
    if user_answer.upper() == "YES":
        print("OK")
        os.system("cls")  # windows
        incorrect_choice = True  # used while incorrect choices are made
        while incorrect_choice:
            choice = input('''Choose your class:
1 for Warrior, 2 for Wizard --> ''')
            if choice == "1":
                incorrect_choice = False
                player_name = input('''You have chosen to be a mighty warrior!
What is your name? --> ''')
                player = Player.Warrior(player_name)
                Utils.Choices.path()
                enemy = Utils.Actions.random_number()
                Utils.Actions.fight(player, enemy)
                print("""Thank you for playing!
Good luck in your next adventures!
Farewell!""")
                play = False

            elif choice == "2":
                incorrect_choice = False
                player_name = input('''You have chosen to be a mighty wizard!
What is your name? --> ''')
                player = Player.Wizard(player_name)
                Utils.Choices.path()
                enemy = Utils.Actions.random_number()
                Utils.Actions.fight(player, enemy)
                print("""Thank you for playing!
Good luck in your next adventures!
Farewell!""")
                play = False

            else:
                incorrect_choice = True
                print("That is not a valid option! Please try again!")

    elif user_answer.upper() == "NO":
        play = False
        print("Thank you, good bye!")
    else:
        print("That is not a valid option. Please try again!")
        play = True

