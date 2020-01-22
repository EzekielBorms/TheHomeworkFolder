import random
q1 = input("What is your first name? ")
q2 = input("What is your last name? ")
print("Hello " + str(q1) + " " + str(q2) + ", Nice to meet you!")
q3 = int(input("How old are you? "))
if (q3 <= 3):
	print("Welcome to our world!")
elif (q3 <= 7):
	print("Congragulations! You are now in elementary school!")
elif (q3 <= 15):
	print("Congragulations! You are now in middle school!")
if (q3 <= 18):
	print("Congragulations! You are now in High School!")
elif (q3 <= 21):
	print("Wow! you are now in college!")
elif (q3 <= 35):
	print("You are now married and are in a good life for a while with your kids!")
elif (q3 <= 50):
	print("You and your wife/husband are now grandparents!")
elif (q3 <= 80):
	print("I am so sorry for the next coming years for you")
else:
	print("You are now dead soon, sorry to hear that")
q4 = int(input("From 1 to 100, Which number do you guess is right? "))

if (q4 >= 101):
	print("Error! invalid response: NUmber does not compute with question....")
else:
	print("Your number is: " + str(random.randint(0,100)))
	
q5 = input("How tall are you? ")

print("Nice! Well " + str(q1) + " " + str(q2) + ", it's been nice talking with you, Goodbye!")
