from statistics import median

salary = input('provide salries: ')
to_list = salary.split()

for i in range(len(to_list)):
    to_list[i] = int(to_list[i])

average = sum(to_list)/len(to_list)

gap = max(to_list) - min(to_list)

print('median: ', int(median(to_list)))
print('Average: ', int(average))
print('Gap: ', gap)
