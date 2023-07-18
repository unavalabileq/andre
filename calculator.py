# Step 1: Plan the calculator's functionality

# Our calculator will be able to perform basic arithmetic operations such as 
# addition, subtraction, multiplication, and division.

# Step 2: Write the code to get user input

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the operator
op = input("Enter an operator (+, -, *, /): ")

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Step 3: Write the code to perform arithmetic operations

# Check which operator the user entered and perform the corresponding arithmetic operation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operator")

# Step 4: Display the result

# Display the result to the user
print("Result: ", result)
end = input()