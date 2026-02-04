# Function jo factorial calculate karega
def factorial(n):
    res = 1
    # 1 se lekar n tak ka loop
    for i in range(1, n + 1):
        res = res * i
    return res

# User se number maangna
num = int(input("Enter a number: "))

# Result ko print karna (Expected output ke hisaab se)
print(f"Factorial of {num} is: {factorial(num)}")