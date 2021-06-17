import os
import random
import winsound
import Player
import Enemies
import random

@staticmethod
def path():
    print("Entering the world...")
    input("Press any key to continue")
    os.system("cls")
    path = input('''A crossroads lies ahead of you...
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
----------------------------------------------
1. Will you go to the village?
2. Do you choose the sneaky forest?
3. Are you confident enough to be exposed in the dessert? 
Choose your destiny! --> ''')
    if path == "1":
        print("""You are walking into the village
From a backside alley an enemy appears...""")
    elif path == "2":
        print("""The darkness of the forest awaits
Two steps into the forest you hear something in the bushes...
You go take a closer look...""")
    elif path == "3":
        print("""The open desert lies ahead.
Something breathes behind you...
You turn around...""")
    else:
        print("Path not available")
    return path

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