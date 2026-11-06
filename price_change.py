original = float(input("What was the original price? "))
new = float(input("What is the new price? "))
change = int(round(((new-original)/original)*100))
print(f"Price changed by {change}%")
