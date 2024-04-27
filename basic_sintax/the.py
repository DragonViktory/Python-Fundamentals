# days = float(input())
# players = float(input()
# group_energy = float(input())
# water_per_day_one_person = float(input())  # 11.3
# food_per_day_for_one_person = float(input())  # 7.2
# energy_loss = float(input())
# total_water = days * players * water_per_day_one_person
# total_food = days * players * food_per_day_for_one_person
# flag = False
#
# for day in range(1, days + 1):
#     group_energy -= energy_loss
# if day % 2 == 0:
#     group_energy += group_energy * 0.05
# total_water -= total_water * 0.30
# current_water = total_water
# if day % 3 == 0:
#     total_food -= total_food * 7
# group_energy += group_energy * 0.10
# if group_energy <= 0:
#     flag = True
# break
# if not flag:
#     print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
# else:
#     print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
