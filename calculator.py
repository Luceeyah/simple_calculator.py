import math
# *********************** HOW TO BUID A SIMPLE CALCULATOR ****************************
""" A Simple calculator with the following functionalities 
ADD
SUBTRACT
MULTIPLY
DIVISION
SQUARE ROOT
RAISE TO POWER """

print(" Select an Operation to perform ")
print ("1. ADD")
print ("2. SUBTRACT")
print ("3. MULTIPLY")
print ("4. DIVISION")
print ("5. SQUARE ROOT")
print ("6. INDEX")

operation = input()

if operation == "1":  # ADDITION
    num1 =eval(input("Enter first number: "))
    num2 =eval(input("Enter second number: "))
    result = "The sum is " + str((num1) + (num2))
    print(result)
elif operation == "2":  # SUBTRACTION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(" The difference is " + str(int(num1) - int(num2)))
elif operation == "3": # MULTIPLICATION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(" The product is " + str(int(num1) * int(num2)))
elif operation == "4":  # DIVISION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(" The result is " + str(int(num1) / int(num2)))
elif operation == "5": # SQUARE ROOT
    num = int(input("Enter number: "))
    print("The square root is %f " %(math.sqrt(num)) )
elif operation == "6": # INDEX
    num = int(input("Enter number: "))
    print("The power is %d " %(math.pow(num, 2)) )
else:
    print("Invalid Entry")

