def smallest_number(numbers):
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_numbers = [first_number, second_number, third_number]
min_number = smallest_number(all_numbers)
print(min_number)

