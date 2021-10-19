import random
import math

def get_card():
    """

    :return:
    """
    card = random.randint(1,10)
    return card

def get_winner():
    ptot = int(get_card() + get_card())
    dtot = int(get_card() + get_card())
    morecard = int(input("Enter the number '1' if you want another card."))
    if morecard == 1:
        ptot + get_card()
    else:
        ptot
    if ptot >= 21:
        return("The dealer wins")
    elif ptot > dtot:
        return("The player wins")
    elif dtot > ptot:
        return("The dealer wins")
    elif ptot == dtot:
        return("The dealer wins")
    else:
        return("Error. Does not compute.")

print (get_winner())