print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

mydata = input('Prompt: ')
print(mydata)

name = input('Enter your name :')
print(f"Hi {name}, let us be friends!")



### get input ###
choice = input("Enter your choice [1-3] :")

### convert string to int type ###
choice = int(choice)

if choice == 1:
    print( "Starting backup... ")
elif choice == 2:
    print("Starting user management...")
elif choice == 3:
    print("Rebooting the server...")
else:
    print("Invalid number. Try again...")


name = input("What's your name? ")
#input name in "" in the answer when the question is prompted
print("Nice to meet you " + name + "!")
age = input("How old are you? ")
print("So, you are already " + str(age) + " years old, " + name + "!")

name = input("what's your name? ")
age = input("Your age? ")
print(age, type(age))
colours = input("Your favourite colors? ")
print(colours)
print(colours, type(colours))

age = input('Your age? ')
print(age, type(age))
age = int(input('Your age? '))
print(age, type(age))
programming_language = input('Your favourite programming languages? ')
print(programming_language, type(programming_language))
programming_language = eval(input("Your favourite programming languages? "))
print(programming_language, type(programming_language))
