# this function is suitable for 1 & 2, num is the number of question.
# it returns to the score for this mode
import random


def calculation_mode_1(num):
    count = 0
    right = 0
    while num > 0:
        # determine the inquiry tips
        num_1 = random.randint(0,100)
        num_2 = random.randint(0,100)
        num_1_str = str(num_1)
        num_2_str = str(num_2)
        op = ["+", "-"]
        rand_op = random.choice(op)
        print('Output: '+num_1_str+rand_op+num_2_str+'=?')
        user_input = input("Input: ")
        result1 = num_1 + num_2
        result2 = num_1 - num_2

        # determine the answer condition
        if user_input == str(result1) and rand_op == "+":  # add case
            print("Good job!")
            right += 1  # right answer number plus 1
            count += 1  # total number plus 1

        elif user_input == str (result2) and rand_op == "-":  # subtraction case
            print("Good job!")
            right += 1
            count += 1

        else:    # wrong answer
            print("Wrong Answer!")
            count += 1

        num -= 1

    score = (right / count)*100

    print("Your score is:")
    print(round(score,2))
