import random

uc = int(input("Please choose 0 for rock, 1 for paper and 2 for scissors\n"))
cp = random.randint(0, 2)

print (f"You choose {uc} \nComputer choose {cp}")
#0 Rock
#1 Paper
#2 Scissors

if uc >= 3 or uc < 0:
    print ("Invalid number")
elif uc == 0 and cp == 2:
    print ("You win")
elif uc == 2 and cp == 0:
    print ("You lose")
elif uc < cp:
    print ("You lose")
elif uc > cp:
    print ("You win")
elif uc == cp:
    print ("Draw")
