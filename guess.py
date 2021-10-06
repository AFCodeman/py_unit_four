import random

def guess_game():
    y = int(input("Guess a random number 1-10."))
    x = random.randint(1,10)
    z = x-y
    if x==y:
        print("Congratulations, you have won the game.")
    elif x>y:
        print("Sorry, the number was",x,"and you put",y,". You were",z,"away from the right answer.")
    elif x<y:
        print("Sorry, the number was",x,"and you put",y,". You were",z,"away from the right answer")

guess_game()