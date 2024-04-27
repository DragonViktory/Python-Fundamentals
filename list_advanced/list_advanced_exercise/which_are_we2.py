first_list = input().split(", ")
second_list = input().split(", ")

result = []

for element in first_list:
    for word in second_list:
        found_element = element in word
        if found_element:
            result.append(element)
            break

print(result)
