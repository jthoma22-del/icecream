
wins = int(input())
total = 0
new_list = []

while wins != 0:
    new_list.append(wins)
    wins = int(input())          # now inside the loop

for i in range(0, len(new_list), 7):
    total += new_list[i]

print(total)


'''
wins = int(input())
total = 0
day = 0

while wins != 0:
    if day % 7 == 0:
        total += wins

    day += 1
    wins = int(input())

print(total)
'''

