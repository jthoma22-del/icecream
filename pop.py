yeah_nums = [1,2,3] 
yeah_nums.pop(1)
# What does the list look like now?
print(yeah_nums)

letters = ["a", "b", "c"] 
# This is identical to pop with no index argument
letter = letters.pop(-1)
# What did I get?
print(letter)

list_a = [1, 2, 3]
list_b = list_a
list_a[0] = 7
# What is printed?
print(list_b)

num_a = 10
num_b = 10
num_b += 10
print(num_a)
