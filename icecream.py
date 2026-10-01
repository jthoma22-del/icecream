ice_cream_flavors=["vanilla", "strawberry","chocolate"]
toppings=["caramel","marshmallow","gummi bears"]

for i in ice_cream_flavors:
    print(i)
for i in ice_cream_flavors:
    for topping in toppings:
        print(f"{i} is tasty with {topping}")
for i in ice_cream_flavors:
    if i=="strawberry":
            print(f"strawberry is fine on its own!")
    else:
        for topping in toppings:
             print(f"{i} is tasty with {topping}")
         
