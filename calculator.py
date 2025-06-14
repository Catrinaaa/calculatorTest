#a calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cannot divide by 0"
    return a / b

print("Simple caalculator: ")
print("Select operation: ")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("enter first number: "))
num2 = float(input("Enter secomd number: "))

if choice == '1':
    print("Result: ", add(num1, num2))
if choice == '2':
    print("Result: ", subtract(num1, num2))
if choice == '3':
    print("Result: ", multiply(num1, num2))
if choice == '4':
    print("Result: ", divide(num1, num2))