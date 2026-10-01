# initialize variables
item = ""
discount = 1
currency = 15

print("Shopkeep: Welcome to my boba shop!")
user_greeting = input("User: ")

if user_greeting == "hello":
    price = 1

if user_greeting == "i love bubble tea":
    price = 0.7

# buy item
print("Shopkeep: What do you want?")
print("slushy: $8")
print("something good: $4")
user_item = input("User: ")

if user_item == "slushy":
    price_after_discount = 8 * price
    currency -= price_after_discount
    item = "slushy"
    print("Cool!")

if user_item == "something good":
    price_after_discount = 4 * price
    currency -= price_after_discount
    item = "something good"
    print("Great choice!")

if user_item != "slushy" and user_item != "something good":
    print("We don't sell that.")

# print summary
print("Item:", item)
print("Discount:", discount)
print("Currency:", currency)