"""Number Guessing Game 
I want to play a game which I can guess a number. The computer chooses a number in the range I chose. So that I can try to find the correct number which was selected by computer. Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages You can assume that the user will enter valid input."""

from random import randint
import timeit

start_time = timeit.default_timer()
a = int(input("Please enter your min value of range  :"))
b = int(input("Please enter your max value of range  :"))

comp_num = randint(a,b)
counter=0
while True:
    nbr = int(input(f"Please make your guess between {a} and {b} both included :"))
    counter +=1 
    if nbr<a or nbr>b:
        print("please make your guess between " + a + " and "+b)
    elif nbr>comp_num:
        print("reduce your guess")
    elif nbr<comp_num:
        print("increase your guess")
    else:
        print("\nCongrats the number is ", comp_num)
        print("You found the number after ", counter, " times guess")

        end = timeit.default_timer()
        elapsed_time = int(end-start_time)
        print(f"Your guessing time is ", elapsed_time, "seconds.")
        break
