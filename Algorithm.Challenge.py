'''
attempt to make an algorithm
'''

import random

n = int(input("Enter a number: "))

if (n >= 0 and n <= 100):
        print ("Grade is valid")
        print ("No error detected\n")
print("Done")

'''
and-Both conditions must be true
'''

gr = int(input("Enter another number: "))

if (gr >= 70 and gr < 80):
    print("C")

'''
or-At least one must be true
'''
ge = int(input("Enter another number2: "))

if (ge < 0 or ge > 100):
    print("Not a correct grade")

'''
not- takes the opposite
'''
grade = int(input("Enter another number3: "))
    
if (not(grade >= 85)):
    print(str(grade))
    print(" is not an A or B")
    
gi = "Enter one final number, 1 to 100"
answer = random.randint(1,100)
c = 0
guess = 0
while (c != answer):
	guess = int(input(gi))
	c = c + 1
	if (guess < answer):
		print("Low! try again!")
	elif(guess > answer):
		print("High! try again!")

print("You did it!")
	
