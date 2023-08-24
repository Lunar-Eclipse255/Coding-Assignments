import random

playerLevel = 1
playerName = "Mallis"

playerHealth = 10.0

playerChoice = 0

rockDamage = 0
hasSword = False

print("What is your character\'s name?")
playerName = input()
print("Welcome, " + playerName + "!")
print("Before you is a large cave mouth. Darkness lies within. Dare you enter the Cave of Wonders?")

print("1. Enter the Cave of Wonders")
print("2. Run away to the safety of your warm bed")
playerChoice = int(input())
if (playerChoice == 1) :

    print("You walk through the entrance of the cave with your head held high.")
    playerLevel += 1
    print("Your bravery has rewarded you! Congratulations, you are " + "now level " + str(playerLevel))
else :
    print(playerName + " You run home and go to sleep.")
    quit()

print("You travel forward into the dark cave. You feel something press against your leg...")
print("It\'s a trap! Suddenly you\'re being bombarded by rocks from above.")
rockDamage = random.randint(0,4)
playerHealth -= rockDamage
print("The rockslide hits you for " + str(rockDamage) + " hp!")
print("You have " + str(playerHealth) + " health remaining.")
print("You pick yourself up from the cave floor and brush a cloud of dust from your clothes.")
print("The cave narrows as you press on until you manage to squeeze through an opening into a large natural cavern")
print("Before you is a treasure chest")
print("1. Open the chest.")
print("2. Ignore the chest. It is obviously another trap.")
playerChoice = int(input())
if (playerChoice == 1) :
    print("Uneasy after your brush with death you slowly open the chest to reveal a magical sword")
    hasSword = True
    playerLevel += 1
    print("You gained another level you are now level " + str(playerLevel))
else :
    print("You decide not to open the chest, never to know if it could have aided you in your adventure.")
print("You leave the cavern and continue your journey")
print("Up ahead the air grows warm and damp. You hear loud snoring")
print("Peeking around a corner you see a monstrous shape! A dragon sleeps in the room ahead.")
print("You swallow hard and decide it\'s time to leave.")
print("As you turn, your foot finds a rock. It thuds loudly against the cave wall. The dragon wakes up!")
print("1. Fight the dragon.")
print("2. Run for your life.")
playerChoice = int(input())
if (playerChoice == 1) :

    print("You feel courage surge through your body as you charge the dragon!")
    if (playerHealth > 6) :
        print("You survive the Dragon\'s first attack and live.")
        if (hasSword == True) :
            print("You raise the magic sword and plunge it into the dragon, slaying the beast.")
            playerLevel += 1
            print("You are now level " + str(playerLevel))
        else :
            print("You pummel the dragon with your fists to no avail. The dragon snarls and swallows you whole. \nGame Over! \nYou got to level " + str(playerLevel))
            quit(0)
    else :
        print("The Dragon attacks you first, slashes you with their claws and you die. \nGame Over! \nYou got to level " + str(playerLevel))
        quit(0)
else :
    print("As you run away to hide in the safety of your warm bed, the dragon yawns and returns to its slumber.")
    quit()
