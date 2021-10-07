import random


def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors
    if user==1 and computer==2:
        return("The computer wins.")
    elif user==2 and computer==3:
        return("The computer wins.")
    elif user==3 and computer==1:
        return("The computer wins.")
    elif user==1 and computer==3:
        return("You win!")
    elif user==2 and computer==3:
        return("You win!")
    elif user==3 and computer==2:
        return("You win!")
    else:
        return("It is a tie")


def main():
    user = int(input("Enter 1 for Rock, Enter 2 for Paper, Enter 3 for Scissors: "))
    computer = random.randint(1,3)
    print(who_wins(user,computer))

if __name__ == '__main__':
    main()