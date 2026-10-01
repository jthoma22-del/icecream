original=float(input("What was the original price? "))
new=float(input("What is the new price? "))
change=round(((new-original)/original)*100)

print("Price changed by ",change,"% ")
