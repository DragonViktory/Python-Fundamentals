even_sum = 0
odd_sum = 0

num_as_str = "1000435"
for digit_as_string in num_as_str:
    digit = int(digit_as_string)
    if digit%2 == 0 :
        evensum += digit
    else:
        odd_sum =+ digit

print(even_sum)
print(odd_sum)
