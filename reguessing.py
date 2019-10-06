import random

random_number = random.randint(1, 10)
guess = None

while True:                 #Can be Played infinite times 
    guess = int(input("Guess a random between 1 and 10: "))
    if random_number > guess:
        print("Too Low")
    elif random_number < guess:
        print("Too High")
    else:
        print("You guessed it! You won!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
           random_number = random.randint(1, 10)
           guess = None 
        else:
            print("Thank You for Playing! Hope you soon back")
            break   
       

