from sys import argv

script, filename = argv

txt = open(filename)

print("This is your file, read it up:")

txt_read = print(txt.read())


print("Please input the filename again!")
file_again = input("->>>> ")

txt_again = open(filename)

print("Yo, check out your file stuff!")
txt_read_again = print(txt_again.read())

