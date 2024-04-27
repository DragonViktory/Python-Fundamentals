count_people = int(input())
season = str(input())
price = 0

if season == 'spring' and count_people <= 5:
    price = count_people * 50
elif season == 'spring' and count_people >=6:
    price = count_people * 48
if season == 'summer' and count_people <= 5:
    price = count_people * 48.50 * 0.85
elif season == 'summer' and count_people >= 6:
    price= count_people * 45 * 0.85
if season == 'autumn' and count_people <= 5:
    price= count_people * 60
elif season == 'autumn' and count_people >= 6:
    price = count_people * 49.50
if season == 'winter' and count_people <= 5:
    price = count_people * 86 * 1.08
elif season == 'winter' and count_people >= 6:
    price = count_people * 85 * 1.08

print(f"{price:.2f} leva.")

