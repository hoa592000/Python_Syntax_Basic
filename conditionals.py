on = True
a = float(input("a is: "))
b = float(input("b is: "))
def sum():
    print(a + b)
def hieu():
    print(a - b)
def thuong():
    print(a / b)
def tich():
    print(a*b)

while on:
    operation = input("please type +, -, *, / or q: ")
    if operation == "+":
        sum()
    elif operation == "-":
        hieu()
    elif operation == "/":
        thuong()
    elif operation == "*":
        tich()
    elif operation == "q":
        on= False
    
    