def even_num(num_list):
    even_list = []
    total = 0
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
            total += num
    return total


if __name__ == "__main__":
    num_list = []
    n = int(input("Enter a number:  "))
    while n != 0:
        num_list.append(n)
        n = int(input("Enter a number:  "))
    print(even_num(num_list))
