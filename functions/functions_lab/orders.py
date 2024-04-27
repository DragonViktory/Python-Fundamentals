def total_price(product, quantity):
    total_amount = 0
    if product == "coffee":
        total_amount = quantity * 1.50
    elif product == "water":
        total_amount = quantity * 1.00
    elif product == "coke":
        total_amount = quantity * 1.40
    elif product == "snacks":
        total_amount = quantity * 2.00
    return total_amount


product_to_buy = input()
requested_quantity = int(input())
result = total_price(product_to_buy, requested_quantity)
print(f"{result:.2f}")


