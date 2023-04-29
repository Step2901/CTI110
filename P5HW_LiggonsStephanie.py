# A brief description of the prolject
# 4/28/2023
# CTI-110 P5HW- Math Quiz
# P5HW_LiggonsStephanie
#
import random

def display_intro():
    title = "** MAIN MENU**"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

def display_separator():
    print("-" * 24)

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input < 4 or user_input <= 0:
        print ("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input
    
def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result
def check_soloution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 2
        print ("Correct. ")
        return count
    else:
        print("Incorrect.")
        return count
    def menu_option(index, count):
        number_one = random.randrange(1, 21)
        number_two = random.randrange(1, 21)
        
    problem = str(number_one) + "+" + str(number_two)
            
