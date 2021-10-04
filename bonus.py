import math


def bonus_math(salary,year):
    salary = float(input("What is your yearly salary at the company?"))
    year = int(input("How many years have you worked at the company?"))
    if year<=5:
        bonus = salary * 1
    if year>5:
        bonus = salary * 1.05
    return(bonus)