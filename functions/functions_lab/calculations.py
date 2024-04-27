def calculation_func(first, second, operation):
    result = 0
    if operation == "multiply":
        return first * second
    elif operation == "divide":
        return int(first / second)
    elif operation == "add":
        return first + second
    elif operation == "subtract":
        return first - second


type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number,second_number, type_of_operation))
