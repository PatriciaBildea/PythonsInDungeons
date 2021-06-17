import os
import winsound
import Player
import Enemies
import random


class Messages:
    @staticmethod
    def intro_message():
        introMsg = """ 
*****************************************************************************************
* Welcome, stranger!                                                                    *
* Here in Hinterlands, you'll get to fight dragons and conquer the deadliest dungeons.  *
* In a country where magic rules, anything is possible if you wish so.                  *
* It all depends on you, brave hero.                                                    *
*****************************************************************************************
        """
        print(introMsg)


class Choices:
    @staticmethod
    def path():
        print("Entering the world...")
        input("Press any key to continue")
        os.system("cls")
        sound = "Exploring.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        print('''A crossroads lies ahead of you...
                      (  )   /  ^  /
                (  ) (    ) /  /  /
               (    )  ||  /  /  /
                 || (  )  /  F  /
  /     \          (    )/  O  /       /_
   |   |         (  )|| /  R  /   /\  /___\ 
/     \         (    ) /  E  /   /__\/_____\  
 |   |/     \     ||  /  S  /   /_||/__| |__\   
_______|___|_________/  T  /__________________      
< -- V I L L A G E            D E S E R T -- >
----------------------------------------------''')
        incorrect_path = True   # used while incorrect paths are chosen
        while incorrect_path:
            path = input('''
1. Will you go to the village?
2. Do you choose the sneaky forest?
3. Are you confident enough to be exposed in the dessert? 
Choose your destiny! --> ''')
            if path == "1":
                incorrect_path = False
                print("""You are walking into the village                    
From a backside alley an enemy appears...""")
            elif path == "2":
                incorrect_path = False
                print("""The darkness of the forest awaits
Two steps into the forest you hear something in the bushes...
You go take a closer look...""")
            elif path == "3":
                incorrect_path = False
                print("""The open desert lies ahead.
Something breathes behind you...
You turn around...""")
            else:
                incorrect_path = True
                print("""Path not available.
Please try again: """)
        return path


class Actions:
    @staticmethod
    def random_number():
        number = random.randint(0, 2)
        sound = "BattleFinal.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        if number == 0:
            enemy = Enemies.Goblin()
            input("Press any key to continue")
        elif number == 1:
            enemy = Enemies.Rat()
            input("Press any key to continue")
        elif number == 2:
            enemy = Enemies.Orc()
            input("Press any key to continue")
        return enemy

    @staticmethod
    def fight(player, enemy):
        os.system("cls")
        while player.health > 0 and enemy.health > 0:
            player.health -= enemy.damage
            enemy.health -= (player.mana + player.damage)
        if enemy.health == 0:
            print(f"""Congratulations, 
You have won your first battle!
And with {player.health} energy to spare! Ha! Ha! Ha!""")
            input("Press any key to continue")
            os.system("cls")
        elif player.health == 0:
            print("The enemy has proven to be stronger than you! Try again!")
            input("Press any key to continue")
            os.system("cls")





