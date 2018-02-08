# this is pseudo code.
#starts with

list_dates = [date1, date2, date3]

list_diff = []

for i in range(len(list_dates)):
    diff = list_dates[i] - list_dates[i-1]
    list_diff.append(diff)

average(list_diff)

#something along these lines


