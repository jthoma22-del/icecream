numbers = []
while True:
    entry = input()
    if entry == "stop".lower():
        break
    numbers.append(int(entry))


new_list = []

for n in numbers:
    if n % 2 == 0:
        new_list.append(n**2)
    else:
        new_list.append(n)
print(new_list)
