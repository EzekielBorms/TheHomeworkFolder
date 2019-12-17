'''
Enter today's day numerically: 17
Sorry, not a payday.
Enter today's day numerically: 30
It's payday!
'''
x = int(input("Enter today's day numerically: "))

if (x != 30 and x != 15):
	print("Sorry, not a payday.")
	
if (x == 30 or x == 15):
	print("It's payday!")
