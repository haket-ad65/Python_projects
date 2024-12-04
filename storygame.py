import time
def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print_slow("Welcome to the Mystic Forest Adeventure!")
    print_slow("You are an adventurer seeking a mysterious artifact which is very valuable!")
    print_slow("Legend says that deep in the Mystic Forest there lies the Obsidian Relic, a powerful artifact. ")
    print_slow("Many have ventured into the forest but never returned. Will you uncover its secrets?")
    print_slow("Your journey begins now...\n")
    return forest_path()

def forest_path():
    print_slow("You arrive at a fork in the forest path.")
    print_slow("Do you: (1) Take the left path into the dense forest , (2) Take the right path towards a glowing light, or (3) Stay where you are and investigate the area?")
    choice= input("Enter 1, 2, or 3 :")

    if choice == "1":
        return dense_forest()
    elif choice == "2":
        return glowing_light()
    elif choice=="3":
        return investigate_area()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return forest_path()
    
def dense_forest():
    print_slow("The dense forest is dark and eerie. You hear rustling in the bushes....")
    print_slow("Suddenly, a wild beast appears!")
    print_slow("Do you: (1) Fight the beast, (2) Run away? or (3) Attempt to tame it?")
    choice = input("Enter 1 2 or 3: ")

    if choice == "1":
        return fight_beast()
    elif choice == "2":
        return run_away()
    elif choice == "3":
        return tame_beast()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return dense_forest()
    
def glowing_light():
    print_slow("The glowing light leads you to a tranquil clearing with a magical fountain.")
    print_slow("The fountain offers two potions: (1) A red potion, (2) A blue potion or (3) Drink from the fountain directly.")
    choice=input("Enter 1,2 or 3 :")
    if choice == "1":
        return red_potion()
    elif choice == "2":
        return blue_potion()
    elif choice == "3":
        return drink_fountain()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return glowing_light()

def investigate_area():
    print_slow("So you decide to stay and investigate the area...")
    print_slow("You find an ancient map buried unde a rock. The map marks a secret cave hidden within the forest.")
    print_slow("Do you: (1) Follow the map to the secret cave, or (2) Ignore the mapand proceed down a random path?")
    choice= input("Enter 1 or 2: ")

    if choice =="1":
        return secret_cave()
    elif choice =="2":
        return random_path()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return investigate_area()
    
def fight_beast():
    print_slow("You braverly fight the beast, but it's too powerful.")
    print_slow("As you fall, the beast reveals it was protecting the artifact. You failed to retrieve it.")
    return game_over()

def run_away():
    print_slow("You manage to escape, but you hear whispers all around you....")
    print_slow("After wandering aimlessly, you find that the forest seems to shift.")
    print_slow("Now you feel lost in the endless and dark jungle.")
    print_slow("Do you: (1) Keep running blindly, or (2) Try to climb a tree to get a better view?")
    choice=input("Enter 1 or 2: ")
    if choice == "1":
        return run_blindly()
    elif choice == "2":
        return climb_tree()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return run_away()
    
def tame_beast():
    print_slow("You cautiously approach the beast and offer it food.")
    print_slow("Amazingly, the beast calm down and become your companion.")
    print_slow("With the beast by your side, you feel more confident to continue your quest.")
    return relic_chamber(beast=True)

def red_potion():
    print_slow("The red potion grants you immense strength!")
    print_slow("You continue your journey and easily overcome all challenges.")
    print_slow("Congratulations! You retrieve the Obsidian Relic and completed your adventure.")
    return play_again()

def blue_potion():
    print_slow("The blue potion can make you shapeshift and its sharpen your senses...")
    print_slow("You fly upward and notice a secret door behind the fountain.")
    return secret_door()

def drink_fountain():
    print_slow("the water transform you into a tree, rooted to the spot for eternity.")
    return game_over()

def secret_cave():
    print_slow("You follow the map and find a hidden cave. Inside, you discover an ancient tablet with riddles.")
    print_slow("Do you: *(1) Solve the riddles to proceed deeper into the cave or (2) Leave the cave?")
    choice= input("Enter 1 or 2: ")

    if choice == "1":
        return solve_riddles()
    elif choice == "2":
        return forest_path()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return secret_cave()
    
def random_path():
        print_slow("You wander down a random path and find yourself back at the fork.")
        print_slow("Fate seems to want to you choose again.")
        return forest_path

