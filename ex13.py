# script = another name for my .py files

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


print(input("Hello, how do you do? "))
print(input("Tell us why you are here? "))
print(input("Do you like bananas? "))

marmelade, jam, strawberries, berries = argv
print("I seriously love", marmelade)
print("I don't know about you, but I'm all about", jam)
print("Whatever dudes, the best thing in the world are", strawberries)
user_pref = (input("How about you? What do you like? "))
print("Me too, I super love", user_pref)
