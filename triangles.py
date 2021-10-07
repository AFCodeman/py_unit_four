import math

def is_triangle(side1, side2, side3):
    if side1 > side2 + side3:
        print("You cannot make a triangle.")
    elif side2 > side1 + side3:
        print("You cannot  make a triangle.")
    elif side3 > side1 + side2:
        print("You cannot make a triangle.")
    elif side1 == side2 + side3:
        print("You can make a degenerate triangle.")
    elif side2 == side1 + side3:
        print("You can make a degenerate triangle.")
    elif side3 == side1 + side2:
        print("You can make a degenerate triangle.")
    else:
        print("Congratulations! You can make a triangle.")



def main():
    side1 = float(input("What is the length of the first stick?"))
    side2 = float(input("What is the length of the second stick?"))
    side3 = float(input("What is the length of the third stick?"))
    is_triangle(side1,side2,side3)

if __name__ == '__main__':
    main()

main()