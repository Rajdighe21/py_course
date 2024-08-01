# # this is stak
# myStack = []
# while True:
#     choice = int(input("Enter a Number :"))
#     if choice == 1:
#         EnterValue = input("Enter List Value :")
#         myStack.append(EnterValue)
#         print(myStack)
#     elif choice == 2:
#         myStack.pop()
#         print(myStack)
#     elif choice == 3:
#         print(myStack[-1])
#     elif choice == 4:
#         print(myStack)
#     else:
#         break

# this is queck
new = []

while True:
    inp = int(input("Enter Queque Value"))
    if inp == 1:
        l = input("Enter New Value")
        new.append(l)
        print(new)
    elif inp == 2:
        del new[0]
        print(new)
