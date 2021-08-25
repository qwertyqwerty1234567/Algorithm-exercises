"""
program	that fulfills the functionalities of a mathematical quiz with the five basic arithmetic	operations
Author: Jonathan Chen
UPI: jche827
id: 679337989
"""
import random

def display_intro():
    print ("*" * 24)
    print ("**", "A Simple Math Quiz", "**")
    print ("*" * 24)

def display_menu():
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Integer Division")
    print ("5. Modulo Operation")
    print ("6. Exit")

def display_separator():
    print ("-"*24)
    
def get_user_input():
    option = int(input("Enter your choice: "))
    if option <1 or option >6:
        print ("Invalid menu option.")
        option = get_user_input()
        return option
        
    else:
        return option

def get_user_solution(problem):
    user_solution = input(problem)
    user_solution = int(user_solution)
    return user_solution

def check_solution(user_solution, solution, count):
    if int(user_solution) == int(solution):
        count += 1
        print ("Correct.")
        return count
    else:
        print ("Incorrect.")
        return count
    
def menu_option (index, count):
    first_number = str(random.randrange(1,31))
    second_number = str(random.randrange(1,31))
    if index == 1:
        print ("Enter your answer:")
        solution = int(first_number) + int(second_number)
        problem = str(first_number + " + " + second_number + " = ")

    elif index == 2:
        print ("Enter your answer:")
        solution = int(first_number) - int(second_number)
        problem = str(first_number + " - " + second_number + " = ")

    elif index == 3:
        print ("Enter your answer:")
        solution = int(first_number) * int(second_number)
        problem = str(first_number + " * " + second_number + " = ")

    elif index == 4:
        print ("Enter your answer:")
        solution = int(first_number) // int(second_number)
        problem = str(first_number + " // " + second_number + " = ")

    elif index == 5:
        print ("Enter your answer:")
        solution = int(first_number) % int(second_number)
        problem = str(first_number + " % " + second_number + "=")
    
    user_solution = get_user_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count
    
def display_result(total, correct):
    percent = round(int(correct) / total *100, 2)
    if percent == 0.0:
        percent = 0
    print ("You answered", total, "questions with", correct,"correct")
    print ("Your score is ", percent, "%. Thank you.", sep="")
    
def main():
    display_intro()
    display_menu()
    display_separator()
    option = get_user_input()
    total = 0
    correct = 0
    while option != 6:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)   
    
main()
