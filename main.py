a = float(input("Enter a number  "))
b = float(input("Enter a number  "))
o = input("Enter an operation  ")

if o == "+":
    print(a + b)

elif o == "-":
    print(a - b)

elif o == "/":
    print(a / b)

elif o == "*":
    print(a * b)

elif o == "mod":
    if b == 0:
        print("Error: Division by 0")
    else:
        print(a % b)

elif o == "pow":
    print(a ** b)

elif o == "div":
    if b == 0:
        print("Error: Division by 0")
    else:
        print(a // b)

else:
    print("Error: Unsupported operation")