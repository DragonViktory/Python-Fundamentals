def get_min_numbers(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number:
            min_number = num
            return get_min_numbers()


first = int(input())
second = int(input())
third = int(input())

print(get_min_numbers([first, second, third]))
