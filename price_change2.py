original=float(input("What is your original price? "))
new_price=float(input("What is your new price? "))
my_difference=new_price-original
percent_change=round((my_difference/original)*100)
print("Price changed by ",percent_change,"%")
