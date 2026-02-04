# Function to calculate factorial
def factorial(n):
    res = 1
    # Loop from 1 to n
    for i in range(1, n + 1):
        res = res * i
    return res

# Taking input from the user
num = int(input("Enter a number: "))

# Printing the final result
print(f"Factorial of {num} is: {factorial(num)}")
