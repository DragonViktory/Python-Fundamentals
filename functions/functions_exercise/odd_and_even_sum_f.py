def get_even_and_odd_sums(digits_as_str):
    even_sum = 0
    odd_sum = 0

    for digit_as_string in digits_as_str:
        digit = int(digit_as_string)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum = + digit
    return [even_sum, odd_sum]

nums_as_str = input()
result = get_even_and_odd_sums(nums_as_str)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")

