budget = int(input())
current_price_as_string= int(input())

while current_price_as_string != "End":
    current_price_as_string = int(current_price_as_string)
    budget -= current_price_as_string
    if budget < 0:
        print(f"You went in overdraft!")
        exit()
    current_price_as_string = input()

print(f"You bought everything needed.")

