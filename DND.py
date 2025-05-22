import os, time, random
from Player import Player
from colorama import Fore, Style, init

init()

def clear(timer=0):
    time.sleep(timer)
    os.system("cls")

  

def choices(event, choice_dict):
    print(event)                                
    for parameter in choice_dict: 
        print(parameter)
    
    while True:
        choice = input("What you wanna do? ")
        if choice.isdigit():
            choice = int(choice)                     
            if 1 <= choice <= len(choice_dict):
                break
        print("!Invalid choice, please use the numbers provided below!")
    
    selected = list(choice_dict.values())[choice - 1]
    
    if callable(selected):
        result = selected()
        if result: 
            print(result)
    else:
        result = selected
    
    return result

# def ded():
#     if player.health <= 0:
#         print("You dead man")
#     choices("Continue" , "Give up") 

characters = [
    Player("Vanguard", 25, 15, 25, 10),
    Player("Warrior", 20, 20, 15, 15),
    Player("Thief", 15, 10, 10, 30),
    Player("Slave", 10, 5, 5, 5)
]

character_choices = {
    f"[1] {Fore.WHITE}Vanguard: Health: {Fore.GREEN}25{Style.RESET_ALL}  Strength: {Fore.RED}15{Style.RESET_ALL}  Defense: {Fore.BLUE}25{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}10{Style.RESET_ALL}": 0,
    f"[2] {Fore.WHITE}Warrior: Health: {Fore.GREEN}20{Style.RESET_ALL}  Strength: {Fore.RED}20{Style.RESET_ALL}  Defense: {Fore.BLUE}15{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}15{Style.RESET_ALL}": 1,
    f"[3] {Fore.WHITE}Thief: Health: {Fore.GREEN}15{Style.RESET_ALL}  Strength: {Fore.RED}10{Style.RESET_ALL}  Defense: {Fore.BLUE}10{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}30{Style.RESET_ALL}": 2,
    f"[4] {Fore.WHITE}Slave: Health: {Fore.GREEN}10{Style.RESET_ALL}  Strength: {Fore.RED}5{Style.RESET_ALL}  Defense: {Fore.BLUE}5{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}5{Style.RESET_ALL}": 3
}


character_index = choices("Choose your character:", character_choices)
player = characters[character_index]
print(f"You chose the {player.name}!")
player.print_stats()


choices("Your naked ass wakes up in the tightest cave known to man. You see a small crevice.", {
    "[1] Give up": lambda: f" You died of starvation! {player.stat_upgrade('health', -1000)}",
    "[2] You crawl through it.": lambda: f"You crawl out, the light burns your eyes as you {player.stat_upgrade('health', -1)}"
})

choices("Your naked ass wakes up in the tightest cave known to man. You see a small crevice.", {
    "[1] Give up": lambda: f" You died of starvation! {player.stat_upgrade('health', -1000)}",
    "[2] You crawl through it.": lambda: f"You crawl out, the light burns your eyes as you {player.stat_upgrade('health', -1)}"
})



player.print_stats()