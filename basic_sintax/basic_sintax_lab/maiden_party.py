price_maiden_party = float(input())
count_love_messages = int(input())
count_wax_roses = int(input())
count_key_chains = int(input())
count_cartoons = int(input())
count_luck_surprise = int(input())
count_items = 0

price_love_messages = count_love_messages * 0.60
price_wax_roses = count_wax_roses * 7.20
price_key_chains = count_key_chains * 3.60
price_cartoons = count_cartoons * 18.20
price_luck_surprise = count_luck_surprise * 22
count_all_items = count_love_messages + count_wax_roses + count_key_chains + count_cartoons + count_luck_surprise
all_costs = price_love_messages + price_wax_roses + price_key_chains + price_cartoons + price_luck_surprise
if count_all_items >= 25:
    all_costs = all_costs - (all_costs * 0.35)
host = all_costs * 0.1
total_price = all_costs - host
diff = abs(total_price - price_maiden_party)
if price_maiden_party < all_costs:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

