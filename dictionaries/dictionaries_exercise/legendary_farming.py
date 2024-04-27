items = {"shards": 0, "fragments": 0, "motes": 0}
concurrent_items = input().split()
needed_parts = 250
obtained = False
while not obtained:
    for index in range(0, len(concurrent_items), 2):
        value = int(concurrent_items[index])
        key = concurrent_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= needed_parts:
            print(f"Shadowmourne obtained!")
            items["shards"] -= needed_parts
            obtained = True
        elif items["fragments"] >= needed_parts:
            print(f"Valanyr obtained!")
            items["fragments"] -= needed_parts
            obtained = True
        elif items["motes"] >= needed_parts:
            print(f"Dragonwrath obtained!")
            items["motes"] -= needed_parts
            obtained = True
        if obtained:
            break
    if obtained:
        break
    concurrent_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")