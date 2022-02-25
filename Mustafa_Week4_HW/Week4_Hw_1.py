#Calculator: General Information: I want to use a program which can calculate basic mathematical operations. Acceptance Criteria:
#The calculator must support the Addition, Subtraction, Multiplication and Division operations.
#All operations must be in a different module as method.
#Operations must define with two float numbers as parametres.
#Use math.ceil() for all results.
#Create a menu to choose an operation.
#User can choose invalid options, so you must handle all possible error. (Use try except :))
#Inform user what type of error occured (TypError, ValueError etc.)
#This process must continue until user want to quit from calculator.*/

# Calculator
  
# Function Sum 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply 
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide 
def divide(num1, num2):
    return num1 / num2
  
print("Please select a mathematical operation -\n" \
        "1 for  Add\n" \
        "2 for  Subtract\n" \
        "3 for  Multiply\n" \
        "4 for  Divide\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1 (Add), 2 (Substract), 3(Multiply), 4(Divide) :"))
  
number_1 = int(input("Please enter first number: "))
number_2 = int(input("Please enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Invalid input") 