def secret_door():
    print_slow("You open the door and find the chamber filled with glowing crystals")
    print_slow("The crystals emit strange whispers. Do you: (1) Touch the crystals, (2) Leave the chamber?")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        return touch_crystals()
    elif choice == "2":
        return forest_path()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return secret_door()
    
def touch_crystals():
    print_slow("You reach out and touch the glowing crystals...")
    print_slow("Suddenly, your mind is flooded with visions of the past, present, and possible futures.")
    print_slow("The crystals seem to be asking you a question: 'What is it that you seek?'")
    print_slow("Do you: (1) Seek power, (2) Seek truth, or (3) Seek the relic?")
    choice=input("Enter the 1, 2, or 3: ")
    if choice=="1":
        return seek_power()
    elif choice=="2":
        return seek_truth()
    elif choice=="3":
        return seek_relic()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return touch_crystals()
    
def solve_riddles():
    print_slow("You solve the riddles, and a hidden passage opens.")
    return relic_chamber(beast=False)

def climb_tree():
    print_slow("You climb a tree and spot a hidden trail leading to an ancient temple.")
    return relic_chamber(beast=False)

def run_blindly():
    print_slow("You run blundly and fall into a hidden pit...")
    print_slow("Darkness surrounds you and you died")
    return game_over()

def seek_power():
    print_slow("The crystals glow brighter, and you feel a surge of strength course through your body.")
    print_slow("But as you gain power, the forest around you grows darker, as if it's feeding on your energy.")
    print_slow("A voice whispers: 'Power always comes with a price. Are you willing to pay?'")
    print_slow("Do you: (1) Accept the cost, or (2) Reject the power?")
    choice=input("Enter 1 or 2: ")
    if choice =="1":
        print_slow("You accept the cost, and the forest consumes your humanity, transforming you into its eternal protector.")
        return game_over()
    elif choice =="2":
        print_slow("You reject the power, and the crystals dim. you feel weaker but  regain your sense of purpose.")
        return relic_chamber(beast=False)
    else:
        print_slow("Invalid choice. Please try again.\n")
        return seek_power()
    
def seek_truth():
    print_slow("The crystals hum, and a vision of the forest's origins unfolds before your eyes.")
    print_slow("You see an ancient civilization that once thrived here, guarding the relic to protect the world from its power.")
    print_slow("A voice asks: 'Now that you know the truth, will you still seek the relic?'")
    print_slow("Do you: (1) Abandon your quest, or (2) Continue seeking the relic?")
    choice=input("Enter 1 or 2: ")
    if choice == "1":
        print_slow("You abandon your quest, leaving the relic untouched. The forest you safe passage out.")
        return play_again()
    elif choice =="2":
        print_slow("You continue your quest. but now you understand the weight of your actions.")
        return relic_chamber(beast=False)
    else:
        print_slow("Invalid choice. Please try again.\n")
        return seek_truth()

def seek_relic():
    print_slow("The crystals show you a vision of the relic, hidden deep within the forest's heart.")
    print_slow("You now know the path, but the vision comes with a warning: 'The relic's power corrupts all who touch it.'")
    print_slow("Do you: (1) Proceed to the relic despite the warning, or (2) Leave the forest?")
    choice=input("Enter 1 or 2: ")
    if choice == "1":
        print_slow("You push forward, driven by determination. the path ahead leads to the relic chamber.")
        return relic_chamber(beast=False)
    elif choice=="2":
        print_slow("You leave forest, heeding the warning, some mysteries are left unsolved.")
        return play_again()
    else:
        print_slow("Invalid choice. Please try again.\n")
        return seek_relic()


def relic_chamber(beast):
    if beast:
        print_slow("With your beast companion, you defeat the traps guarding the relic.")
        print_slow("Congratulations! You retrieve the Osidian Relic and complete your adventure.")
    else:
        print_slow("You enter the final chamber and retrieve the Osidiab Relic.")
        print_slow("However, the relic demands a price: your freedom. Your become its eternal guradian.")
    return play_again()


def game_over():
    print_slow("\nGAME OVER. Better luck next time!")
    return play_again()

def play_again():
    print_slow("Do you want to play again? (yes or no)")
    choice = input("Enter yes or no: ").strip().lower()

    if choice == "yes":
        return intro()
    elif choice == "no":
        print_slow("Thank you for playing! Goodbye!")
    else: 
        print_slow("Invalid choice. Please try again.")
        return play_again()
    
intro()