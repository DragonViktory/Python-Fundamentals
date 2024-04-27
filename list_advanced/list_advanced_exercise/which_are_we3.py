def is_substr(word, seq):
    for el in seq:
        found_substr = word in el
        if found_substr:
            return True

    return False


first_list = input().split(", ")
second_list = input().split(", ")

result = [x for x in first_list if is_substr(x, second_list)]
print(result)
