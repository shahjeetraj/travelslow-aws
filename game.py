import random
level = 0
guess = 0
# ASK FOR LEVEL WHILE IT IS A POSITIVE INTEGER

def get_level():
    while True:
         try:
            l = int(input("Level: "))
            return l
         except ValueError:
             pass

# ASK USER TO GUESS THE VALUE, TILL IT IS RIGHT

while level ==0:
    level = get_level()

# GENERATE A RANDOM GUESS
rand_guess = random.randint(1,level+1)
#print(rand_guess)

def get_guess():
    while True:
        try:
            g = int(input("Guess: "))
            return g
        except ValueError:
            pass

# CREATE A COMPARE FUNCTION THAT CHECKS WHETHER VALUE MATCHES RANDOM GUESS AND RETURNS THE RESPONSE REQUIRED
def compare(g,rg):
    if g == rg:
        return("Just right!")
    elif g < rg:
        return("Too small!")
    elif g > rg:
        return("Too large!")

while compare(guess,rand_guess) != "Just right!":
    guess = get_guess()
    print(compare(guess,rand_guess))
    #print(f"Guess is: {guess}\nRandom_Guess is: {rand_guess}")