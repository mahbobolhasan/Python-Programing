import random
for i in range(1,10):
    guess_Number = int(input("Guess the Number Between 1 to 10:"))
    randomNumber = random.randint(1,10)
    if guess_Number == randomNumber:
     print("You guessed the right number!")
    else:
     print("Sorry try again")
     print("Random Number is", randomNumber)
