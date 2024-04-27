username = input()
command = input().split()
current_command = command[0]

while current_command != "Registration":
    if current_command == "Letters":
        print(username.lower())
    elif current_command == "Reverse":
        start_index = int(command[1])  # 1
        end_index = int(command[2])  # 3
        if start_index > 0 and end_index > 0:
            if username.index(username) > start_index and username.index(username) > end_index:
                continue
        new_user = list(username)
        new_user_name = reversed(new_user)
        print(new_user_name)
    elif current_command == "Substring":
        substring = current_command[1]
        if substring in username:
            new_data = username.substring

            print()

        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif command == "Replase":
        string = command[1]
        new_string = command.replace(string)
    elif command == "IsValid":
        char = command[1]
        if char in command:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")


    command = input().split()
