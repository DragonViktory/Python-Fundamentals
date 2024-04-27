count_wrapping_paper = int(input())
count_cloth = int(input())
liters_of_glue = float(input())
percent_discount = int(input())

cost_wrapping_paper = count_wrapping_paper * 5.80
cost_cloth = count_cloth * 7.20
cost_liters_of_glue = liters_of_glue * 1.20

all_material_price = cost_wrapping_paper + cost_cloth + cost_liters_of_glue
discount = all_material_price * percent_discount / 100
price_discounted = all_material_price - discount

print(f"{price_discounted:.3f}")
