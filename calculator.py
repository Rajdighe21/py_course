# HELLO WE CREATE CALCULATOR IN PYTHON

getFirstInput =  eval(input("Enter First Value :"))
getSecondInput = eval(input("Enter Second Value :"))

getMath = input("Use +,-,*,/ For Sum :")

if getMath == "+":
    a = getFirstInput + getSecondInput
    print(a)
elif getMath == "-":
    a = getFirstInput - getSecondInput
    print(a)
elif getMath == "*":
    a = getFirstInput * getSecondInput
    print(a)
elif getMath == "/":
    a = getFirstInput / getSecondInput
    print(a)
else:l
    print("Enter Right Math Sum")

