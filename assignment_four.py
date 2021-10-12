import random
import math

def get_card():
    """

    :return:
    """
    card = random.randint(1,10)
    return card

def get_winner():
    ptot = get_card() + get_card()
    dtot = get_card() + get_card()
    print(ptot)
    another = int((input("Type 1 if you want another card, type 2 if you want to continue"))
    if ptot >= 21:
        return("The dealer wins")
    elif ptot > dtot:
        return("The player wins")
    elif dtot > ptot:
        return("The dealer wins")
    elif ptot == dtot:
        return("The dealer wins")
    else:
        return("What?!?")

print (get_winner())