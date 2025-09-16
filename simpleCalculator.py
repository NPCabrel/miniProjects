#Ask the user to enter two numbers and an operator (+, -, *, /).

#Use a function to compute and print the result.

#Handle errors (e.g., division by zero).

while True:
    def simple_calculator():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                return "Invalid operator. Please use +, -, *, or /."
            
            return f"The result is: {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    print(simple_calculator())


# I added a while loop to allow continuous calculations until the user decides to stop it manually.