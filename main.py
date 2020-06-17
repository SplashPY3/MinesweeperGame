a = float(input("Enter a number\t"))
b = float(input("Enter a number\t"))
o = input("Enter an operation\t")

if o == "+":
    print(a + b)

elif o == "-":   # decreasing b by a
    print(a - b)

elif o == "/":
    if a or b == 0:
        print("Error: Division by 0")
    else:
        print(a / b)

elif o == "*":
    print(a * b)

elif o == "mod":
    print(a % b)

elif o == "pow":
    print(a ** b)

elif o == "div":
    if a or b == 0:
        print("Error: Division by 0")
    else:
        print(a // b)

else:
    print("Error: Unsupported operation")