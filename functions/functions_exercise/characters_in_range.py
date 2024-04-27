def collect_charters(first, second):
    charters = []
    for current_charter in range(ord(first) + 1, ord(second)):
        charters.append(chr(current_charter))
    return charters


first_character = input()
second_character = input()
result = collect_charters(first_character, second_character)
print(' '.join(result))