n = int(input("Enter a positive number: "))

max = n

while (n != -1):
	n = int(input("Enter a positive number: "))
	if (max < n):
		max = n
print("The largest value is " + str(max))
