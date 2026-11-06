'''For this problem you'll determine the distance between two points.
Make sure you name the file seconds.py (all lower case). You should ask the user how many days, hours, minutes, and seconds have elapsed that they want to convert into just seconds. Then you should calculate the number of seconds. You can take all of these as integers, do not allow floating point values.

Sample input:
'''

days = int(input("How many days have elapsed? "))
hours = int(input("How many additional hours have elapsed? "))
minutes = int(input("How many additional minutes have elapsed? "))
seconds = int(input("How many additional seconds have elapsed? "))

hours += days*24
minutes += hours*60
seconds += minutes*60


print(f"The total amount of time elapsed is {seconds} seconds")
