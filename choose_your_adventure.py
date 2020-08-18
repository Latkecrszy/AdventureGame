#Choose your own adventure
#Created by Seth Raphael
#Created on 5/24/2020
#import the random module
import random
#Import the time module
import time
#Initialize the waits variable
waits = 0
#Initialize the deaths variable
deaths = 0
#Initialize the items list
items = []
#Initialize the loop variable
loop = True
#Choice 1 option
print('''You have fallen into a deep pit. When you look around, all that you see is darkness, except two tunnels ahead of you from which light is emminating.
You are stuggling to remember what has happened.\n''')
time.sleep(1)
#Start the main loop
while loop:
    if waits == 12:
        print('''Congratulations! Your time and patience payed off! You remember how you got in and who you are, and remember that you have a phone! You pull it out and call 911.
You are rescued within the hour, and return home to your family.\n''')
        time.sleep(1)
        again = input("Would you like to return to the beginning and try to achieve success through a way other than your patiencec? Y/N >>> ")
        if again == "Y":
            loop = True
            continue
        elif again == "N":
            print("Ok. Try again soon!")
            loop = False
            break
        else:
            print("You did not enter a valid option. You died.")
            loop = False
            break
        
    choice1 = input('''Do you:
1) Walk forward towards the tunnel on the right\n
2) Walk forward towards the tunnel on the left\n
3) Attempt to scale the walls of the pit that you are in\n
4) Stand and think for 5 seconds\n
5) Quit\n
What is your choice? >>> ''')
    if choice1 == "1":
        #Choice 2 option
        choice2 = input('''When you reach the entrance to the tunnel, you see something shimmering on the walls. The light that was coming from the tunnel was from
candles on the walls. You can't quite discern what the shimmering sight is. Do you:\n
1) Continue onwards into the tunnel\n
2) Walk back to where you started\n
What is your choice? >>> ''')
        if choice2 == "1":
            #Choice 3 option
            choice3 = input('''As you walk into the tunnel, some of the shimmering substance drips onto your hand. It burns, and a divot appears where the liquid dropped.
You realize that the entire tunnel is coated in acid. Do you:\n
1) Try to reach the end of the tunnel as quickly as you can with your hands tucked into your shirt\n
2) Retreat back to where you started\n
What is your choice? >>> ''')
            if choice3 == "1":
                print("As you run along the tunnel, your footsteps shake the ground and the acid falls faster. Overwhelmed by pain and dissolving into a puddle, you die a horrible and gruesome death.")
                deaths += 1
                time.sleep(1)
                again = input("Would you like to return to the beginning and try again? Y/N >>> ")
                if again == "Y":
                    loop = True
                    continue
                elif again == "N":
                    print("Ok. Try again soon!")
                    loop = False
                    break
                else:
                    print("You did not enter a valid option. You died.")
                    loop = False
                    break
            elif choice3 == "2":
                print("Even running as fast as you can, you barely make it out alive. Your shirt is now tattered and almost gone, and you have numerous burns all over your body.")
                time.sleep(1)
                loop = True
                continue
            else:
                print("You did not enter a valid option. You died.")
                loop = False
                break
                
        elif choice2 == "2":
            time.sleep(1)
            loop = True
            continue

        else:
            print("You did not enter a valid option. You died.")
            loop = False
            break
    elif choice1 == "2":
        #Choice 2 option
        choice2 = input('''When you reach the entrance to the tunnel, you see a single candle at the end of the tunnel. You can't make out anything else about the tunnel, except a figure by the flame.
Do you:\n
1) Continue down the tunnel to the figure at the end\n
2) Retreat back to where you started\n
What is your choice? >>> ''')
        if choice2 == "1":
            #Choice 3 option
            nums = ["1", "2", "3", "4"]
            drink = random.choice(nums)
            choice3 = input('''At the end of the tunnel, you can see the figure in much more detail. It is an old man, hunched over and covered in a cloak. He comes up to you.\n
He says, "I can offer you an elixer, a potion of sorts, which is the only way to make it through here alive." He snaps his fingers, and suddenly a wall of flames erupt in the tunnel ahead.\n
He whips a black cloth off of the table, revealing four bottles of mysterious swirling liquid. Their positions change every 30 seconds, so the choice is never the same. He gestured for you to choose one.\n

Do you:\n
1) Choose the first potion, brilliant blue in color\n
2) Choose the second potion, as red as blood. Is that blood in that bottle?\n
3) Choose the third potion, a deep purple\n
4) Choose the fourth potion, a muddled brown\n
5) Drink all at once\n
What is your choice? >>> ''')
            if choice3 == "5":
                print("This was an obvious mistake, and you realize it as soon as you down the last drop. You explode into a fiery inferno, and die a painful and gruesome death.")
                again = input("Would you like to return to the beginning and try again? Y/N >>> ")
                if again == "Y":
                    loop = True
                    continue
                elif again == "N":
                    print("Ok. Try again soon!")
                    loop = False
                    break
                else:
                    print("You did not enter a valid option. You died.")
                    loop = False
                    break
            if choice3 == drink:
                #Choice 4 option
                print('''The very moment you take the potion, your body is wrought with pain. You fall to the floor, writhing in agony. When at last the pain subsides, the old man nods.\n
He is indicating that you chose correctly, and you stride into the fire. Surprisingly, the flames only tickle, and you emerge from the inferno unscathed.''')
                loop2 = True
                while loop:
                    choice4 = input('''The tunnel branches off into two directions.\n
One is going to the left, and the other is continuing straight. The one heading straight is producing a faint glow, while the left one is pitch black.\n
Do you:\n
1) Continue straight towards the light\n
2) Turn left into the darkness\n
3) Head back through the fire the way that you came\n
What is your choice? >>> ''')
                    if choice4 == "1":
                    
                        #choice 5 option
                        choice5 = input('''Upon entering the corridor, you notice that it leads to nowhere, it is a dead end. But, there is something glimmering tantalizingly in front of the wall at the end.
Do you:\n
1) Head back to the fork in the tunnel\n
2) Continue to the end of the tunnel to investigate the shining object\n
What is your choice? >>> ''')
                        if choice5 == "1":
                            loop2 = True
                            continue
                        elif choice5 == "2":
                            #Choice 6 option
                            choice6 = input('''When you reach the end of the corridor, the shimmering object comes into focus. It is a sword. Do you:\n
1) Pick up the sword\n
2)Leave it where it is and continue back\n
What is your choice? >>> ''')
                            if choice6 == "1":
                                print('''You just acquired your first item! You gained a sword that deals 90 damage and has a durability of 10 hits.
To see your weapons inventory at any time, type in 'weapons,' and they will be displayed.''')
                                loop = True
                            #CONTINUE HERE CONTINUE HERE CONTINUE HERE
                            #CONTINUE HERE CONTINUE HERE CONTINUE HERE
                            #CONTINUE HERE CONTINUE HERE CONTINUE HERE
                            
            elif choice3 != drink:
                print("You chose... poorly. Remember that if you try again, the potions change, and the one that was wrong last time may be correct the next.")
                print("You died a painful and horrible death to the old man laughing and cackling away.")
                again = input("Would you like to return to the beginning and try again? Y/N >>> ")
                if again == "Y":
                    loop = True
                    continue
                elif again == "N":
                    print("Ok. Try again soon!")
                    loop = False
                    break
                else:
                    print("You did not enter a valid option. You died.")
                    loop = False
                    break
        elif choice2 == "2":
            loop = True
            continue
            

    elif choice1 == "3":
        print('''You run to the wall, find some foot and handholds, and start to climb. You climb for 15 minutes straight, and still have no glimpse of the sun.\n
You try to turn back, but it is too late. You fall to the ground and die a painful and horrible death.\n''')
        time.sleep(1)
        deaths += 1
        again = input("Would you like to return to the beginning and try again? Y/N >>> ")
        if again == "Y":
            loop = True
            continue
        elif again == "N":
            print("Ok. Try again soon!")
            loop = False
            break
        else:
            print("You did not enter a valid option. You died.")
            loop = False
            break
    elif choice1 == "4":
        time.sleep(5)
        print("You have waited to reconsider your options. Remember that time and patience are a virtue!\n")
        time.sleep(1)
        waits += 1

    elif choice1 == "5":
        print("Ok. Return to attempt escape another day!")
        loop = False
        break
        














