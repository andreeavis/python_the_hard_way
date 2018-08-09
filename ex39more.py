
# create a dictionary
released = {
	"iPhone": 2007,
	"iPhone 3G": 2008,
	"iPhone 4": 2010,
	"iPhone 5": 2012,
	"iPhone 6": 2013,
	"iPhone 7": 2015,
	'iPhone X': 2017
} 
# print(released)

# add a value to the dictionary
released["iPhone 8"] = 2016
# print(released)

# remove a key-value pair with the del operator
del released["iPhone 3G"]
# print(released)

# check the length  = the number of pairs
print(len(released))

# check if a key exists in the dictionary
for item in released:
	if "iPhone 11" in released:
		print("Key found!")
		break
	else:
		print("No keys found with that value.")
		break

# get a value of a specific key
print(released.get("iPhone", 'none'))


# print all keys with a for loop
print('*' * 30)
print('iPhone releases so far: ')
print('_' * 10)
for release in released:
	print(release) 

# print all keys and values
print("<>" * 30)
for key, val in released.items():
	print(key, "===>", val)

# get only the keys from the dictionary
print("<<>>" * 20)
phones = released.keys()
print(phones)

print("This dictionary contains these keys:"," ".join(released))
print("This dictionary containes these keys:", " ", released.keys())

# print the values
print(">><<" * 20)
print(released["iPhone"])
print("Values")

# printint with ppprint
print("<>" * 30)
import pprint
pprint.pprint(released)

# sort the dictionary
print("/\\" * 20)
for key, value in sorted(released.items()):
	print(key, value)

print("/\\" * 20)
for phones in sorted(released, key = len):
	print(phones, released[phones])

# counting
print("@" * 40)
count = {}
for element in released:
	count[element] = count.get(element, 0) + 1 
print(count)





















