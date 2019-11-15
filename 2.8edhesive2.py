lat = input("Enter lat: ")

lon = input("Enter lon: ")

lat_list = [float(s) for s in lat.split(',')]

lon_list = [float(s) for s in lon.split(',')] 


a = max(lat_list)

b = max(lon_list)

c = min(lat_list)

d = min(lon_list)

print("Farthest North: " + str(a))
print("Farthest West: " + str(b))
print("Farthest South: " + str(c))
print("Farthest East: " + str(d))
