messages = input().split()
final_message = []
for message in messages:
    number = ""
    current_massage = ""
    for character in message:
        if character.isdigit():
            number += character
        else:
            break
    message = message.replace(number, '')
    number = int(number)
    current_massage += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_massage += message
    final_message.append(current_massage)

print(" ".join(final_message))


