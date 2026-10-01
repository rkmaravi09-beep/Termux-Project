print("Simple Calculator")
print("------------------")

a = float(input("Pehla number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Dusra number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "0 se divide nahi kar sakte"
    else:
        result = a / b
else:
    result = "Invalid operation"

print("Result:", result)
