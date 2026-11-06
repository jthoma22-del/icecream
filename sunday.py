
values = input().split()
new_list = []
for value in values:
    wins = int(value)

    if wins == 0:
        break

    new_list.append(wins)

sunday_totals = []
total = 0

for i in range(0, len(new_list), 7):
    total += new_list[i]
    sunday_totals.append(total)

print(sunday_totals)