def welcome():
    print('''
Welcome to Calculator
''')


...
welcome()


# Define our function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input('Enter your first number: '))
    number_2 = float(input('Enter your second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = {}'.format(number_1, number_2, number_1 + number_2))
    # Subtraction
    elif operation == '-':
        print('{} - {} = {} '.format(number_1, number_2, number_1 - number_2))
    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2, number_1 * number_2))
    # Division
    elif operation == '/':
        number_x = (number_2 < 0, number_2 == 0, number_2 > 0)
        for number_2 in number_x:
            if number_2 == 0:
                print("Cannot divide by 0")
            else:
                number_2 = float(input('Enter your second number: '))
                print('{} / {} = {}'.format(number_1, number_2, number_1 / number_2))
            if number_2 > 0:
                break
            elif number_2 < 0:
                break

    else:
        print('You have not typed a valid operator, please tun the program again.')

    # Add again() function to calculate() function
    again()


# Define again() function to ask user if they want to use the calculation again
def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y/y for Yes or N/n for No,
''')

    # If user types Y, run the calculated() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say goodbye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


# Call calculate() outside the function
calculate()
