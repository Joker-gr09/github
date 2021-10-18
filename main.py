# main page
from Mode_1 import *
from Mode_2 import *
from Mode_3 import *


def main():
    print("Please enter your grade?")
    grad = input("Grade:")

    print("Please enter the number of questions?")
    number_str = input("Number:")
    number = int(number_str)

    if grad == str(1) or grad == str(2):
        calculation_mode_1(number)

    elif grad == str(3) or grad == str(4):
        calculation_mode_2(number)

    elif grad == str(5) or grad == str(6):
        calculation_mode_3(number)


main()