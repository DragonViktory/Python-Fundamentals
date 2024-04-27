def intro():
    return '''####################################
#   Welcome to SoftUni Calculator  #
#   Please select an option to     #
#           continue               #
#                                  #
#                                  #
#                                  #  
#   Autor: Mario Zahariev          #
#   Course: SoftUni Fundamentals   #
####################################\n'''
def add(n1,n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

print(intro())

while True:
    choice = input('1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\nEnter your choice:')
    if choice == "5":
        print("Thank you for using our calculator!!!")
        break

    n1 = float(input("Enter first number:"))
    n2 = float(input("Enter second number:"))

    if choice == "1":
        print("The sum of is :", add(n1, n2), '\n')
    if choice == "2":
        print("The result of the subtract is :", subtract(n1, n2), '\n')
    if choice == "3":
        print("The result of the multiply is :", multiply(n1, n2), '\n')
    if choice == "4":
        print("The result of the divide is :", divide(n1, n2), '\n')
