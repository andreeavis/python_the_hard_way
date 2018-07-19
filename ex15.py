# from module 'sys' import a function / parameter called 'argv'
from sys import argv

# define values for argv: script, filename
script, filename = argv	

# opens 'filename' introduced by the user
txt = open(filename)

#prints "Here's your <filename>" filname value introduced by the user
print(f"Here's your file {filename}:")
#prints the text in the filename introduced by the user
print(txt.read())

# prints "The filename again"
print("Type the filename again:")

# asks for input from user - to type the filename again + '> ' added tpo the answer
file_again = input('> ')

# open filename introduced by the user
txt_again = open(file_again)

# prints text in the file introduced by the user 
print(txt_again.read())

print()


