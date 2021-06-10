import os
import winsound
import Player

introMsg = """ 
*****************************************************************************************
* Welcome, stranger!                                                                    *
* Here in Hinterlands, you'll get to fight dragons and conquer the deadliest dungeons.  *
* In a country where magic rules, anything is possible if you wish so.                  *
* It all depends on you, brave hero.                                                    *
*****************************************************************************************
"""

sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)
print(introMsg)
user_answer = input(''' Would you like to start the adventure?
Yes or No -> ''')
if user_answer.upper() == "YES":
    print("OK")
    os.system("cls")  # windows
    choice = input('''Choose your class:
1 for Warrior, 2 for Wizard --> ''')
    if choice == "1":
        player_name = input('''You have chosen o be a mighty warrior!
What is your name? --> ''')
        player = Player.Warrior(player_name)
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
    elif choice == "2":
        player_name = input('''You have chosen o be a mighty wizard!
What is your name? --> ''')
        player = Player.Wizard(player_name)
        print("Entering the world...")
        os.system("cls")
        sound = "Exploring.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
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
    else:
        print("That is not a valid option!")

else:
    print("Thank you, good bye!")
