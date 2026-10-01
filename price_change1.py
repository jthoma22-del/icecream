original=float(input("What was the original price? "))
new=float(input("What is the new price? "))
my_difference=round(new-original)
change=int((my_difference/original)*100)

print("Price changed by ",change,"% ")


