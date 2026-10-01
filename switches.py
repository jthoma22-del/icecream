"""
Joshua Thomas (Section 16)
The program takes input from the user to determine how to open
the lock on the door in a video game given a few constraints.
To open the lock, the following must be true:
The first knob must be set to an even position.
The second knob must be set to an odd position.
The switch must be set to "up".
"""
knob1=int(input())
knob2=int(input())
switch=input()

if knob1<1 or knob2>12 or knob2<1 or knob2>12:
    print(" Knobs need to be set between 1-12")
elif knob1%2==0 and knob2%2!=0 and switch=="up":
    print("The door opens, you get all the loot.")
elif (knob1%2==0 or knob2%2!=0) and switch!="up":
    print("The door clanks but does not open, try again.")
else:
    print("The handle doesn't budge.")

