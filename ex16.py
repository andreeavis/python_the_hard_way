# import function argv from module sys
from sys import argv

# give value to the argv function
script, filename = argv

# print our dialogue using the 'filename' value above
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")       
print("If you do want that, hit RETURN")

# print a question mark for the user to input his choice
input("?")

# dialogue to the user that we are opening the file per his choice (which is Return)
print("Opening the file...")
# opens the filename
target = open(filename, 'w')

# prints to the user what the system is doing and it erases the file contents 
print("Truncating the file. Goodbye!")
target.truncate()

#tells the user that we're going to modify the file
print("Now I'm going to ask you for three lines.")

# asks the user to input the contents he wants in the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# tells the user his input is going into the file 
print("I'm going to write these to the file.")

# writes the user's content into the erased file with \n break between each line so they're on different lines
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# tells the user we're closing the file and closes it
print("And finally, we close it.")
target.close()


