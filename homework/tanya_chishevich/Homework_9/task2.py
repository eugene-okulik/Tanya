temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


hot_days = filter(lambda x: x > 28, temperatures)
hot_days_list = list(hot_days)
print(hot_days_list)

average_temp = (round(sum(hot_days_list) / len(hot_days_list)))
print(average_temp)

print(min(hot_days_list))
print(max(hot_days_list))
