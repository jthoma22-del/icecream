"""
Joshua Thomas Section 16
September 09, 2026
LOTR Character Identifier
This program identifies which Lord of the Ring character the user most 
aligns with using a series of questions to narrow down the possibilities
to a single character.
"""
race=input("Are you human, maiar or hobbit? ")
if race=="human":
    king=input("Are you King of Gondor? ")
    if king=="yes":
        print("You are Aragorn son of Arathorn")
    else:
        ring=input("Did you try to take the ring from Frodo? ")
        if ring=="yes":
            print("You are Boromir, poor guy...")
        else:
            print("You are Theoden, probably")
elif race=="maiar":
    character=input("Are you good or evil? ")
    if character=="good":
        print("You are Gandalf")
    else:
        truth=input("Did you forge the One Ring? ")
        if truth=="yes":
            print("You are Sauron")
        else:
            print("You are Saruman")
elif race=="hobbit":
    real=input("Do you carry the One Ring? ")
    if real=="yes":
        print( "You are Frodo Baggins")
    else:
        choice=input( "Are you are a gardener? ")
        if choice=="yes":
            print("You are Samwise")
        else:
            print("You are either Merry or Pippin.")
else:
    print("You are an Orc, sorry about that.")

          