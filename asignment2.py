a = int(input("Enter Side A: "))
b = int(input("Enter Side B: "))
c = int(input("Enter Side C: "))
d = int(input("Enter Side D: "))
e = int(input("Enter Side E: "))

aminusc = a - c

areatirangle = (0.5*(aminusc)*e)

areassquarebytriangle = (d - b - e)*aminusc

bigtriangle = b*a

total = areatirangle +areassquarebytriangle + bigtriangle

print (float(total))
