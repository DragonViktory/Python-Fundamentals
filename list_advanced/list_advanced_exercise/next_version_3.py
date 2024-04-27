version = input().replace(".", "")
new_number = int(version) + 1
new_list = [x for x in str(new_number)]

print(".".join(new_list))
