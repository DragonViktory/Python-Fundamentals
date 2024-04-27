#  На първия ред – N – брой дни, в които г-жа Иванова тренира – цяло число в интервала [1...50]
#  На втория ред – M – километрите, които е избягала първия ден – реално число в интервала
# [1.00…500.00]
#  За всеки един ден на отделен ред :
#  Процентите, с които се увеличава дневната си норма – цяло число в интервала [1…100

training_days = int (input())
km_first_day = float(input())
percent_each_day = int (input())
km = 0

for km in range( km_first_day, km + 1):
    total_km = km_first_day + km_first_day * percent_each_day / 100



    if km > 1000:
        print(f"You've done a great job running {diff} more kilometers!")
    else:
        print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")