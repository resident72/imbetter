import os, time, random
from colorama import Fore, Style, init
from Player import Player

init()

def clear(timer=0):
    time.sleep(timer)
    os.system("cls")


def choices(choice_list):                                                   #temporary variable in the function (parameter)
    for parameter in choice_list: print(parameter)
    choice = 0
    while choice not in range(1, len(choice_list)):
        choice = input("What you wanna do? ")
        if choice.isdigit():
            choice = int(choice)
            print(f"You chose: {choice}.")   
            if choice not in range(1, len(choice_list) + 1):
                print("!Invalid choice, please use the numbers provided below!")   
                choice = -1                     
        else:   
            choice = -1
            print("!Invalid choice, please use the numbers provided below!")
    return choice - 1

character_choices = [
f"[1] {Fore.WHITE}Vanguard: Health: {Fore.GREEN}25{Style.RESET_ALL}  Strength: {Fore.RED}15{Style.RESET_ALL}  Defense: {Fore.BLUE}25{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}10{Style.RESET_ALL}",
f"[2] {Fore.WHITE}Warrior: Health: {Fore.GREEN}20{Style.RESET_ALL}  Strength: {Fore.RED}20{Style.RESET_ALL}  Defense: {Fore.BLUE}15{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}15{Style.RESET_ALL}",
f"[3] {Fore.WHITE}Thief: Health: {Fore.GREEN}15{Style.RESET_ALL}  Strength: {Fore.RED}10{Style.RESET_ALL}  Defense: {Fore.BLUE}10{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}30{Style.RESET_ALL}",
f"[4] {Fore.WHITE}Slave: Health: {Fore.GREEN}10{Style.RESET_ALL}  Strength: {Fore.RED}5{Style.RESET_ALL}  Defense: {Fore.BLUE}5{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}5{Style.RESET_ALL}"
]

characters = [
    Player("Vanguard", 25, 15, 25, 10),
    Player("Warrior", 20, 20, 15, 15),
    Player("Thief", 15, 10, 10, 30),
    Player("Slave", 10, 5, 5, 5)
]

choice = choices(character_choices)
player = characters[choice]

choices("You find a chest.", {"Open it":f"Nothing happens {player.stat_upgrade("strength", 100)}", "Examine":"you're gay as hell"})



print(f"You chose the {player.name}!")

player.print_stats()










# while True:    
#     print("You wake up in a random hole with nothing on your ass, you see some pants on the ground, do you take em or not?")
#     choice = int(input("[1] Take the pants and put em on \n[2] Stay butt ass naked\n"))
#     os.system("cls")
#     if choice == 1:
#         player.defense += 1
#         print("Your ass is covered [+ 1 Defense]")
#     elif choice == 2:
#         player.health -= 1
#         print("Your ass shivers [-1 Health]")
#     else:
#         print("[!]DUMBASS YOU GOT TO SAY 1 OR 2, HOW CLUELESS CAN YOU GET?[!]")
#         continue
#     print_stats()
#     break


    # while True:       
    #     try:
    #         choice = int(input("What you wanna do? ")) - 1
    #         choice_list[choice]
    #     except IndexError:
    #         continue
    #     return choice



# classes = {
#     1: {"name": "Vanguard", "health": 25, "strength": 15, "defense": 25, "dexterity": 10},
#     2: {"name": "Warrior",  "health": 20, "strength": 20, "defense": 15, "dexterity": 15},
#     3: {"name": "Thief",    "health": 15, "strength": 10, "defense": 10, "dexterity": 30},
#     4: {"name": "Slave",    "health": 10, "strength": 5,  "defense": 5,  "dexterity": 5}
# }
