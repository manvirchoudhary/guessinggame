import random

random = random.randint(1, 10)
guess = None

while guess != random:   #Can be played oly one time .
    guess = int(input("Guess a random between 1 and 10: "))
    if random > guess:
        print("Too Low")
    elif random < guess:
        print("Too High")
    else:
        print("You guessed it! You won!")
print(random)        