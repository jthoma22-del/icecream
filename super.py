user=input("Are you a hero or villian? ")
if user=="hero":
    num=int(input("how many people have you saved? "))
    if num>10 and num<100:
        print("Sounds like you're making  difference! ")
    elif num<=10:
        print("Go on more patrols")
    else:
        print("Wow, great job saving the city! ")
elif user == "villian":
    name = input("What is your name? ")
    if name:
        print(name + " sounds pretty evil")
    
    
        
        
    
