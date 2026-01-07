#python program to create a simple calculator(plan)

# Steps to build calculator program
# functions for operations
# user input 
# print result

#Function to add 2 number
def add(num1, num2):
    return num1 + num2

#Function to sub 2 number
def sub(num1, num2):
    return num1 - num2

#Function to multiply 2 number
def multiply(num1, num2):
    return num1 * num2

#Function for division
def division(num1, num2):
    return num1 / num2

#Function for avg
def avg(num1, num2):
    return (num1 + num2) / 2




#step 3 print result
val = 'y'
while(val == 'y'):
    #step 2(User input)
    print("Please select a operation: \n " \
    "1. Addition\n" \
    "2. Substration\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Average\n")

    select = int(input("Select a operation from 1 -> +,2 -> -,3 -> *,4-> /,5-> avg: "))
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter Second number: "))
    
    match select:
        case 1:
            res = add(num1, num2)
            print(res)
        case 2:
            res = sub(num1, num2)
            print(res)
        case 3:
            res = multiply(num1, num2)
            print(res)
        case 4:
            res = division(num1, num2)
            print(res)
        case 5:
            res = avg(num1, num2)
            print(res)
        case _:
            print("please enter valid symbol")
            
    val = input("You want to play again!(y/n): ")