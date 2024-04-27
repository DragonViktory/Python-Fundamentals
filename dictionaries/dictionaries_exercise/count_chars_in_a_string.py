current_input = input().split()
symbols = "".join(current_input)  # texttexttext
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1  # {'t': 6, 'e': 3, 'x': 3}
for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")
#t -> 6
#e -> 3
#x -> 3